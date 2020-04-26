---
title: RHEL7 配置网卡信息
url: linux-rhel-7-config-network
---

在 RHEL5, RHEL6 中, 网卡配置文件的前缀为 eth, 第 1 块网卡为 eth0, 第 2 块网卡为 ethl; 以此类推. 而在 RHEL7 中, 网卡配置文件的前缀则以 ifcfg 开始, 加上网卡名称共同组成了网卡配置文件的名字, 例如 `ifcfg-eno16777736`.

## 使用 ifconfig 命令确认电脑网卡名称

```bash
[root@ryanjie Desktop]$ ifconfig
eno16777736: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether 00:0c:29:d3:40:89  txqueuelen 1000  (Ethernet)
        RX packets 24  bytes 2290 (2.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 0  (Local Loopback)
        RX packets 394  bytes 31648 (30.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 394  bytes 31648 (30.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## 切换到网卡配置文件目录

```bash
[root@ryanjie Desktop]$ cd /etc/sysconfig/network-scripts/
```

## 修改网卡配置信息

- HWADDR = 00:0C:29:D3:40:89 // 网卡 MAC 地址
- TYPE = Ethernet // Ethernet 以太网 onboard 内置
- BOOTPROTO = dhcp // 启动协议: dhcp 动态地址协议 static 静态地址协议
- DEFROUTE = yes // 默认路由
- PEERDNS = no // 使用 DNS 选项的值替代 /etc/resolv.conf 中的配置. 如果使用 DHCP, yes 则为的默认
- PEERROUTES = yes // 使用 路由选项的值替代 /etc/resolv.conf 中的配置.
- IPV4_FAILURE_FATAL = no // 如果 IPv4 配置失败, 此接口不会被禁用
- IPV6INIT = yes // 是否支持 IPV6 初始化
- IPV6_AUTOCONF = yes //是否 IPV6 自动配置
- IPV6_DEFROUTE = yes // IPV6 默认路由
- IPV6_PEERDNS = no // 与 IPV4 PEERDNS 同理
- IPV6_PEERROUTES = yes // 与 IPV4 PEERROUTES 同理
- IPV6_FAILURE_FATAL = no // 如果 IPV6 配置失败, 此接口不会被禁用的
- NAME = eno16777736 // 网卡名称
- UUID = 1ca24e02-2c2e-4a41-b496-6d02147aeb2b // 通用唯一标识码
- ONBOOT = yes // 配置是否随网络服务启动设备生效
- IPADDR = 192.168.10.10 // IP 地址
- NETMASK = 255.255.255.0 // 子网掩码
- GATEWAY = 192.168.10.1 // 网关地址
- DNS1 = 180.76.76.76 // DNS 地址 1
- DNS2 = 101.6.6.6 // DNS 地址 2
- DNS3 = 117.50.11.11 // DNS 地址 3

### 桥接模式 VMnet0

![vmnet0-vmnet8](https://img.zxj.guru/learn/linux/03/vmnet0-vmnet8.jpg)

虚拟机的网络配置方式采用桥接模式 (bridged networking) , 在这种模式下, VMWare 虚拟出来的操作系统就像是局域网中的一台独立的主机, 它可以访问局域网内任何一台机器. 在桥接模式下, 如果设置 IP 启动协议为静态地址协议 `BOOTPROTO = static` , 你需要手工为虚拟系统配置 IP 地址, 子网掩码, 而且还要和宿主机器处于同一网段, 这样虚拟系统才能和宿主机器进行通信. 同时, 配置好网关和 DNS 的地址后, 以实现通过局域网的网关或路由器访问互联网. 桥接模式相当于是交换机上又接了个独立主机, 这个在不好的时候是会向子网中传递信号的, 一般是作为子网中提供服务用的.

![vmnet0](https://img.zxj.guru/learn/linux/03/vmnet0.jpg)

#### 修改网卡配置信息

- BOOTPROTO = static 静态地址. 一般用于多台机器一起使用时 (防止 IP 冲突) 或者使用 ssh 工具连接虚拟机时 (避免每次开机都要更换 IP 地址)
- BOOTPROTO = dhcp 动态获取, 配置简单.

```bash
[root@ryanjie Desktop]$ vim /etc/sysconfig/network-scripts/ifcfg-eno16777736

HWADDR = 00:0C:29:D3:40:89
TYPE = Ethernet
BOOTPROTO = static
DEFROUTE = yes
PEERDNS = no
PEERROUTES = yes
IPV4_FAILURE_FATAL = no
IPV6INIT = yes
IPV6_AUTOCONF = yes
IPV6_DEFROUTE = yes
IPV6_PEERDNS = yes
IPV6_PEERROUTES = yes
IPV6_FAILURE_FATAL = no
NAME = eno16777736
UUID = 1ca24e02-2c2e-4a41-b496-6d02147aeb2b
ONBOOT = yes
IPADDR = 192.168.1.8
NETMASK = 255.255.255.0
GATEWAY = 192.168.1.1
DNS1 = 180.76.76.76
```

![vmnet0-ifconfig](https://img.zxj.guru/learn/linux/03/vmnet0-ifconfig.png)

### NAT 模式 VMnet8

![vmnet8](https://img.zxj.guru/learn/linux/03/vmnet8.jpg)

#### 查看 VMnet8 路由地址

在宿主机 Windows 的 powershell 中输入 ipconfig 命令查看 VMnet8 的 IP(路由) 地址.

```powershell
$ ipconfig

以太网适配器 VMware Network Adapter VMnet8:

   连接特定的 DNS 后缀 . . . . . . . :
   本地链接 IPv6 地址. . . . . . . . : fe80::f4d1:f28:97f2:8692%2
   IPv4 地址 . . . . . . . . . . . . : 192.168.233.1
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . :
```

VMnet8 路由地址为 `192.168.233.1`

#### 查看 VMnet8 网关地址

在 VMware 的菜单中查看 VMware 的网关地址.

![vmnet8-gateway](https://img.zxj.guru/learn/linux/03/vmnet8-gateway.png)

VMnet8 网关地址为 `192.168.233.2`.

#### 修改网卡配置信息

- BOOTPROTO = static 静态地址. 一般用于多台机器一起使用时 (防止 IP 冲突) 或者使用 ssh 工具连接虚拟机时 (避免每次开机都要更换 IP 地址)
- BOOTPROTO = dhcp 动态获取, 配置简单.

```bash
[root@ryanjie Desktop]$ vim /etc/sysconfig/network-scripts/ifcfg-eno16777736

HWADDR = 00:0C:29:D3:40:89
TYPE = Ethernet
BOOTPROTO = static
DEFROUTE = yes
PEERDNS = no
PEERROUTES = yes
IPV4_FAILURE_FATAL = no
IPV6INIT = yes
IPV6_AUTOCONF = yes
IPV6_DEFROUTE = yes
IPV6_PEERDNS = no
IPV6_PEERROUTES = yes
IPV6_FAILURE_FATAL = no
NAME = eno16777736
UUID = 1ca24e02-2c2e-4a41-b496-6d02147aeb2b
ONBOOT = yes
IPADDR = 192.168.233.6 // 默认最后一位从 3 开始, 1 路由器, 2 网关 (gateway), 255 广播地址 (broadcast)
NETMASK = 255.255.255.0
GATEWAY = 192.168.233.2
DNS1 = 180.76.76.76
```

![vmnet8-ifconfig](https://img.zxj.guru/learn/linux/03/vmnet8-ifconfig.png)

> NAT 相当于是局域网中的局域网, 把 192.168.21.1 当作外网 ip, 重新划分了一个网关 (192.168.233.x) .
>
> 网桥只是把网络桥接起来, 还是原来的网关 (192.168.1.x) , 虚拟机相当于和宿主机是平行关系.

## 重启网络服务

```bash
[root@ryanjie Desktop]$ systemctl restart network
```

## 测试网络

```bash
[root@ryanjie Desktop]$ ping www.baidu.com
PING www.a.shifen.com (220.181.38.150) 56(84) bytes of data.
64 bytes from 220.181.38.150: icmp_seq=1 ttl=128 time=36.6 ms
64 bytes from 220.181.38.150: icmp_seq=2 ttl=128 time=36.2 ms
64 bytes from 220.181.38.150: icmp_seq=3 ttl=128 time=38.7 ms
64 bytes from 220.181.38.150: icmp_seq=4 ttl=128 time=40.6 ms
64 bytes from 220.181.38.150: icmp_seq=5 ttl=128 time=36.0 ms
^C
--- www.a.shifen.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4008ms
rtt min/avg/max/mdev = 36.052/37.659/40.611/1.762 ms
[root@ryanjie Desktop]$
```

![rhel-network-config](https://img.zxj.guru/learn/linux/03/rhel-network-config.png)

## 配置 DNS

### DNS 介绍

域名系统 (Domain Name System 缩写 DNS, Domain Name 被译为域名) 是因特网的一项核心服务, 它作为可以将域名和 IP 地址相互映射的一个分布式数据库, 能够使人更方便的访问互联网, 而不用去记住能够被机器直接读取的 IP 数串.

域名系统 (Domain Name System,DNS) 是 Internet 上解决网上机器命名的一种系统. 就像拜访朋友要先知道别人家怎么走一样, Internet 上当一台主机要访问另外一台主机时, 必须首先获知其地址, TCP/IP 中的 IP 地址是由四段以"."分开的数字组成, 记起来总是不如名字那么方便, 所以, 就采用了域名系统来管理名字和 IP 的对应关系.

> 有时候我们会碰到 DNS 劫持, 比如打开网站莫名其妙被跳转到别的地方, 没有广告的网站莫名其妙多出了广告, 使用运营商的错误页面, 或者是无法访问的网站被强制跳转到特定页面 (移不动公司最爱做的事之一) , 这时候就需要更换一个靠谱的 DNS 来解决这些问题, 这款软件就能帮到你!
>
> ```bash
> nslookup whether.114dns.com 114.114.114.114
> ```
>
> 如果解析的结果中有 127.0.0.1 之类的就说明你可能被劫持了, 这种情况下更换 dns 可能也无法达到避免劫持的效果.
> 包括想用运营商 dns 又不想要被劫持的同学, 都可以尝试拨打运营商客服电话, 要求他们把你加入白名单, 如果他们不处理, 也可以尝试向工信部反映情况, 一般都直接给你加白名单完事了, 不然你投诉上去, 对他们也会有一定的影响.
>
> 挑选适合自己的公共 DNS 小工具 - [DNS 优选 (挑选适合自己的 DNS, 拒绝 DNS 劫持)](https://www.52pojie.cn/thread-1129234-1-1.html)

### 常用公共 DNS

| DNS 名称       | DNS1            | DNS2            |
| -------------- | --------------- | --------------- |
| 百度 DNS       | 180.76.76.76    |                 |
| ONE DNS 拦截版 | 117.50.11.11    | 52.80.66.66     |
| TUNA DNS       | 101.6.6.6       |                 |
| ONE DNS 纯净版 | 117.50.10.10    | 52.80.52.52     |
| 阿里 DNS       | 233.5.5.5       | 233.6.6.6       |
| 中国互联网中心 | 210.2.4.8       |                 |
| 腾讯 DNS       | 119.29.29.29    | 182.254.116.116 |
| 114DNS         | 114.114.114.114 | 114.114.115.115 |
| PdoMo-DNS      | 101.132.183.99  | 193.112.15.186  |
| DNS 派         | 101.226.4.6     | 218.30.118.6    |
| 谷歌 DNS       | 8.8.8.8         | 8.8.4.4         |
| BAI DNS        | 223.113.97.99   |                 |
| Open DNS       | 208.67.222.222  | 208.67.220.220  |
| IBM Quad9      | 9.9.9.95        |                 |

### DNS 配置

```bash
[root@ryanjie Desktop]$ vim /etc/resolv.conf
[root@ryanjie Desktop]$ cat /etc/resolv.conf
# Generated by NetworkManager
domain localdomain
search localdomain
nameserver 180.76.76.76
nameserver 101.6.6.6
nameserver 117.50.11.11
[root@ryanjie Desktop]$ ping www.baidu.com
PING www.a.shifen.com (14.215.177.39) 56(84) bytes of data.
64 bytes from 14.215.177.39: icmp_seq=1 ttl=128 time=49.0 ms
64 bytes from 14.215.177.39: icmp_seq=2 ttl=128 time=49.0 ms
64 bytes from 14.215.177.39: icmp_seq=3 ttl=128 time=49.6 ms
64 bytes from 14.215.177.39: icmp_seq=4 ttl=128 time=49.4 ms
64 bytes from 14.215.177.39: icmp_seq=5 ttl=128 time=49.0 ms
^C
--- www.a.shifen.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4004ms
rtt min/avg/max/mdev = 49.020/49.258/49.695/0.326 ms
[root@ryanjie Desktop]$
```

![rhel-dns-confg](https://img.zxj.guru/learn/linux/03/rhel-dns-confg.png)

## 参考

- [Linux 最小安装 + 桥接模式 + 网络配置](https://blog.csdn.net/fxq8866/article/details/50776184)

- [Linux 配置网卡](https://www.cnblogs.com/aknife/p/11181805.html)

- [NAT 和桥接的区别](https://www.cnblogs.com/wmxl/p/9379562.html)

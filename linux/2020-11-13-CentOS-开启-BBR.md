---
title: CentOS 开启 BBR
abstract: Bottleneck Bandwidth and Round-trip propagation time（BBR），是 Google 在2016年开发的 TCP 拥塞控制算法，可以使 Linux 服务器显着地提高吞吐量和减少 TCP 连接的延迟。
url: centos-enable-bbr
permalink: centos-enable-bbr
date: 2020-11-13 21:42:36
category:
  - CentOS
tags:
  - CentOS
---

![centos-enable-bbr](https://img.zxj.guru/2020/11/centos-enable-bbr.png)

Bottleneck Bandwidth and Round-trip propagation time（BBR），是 Google 在 2016 年开发的 TCP 拥塞控制算法，可以使 Linux 服务器显着地提高吞吐量和减少 TCP 连接的延迟。

> 注意：
>
> 1. 由于是使用最新版系统内核，最好请勿在生产环境安装，以免产生不可预测之后果。
> 2. BBR 不支持虚拟方式为 OpenVZ 和 LXC 的服务器。如果你的服务器使用以下命令返回 `openvz`, `lxc` 字段，那么你就没必要继续阅读本文了 😂。如果返回其它字段（例如：`kvm`, `xen` , `vmware` 等），那么你可以参考以下步骤开启 BBR。
>
>    ```bash
>    echo $(systemd-detect-virt)
>    echo $(virt-what)
>    ```

---

> TCP BBR（Bottleneck Bandwidth and Round-trip propagation time）是由 Google 设计，于 2016 年发布的拥塞算法。以往大部分拥塞算法是基于丢包来作为降低传输速率的信号，而 BBR 则基于模型主动探测。该算法使用网络最近出站数据分组当时的最大带宽和往返时间来创建网络的显式模型。数据包传输的每个累积或选择性确认用于生成记录在数据包传输过程和确认返回期间的时间内所传送数据量的采样率。[39]该算法认为随着网络接口控制器逐渐进入千兆速度时，与缓冲膨胀相关的延迟相比丢包更应该被认为是识别拥塞的主要决定因素，所以基于延迟模型的拥塞控制算法（如 BBR）会有更高的吞吐量和更低的延迟，可以用 BBR 来替代其他流行的拥塞算法，例如 CUBIC。Google 在 YouTube 上应用该算法，将全球平均的 YouTube 网络吞吐量提高了 4%，在一些国家超过了 14%。[40]
>
> BBR 之后移植入 Linux 内核 4.9 版本，[41][42]并且对于 QUIC 可用。
>
> BBR 效率很高，速度也很快，但是它与非 BBR 的流的公平性有争议。虽然谷歌的展示显示 BBR 与 CUBIC 共存良好，但像杰夫·休斯顿和霍克、布利斯和齐特巴特等研究者发现它对其他流不公平，并且不可扩展。[43]霍克等人还发现，在 Linux 4.9 的 BBR 实现中"存在一些严重的固有问题，如排队延迟增加、不公平和大量数据包丢失"。[44]
>
> 索海尔·阿巴斯洛等人(C2TCP 的作者)指出，BBR 在动态环境中表现不佳，比如蜂窝网络。[45][46]他们还表明 BBR 存在不公平问题。例如，当一个 CUBIC 流(在 Linux、Android 和 MacOS 中是默认的 TCP 实现)与网络中的 BBR 流共存时，BBR 流可以支配 CUBIC 流并从中获得整个链路带宽[45]。
>
> -- [TCP BBR - Wikipedia](https://zh.wikipedia.org/wiki/TCP拥塞控制#TCP_BBR)

## 一键脚本

> 以下一键脚本内容转载于：[一键安装最新内核并开启 BBR 脚本 | 秋水逸冰](https://teddysun.com/489.html)

### 本脚本适用环境

- 系统支持：CentOS 6+，Debian 8+，Ubuntu 16+
- 虚拟技术：OpenVZ 以外的，比如 KVM、Xen、VMware
- 内存要求：≥128M
- 日期　　：2020 年 9 月 8 日

### 关于本脚本

1. 本脚本已在 **Vultr** 上的 VPS 全部测试通过。
2. 当脚本检测到 VPS 的虚拟方式为 OpenVZ 时，会提示错误，并自动退出安装。
3. 脚本运行完重启发现开不了机的，打开 VPS 后台控制面板的 VNC, 开机卡在 grub 引导, 手动选择内核即可。
4. 由于是使用最新版系统内核，最好请勿在生产环境安装，以免产生不可预测之后果。

### 使用方法

使用 root 用户登录，运行以下命令：

```bash
wget --no-check-certificate -O /opt/bbr.sh https://github.com/teddysun/across/raw/master/bbr.sh
chmod 755 /opt/bbr.sh
/opt/bbr.sh
```

安装完成后，脚本会提示需要重启 VPS，输入 y 并回车后重启。
重启完成后，进入 VPS，验证一下是否成功安装最新内核并开启 TCP BBR，输入以下检查：

1. 查看内核版本

   ```bash
   uname -r
   ```

   查看内核版本，显示为新版内核就表示 OK 了。

2. 验证是否成功开启了 BBR。

   ```bash
   sysctl net.ipv4.tcp_available_congestion_control
   # 返回值一般为：
   # net.ipv4.tcp_available_congestion_control = bbr cubic reno
   # 或者：
   # net.ipv4.tcp_available_congestion_control = reno cubic bbr
   ```

   ```bash
   sysctl net.ipv4.tcp_congestion_control
   # 返回值一般为：
   # net.ipv4.tcp_congestion_control = bbr
   ```

   ```bash
   sysctl net.core.default_qdisc
   # 返回值一般为：
   # net.core.default_qdisc = fq
   ```

3. 查看内核模块是否加载。

   ```bash
   lsmod | grep bbr
   ```

   返回值有 tcp_bbr 模块即说明 bbr 已启动。比如：

   ```bash
   tcp_bbr                20480  3
   ```

   > 注意：并不是所有的 VPS 都会有此返回值，若没有也属正常。

### 特别说明

如果你使用的是 Google Cloud Platform （GCP）更换内核，有时会遇到重启后，整个磁盘变为只读的情况。只需执行以下命令即可恢复：

```bash
mount -o remount rw /
```

## CentOS 7 手动开启

### 更换内核

由于开启 BBR 需 4.10 以上版本 Linux 内核，如果您的 Linux 服务器内核低于 4.10（例如：腾讯云控制台安装的 CentOS 7 系统内核是 `3.10`，低于开启 BBR 最低要求的版本 `4.10`，所以我们需要手动更换为默认内核后再作升级）。

手动更换内核的步骤可以看我之前的文章：[CentOS 手动更换内核](https://www.zxj.guru/centos-upgrade-kernel.html)。

### 开启 BBR

1. 编辑 `/etc/sysctl.conf` 文件，添加如下内容。

   ```bash
   net.core.default_qdisc=fq
   net.ipv4.tcp_congestion_control=bbr
   #bash
   sudo sed -i '/net.core.default_qdisc/d' /etc/sysctl.conf
   sudo sed -i '/net.ipv4.tcp_congestion_control/d' /etc/sysctl.conf
   sudo echo "net.core.default_qdisc = fq" >> /etc/sysctl.conf
   sudo echo "net.ipv4.tcp_congestion_control = bbr" >> /etc/sysctl.conf
   ```

2. 从配置文件中加载内核参数设置。

   ```bash
   sysctl -p >/dev/null 2>&1
   ```

3. 验证是否成功开启了 BBR。

   ```bash
   sysctl net.ipv4.tcp_available_congestion_control | grep -o 'net.ipv4.tcp_available_congestion_control = reno cubic bbr'
   sysctl net.ipv4.tcp_available_congestion_control | grep -o 'net.ipv4.tcp_available_congestion_control = bbr cubic reno'
   # 高亮显示如下任意一条内容即可：
   # net.ipv4.tcp_available_congestion_control = reno cubic bbr
   # net.ipv4.tcp_available_congestion_control = bbr cubic reno
   ```

   ```bash
   sysctl net.ipv4.tcp_congestion_control | grep -o 'net.ipv4.tcp_congestion_control = bbr'
   # 高亮显示如下内容即可：
   # net.ipv4.tcp_congestion_control = bbr
   ```

   ```bash
   sysctl net.ipv4.tcp_available_congestion_control | grep -o 'net.ipv4.tcp_available_congestion_control = reno cubic bbr'
   # 高亮显示如下内容即可：
   # net.ipv4.tcp_available_congestion_control = reno cubic bbr
   ```

4. 查看内核模块是否加载。

   ```bash
   $ lsmod | grep bbr
   tcp_bbr                20480  1
   ```

5. 更改文件权限。

   ```bash
   sudo chmod 644 /etc/sysctl.conf
   ```

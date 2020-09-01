---
title: Windows Server 系统 DD 镜像
date: 2019-07-18 22:12:34
categories: System
tags: System
---

<!-- more -->

<!-- TOC -->

- [Windows Server 系统 DD 镜像](#windows-server-系统-dd-镜像)
  - [镜像列表](#镜像列表)
  - [镜像特点](#镜像特点)
  - [安装方式](#安装方式)
    - [在基于 virtio 的 KVM 上安装过程](#在基于-virtio-的-kvm-上安装过程)
    - [在 Kimsufi 的服务器上安装过程](#在-kimsufi-的服务器上安装过程)
    - [远程桌面的默认用户名和密码](#远程桌面的默认用户名和密码)
  - [下载链接(DD download URL)](#下载链接dd-download-url)
    - [链接地址 1](#链接地址-1)
    - [链接地址 2](#链接地址-2)
    - [KMS 客户端安装密钥](#kms-客户端安装密钥)
  - [校验信息](#校验信息)
  - [写在最后](#写在最后)

<!-- /TOC -->

<a id="markdown-windows-server-系统-dd-镜像" name="windows-server-系统-dd-镜像"></a>

# Windows Server 系统 DD 镜像

> 原文地址：[介绍几款 Windows DD 镜像](https://teddysun.com/545.html)
>
> 作者： [秋水逸冰](https://teddysun.com/author/teddysun)

DD 命令是 Linux 下的磁盘读写常用命令。它可以将已有的硬盘镜像文件直接写到硬盘上。通过 DD 命令，我们可以把系统由 Linux 改造成 Windows，这样不仅能获得一个纯净的系统，而且也能省下不少费用。网上 DD 镜像文件有很多，但是鱼龙混杂，不是版本不合适，就是害怕有后门木马。

<a id="markdown-镜像列表" name="镜像列表"></a>

## 镜像列表

1. 中文版 Windows Server 2019 Datacenter
2. 英文版 Windows Server 2019 Datacenter
3. 日文版 Windows Server 2019 Datacenter
4. 中文版 Windows Server 2016 Datacenter
5. 英文版 Windows Server 2016 Datacenter
6. 日文版 Windows Server 2016 Datacenter
7. 中文版 Windows Server 2012 R2 Datacenter
8. 英文版 Windows Server 2012 R2 Datacenter
9. 日文版 Windows Server 2012 R2 Datacenter

以上镜像按顺序，分别基于以下 MSDN 原版镜像制作完成：

1. cn_windows_server_2019_x64_dvd_2d80e042.iso
2. en_windows_server_2019_x64_dvd_3c2cf1202.iso
3. ja_windows_server_2019_x64_dvd_d7f8ec54.iso
4. cn_windows_server_2016_vl_x64_dvd_11636695.iso
5. en_windows_server_2016_vl_x64_dvd_11636701.iso
6. ja_windows_server_2016_vl_x64_dvd_11645964.iso
7. cn_windows_server_2012_r2_vl_with_update_x64_dvd_6052729.iso
8. en_windows_server_2012_r2_vl_with_update_x64_dvd_6052766.iso
9. ja_windows_server_2012_r2_vl_with_update_x64_dvd_6052800.iso

<a id="markdown-镜像特点" name="镜像特点"></a>

## 镜像特点

1. 集成 virtio 驱动以及 Intel 的网卡驱动， 因此适用于大部分 KVM 的 VPS 以及 Kimsufi 服务器
2. 无需 VNC 交互直接无人值守安装， DD 完成即可远程登录桌面
3. 基于 VOL 版制作，因此可用 KMS 方式激活系统
4. 关闭 Ctrl + Alt + Del 快捷键登录方式
5. 关闭服务器管理器开机自启动
6. 关闭 IE 安全增强配置
7. 开启 Windows 远程桌面
8. 关闭 Windows 自带防火墙
9. 其他基于 Dism++ 自带的一些系统优化，如去掉快捷方式小箭头等

<a id="markdown-安装方式" name="安装方式"></a>

## 安装方式

目前经过测试已在腾讯云，Vultr，DigitalOcean，Cloudcone，Kimsufi 上成功安装。

<a id="markdown-在基于-virtio-的-kvm-上安装过程" name="在基于-virtio-的-kvm-上安装过程"></a>

### 在基于 virtio 的 KVM 上安装过程

选 CentOS 7 或 Debian 9 系统。内存不能太小，建议 4GB 起步。用 root 用户 ssh 进去后执行以下的命令，然后静静等待即可。
安装速度取决于网络下载镜像的速度，基本上等待 15 – 60 分钟后，再次打开 VNC 就能看到熟悉的 Windows 登录界面了。

```bash
wget -qO DebianNET.sh qiu.sh/dd && bash DebianNET.sh -dd "DD download URL"
```

注：DebianNET.sh 脚本由 Vicer 开发，参考网址：[https://moeclub.org](https://moeclub.org/)

<a id="markdown-在-kimsufi-的服务器上安装过程" name="在-kimsufi-的服务器上安装过程"></a>

### 在 Kimsufi 的服务器上安装过程

进入救援模式后，用 root 用户 ssh 进去后执行以下的命令，然后静静等待即可。

```bash
wget -O- "DD download URL" | gunzip | dd of=/dev/sda
```

注：关于 Kimsufi 的服务器如何进入救援模式，网上有很多图文教程，一搜便知。

<a id="markdown-远程桌面的默认用户名和密码" name="远程桌面的默认用户名和密码"></a>

### 远程桌面的默认用户名和密码

用户名: `administrator`
密码: `Password147`

**注意：请在安装完成后登录远程桌面，立即进行 Windows 自动更新以及修改 Administrator 的密码。**
**注意：请在安装完成后登录远程桌面，立即进行 Windows 自动更新以及修改 Administrator 的密码。**
**注意：请在安装完成后登录远程桌面，立即进行 Windows 自动更新以及修改 Administrator 的密码。**

<a id="markdown-下载链接dd-download-url" name="下载链接dd-download-url"></a>

## 下载链接(DD download URL)

<a id="markdown-链接地址-1" name="链接地址-1"></a>

### 链接地址 1

（被 VPS 商家取消，以下链接已全部失效，请换成备用链接）

- ~~[cn_windows2019.gz](https://la1.teddyvps.com/iso/cn_windows2019.gz)~~
- ~~[en_windows2019.gz](https://la1.teddyvps.com/iso/en_windows2019.gz)~~
- ~~[ja_windows2019.gz](https://la1.teddyvps.com/iso/ja_windows2019.gz)~~
- ~~[cn_windows2016.gz](https://la1.teddyvps.com/iso/cn_windows2016.gz)~~
- ~~[en_windows2016.gz](https://la1.teddyvps.com/iso/en_windows2016.gz)~~
- ~~[ja_windows2016.gz](https://la1.teddyvps.com/iso/ja_windows2016.gz)~~
- ~~[cn_windows2012r2.gz](https://la1.teddyvps.com/iso/cn_windows2012r2.gz)~~
- ~~[en_windows2012r2.gz](https://la1.teddyvps.com/iso/en_windows2012r2.gz)~~
- ~~[ja_windows2012r2.gz](https://la1.teddyvps.com/iso/ja_windows2012r2.gz)~~

<a id="markdown-链接地址-2" name="链接地址-2"></a>

### 链接地址 2

（感谢 HKServerSolution 的分流下载）

- [cn_windows2019.gz](https://delivery.yuntu.moe/teddysun/cn_windows2019.gz)
- [en_windows2019.gz](https://delivery.yuntu.moe/teddysun/en_windows2019.gz)
- [ja_windows2019.gz](https://delivery.yuntu.moe/teddysun/ja_windows2019.gz)
- [cn_windows2016.gz](https://delivery.yuntu.moe/teddysun/cn_windows2016.gz)
- [en_windows2016.gz](https://delivery.yuntu.moe/teddysun/en_windows2016.gz)
- [ja_windows2016.gz](https://delivery.yuntu.moe/teddysun/ja_windows2016.gz)
- [cn_windows2012r2.gz](https://delivery.yuntu.moe/teddysun/cn_windows2012r2.gz)
- [en_windows2012r2.gz](https://delivery.yuntu.moe/teddysun/en_windows2012r2.gz)
- [ja_windows2012r2.gz](https://delivery.yuntu.moe/teddysun/ja_windows2012r2.gz)

<a id="markdown-kms-客户端安装密钥" name="kms-客户端安装密钥"></a>

### KMS 客户端安装密钥

[KMS 客户端安装密钥 kmsclientkeys](https://docs.microsoft.com/zh-cn/windows-server/get-started/kmsclientkeys)

<a id="markdown-校验信息" name="校验信息"></a>

## 校验信息

镜像文件名. 大小. SHA-1 和 MD5 信息如下

1. cn_windows2019.gz, 4.14GB, 7c54a1b070457c191622cdafffb8766718d931c6, 42c9d56eab7cef089a88476d69f2bb54
2. en_windows2019.gz, 3.66GB, 355140cd63be0b4bc2c1231502a1e333ad0051d2, 1addafe1352ee50f0663641c8334b61a
3. ja_windows2019.gz, 4.07GB, d602c215fbb28cc1b7d856f0d7133823bd41c771, c0ebb59138e2a2e423f45a01c565bb65
4. cn_windows2016.gz, 4.21GB, e5327ad1858d44428be9f14b7e636eb11e98bda6, 2ce003299e940c1327e70340e38599b8
5. en_windows2016.gz, 4.05GB, f74f0725c1673b64ab2271d570980b7b82e562b3, cebad56bc1da0f469c4fa6363bf7fa58
6. ja_windows2016.gz, 4.12GB, 709fceb1dba296b04c385bfa60190dcf16187583, c4c000d02901d1eec10d53ee97e743ab
7. cn_windows2012r2.gz, 4.51GB, 8d9f3966e251e2f31ddfd3d06f00436fa002f774, c91d8181b2af823d35c54d2c2568b50e
8. en_windows2012r2.gz, 3.72GB, 81d93cb457abe13d455d639f957f826a4893aa33, 6138ebc7a083c5ca192e8dfe9bfcee93
9. ja_windows2012r2.gz, 4.45GB, 8aae0fb972358a445cb3d44677b36e999e385bad, 6abab80539c48a7f5c147f93af4e974e

<a id="markdown-写在最后" name="写在最后"></a>

## 写在最后

1. 这些镜像仅出于学习目的制作，如您需要长期使用，请使用正版 Windows key 激活系统。
2. 镜像全部是由原版 MSDN 制作完成，本人可以保证没有夹带任何私货，若不相信本人者，请不要使用。
3. 在某些基于 KVM 的 VPS 上安装完成后，比如 Vultr，DigitalOcean，第一次登录远程桌面，您会看到一个黑窗口一闪而过，那是自动识别分区的命令在执行。因此，无需您手动扩展，硬盘已自动扩展成功。
4. Windows Server 2019 的 DD 镜像为 15GB 的 VHD，其余皆为 12GB 的 VHD，有时在某些服务器上安装成功后需要手动扩展磁盘，比如 Kimsufi。
5. 使用 Windows DD 镜像有可能会违反某些商家的 TOS，如果因为使用本人制作的镜像而导致被商家惩罚，本人概不负责。
6. **注意：请在安装完成后登录远程桌面，立即进行 Windows 自动更新打补丁以及修改 Administrator 的密码（建议使用密码生成器，30 位左右即可）。**

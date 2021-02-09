---
title: 部署虚拟环境安装 RHEL 7 系统
url: install-rhel-7
---

# 部署虚拟环境安装 RHEL 7 系统

Linux 操作系统安装方式：

- 基于光盘介质实现系统安装；（硬件服务器有光驱设备）
- 基于 U 盘、移动硬盘实现系统安装；（要求服务器 USB 接口）
- 基于批量的工具：Kickstart、Cobbler 实现系统安装；
- 基于虚拟机应用程序实现系统安装；（VMWare，VirtualBox，WSL，Windows 下的 Docker）
- 基于 Docker 应用程序实现系统安装；（指 Linux 下的 Docker 安装 Linux）

> 建议在学习期间建议不要把 Linux 系统安装到真机上面，因为在学习过程中都免不了要"折腾"您的 Linux 操作系统。推荐使用虚拟机应用程序实现系统安装。通过虚拟机软件安装的系统不仅可以模拟出硬件资源，把实验环境与真机文件分离保证数据安全，更酷的是当操作失误或配置有误导致系统异常的时候，可以快速把操作系统还原至出错前的环境状态，进而减少重装系统的等待时间（在真机上安装 Linux 操作系统每次至少需要 30 分钟）。

## 工具下载

> [https://www.linuxprobe.com/tools](https://www.linuxprobe.com/tools)

### RHEL 7

- 百度网盘 1：[https://pan.baidu.com/s/1eGfv3_E9dtAGuLc0iJaEOw#3e6m](https://pan.baidu.com/s/1eGfv3_E9dtAGuLc0iJaEOw#3e6m) 验证码 3e6m
- 百度网盘 2：[http://pan.baidu.com/s/1dEWdcch#j94c](http://pan.baidu.com/s/1dEWdcch#j94c) 验证码 j94c
- 本站分流 1：[https://file.ryanjie.cn/ISO/Red.Hat.Enterprise.Linux](https://file.ryanjie.cn/ISO/Red.Hat.Enterprise.Linux)
- 本站分流 2：[https://pan.ryanjie.cn](https://pan.ryanjie.cn) 路径：`/ISO/Red.Hat.Enterprise.Linux`

> **文件校验**
>
> ```ini
> 文件名称: RHEL-server-7.0-x86_64-LinuxProbe.Com.iso
> 文件大小: 3.48 GB (3,743,416,320 字节)
> MD5: 08961a5cb32d2cdf72026bec43876b7f
> SHA1: ce5b360b8ef96fa2105a13cf981f2e3d148931d6
> SHA256: 85a9fedc2bf0fc825cc7817056aa00b3ea87d7e111e0cf8de77d3ba643f8646c
> ```

### RHEL 8

- 百度网盘 1：[https://pan.baidu.com/s/1B1NH0SM7TIYW9HSmgrf50g](https://pan.baidu.com/s/1B1NH0SM7TIYW9HSmgrf50g) 验证码 brik
- 百度网盘 2：[https://pan.baidu.com/s/1BpE-ggM7cCdqmztvBE74Og#y5hw](https://pan.baidu.com/s/1BpE-ggM7cCdqmztvBE74Og#y5hw) 验证码 y5hw
- 本站分流 1：[https://file.ryanjie.cn/ISO/Red.Hat.Enterprise.Linux](https://file.ryanjie.cn/ISO/Red.Hat.Enterprise.Linux)
- 本站分流 2：[https://pan.ryanjie.cn](https://pan.ryanjie.cn) 路径：`/ISO/Red.Hat.Enterprise.Linux`

> **文件校验**
>
> ```ini
> 文件名称: rhel-8.0-x86_64-linuxprobe.com.iso
> 文件大小: 6.61 GB (7,103,053,824 字节)
> MD5: 8a0bca1c323ad8628b09d0a7cce43f39
> SHA1: 66cad03832dbc99206d2dddd935c3174f8b3cff5
> SHA256: 005d4f88fff6d63b0fc01a10822380ef52570edd8834321de7be63002cc6cc43
> ```

## 虚拟机安装 RHEL 7

详细步骤建议看刘遄老师的文章（文章讲的很详细，这里就不复制粘贴了~）：[第 1 章 部署虚拟环境安装 linux 系统 | 《Linux 就该这么学》](https://www.linuxprobe.com/chapter-01.html)

> Linux 操作系统对硬盘进行分区，企业 300G 硬盘规范：
>
> - `/boot` 分区，300MB，称之为 Linux 内核引导分区，Linux 系统启动时加载和读取内核镜像，从而启动 Linux 操作系统；
> - `Swap` 分区，512MB，交换分区，称为虚拟内存，当物理内存不足时，应用程序可以使用虚拟内存；
> - `/` 根分区，40GB，根文件系统，所有分区、目录的起始挂载点，Linux 系统核心分区，存储 Linux 系统必备的软件、库文件等；
> - `/data` 分区，剩余空间大小，数据分区，主要是用于存储各种应用数据、软件程序、WEB 网站、数据库等；

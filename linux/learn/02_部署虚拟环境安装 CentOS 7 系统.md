---
title: 部署虚拟环境安装 CentOS 7 系统
url: install-centos-7
---

# 部署虚拟环境安装 CentOS 7 系统

Linux 操作系统安装方式：

- 基于光盘介质实现系统安装；（硬件服务器有光驱设备）
- 基于 U 盘、移动硬盘实现系统安装；（要求服务器 USB 接口）
- 基于批量的工具：Kickstart、Cobbler 实现系统安装；
- 基于虚拟机应用程序实现系统安装；（VMWare，VirtualBox，WSL，Windows 下的 Docker）
- 基于 Docker 应用程序实现系统安装；（指 Linux 下的 Docker 安装 Linux）

> 建议在学习期间建议不要把 Linux 系统安装到真机上面，因为在学习过程中都免不了要"折腾"您的 Linux 操作系统。推荐使用虚拟机应用程序实现系统安装。通过虚拟机软件安装的系统不仅可以模拟出硬件资源，把实验环境与真机文件分离保证数据安全，更酷的是当操作失误或配置有误导致系统异常的时候，可以快速把操作系统还原至出错前的环境状态，进而减少重装系统的等待时间（在真机上安装 Linux 操作系统每次至少需要 30 分钟）。

## 工具下载

> [https://www.linuxprobe.com/tools](https://www.linuxprobe.com/tools)

CentOS，是基于 Red Hat Linux 提供的可自由使用源代码的企业级 Linux 发行版本；是一个稳定，可预测，可管理和可复制的免费企业级计算平台。

## CentOS 镜像下载

### 镜像区别

- DVD ISO：完整安装版镜像，可离线安装到计算机硬盘上，包含常用软件，一般推荐下载这个镜像。
- NetInstall ISO：在线安装版本/救援系统镜像，启动后需要联网边下载边安装，带宽大的可以选择这种。
- Everything ISO：包含了完整安装版的内容，并对其进行补充，集成了所有软件。至少需要 10G 左右空间。
- Minimal ISO：精简版的镜像，可以安装一个基本的 CentOS 系统，包含了可启动系统基本所需的最小安装包。
- LiveGNOME/LiveKDE ISO: 在精简版镜像的基础上集成了 GNOME/KDE 桌面环境。

### sha256sum

```markdown
689531cce9cf484378481ae762fae362791a9be078fda10e4f6977bf8fa71350 CentOS-7-x86_64-Everything-2009.iso
b79079ad71cc3c5ceb3561fff348a1b67ee37f71f4cddfec09480d4589c191d6 CentOS-7-x86_64-NetInstall-2009.iso
07b94e6b1a0b0260b94c83d6bb76b26bf7a310dc78d7a9c7432809fb9bc6194a CentOS-7-x86_64-Minimal-2009.iso
e33d7b1ea7a9e2f38c8f693215dd85254c3a4fe446f93f563279715b68d07987 CentOS-7-x86_64-DVD-2009.iso
```

### 镜像下载

**镜像下载之后一定要使用校验工具校验 sha256sum。**

#### 阿里

| 镜像                                                                                                                               | 大小      |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [CentOS-7-x86_64-DVD-2009.iso](https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso)                       | 4.4 GiB   |
| [CentOS-7-x86_64-DVD-2009.torrent](https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.torrent)               | 176.1 KiB |
| [CentOS-7-x86_64-Everything-2009.iso](https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.iso)         | 9.5 GiB   |
| [CentOS-7-x86_64-Everything-2009.torrent](https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.torrent) | 380.6 KiB |
| [CentOS-7-x86_64-Minimal-2009.iso](https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.iso)               | 973.0 MiB |
| [CentOS-7-x86_64-Minimal-2009.torrent](https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.torrent)       | 38.6 KiB  |
| [CentOS-7-x86_64-NetInstall-2009.iso](https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-NetInstall-2009.iso)         | 575.0 MiB |
| [CentOS-7-x86_64-NetInstall-2009.torrent](https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-NetInstall-2009.torrent) | 23.0 KiB  |

#### 腾讯

| 镜像                                                                                                                                      | 大小      |
| ----------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [CentOS-7-x86_64-DVD-2009.iso](https://mirrors.cloud.tencent.com/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso)                       | 4.4 GiB   |
| [CentOS-7-x86_64-DVD-2009.torrent](https://mirrors.cloud.tencent.com/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.torrent)               | 176.1 KiB |
| [CentOS-7-x86_64-Everything-2009.iso](https://mirrors.cloud.tencent.com/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.iso)         | 9.5 GiB   |
| [CentOS-7-x86_64-Everything-2009.torrent](https://mirrors.cloud.tencent.com/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.torrent) | 380.6 KiB |
| [CentOS-7-x86_64-Minimal-2009.iso](https://mirrors.cloud.tencent.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.iso)               | 973.0 MiB |
| [CentOS-7-x86_64-Minimal-2009.torrent](https://mirrors.cloud.tencent.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.torrent)       | 38.6 KiB  |
| [CentOS-7-x86_64-NetInstall-2009.iso](https://mirrors.cloud.tencent.com/centos/7/isos/x86_64/CentOS-7-x86_64-NetInstall-2009.iso)         | 575.0 MiB |
| [CentOS-7-x86_64-NetInstall-2009.torrent](https://mirrors.cloud.tencent.com/centos/7/isos/x86_64/CentOS-7-x86_64-NetInstall-2009.torrent) | 23.0 KiB  |

#### HUAWEI

| 镜像                                                                                                                                    | 大小      |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [CentOS-7-x86_64-DVD-2009.iso](https://mirrors.huaweicloud.com/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso)                       | 4.4 GiB   |
| [CentOS-7-x86_64-DVD-2009.torrent](https://mirrors.huaweicloud.com/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.torrent)               | 176.1 KiB |
| [CentOS-7-x86_64-Everything-2009.iso](https://mirrors.huaweicloud.com/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.iso)         | 9.5 GiB   |
| [CentOS-7-x86_64-Everything-2009.torrent](https://mirrors.huaweicloud.com/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.torrent) | 380.6 KiB |
| [CentOS-7-x86_64-Minimal-2009.iso](https://mirrors.huaweicloud.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.iso)               | 973.0 MiB |
| [CentOS-7-x86_64-Minimal-2009.torrent](https://mirrors.huaweicloud.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.torrent)       | 38.6 KiB  |
| [CentOS-7-x86_64-NetInstall-2009.iso](https://mirrors.huaweicloud.com/centos/7/isos/x86_64/CentOS-7-x86_64-NetInstall-2009.iso)         | 575.0 MiB |
| [CentOS-7-x86_64-NetInstall-2009.torrent](https://mirrors.huaweicloud.com/centos/7/isos/x86_64/CentOS-7-x86_64-NetInstall-2009.torrent) | 23.0 KiB  |

#### TUNA

| 镜像                                                                                                                                         | 大小      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [CentOS-7-x86_64-DVD-2009.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso)                       | 4.4 GiB   |
| [CentOS-7-x86_64-DVD-2009.torrent](https://mirrors.tuna.tsinghua.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.torrent)               | 176.1 KiB |
| [CentOS-7-x86_64-Everything-2009.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.iso)         | 9.5 GiB   |
| [CentOS-7-x86_64-Everything-2009.torrent](https://mirrors.tuna.tsinghua.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.torrent) | 380.6 KiB |
| [CentOS-7-x86_64-Minimal-2009.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.iso)               | 973.0 MiB |
| [CentOS-7-x86_64-Minimal-2009.torrent](https://mirrors.tuna.tsinghua.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.torrent)       | 38.6 KiB  |
| [CentOS-7-x86_64-NetInstall-2009.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-NetInstall-2009.iso)         | 575.0 MiB |
| [CentOS-7-x86_64-NetInstall-2009.torrent](https://mirrors.tuna.tsinghua.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-NetInstall-2009.torrent) | 23.0 KiB  |

## 虚拟机安装 CentOS 7

CentOS 7 安装步骤和 RHEL 7 安装基本一致，详细步骤建议看刘遄老师的文章（文章讲的很详细，这里就不复制粘贴了~）：[第 1 章 部署虚拟环境安装 linux 系统 | 《Linux 就该这么学》](https://www.linuxprobe.com/chapter-01.html)

> Linux 操作系统对硬盘进行分区，企业 300G 硬盘规范：
>
> - `/boot` 分区，300MB，称之为 Linux 内核引导分区，Linux 系统启动时加载和读取内核镜像，从而启动 Linux 操作系统；
> - `Swap` 分区，512MB，交换分区，称为虚拟内存，当物理内存不足时，应用程序可以使用虚拟内存；
> - `/` 根分区，40GB，根文件系统，所有分区、目录的起始挂载点，Linux 系统核心分区，存储 Linux 系统必备的软件、库文件等；
> - `/data` 分区，剩余空间大小，数据分区，主要是用于存储各种应用数据、软件程序、WEB 网站、数据库等；

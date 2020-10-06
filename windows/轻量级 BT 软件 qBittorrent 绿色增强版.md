---
title: 轻量级 BT 软件 qBittorrent 绿色增强版
date: 2019-04-16 10:43:10
categories: Program
---

<!-- more -->

<!-- TOC -->

- [轻量级 BT 软件 qBittorrent 绿色增强版](#轻量级-bt-软件-qbittorrent-绿色增强版)
  - [特点](#特点)
  - [更新日志](#更新日志)
    - [v4.2.3.10](#v42310)
    - [v4.2.2.10](#v42210)
    - [v4.1.9.16](#v41916)
  - [软件下载](#软件下载)
    - [Arch Linux](#arch-linux)
    - [Debian](#debian)
    - [openSUSE/RPM-based Linux distro](#opensuserpm-based-linux-distro)
    - [Ubuntu](#ubuntu)
    - [macOS (Homebrew)](#macos-homebrew)
    - [Windows (Chocolatey)](#windows-chocolatey)

<!-- /TOC -->

<a id="markdown-轻量级-bt-软件-qbittorrent-绿色增强版" name="轻量级-bt-软件-qbittorrent-绿色增强版"></a>

# 轻量级 BT 软件 qBittorrent 绿色增强版

qBittorrent，开源轻量级 BitTorrent 客户端，自动过滤器基于 UPnP/NAT-PMP 端口映射，采用 Vuze 兼容协议加密，代理链接，电骡或者 Peerguardian 兼容 IP 过滤，激流排队和优先次序，支持 DHT 网络及 RSS 订阅，使用的 Ajax 技术，下载 BT 种子同时可以调用第三方播放器边下边播，此外具有强大的资源搜索引擎插件。

[github author="c0re100" project="qBittorrent-Enhanced-Edition"][/github]

qBittorrent 是由 Arvid Norberg 使用 C ++ / Qt 编程的 bittorrent 客户端，它使用 libtorrent（有时称为 libtorrent-rasterbar）。

它的目标是成为所有其他 bittorrent 客户的理想选择。 qBittorrent 快速，稳定并且提供 unicode 支持以及许多功能。

[DB-IP](https://db-ip.com/)提供的免费[IP to Country Lite 数据库](https://db-ip.com/db/download/ip-to-country-lite)用于解析对等国家。 该数据库是根据[知识共享署名 4.0 国际许可](https://creativecommons.org/licenses/by/4.0/)获得许可的。

![qBittorrent](https://pic.ryanjie.cn/2019/04/qBittorrent.png "qBittorrent")

<a id="markdown-特点" name="特点"></a>

## 特点

> 1. Auto Ban Xunlei, QQ, Baidu, Xfplay, DLBT and Offline downloader
> 2. Temporary IP Filter API for advanced user
> 3. Update MessageBox with changelog if NEW version is available
> 4. Auto Ban Unknown Peer from China Option(Default: OFF)
> 5. Show Tracker Authentication Window(Default: ON)
> 6. Auto Update Public Trackers List(Default: OFF)
> 7. Multiple qBittorrent instances

1. 自动屏蔽迅雷、QQ、百度、Xfplay、DLBT 和离线下载客户端
2. 为高级用户提供临时 IP 过滤 API
3. 如果有新版本可用，消息框会显示更新日志
4. 自动屏蔽来自中国 IP 的未知客户端(默认关闭)
5. 显示追踪验证窗口(默认打开)
6. 自动更新 tracker 服务器列表(默认关闭)
7. 应用多开
8. 尝试记录登陆失败的 WebUI/API
9. 推出选项时重置 IPFilter 配置

<a id="markdown-更新日志" name="更新日志"></a>

## 更新日志

<a id="markdown-v42310" name="v42310"></a>

### v4.2.3.10

1. [Windows] Use NTFS compression to reduce the PDB filesize ([#108](https://github.com/c0re100/qBittorrent-Enhanced-Edition/issues/108))

<a id="markdown-v42210" name="v42210"></a>

### v4.2.2.10

1. Add cacao torrent to client blacklist
2. Use official method for multiple instances

<a id="markdown-v41916" name="v41916"></a>

### v4.1.9.16

For stick with v4.1.x series user

1. Add cacao torrent to client blacklist
2. Latest commit from upstream(GeoIP, Web API change)

<a id="markdown-软件下载" name="软件下载"></a>

## 软件下载

- [Github - Release](https://github.com/c0re100/qBittorrent-Enhanced-Edition/releases/latest)
- 最新 AppImage : [qBittorrent-Enhanced-Edition.AppImage](https://github.com/c0re100/qBittorrent-Enhanced-Edition/releases/latest/download/qBittorrent-Enhanced-Edition.AppImage)
- [tracker 服务器列表推荐 by 小樱の ITZMX](http://github.itzmx.com/1265578519/OpenTracker/master/tracker.txt)

<a id="markdown-arch-linux" name="arch-linux"></a>

### Arch Linux

Maintainer: [c0re100](https://github.com/c0re100)

- [AUR](https://aur.archlinux.org/packages/qbittorrent-enhanced-git/)
- [nox AUR](https://aur.archlinux.org/packages/qbittorrent-enhanced-nox-git/)

<a id="markdown-debian" name="debian"></a>

### Debian

Maintainer: [yangfl](https://github.com/yangfl)

- [repo](https://repo.debiancn.org/pool/main/q/qbittorrent-enhanced/)

<a id="markdown-opensuserpm-based-linux-distro" name="opensuserpm-based-linux-distro"></a>

### openSUSE/RPM-based Linux distro

Maintainer: [PhoenixEmik](https://github.com/PhoenixEmik)

- [openSUSE repo](https://build.opensuse.org/package/show/home:PhoenixEmik/qbittorrent-enhanced-edition)

<a id="markdown-ubuntu" name="ubuntu"></a>

### Ubuntu

Maintainer: [poplite](https://github.com/poplite)

- [PPA](https://launchpad.net/~poplite/+archive/ubuntu/qbittorrent-enhanced)

<a id="markdown-macos-homebrew" name="macos-homebrew"></a>

### macOS (Homebrew)

Maintainer: [AlexaraWu](https://github.com/AlexaraWu)

```bash
brew cask install c0re100-qbittorrent
```

<a id="markdown-windows-chocolatey" name="windows-chocolatey"></a>

### Windows (Chocolatey)

Maintainer: [iYato](https://github.com/iYato)

```bash
choco install qbittorrent-enhanced
```

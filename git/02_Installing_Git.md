---
title: 安装 Git 环境
abstract: Git 环境搭建，在各系统中安装 git 工具。
url: git-1
permalink: git-1
date: 2020-03-05 18:35:43
category:
  - [Git]
tags:
  - [Git]
---

`Git` 可以通过图形化界面管理，也可以通过命令行管理，在刚开始学习阶段为了更好地理解 `Git` 的操作和使用效率，推荐使用命令行管理操作。

`Git` 的安装相对来说非常简单， 并且不少 Linux 系统自带了 `Git` 工具；如果你的系统当中已经安装了 `Git`，那么可以跳过相应的安装步骤，是否已经安装，可以通过下面安装的验证环节进行验证。

## Linux 安装 Git

### CentOS

使用 CentOS 自带的 git 在执行克隆、推送和拉取的时候会报 `fatal: HTTP request failed` 错误，原因是系统自带的git版本过低造成的。这时我们需要升级 git 的版本。

#### 查看系统环境

```bash
$ cat /etc/centos-release
CentOS Linux release 7.9.2009 (Core)
$ cat /proc/version
Linux version 3.10.0-1127.19.1.el7.x86_64 (mockbuild@kbuilder.bsys.centos.org) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-39) (GCC) )
```

#### 卸载系统自带的 Git

```bash
$ yum info git
Available Packages
Name         : git
Version      : 1.8.3.1
Release      : 23.el7_8
Arch         : x86_64
Size         : 4.4 M
Source       : git-1.8.3.1-23.el7_8.src.rpm
Repo         : os
Summary      : Fast Version Control System
URL          : http://git-scm.com/
License      : GPLv2
Description  : Git is a fast, scalable, distributed revision
             : control system with an unusually rich command
             : set that provides both high-level operations
             : and full access to internals.
             : 
             : The git rpm installs the core tools with
             : minimal dependencies.  To install all git
             : packages, including tools for integrating with
             : other SCMs, install the git-all meta-package.
             
$ sudo yum remove -y git            
```

#### 安装依赖工具

```bash
sudo yum install -y curl-devel expat-devel gettext-devel \
    openssl-devel zlib-devel
```

#### 下载源代码

```bash
wget -N https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.29.2.tar.gz
# 国内镜像
# wget -N https://files.ryanjie.vercel.app/git-2.29.2.tar.gz
```

#### 解压编译安装

```bash
sudo tar -zxf git-2.29.2.tar.gz -C /usr/local/src/
rm -rf git-2.29.2.tar.gz && cd /usr/local/src/git-2.29.2
make prefix=/usr/local all
sudo make prefix=/usr/local install
```

#### 验证安装

```bash
$ git --version
git version 2.24.3
```

### Ubuntu/Debian 

在终端中运行下面命令直接安装：

```bash
sudo apt install -y git
```

## Mac OS 安装 Git

Mac 系统默认已经安装了 `Git`，可以跳过下面安装步骤直接到验证环节进行验证。如果你的 Mac 系统当中没有 `Git` 工具，那么就按照下面的安装步骤进行安装，**推荐使用 Homebrew 安装**。

### 使用安装包安装

- Mac 版本 Git 下载地址：[https://git-scm.com/download/mac](https://git-scm.com/download/mac)
- 国内华为镜像地址：[https://mirrors.huaweicloud.com/git-for-macos](https://mirrors.huaweicloud.com/git-for-macos)

从上面链接中找到最新的下载。下载下来之后可以看到一个 `dmg` 文件，双击打开 `dmg` 压缩文件，打开后双击 `pgk` 文件进行安装就行。

### 使用 Homebrew 安装

在终端中运行下面命令直接安装：

```bash
# 安装 Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# 安装 Git
brew install git
```

### 验证安装

```bash
$ git --version
git version 2.24.3
```

## Windows 安装 Git

Windows 系统，默认是没有安装 `Git` 工具的，可以通过下面的方法进行安装。

### 使用安装包安装

- Windows 版本 Git 下载地址：[https://git-scm.com/download/win](https://git-scm.com/download/win)
- 国内华为镜像地址：[https://mirrors.huaweicloud.com/git-for-windows](https://mirrors.huaweicloud.com/git-for-windows)

从上面链接中找到最新的下载。下载下来之后可以看到一个 `exe` 文件，双击打开 `exe` 文件进行安装就行。

### 使用 Scoop 安装

在 Powershell 中运行下面命令直接安装：

```powershell
# 安装 Scoop
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
# or shorter
iwr -useb get.scoop.sh | iex
# 安装 Git
scoop install git
```

### 验证安装

```bash
$ git --version
git version 2.24.3
```

> PS：以下辅助工具可以在终端或者 powershell 中输入命令时提供智能提示和自动补全：
>
> 1. Windows：  `posh` + `oh-my-posh` ，安装使用说明：
> 2. Mac OS： `zsh` + `oh-my-zsh` ，安装使用说明：
> 3. Linux： `zsh` + `oh-my-zsh` ，安装使用说明：

## 小结

1. Linux 下可以选择 **源码编译** 和 **包管理器** 两种方式安装 git；
2. Mac OS 和 Windows 下可以使用 **安装包** 和 **包管理器** 两种方式安装 git；
3. 安装完成后使用 `git --version`命令验证是否安装成功。
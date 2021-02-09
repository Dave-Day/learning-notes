# CentOS 7 安装 Git2

CentOS yum 源里的 git 版本太低（1.8.x），连 Github 都已不再支持。因此我们需要手动安装 git2.x。

```bash
Available Packages
Name        : git
Arch        : x86_64
Version     : 1.8.3.1
Release     : 23.el7_8
Size        : 4.4 M
Repo        : base/7/x86_64
Summary     : Fast Version Control System
URL         : http://git-scm.com/
License     : GPLv2
Description : Git is a fast, scalable, distributed revision control system with
            : an unusually rich command set that provides both high-level
            : operations and full access to internals.
            : 
            : The git rpm installs the core tools with minimal dependencies.  To
            : install all git packages, including tools for integrating with
            : other SCMs, install the git-all meta-package.
```

## 源码安装

```bash
$ sudo su -

# 安装依赖
yum install -y wget gcc-c++ zlib-devel perl-ExtUtils-MakeMaker

# 下载 git 源码
# https://github.com/git/git/archive/v2.30.0.tar.gz
# https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.30.0.tar.gz
cd /usr/src/ && wget -O git-2.30.0.tar.gz https://github.com/git/git/archive/v2.30.0.tar.gz

# 解压
tar -zxf git-2.30.0.tar.gz && cd git-2.30.0

# 配置
make configure
./configure --prefix=/usr/local

# 安装
make install

# 检查安装
$ git --version
git version 2.30.0

# 查看 git 
$ which git
/usr/local/bin/git
```

## yum 安装

```shell
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install Git
brew install git
```


---
title: CentOS 7 配置
abstract: CentOS 7 配置。
url: website-primer-1
permalink: website-primer-1
date: 2020-03-05 18:35:43
category:
  - [Linux]
tags:
  - [Linux]
  - [CentOS]
  - [VMWare]

---

CentOS 7 配置 (一) 更换国内源及安装配置 Git2。

## 更换国内源

### CentOS

#### 备份旧源

```bash
sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
```

#### 下载新源

阿里：

```bash
# wget
sudo wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo

# curl
sudo curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
```

TUNA：

```bash
sudo tee /etc/yum.repos.d/CentOS-Base.repo <<-'EOF'
[base]
name=CentOS-$releasever - Base
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/os/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-7

[updates]
name=CentOS-$releasever - Updates
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/updates/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-7

[extras]
name=CentOS-$releasever - Extras
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/extras/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-7

[centosplus]
name=CentOS-$releasever - Plus
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-7
-EOF
```

#### 更新软件包缓存

```bash
sudo yum makecache
```

### EPEL

#### 备份旧源

```bash
sudo mv /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.bak
sudo mv /etc/yum.repos.d/epel-testing.repo /etc/yum.repos.d/epel-testing.repo.bak
```

#### 下载新源

阿里：

```bash
# wget
sudo wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

# curl
sudo curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
```

TUNA：

```bash
sudo tee /etc/yum.repos.d/epel.repo <<-'EOF'
[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/epel/7/$basearch
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

[epel-debuginfo]
name=Extra Packages for Enterprise Linux 7 - $basearch - Debug
baseurl=https://mirrors.tuna.tsinghua.edu.cn/epel/7/$basearch/debug
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux 7 - $basearch - Source
baseurl=https://mirrors.tuna.tsinghua.edu.cn/epel/7/SRPMS
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1
EOF
```

#### 更新软件包缓存

```bash
sudo yum makecache
```

## 安装 Git2

[![ohmyzsh](https://github-readme-stats.vercel.app/api/pin/?username=iusrepo&repo=git224&show_owner=true&theme=nightowl)](https://github.com/iusrepo/git224)

### 安装 IUS 存储库

```bash
yum install \
https://repo.ius.io/ius-release-el7.rpm \
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y
```

### 更新软件包缓存

```bash
sudo yum makecache
```

### 查找 Git2 软件包

```bash
yum list git2* --showduplicates | sort -r
```

### 安装 Git

```bash
sudo yum install -y git224
```

### 校验安装

```bash
$ git --version
git version 2.24.3
```

## 参考

- [CentOS 安装教程 - 阿里巴巴开源镜像站](https://developer.aliyun.com/mirror/centos)
- [EPEL 安装教程 - 阿里巴巴开源镜像站](https://developer.aliyun.com/mirror/epel)
- [CentOS 镜像使用帮助 - 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/centos/)
- [EPEL 镜像使用帮助 - 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/epel/)
- [iusrepo/git224](https://github.com/iusrepo/git224)


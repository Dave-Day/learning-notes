---
title: RHEL7 配置网络 yum 源
url: rhel-7-config-network-yum-repo
---

# RHEL7 配置网络 yum 源

## 问题

在使用 RHEL 7 的 yum 来安装或者更新软件的时候会有如下提示：

```bash
[root@Ryanjie rpm]$ yum install tree -y
Loaded plugins: langpacks, product-id, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
Setting up Install Process
Nothing to do
```

原因： RHEL 的 yum 在线安装更新是订阅收费的，如果没有注册订阅则不能使用。
解决方案：使用 CentOS 的 yum 源进行替代。因为 CentOS 基于 redhat 红帽 RHEL 的开源源码所编译而成，两者只是在系统包装方面各有自身的特点，我们无需担心软件包的兼容问题。

## 解决方案

### 下载 yum 配置文件

```bash
[root@ryanjie rpm]$ wget -c -nv -O /etc/yum.repos.d/RHEL7-CentOS-Base.repo https://img.zxj.guru/learn/linux/repo/RHEL7-CentOS-Base.repo
2020-06-27 18:40:29 URL:https://img.zxj.guru/learn/linux/repo/RHEL7-CentOS-Base.repo [837/837] -> "/etc/yum.repos.d/RHEL7-CentOS-Base.repo" [1]
```

### 下载 RPM GPG 公钥

```bash
[root@ryanjie rpm]$ wget -c -nv -O /etc/pki/rpm-gpg/RPM-GPG-KEY-7 https://mirrors.tuna.tsinghua.edu.cn/centos/7/os/x86_64/RPM-GPG-KEY-CentOS-7
2020-06-27 18:41:53 URL:https://mirrors.tuna.tsinghua.edu.cn/centos/7/os/x86_64/RPM-GPG-KEY-CentOS-7 [1690/1690] -> "/etc/pki/rpm-gpg/RPM-GPG-KEY-7" [1]
```

### 更新软件包缓存

```bash
[root@ryanjie rpm]$ yum makecache
Loaded plugins: fastestmirror, langpacks, product-id, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
Loading mirror speeds from cached hostfile
base | 3.6 kB 00:00
extras | 2.9 kB 00:00
updates | 2.9 kB 00:00
(1/10): base/group_gz | 153 kB 00:00
(2/10): base/primary_db | 6.1 MB 00:02
(3/10): extras/primary_db | 194 kB 00:00
(4/10): extras/other_db | 122 kB 00:00
(5/10): extras/filelists_db | 205 kB 00:01
(6/10): base/other_db | 2.6 MB 00:01
(7/10): base/filelists_db | 7.1 MB 00:05
(8/10): updates/filelists_db | 1.6 MB 00:02
(9/10): updates/primary_db | 2.9 MB 00:02
(10/10): updates/other_db | 239 kB 00:00
Metadata Cache Created
```

### 测试 yum 安装

```bash
[root@ryanjie rpm]$ yum install tree -y
Loaded plugins: langpacks, product-id, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
Resolving Dependencies
--> Running transaction check
---> Package tree.x86_64 0:1.6.0-10.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package        Arch             Version                   Repository      Size
================================================================================
Installing:
 tree           x86_64           1.6.0-10.el7              base            46 k

Transaction Summary
================================================================================
Install  1 Package

Total download size: 46 k
Installed size: 87 k
Downloading packages:
warning: /var/cache/yum/x86_64/7Server/base/packages/tree-1.6.0-10.el7.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID f4a80eb5: NOKEY
Public key for tree-1.6.0-10.el7.x86_64.rpm is not installed
tree-1.6.0-10.el7.x86_64.rpm                               |  46 kB   00:00
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-7
Importing GPG key 0xF4A80EB5:
 Userid     : "CentOS-7 Key (CentOS 7 Official Signing Key) <security@centos.org>"
 Fingerprint: 6341 ab27 53d7 8a78 a7c2 7bb1 24c6 a8a7 f4a8 0eb5
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-7
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : tree-1.6.0-10.el7.x86_64                                     1/1
  Verifying  : tree-1.6.0-10.el7.x86_64                                     1/1

Installed:
  tree.x86_64 0:1.6.0-10.el7

Complete!
[root@ryanjie Desktop]$
```

![tuna-tsinghua-yum](https://img.zxj.guru/learn/linux/04/tuna-tsinghua-yum.png)

## 卸载 RHEL 系统自带 yum 软件包

如果以上步骤没问题，建议不要卸载 RHEL 系统自带 yum 软件包。

### 查看 RHEL 自带的 yum 软件包

```bash
[root@Ryanjie rpm]$ rpm -qa | grep yum
yum-utils-1.1.31-24.el7.noarch
yum-langpacks-0.4.2-3.el7.noarch
yum-metadata-parser-1.1.4-10.el7.x86_64
yum-rhn-plugin-2.0.1-4.el7.noarch
PackageKit-yum-0.8.9-11.el7.x86_64
yum-3.4.3-118.el7.noarch
```

### 卸载 RHEL 自带的 yum 软件包

```bash
[root@Ryanjie rpm]$ rpm -qa | grep yum | xargs rpm -e --nodeps
```

### 下载 CentOS 的 yum 软件包

```bash
[root@Ryanjie rpm]$ wget -c -nv https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/PackageKit-yum-1.1.10-2.el7.centos.x86_64.rpm https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-3.4.3-167.el7.centos.noarch.rpm https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-langpacks-0.4.2-7.el7.noarch.rpm https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-metadata-parser-1.1.4-10.el7.x86_64.rpm https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-rhn-plugin-2.0.1-10.el7.noarch.rpm https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-utils-1.1.31-53.el7.noarch.rpm
2020-06-27 18:39:02 URL:https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/PackageKit-yum-1.1.10-2.el7.centos.x86_64.rpm [76908/76908] -> "PackageKit-yum-1.1.10-2.el7.centos.x86_64.rpm" [1]
2020-06-27 18:39:02 URL:https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-3.4.3-167.el7.centos.noarch.rpm [1298672/1298672] -> "yum-3.4.3-167.el7.centos.noarch.rpm" [1]
2020-06-27 18:39:02 URL:https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-langpacks-0.4.2-7.el7.noarch.rpm [31312/31312] -> "yum-langpacks-0.4.2-7.el7.noarch.rpm" [1]
2020-06-27 18:39:02 URL:https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-metadata-parser-1.1.4-10.el7.x86_64.rpm [28348/28348] -> "yum-metadata-parser-1.1.4-10.el7.x86_64.rpm" [1]
2020-06-27 18:39:02 URL:https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-rhn-plugin-2.0.1-10.el7.noarch.rpm [83040/83040] -> "yum-rhn-plugin-2.0.1-10.el7.noarch.rpm" [1]
2020-06-27 18:39:03 URL:https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/yum-utils-1.1.31-53.el7.noarch.rpm [124628/124628] -> "yum-utils-1.1.31-53.el7.noarch.rpm" [1]
FINISHED --2020-06-27 18:39:03--
Total wall clock time: 1.4s
Downloaded: 6 files, 1.6M in 0.3s (5.87 MB/s)
```

### 安装 CentOS 的 yum 软件包

```bash
[root@Ryanjie rpm]$ rpm -ivh --force --nodeps *.rpm
Preparing...                          ################################# [100%]
Updating / installing...
   1:yum-metadata-parser-1.1.4-10.el7 ################################# [ 17%]
   2:yum-3.4.3-167.el7.centos         ################################# [ 33%]
   3:PackageKit-yum-1.1.10-2.el7.cento################################# [ 50%]
   4:yum-langpacks-0.4.2-7.el7        ################################# [ 67%]
   5:yum-rhn-plugin-2.0.1-10.el7      ################################# [ 83%]
   6:yum-utils-1.1.31-53.el7          ################################# [100%]
```

![remove-rhel-yum-packages](https://img.zxj.guru/learn/linux/04/remove-rhel-yum-packages.png)

## 参考

- [RHEL7 配置网络 yum 源](https://www.cnblogs.com/lt1993/p/10263596.html)
- [Redhat7 配置 yum 源(本地源和网络源)](https://www.cnblogs.com/Rcsec/p/10246995.html)
- [RedHat 网络 yum 源的配置](https://www.linuxidc.com/Linux/2017-07/145578.htm)

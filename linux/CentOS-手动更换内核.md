---
title: CentOS 手动更换内核
abstract: 云服务器安装的 CentOS 系统内核是 `3.10`，低于开启 BBR 最低要求的版本 `4.10`，所以我们需要手动更换为默认内核后再作升级。
url: centos-upgrade-kernel
permalink: centos-upgrade-kernel
date: 2020-11-13 21:26:07
category:
  - CentOS
tags:
  - CentOS
  - Kernel
---

![centos-upgrade-kernel](https://img.zxj.guru/2020/11/centos-upgrade-kernel.png)

由于开启 BBR 需 `4.10` 以上版本 Linux 内核， 但是云服务器安装的 CentOS 7 系统内核是 `3.10`，低于开启 BBR 最低要求的版本 `4.10`，所以我们需要手动更换为默认内核后再作升级。

> 由于是使用最新版系统内核，最好请勿在生产环境安装，以免产生不可预测之后果。

## 安装 ELRepo yum 源

1. 查看当前 `Kernel` 版本。

   ```bash
   $ uname -r
   kernel-3.10.0-1160.11.1.el7.x86_64
   ```

2. 更新软件包。

   ```bash
   su - root
   yum update -y
   ```

3. 导入 `ELRepo` 公钥。

   ```bash
   rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
   ```

4. 安装 `ELRepo` 的 yum 源。

   ```bash
   #RHEL-8 或者 CentOS-8
   yum install -y https://www.elrepo.org/elrepo-release-8.el8.elrepo.noarch.rpm

   #RHEL-7, SL-7 或者 CentOS-7
   yum install -y https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm

   #RHEL-6, SL-6 或者 CentOS-6
   yum install -y https://www.elrepo.org/elrepo-release-6.el6.elrepo.noarch.rpm
   ```

5. 安装国内镜像。

   ```bash
   #备份 /etc/yum.repos.d/elrepo.repo
   cp /etc/yum.repos.d/elrepo.repo /etc/yum.repos.d/elrepo.repo.bak

   #安装 TUNA 镜像源
   sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/elrepo.repo
   sed -i 's+elrepo.org/linux+mirrors.tuna.tsinghua.edu.cn/elrepo+' /etc/yum.repos.d/elrepo.repo
   ```

6. 更新软件包缓存。

   ```bash
   yum makecache
   ```

## 安装新内核

1. 查看 `ELRepo` 仓库下当前系统支持的内核包。

   ```bash
   yum --disablerepo="*" --enablerepo="elrepo-kernel" list available
   ```

2. 安装最新的主线稳定`Kernel` 。

   ```bash
   yum --enablerepo=elrepo-kernel install -y kernel-ml
   ```

## 更改 grub 配置默认启动新内核

安装完`kernel-ml`之后，系统没有自动切换到新内核，重启之后也不会切换到新内核。我们需要更改 `grub` 配置默认启动新内核。

1. 打开 `/etc/default/grub` 文件，将文件中`GRUB_DEFAULT=saved`修改为`GRUB_DEFAULT=0`。不会 Vim 操作的使用下面命令。

   ```bash
   sed -i 's+GRUB_DEFAULT=saved+GRUB_DEFAULT=0+' /etc/default/grub
   ```

2. 重新生成 `Kernel` 配置。

   ```bash
   grub2-mkconfig -o /boot/grub2/grub.cfg
   ```

3. 重启服务器。

   ```bash
   reboot
   ```

4. 检查是否更改为新 `Kernel` 。

   ```bash
   $ uname -r
   5.10.4-1.el7.elrepo.x86_64
   ```

## 删除多余内核

> 如果空间充裕建议不要卸载旧内核。

1. 查看所有版本的 `Kernel` 。

   ```bash
   rpm -qa | grep kernel
   ```

2. 删除旧版本的 `Kernel` 。

   ```bash
   sudo yum remove -y kernel-3.10.*
   ```

3. 重新生成 `Kernel` 配置。

   ```bash
   sudo grub2-mkconfig -o /boot/grub2/grub.cfg
   ```

## 参考

- [elrepo | 镜像站使用帮助 | 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/elrepo/)

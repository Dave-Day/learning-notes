---
title: RHEL7 配置本地 yum 源
url: linux-rhel-7-config-local-yum-repo
---

## yum 仓库介绍

yum 软件仓库的作用是为了进一步简化 RPM 管理软件的难度以及自动分析所需软件包及其依赖关系的技术。可以把 yum 想象成是一个硕大的软件仓库，里面保存有几乎所有常用的工具，而且只需要说出所需的软件包名称，系统就会自动为您搞定一切。既然要使用 yum 软件仓库，就要先把它搭建起来，然后将其配置规则确定好才行。

## 步骤

搭建并配置 Yum 软件仓库的大致步骤如下所示。

### 切换 yum 仓库配置文件目录

```bash
$ cd /etc/yum.repos.d/
```

### 新建本地 yum 仓库配置文件

使用 Vim 编辑器创建一个名为 rhel7.repo 的新配置文件（文件名称可随意，但后缀必须为.repo），逐项写入下面加粗的配置参数并保存退出（不要写后面的中文注释）。

- [rhel-media] ：Yum 软件仓库唯一标识符，避免与其他仓库冲突。
- name = linuxprobe：Yum 软件仓库的名称描述，易于识别仓库用处。
- baseurl = file:///media/cdrom：提供的方式包括 FTP（ftp://..）、HTTP（http://..）、本地
  （file:///..）。`file:///media/cdrom` 指挂载点为本地 `/media/cdrom` 目录。
- enabled = 1：设置此源是否可用；1 为可用，0 为禁用。
- gpgcheck = 0：设置此源是否校验文件；1 为校验，0 为不校验。
- gpgkey = file:///media/cdrom/RPM-GPG-KEY-redhat-release：若上面参数开启校验，那么请指定公钥文件地址。

```bash
$ sudo vim rhel7.repo
[rhel7-ryanjie]
name = rhel-ryanjie
baseurl = file:///media/cdrom
enable = 1
gpgcheck = 0
```

### 根据挂载点路径挂在光盘

- `mount /dev/cdrom /media/cdrom` 将设备 `dev/cdrom` 挂载到 `/media/cdrom` 目录

```bash
$ sudo mkdir -p /media/cdrom
$ sudo mount /dev/cdrom /media/cdrom
```

### 设置开机自动挂载

- `dev/cdrom` 设备名称
- `/media/cdrom` 本地挂载点

- `iso9660` ISO 9660 文件系统是一个标准 CD-ROM 文件系统
- `defaults 0 0` 第一个为 `fs_freq` ，用来决定哪一个文件系统需要执行 `dump` 操作(`dump`执行`ext2`的文件系统的备份操作)，0 就是不需要；第二个叫 `fs_passno` ，是系统重启时 fsck 程序检测磁盘(fsck 检测和修复文件系统)的顺序号，0 表示该文件系统不被检测，1 是 root 文件系统，2 是别的文件系统。fsck 按序号检测磁盘。 --- [百度知道](https://zhidao.baidu.com/question/1497348692542331339.html)
- `-o loop`：使用 loop 模式用来将一个档案当成硬盘分割挂上系统。

```bash
$ sudo vim /etc/fstab
/dev/cdrom /media/cdrom iso9660 defaults 0  0
```

### 测试本地 yum 源是否配置正确

```bash
$ sudo yum install httpd -y
```

若出现 Complete！则代表配置正确。

![rhel7-yum](https://img.zxj.guru/learn/linux/05/rhel7-yum.png)

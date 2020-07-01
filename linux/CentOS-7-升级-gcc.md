---
title: CentOS 7 升级 gcc
abstract: Centos7 gcc版本默认4.8.5，而有些软甲的编译安装需要最低支持c++11的 gcc 5.x版本。我们在需要升级 gcc 的版本。
url: centos-7-upgrade-gcc
permalink: centos-7-upgrade-gcc
date: 2020-08-01 20:33:16
category:
  - CentOS
tags:
  - CentOS
  - gcc
---

Centos7 gcc 版本默认 4.8.5，而有些软件（例如：Redis6、Mariadb10 等）的编译安装需要最低支持 c++11 的 gcc 5.x 版本。我们在需要升级 gcc 的版本。但是 Red Hat 为了软件的稳定和版本支持，yum 上版本也是 4.8.5，所以无法使用 yum 进行软件更新，需要安装 SCL 源升级 gcc。

```bash
$ gcc -v
gcc version 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC)
```

## 安装 SCL 源

SCL 软件集(Software Collections),是为了给 RHEL/CentOS 用户提供一种以方便、安全地安装和使用应用程序和运行时环境的多个（而且可能是更新的）版本的方式，同时避免把系统搞乱。

```bash
yum install -y centos-release-scl scl-utils-build
```

## 更换国内镜像源

执行替换命令将软件仓库地址替换为国内镜像地址。

```bash
# 清华大学
sed -i 's+#baseurl=http://mirror.centos.org+baseurl=https://mirrors.tuna.tsinghua.edu.cn+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+# baseurl=http://mirror.centos.org+baseurl=https://mirrors.tuna.tsinghua.edu.cn+' /etc/yum.repos.d/CentOS-SCLo-scl.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl.repo

# 阿里云
sed -i 's+#baseurl=http://mirror.centos.org+baseurl=https://mirrors.aliyun.com+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+# baseurl=http://mirror.centos.org+baseurl=https://mirrors.aliyun.com+' /etc/yum.repos.d/CentOS-SCLo-scl.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl.repo

# 腾讯云
sed -i 's+#baseurl=http://mirror.centos.org+baseurl=https://mirrors.cloud.tencent.com+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+# baseurl=http://mirror.centos.org+baseurl=https://mirrors.cloud.tencent.com+' /etc/yum.repos.d/CentOS-SCLo-scl.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl.repo

# 腾讯云内网
sed -i 's+#baseurl=http://mirror.centos.org+baseurl=https:///mirrors.tencentyun.com+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+# baseurl=http://mirror.centos.org+baseurl=https:///mirrors.tencentyun.com+' /etc/yum.repos.d/CentOS-SCLo-scl.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl.repo

# 阿里云内网
sed -i 's+#baseurl=http://mirror.centos.org+baseurl=https://mirrors.cloud.aliyuncs.com+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i 's+# baseurl=http://mirror.centos.org+baseurl=https://mirrors.cloud.aliyuncs.com+' /etc/yum.repos.d/CentOS-SCLo-scl.repo
sed -i 's+mirrorlist=+#mirrorlist=+' /etc/yum.repos.d/CentOS-SCLo-scl.repo
```

替换后的文件内容如下。

```ini
# CentOS-SCLo-sclo.repo
#
# Please see http://wiki.centos.org/SpecialInterestGroup/SCLo for more
# information

[centos-sclo-sclo]
name=CentOS-7 - SCLo sclo
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/7/sclo/$basearch/sclo/
#mirrorlist=http://mirrorlist.centos.org?arch=$basearch&release=7&repo=sclo-sclo
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo

[centos-sclo-sclo-testing]
name=CentOS-7 - SCLo sclo Testing
baseurl=http://buildlogs.centos.org/centos/7/sclo/$basearch/sclo/
gpgcheck=0
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo

[centos-sclo-sclo-source]
name=CentOS-7 - SCLo sclo Sources
baseurl=http://vault.centos.org/centos/7/sclo/Source/sclo/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo

[centos-sclo-sclo-debuginfo]
name=CentOS-7 - SCLo sclo Debuginfo
baseurl=http://debuginfo.centos.org/centos/7/sclo/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo
```

```ini
# CentOS-SCLo-sclo.repo
#
# Please see http://wiki.centos.org/SpecialInterestGroup/SCLo for more
# information

[centos-sclo-sclo]
name=CentOS-7 - SCLo sclo
# baseurl=http://mirror.centos.org/centos/7/sclo/$basearch/sclo/
mirrorlist=http://mirrorlist.centos.org?arch=$basearch&release=7&repo=sclo-sclo
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo

[centos-sclo-sclo-testing]
name=CentOS-7 - SCLo sclo Testing
baseurl=http://buildlogs.centos.org/centos/7/sclo/$basearch/sclo/
gpgcheck=0
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo

[centos-sclo-sclo-source]
name=CentOS-7 - SCLo sclo Sources
baseurl=http://vault.centos.org/centos/7/sclo/Source/sclo/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo

[centos-sclo-sclo-debuginfo]
name=CentOS-7 - SCLo sclo Debuginfo
baseurl=http://debuginfo.centos.org/centos/7/sclo/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo
```

## 更新软件包缓存

```bash
yum makecache fast
```

## 查看源中关于 devtoolset-gcc 的软件包

devtoolset (Developer Toolset)是按照 Software Collections 的规范打出来的一套 rpm 包，提供了最新版本的 GNU 编译器集合，GNU 调试器以及其他开发，调试和性能监视工具。

```bash
# yum list all --enablerepo='centos-sclo-rh' | grep devtoolset-9-gcc
Repository epel is listed more than once in the configuration
devtoolset-9-gcc.x86_64                    9.3.1-2.el7            centos-sclo-rh
devtoolset-9-gcc-c++.x86_64                9.3.1-2.el7            centos-sclo-rh
devtoolset-9-gcc-gdb-plugin.x86_64         9.3.1-2.el7            centos-sclo-rh
devtoolset-9-gcc-gfortran.x86_64           9.3.1-2.el7            centos-sclo-rh
devtoolset-9-gcc-plugin-devel.x86_64       9.3.1-2.el7            centos-sclo-rh
```

## 安装软件包

```bash
yum install -y devtoolset-9-gcc devtoolset-9-gcc-c++ devtoolset-9-binutils
```

## 切换 gcc 版本

```bash
// 临时有效，退出 shell 或重启会恢复原 gcc 版本
scl enable devtoolset-9 bash

// 长期有效
echo "source /opt/rh/devtoolset-9/enable" >>/etc/profile
```

此时再查看 gcc 版本。

```bash
$ gcc -v
gcc version 9.3.1 20200408 (Red Hat 9.3.1-2) (GCC)
```

## 查看从 SCL 源中安装的软件包

```bash
$ scl -l
devtoolset-9
```

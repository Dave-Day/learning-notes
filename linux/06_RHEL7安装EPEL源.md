---
title: RHEL7 安装 EPEL 源
url: linux-rhel-7-install-epel-repo
---

## 介绍

> What is EPEL?
>
> EPEL (企业版 Linux 附加软件包) 是一个由 Fedora 社区志愿者推动的一个为 红帽企业 Linux 和相应衍生版本，比如 CentOS 和 Scientific Linux，补充高质量附加软件包的项目。
>
> 作为 Fedora 打包社区的一部分，EPEL 的所有软件包都是 100% 免费且自由的开源软件(FLOSS)。

EPEL (Extra Packages for Enterprise Linux) 是由 Fedora Special Interest Group 为企业 Linux 创建、维护和管理的一个高质量附加包集合，适用于但不仅限于 Red Hat Enterprise Linux (RHEL), CentOS, Scientific Linux (SL), Oracle Linux (OL)。

EPEL 软件包通常基于与 Fedora 对应的软件包，并且永远不会与 Red Hat Enterprise Linux (RHEL)发行版中的软件包发生冲突或替换。 EPEL 使用与 Fedora 相同的基础架构，包括构建系统，bugzilla 实例，更新管理器，镜像管理器等等。

## 步骤

### 安装 epel-release

```bash
[root@ryanjie yum.repos.d]$ yum install -y https://mirrors.tuna.tsinghua.edu.cn/centos/7/extras/x86_64/Packages/epel-release-7-11.noarch.rpm
Loaded plugins: langpacks, product-id, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
epel-release-7-11.noarch.rpm                                          |  15 kB  00:00:00
Examining /var/tmp/yum-root-AQx6dp/epel-release-7-11.noarch.rpm: epel-release-7-11.noarch
Marking /var/tmp/yum-root-AQx6dp/epel-release-7-11.noarch.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package epel-release.noarch 0:7-11 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

=============================================================================================
 Package              Arch           Version         Repository                         Size
=============================================================================================
Installing:
 epel-release         noarch         7-11            /epel-release-7-11.noarch          24 k

Transaction Summary
=============================================================================================
Install  1 Package

Total size: 24 k
Installed size: 24 k
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : epel-release-7-11.noarch                                                  1/1
  Verifying  : epel-release-7-11.noarch                                                  1/1

Installed:
  epel-release.noarch 0:7-11

Complete!
[root@ryanjie yum.repos.d]$
```

### 使用 tuna 的 epel 镜像

修改 `/etc/yum.repos.d/epel.repo` 和 `/etc/yum.repos.d/epel-testing.repo` 文件，将以 `mirrorlist` 和 `metalink` 开头的行注释掉。然后取消注释以 `baseurl` 开头的行，并将其中的 `http://download.fedoraproject.org/pub` 替换成 `https://mirrors.tuna.tsinghua.edu.cn` 。

可以用如下命令自动替换：（来自 [https://github.com/tuna/issues/issues/687](https://github.com/tuna/issues/issues/687)）

```bash
$ sed -e 's!^metalink=!#metalink=!g' \
    -e 's!^#baseurl=!baseurl=!g' \
    -e 's!//download\.fedoraproject\.org/pub!//mirrors.tuna.tsinghua.edu.cn!g' \
    -e 's!http://mirrors\.tuna!https://mirrors.tuna!g' \
    -i /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel-testing.repo
```

修改后的文件：

- `epel.repo`: [https://img.zxj.guru/learn/linux/repo/epel.repo](https://img.zxj.guru/learn/linux/repo/epel.repo)
- `epel-testing.repo`: [https://img.zxj.guru/learn/linux/repo/epel-testing.repo](https://img.zxj.guru/learn/linux/repo/epel-testing.repo)

### 启用 extras 和 HA 存储库

对于**RHEL 7 订阅用户**来说，建议启用 `optional`,`extras` 和 `HA repositories`，因为 EPEL 包可能依赖于这些存储库中的包。

```bash
$ subscription-manager repos --enable "rhel-*-optional-rpms" --enable "rhel-*-extras-rpms"  --enable "rhel-ha-for-rhel-*-server-rpms"
```

![rhel-install-epel](https://img.zxj.guru/learn/linux/06/rhel-install-epel.png)

## 参考

- [EPEL WIKI](https://fedoraproject.org/wiki/EPEL)
- [EPEL FAQ](https://fedoraproject.org/wiki/EPEL/FAQ)
- [TUNA EPEL 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/epel)

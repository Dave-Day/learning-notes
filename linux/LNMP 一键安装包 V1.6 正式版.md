---
title: LNMP 一键安装包 V1.6 正式版
date: 2019-06-02 10:42:50
categories: Linux
---

<!-- more -->

<!-- TOC -->

- [LNMP 一键安装包 V1.6 正式版](#lnmp-一键安装包-v16-正式版)
  - [LNMP 介绍](#lnmp-介绍)
  - [安装步骤](#安装步骤)
    - [使用 `putty` 或类似的 `SSH` 工具登陆 `VPS` 或服务器](#使用-putty-或类似的-ssh-工具登陆-vps-或服务器)
    - [下载并安装 LNMP 一键安装包](#下载并安装-lnmp-一键安装包)
    - [安装完成](#安装完成)
    - [安装失败](#安装失败)
    - [添加、删除虚拟主机及伪静态管理](#添加删除虚拟主机及伪静态管理)
    - [eAccelerator 、 xcache 、 memcached 、 imageMagick 、 ionCube 、 redis 、 opcache 的安装](#eaccelerator--xcache--memcached--imagemagick--ioncube--redis--opcache-的安装)
    - [LNMP 相关软件目录及文件位置](#lnmp-相关软件目录及文件位置)
    - [LNMP 状态管理命令](#lnmp-状态管理命令)
    - [仅安装数据库、 `Nginx`](#仅安装数据库-nginx)
  - [V1.6 更新记录](#v16-更新记录)
  - [关于升级到当前版本](#关于升级到当前版本)

<!-- /TOC -->

<a id="markdown-lnmp-一键安装包-v16-正式版" name="lnmp-一键安装包-v16-正式版"></a>

# LNMP 一键安装包 V1.6 正式版

<a id="markdown-lnmp-介绍" name="lnmp-介绍"></a>

## LNMP 介绍

`LNMP` 一键安装包是一个用 `Linux Shell` 编写的可以为 `CentOS/RHEL/Fedora/Aliyun/Amazon、Debian/Ubuntu/Raspbian/Deepin/Mint Linux VPS` 或独立主机安装 `LNMP(Nginx/MySQL/PHP)、LNMPA(Nginx/MySQL/PHP/Apache)` 、 `LAMP(Apache/MySQL/PHP)` 生产环境的 `Shell` 程序。

支持自定义 `Nginx` 、 `PHP` 编译参数及网站和数据库目录、支持生成 `LetseEcrypt` 证书、 `LNMP` 模式支持多 `PHP` 版本、支持单独安装 `Nginx/MySQL/MariaDB/Pureftpd` 服务器，同时提供一些实用的辅助工具如：虚拟主机管理、 `FTP` 用户管理、 `Nginx` 、 `MySQL/MariaDB` 、 `PHP` 的升级、常用缓存组件 `Redis/Xcache` 等的安装、重置 `MySQL root` 密码、 `502` 自动重启、日志切割、 `SSH` 防护 `DenyHosts/Fail2Ban` 、备份等许多实用脚本。

`LNMP` 一键安装包 `v1.6` 正式版主要增加 `PHP 7.3` 、 `Nginx/Apache` 的 `TLS 1.3` 支持、增加 `MariaDB 13` 、 `lnmp` 管理脚本新增使用 `DNS API` 方式只创建 `SSL` 证书、放宽数据安装内存限制、优化部分发行版新版本下的支持及很多细微的调整。

[安装前建议使用 screen](https://www.vpser.net/manage/run-screen-lnmp.html)，执行：
`screen -S lnmp` 后，执行： `wget http://soft.vpser.net/lnmp/lnmp1.6.tar.gz -cO lnmp1.6.tar.gz && tar zxf lnmp1.6.tar.gz && cd lnmp1.6 && ./install.sh lnmp`
请注意最后面的 `lnmp` 参数，如需要 `lnmpa` 或 `lamp` 模式，请替换 `lnmp` 为您要安装的模式。

- **[问题反馈及使用交流论坛](https://bbs.vpser.net/forum-25-1.html)**
- **[打赏捐赠](https://lnmp.org/donation.html)**
- LNMP 一键安装包官网地址：[lnmp](https://lnmp.org)

<a id="markdown-安装步骤" name="安装步骤"></a>

## 安装步骤

<a id="markdown-使用-putty-或类似的-ssh-工具登陆-vps-或服务器" name="使用-putty-或类似的-ssh-工具登陆-vps-或服务器"></a>

### 使用 `putty` 或类似的 `SSH` 工具登陆 `VPS` 或服务器

登陆后运行： `screen -S lnmp`
如果提示 `screen: command not found` 命令不存在可以执行： `yum install screen` 或 `apt-get installscreen` 安装，详细内容参考 [screen 教程](https://www.vpser.net/manage/run-screen-lnmp.html)。

<a id="markdown-下载并安装-lnmp-一键安装包" name="下载并安装-lnmp-一键安装包"></a>

### 下载并安装 LNMP 一键安装包

您可以选择使用下载版(推荐美国及海外 `VPS` 或空间较小用户使用)或者完整版(推荐国内 `VPS` 使用，国内用户可用在 [下载](https://lnmp.org/download.html)中找国内下载地址替换)，两者没什么区别，只是完整版把一些需要的源码文件预先放到安装包里。

**安装 `LNMP` 稳定版**

如需无人值守安装，请使用 [无人值守命令生成工具](https://lnmp.org/auto.html)，或[查看无人值守说明教程](https://lnmp.org/faq/v1-5-auto-install.html)

```bash
wget http://soft.vpser.net/lnmp/lnmp1.6.tar.gz -cO lnmp1.6.tar.gz && tar zxflnmp1.6.tar.gz && cd lnmp1.6 && ./install.sh lnmp
```

如需要安装 `LNMPA` 或 `LAMP` ，将 `./install.sh` 后面的参数 `lnmp` 替换为 `lnmpa` 或 `lamp` 即可。如需更改网站和数据库目录、自定义 `Nginx` 参数、 `PHP` 参数模块、开启 `lua` 等需在运行 `./install.sh` 命令前修改安装包目录下的 `lnmp.conf` 文件，详细可以查看 [lnmp.conf 文件参数说明](https://lnmp.org/faq/lnmp-software-list.html#lnmp.conf)。

如提示 `wget: command not found` ，使用 `yum install wget` 或 `apt-get install wget` 命令安装。

如下载速度慢或无法下载请更换其他下载节点，请查看 [LNMP 下载节点具体替换方法](https://lnmp.org/faq/lnmp-download-source.html)。

运行上述 `LNMP` 安装命令后，会出现如下提示：

![](https://lnmp.org/images/1.5/lnmp1.5-install-1.png)

目前提供了较多的 `MySQL` 、 `MariaDB` 版本和不安装数据库的选项，需要 **注意的是 `MySQL 5.6` , `5.7` 及 `MariaDB10` 必须在 `1G` 以上内存的更高配置上才能选择**
！如仅需安装数据库在 lnmp 安装包目录下执行： `./install.sh db`

输入对应 `MySQL` 或 `MariaDB` 版本前面的序号，回车进入下一步.

![](https://lnmp.org/images/1.5/lnmp1.5-install-2.png)

设置 `MySQL` 的 `root` 密码（为了安全不输入直接回车将会设置为 `lnmp.org` #随机数字）如果输入有错误需要删除时，可以按住 `Ctrl` 再按 `Backspace` 键进行删除(个别情况下是只需要 `Backspace` 键)。输入后回车进入下一步，如下图所示：

![](https://lnmp.org/images/1.5/lnmp1.5-install-3.png)

询问是否需要启用 `MySQL InnoDB` ， `InnoDB` 引擎默认为开启，一般建议开启，直接回车或输入 `y` ，如果确定确实不需要该引擎可以输入 `n` ，( `MySQL5.7+` 版本无法关闭 `InnoDB` ), 输入完成，回车进入下一步。

![](https://lnmp.org/images/1.5/lnmp1.5-install-4.png)

注意：选择 `PHP 7+` 版本时需要自行确认 `PHP` 版本是否与自己的程序兼容。

输入要选择的 `PHP` 版本的序号，回车进入下一步，选择是否安装内存优化:

![](https://lnmp.org/images/1.5/lnmp1.5-install-5.png)

可以选择不安装、 `Jemalloc` 或 `TCmalloc` ，输入对应序号回车，直接回车为默认为不安装。

如果是 `LNMPA` 或 `LAMP` 的话还会提示设置邮箱和选择 `Apache`

![](https://lnmp.org/images/1.5/lnmp1.5-install-6.png)

" `Please enter Administrator Email Address:` "，需要设置管理员邮箱，该邮箱会在报错时显示在错误页面上。

再选择 `Apache` 版本

![](https://lnmp.org/images/1.5/lnmp1.5-install-7.png)

按提示输入对应版本前面的数字序号，回车。

提示" `Press any key to install...or Press Ctrl+c to cancel` "后，按回车键确认开始安装。
`LNMP` 脚本就会自动安装编译 `Nginx` 、 `MySQL` 、 `PHP` 、 `phpMyAdmin` 等软件及相关的组件。

安装时间可能会几十分钟到几个小时不等，主要是机器的配置网速等原因会造成影响。

<a id="markdown-安装完成" name="安装完成"></a>

### 安装完成

如果显示 `Nginx: OK，MySQL: OK，PHP: OK`

![](https://lnmp.org/images/1.5/lnmp1.5-install-success.png)

并且 `Nginx` 、 `MySQL` 、 `PHP` 都是 `running` ， `80` 和 `3306` 端口都存在，并提示安装使用的时间及 `Install lnmp V1.6 completed! enjoy it.` 的话，说明已经安装成功。
某些系统可能会一直卡在 `Install lnmp V1.5 completed! enjoy it.` 不自动退出，可以按 `Ctrl+c` 退出。

安装完成接下来开始使用就可以了，按 [**添加虚拟主机教程**](https://lnmp.org/faq/lnmp-vhost-add-howto.html) ，添加虚拟主机后可以使用 [sftp](https://lnmp.org/faq/sftp.html) 或 [ftp 服务器](https://lnmp.org/faq/ftpserver.html) 上传网站代码，将域名解析到 `VPS` 或服务器的 `IP` 上，解析生效即可使用。

<a id="markdown-安装失败" name="安装失败"></a>

### 安装失败

![](https://lnmp.org/images/1.5/lnmp1.5-install-failed.png)

如果出现类似上图的提示，有一个或几个没安装成功表明安装失败！！需要用 [winscp](http://www.vpser.net/manage/winscp.html) 或其他类似工具，将 `/root` 目录下面的 `lnmp-install.log` 下载下来，到 [LNMP 支持论坛](http://bbs.vpser.net/forum-25-1.html) 发帖注明您的系统发行版名称及版本号、 `32` 位还是 `64` 位等信息，并将 `lnmp-install.log` 压缩以附件形式上传到论坛，我们会通过日志查找错误，并给予相应的解决方法。

**默认 `LNMP` 是不安装 `FTP` 服务器的，如需要 `FTP` 服务器：[ftpserver](https://lnmp.org/faq/ftpserver.html)**

<a id="markdown-添加删除虚拟主机及伪静态管理" name="添加删除虚拟主机及伪静态管理"></a>

### 添加、删除虚拟主机及伪静态管理

[lnmp-vhost-add-howto](https://lnmp.org/faq/lnmp-vhost-add-howto.html)

<a id="markdown-eaccelerator--xcache--memcached--imagemagick--ioncube--redis--opcache-的安装" name="eaccelerator--xcache--memcached--imagemagick--ioncube--redis--opcache-的安装"></a>

### eAccelerator 、 xcache 、 memcached 、 imageMagick 、 ionCube 、 redis 、 opcache 的安装

[addons](https://lnmp.org/faq/addons.html)

<a id="markdown-lnmp-相关软件目录及文件位置" name="lnmp-相关软件目录及文件位置"></a>

### LNMP 相关软件目录及文件位置

[lnmp-software-list](https://lnmp.org/faq/lnmp-software-list.html)

<a id="markdown-lnmp-状态管理命令" name="lnmp-状态管理命令"></a>

### LNMP 状态管理命令

[lnmp-status-manager](https://lnmp.org/faq/lnmp-status-manager.html)

<a id="markdown-仅安装数据库-nginx" name="仅安装数据库-nginx"></a>

### 仅安装数据库、 `Nginx`

`lnmp 1.5` 开始支持只安装 `MySQL/MariaDB` 数据库或 `Nginx` 增加单独 `nginx` 安装，安装包目录下运行： `./install.sh nginx` 进行安装；  
增加单独数据库安装，安装包目录下运行： `./install.sh db` 进行安装；

<a id="markdown-v16-更新记录" name="v16-更新记录"></a>

## V1.6 更新记录

> 增加 `PHP 7.3` 支持;
> 增加 `PHP 7.3` 支持;
> 增加 `MariaDB 10.3` 支持；
> 增加 `Nginx/Apache TLS 1.3` 支持；
> 增加使用 `DNS API` 方式只创建 `SSL` 证书不添加网站，命令 `lnmp onlyssl` ；
> 增加 `Fedora 30` 、 `Ubuntu 19.04` 、 `RHEL 8` 等新版本的支持；
> 增加 `nginx` 、 `apache` 等一些例子，并移至 `conf/example` 目录下；
> 增加在低于 `2048MB` 内存是增加 `2GB SWAP` 或低于 `1024MB` 时增加 `1GB SWAP` 的选项；
> 增加反向代理配置例子文件 `nginx-reverse-proxy-example.conf` ；
> 增加只安装 `nginx` 模式增加拷贝 `lnmp` 管理工具；
> 增加 `RHELRepo=local` 参数， `RHEL` 安装时使用 `RHEL` 本地源，不设置源为 `163 centos` 源；
> 增加 `CheckMirror=n` 参考，安装时不检查下载镜像，方便无网络安装；
> 优化不安装数据库时的处理流程；
> 优化 `acme.sh` 规则可能不生效的情况；
> 优化 `nginx` 系统满足条件是启用 `reuseport` ；
> 优化程序代码目录清理；
> 优化重写 `nginx` 管理脚本；
> 优化安装数据库时的内存判断，放宽内存限制；
> 修复新版深度 `Deepin 15.8` 桌面版问题；
> 修复新版 `Fedora 29` 下问题；
> 调整 `mysql` 使用带 `boost` 源码，同时支持不带 `boost` 安装方式；
> 调整卸载时不删除安装时添加的 `iptables` 规则；
> 调整 `fileinfo` 安装选项，内存满足时自动安装(可关闭)；
> 升级 `Nginx` 至 `1.16.0` ；…………
> 升级各程序版本；
> 更新诸多软件版本；
> 其他一些功能优化及调整......
> ...... 更多更新信息请访问[lnmp 官网更新记录](https://lnmp.org/changelog.html)查看

`LNMP` 状态管理： **lnmp {start|stop|reload|restart|kill|status}**  
`LNMP` 各个程序的状态管理： **lnmp {nginx|mysql|mariadb|php-fpm|pureftpd}
{start|stop|reload|restart|kill|status}**  
虚拟主机管理： **lnmp vhost {add|list|del}**  
数据库管理： **lnmp database {add|list|edit|del}**  
`FTP` 用户管理： **lnmp ftp {add|list|edit|del|show}**  
已存在虚拟主机添加 SSL： **lnmp ssl add**  
通过 `DNS API` 方式生成证书并创建虚拟主机： **lnmp dns {cx|dp|ali|...}**  
只通过 `DNS API` 方式生成 `SSL` 证书： **lnmp onlyssl {cx|dp|ali|...}**

<a id="markdown-关于升级到当前版本" name="关于升级到当前版本"></a>

## 关于升级到当前版本

目前 `1.5` 版本与 `1.6` 版本编译参数、管理脚本方面相差很小。一般只需要 `./upgrade1.x-1.6.sh` 升级一下管理脚本，如果需要 `TLS 1.3` 的话，使用 1.6 的升级脚本升级一下 `nginx` ，调整一下 SSL 虚拟主机中的几个参数即可；如果想使用 `PHP7.3` 的话，使用升级脚本升级 `PHP` 。如果没 `TLS 1.3` 、 `PHP 7.3` 之类的需求不需要进行升级，新装的话可以直接使用 `1.6` 。

添加、删除虚拟主机及伪静态管理：[lnmp-vhost-add-howto](https://lnmp.org/faq/lnmp-vhost-add-howto.html)

`eAccelerator` ， `xcache` ， `memcached` ， `imageMagick` ， `ionCube` 、 `opcache` 、 `redis` 的安装：[addons](https://lnmp.org/faq/addons.html)

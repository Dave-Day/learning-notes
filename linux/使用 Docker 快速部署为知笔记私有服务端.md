---
title: 使用 Docker 快速部署为知笔记私有服务端
date: 2019-11-09 08:29:33
categories: Website
---

<!-- more -->

<!-- TOC -->

- [使用 Docker 快速部署为知笔记私有服务端](#使用-docker-快速部署为知笔记私有服务端)
- [系统配置](#系统配置)
- [安装 docker](#安装-docker)
  - [使用官方脚本安装](#使用官方脚本安装)
  - [使用国内镜像源安装](#使用国内镜像源安装)
- [下载 wiz docker 镜像](#下载-wiz-docker-镜像)
  - [建立文件夹存放数据](#建立文件夹存放数据)
  - [使用国内 Dockerhub 镜像加速源（可选）](#使用国内-dockerhub-镜像加速源可选)
  - [拉取镜像](#拉取镜像)
- [启动容器](#启动容器)
  - [提示 80 端口被占用](#提示-80-端口被占用)
- [访问部署好的为知笔记](#访问部署好的为知笔记)
  - [云服务器开启端口](#云服务器开启端口)
    - [Linux 设置开放开放端口](#linux-设置开放开放端口)
    - [腾讯云 or 阿里云 or 华为云 等等 安全组放行端口](#腾讯云-or-阿里云-or-华为云-等等-安全组放行端口)
  - [浏览器访问](#浏览器访问)
  - [客户端访问](#客户端访问)
- [其他命令](#其他命令)
  - [系统重启后启动 Wiz](#系统重启后启动-wiz)
  - [修改启动参数，重新启动服务](#修改启动参数重新启动服务)
  - [更新镜像](#更新镜像)
  - [容器名被占用](#容器名被占用)
- [常见问题](#常见问题)
  - [💰 该服务如何收费](#💰-该服务如何收费)
  - [如何配置 `https`](#如何配置-https)
  - [管理员账号是什么](#管理员账号是什么)
  - [为知笔记数据保存在哪里](#为知笔记数据保存在哪里)
  - [重新启动服务器/电脑后，如何重新启动为知笔记服务](#重新启动服务器电脑后如何重新启动为知笔记服务)
  - [可以使用企业已有用户登录吗](#可以使用企业已有用户登录吗)
  - [数据可以保存在专用的存储设备或者私有云里面吗](#数据可以保存在专用的存储设备或者私有云里面吗)
  - [可以使用客户端访问吗](#可以使用客户端访问吗)
  - [可以禁止客户端访问吗](#可以禁止客户端访问吗)
  - [为知笔记服务端有时间限制吗](#为知笔记服务端有时间限制吗)
  - [如何升级为知笔记服务端](#如何升级为知笔记服务端)
  - [使用一段时间后，如果想要将数据从本地硬盘迁移到 `NAS` 或者云存储里面可以吗](#使用一段时间后如果想要将数据从本地硬盘迁移到-nas-或者云存储里面可以吗)
  - [如何进行数据备份](#如何进行数据备份)
  - [可以部署在路由器里面吗](#可以部署在路由器里面吗)
  - [可以支持微信/微博/邮件收藏吗](#可以支持微信微博邮件收藏吗)
  - [服务启动后新建笔记时间不正确](#服务启动后新建笔记时间不正确)
  - [群晖 NAS 使用 docker 镜像注意问题](#群晖-nas-使用-docker-镜像注意问题)

<!-- /TOC -->

<a id="markdown-使用-docker-快速部署为知笔记私有服务端" name="使用-docker-快速部署为知笔记私有服务端"></a>

## 使用 Docker 快速部署为知笔记私有服务端

使用 Docker 快速部署为知笔记私有服务端，掌控关键数据，将为知笔记服务端部署在自己的 Linux 云服务器。

<a id="markdown-系统配置" name="系统配置"></a>

## 系统配置

- 操作系统： CentOS Linux 7.6.1810 (Core)
- CPU：Intel(R) Xeon(R) CPU E5-26xx v4 \*1
- 内存：2G，推荐 8G 或者更多。 **要启动为知笔记服务端所有功能，需要将 docker 引擎的内存设置为至少 4G。如果您的系统内存不够，可以通过禁止为知笔记搜索服务，来降低内存占用（使用默认的 2G 内存）。**

<a id="markdown-安装-docker" name="安装-docker"></a>

## 安装 docker

<a id="markdown-使用官方脚本安装" name="使用官方脚本安装"></a>

### 使用官方脚本安装

```bash
## 使用官方安装脚本安装(速度会有点慢)
curl -sSL https://get.docker.com/ | sh
```

<a id="markdown-使用国内镜像源安装" name="使用国内镜像源安装"></a>

### 使用国内镜像源安装

```bash
## 卸载之前安装的 docker
sudo yum remove docker docker-common docker-selinux docker-engine

## 安装一些依赖
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

## 下载 Docker 软件包源 repo 文件
wget -O /etc/yum.repos.d/docker-ce.repo https://download.docker.com/linux/centos/docker-ce.repo

## 将 repo 文件中软件仓库地址更换为国内 TUNA
sudo sed -i 's+download.docker.com+mirrors.tuna.tsinghua.edu.cn/docker-ce+' /etc/yum.repos.d/docker-ce.repo

## 安装 Docker 软件包
sudo yum makecache fast
sudo yum install docker-ce

## 启动 Docker 服务
systemctl start docker

## 设置 Docker 开机启动·
systemctl enable docker
```

<a id="markdown-下载-wiz-docker-镜像" name="下载-wiz-docker-镜像"></a>

## 下载 wiz docker 镜像

<a id="markdown-建立文件夹存放数据" name="建立文件夹存放数据"></a>

### 建立文件夹存放数据

建立一个 `wizdata` 的文件夹用于存放数据。为知笔记服务端会把所有的数据保存在这个目录里面。如果是正式使用，请注意定时备份该目录。

```bash
## 建立一个 wizdata 的文件夹用于存放数据
cd ~ && mkdir wizdata
```

<a id="markdown-使用国内-dockerhub-镜像加速源可选" name="使用国内-dockerhub-镜像加速源可选"></a>

### 使用国内 Dockerhub 镜像加速源（可选）

**Wiz Docker 镜像文件 1G 左右，使用默认国外 Dockerhub 源下载会很慢。推荐使用华为镜像站(需要华为云账号，没有的可以注册一个)**

通过修改 **daemon** 配置文件 **/etc/docker/daemon.json** 来使用加速器：

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<- 'EOF'
{
    "registry-mirrors": ["自己的加速器地址"]
}
EOF

## 重载配置文件
sudo systemctl daemon-reload

## 重启 Docker 服务
sudo systemctl restart docker
```

<a id="markdown-拉取镜像" name="拉取镜像"></a>

### 拉取镜像

```bash
## 查找镜像
docker search wiznote

## 拉取最新镜像
docker pull wiznote/wizserver:latest
```

<a id="markdown-启动容器" name="启动容器"></a>

## 启动容器

```bash
## 内存为 2G
docker run --name wiz -it -d -v ~/wizdata:/wiz/storage -v /etc/localtime:/etc/localtime -p 80:80 -e SEARCH=false wiznote/wizserver

## 内存为 4G 及 4G 以上
docker run --name wiz -it -d -v ~/wizdata:/wiz/storage -v /etc/localtime:/etc/localtime -p 80:80 -e SEARCH=true wiznote/wizserver
```

第一次启动容器，因为需要下载 `docker` 镜像，并且初始化数据，速度要慢一些。请耐心等待。（根据网络状况，可能需要 `10` 分钟或者更长时间。）在下载完成后，第一次启动镜像大概需要 `2-3` 分钟时间。

<a id="markdown-提示-80-端口被占用" name="提示-80-端口被占用"></a>

### 提示 80 端口被占用

如果您当前服务器的 `80` 端口已经被占用，则可以使用其他的端口，例如使用 `8999` 端口

```bash
## 端口 80 被占用的可更换为其他端口，例如 8999 端口
docker stop wiz
docker rm wiz
docker run --name wiz -it -d -v ~/wizdata:/wiz/storage -v /etc/localtime:/etc/localtime -p 8999:80 -e SEARCH=true wiznote/wizserver
```

<a id="markdown-访问部署好的为知笔记" name="访问部署好的为知笔记"></a>

## 访问部署好的为知笔记

<a id="markdown-云服务器开启端口" name="云服务器开启端口"></a>

### 云服务器开启端口

<a id="markdown-linux-设置开放开放端口" name="linux-设置开放开放端口"></a>

#### Linux 设置开放开放端口

开放的端口位于 `/etc/sysconfig/iptables` 中 。

```bash
## 查询所有开放端口信息
netstat -anp

## 查看 Wiz 8999 端口号状态
netstat -nat | grep 8999

## 开启 Wiz 8999 端口
itables -I INPUT -p tcp --dport 8999 -j ACCEPT

## 保存到 /etc/sysconfig 目录下的 iptables 文件中
service iptables save

## 重启 iptables 服务
service iptables restart
```

备注：关闭 `Wiz 8999` 端口命令为

```bash
## 关闭 Wiz 8999 端口
iptables -A OUTPUT -p tcp --dport 8999 -j DROP
```

如果您购买的是腾讯云 or 阿里云 or 华为云等等的云服务器，您还需要在云服务商的控制面板里进行相关设置，方法如下。

<a id="markdown-腾讯云-or-阿里云-or-华为云-等等-安全组放行端口" name="腾讯云-or-阿里云-or-华为云-等等-安全组放行端口"></a>

#### 腾讯云 or 阿里云 or 华为云 等等 安全组放行端口

在各种云（腾讯云 or 阿里云 or 华为云等等） `控制面板 -> 云服务器 -> 安全组` 中添加入站和出站规则。

腾讯云安全组传送门： [securitygroup](https://console.cloud.tencent.com/cvm/securitygroup)

<a id="markdown-浏览器访问" name="浏览器访问"></a>

### 浏览器访问

打开浏览器，在地址栏里面输入：**`http://服务器IP地址:端口号`** ，如果服务正常，则会出现下面的界面 。

![为知笔记服务启动](https://pic.ryanjie.cn/2019/11/006pYIPbly1g8axp9gulsj30x80k3wfm.jpg)

默认管理员账号：`admin@wiz.cn` ，密码：`123456` 。请在部署完成后，使用这个账号，登录网页版，然后修改管理员密码。其他用户，请自行注册。免费版本可以注册 `5` 个用户（不包含管理员账号）

![wiz1](https://pic.ryanjie.cn/2019/11/006pYIPbly1g8axp8yeffj30x80k33zc.jpg)

![wiz2](https://pic.ryanjie.cn/2019/11/006pYIPbly1g8axp92jbej30x80k374z.jpg)

遇到提示 `nginx error!` 的界面， 表示为知笔记服务还没有启动起来，请继续等待并刷新浏览器。

![为知笔记服务未启动](https://pic.ryanjie.cn/2019/11/006pYIPbly1g8axp9mb09j30x70i5q4z.jpg)

<a id="markdown-客户端访问" name="客户端访问"></a>

### 客户端访问

在 [下载页面](https://www.wiz.cn/zh-cn/download.html) 下载客户端。 在登录的时候，选择登录到企业私有服务器即可。注意：该功能仅限于客户端所在网络可以访问到您的企业私有服务器才可以。例如，手机客户端，在离开公司网络的环境下，通常无法访问私有部署的为知笔记。但是已经离线的数据，则可以正常访问。也可以在离线环境下新建/修改笔记，并在回到公司后进行同步。

![wiz3](https://pic.ryanjie.cn/2019/11/006pYIPbly1g8axp9bkxfj31160jrgob.jpg)

<a id="markdown-其他命令" name="其他命令"></a>

## 其他命令

<a id="markdown-系统重启后启动-wiz" name="系统重启后启动-wiz"></a>

### 系统重启后启动 Wiz

```bash
docker start wiz
```

<a id="markdown-修改启动参数重新启动服务" name="修改启动参数重新启动服务"></a>

### 修改启动参数，重新启动服务

```bash
docker stop wiz
docker rm wiz
docker run --name wiz -it -d -v  ~/wizdata:/wiz/storage -p 8999:80 -e SEARCH=true wiznote/wizserver
```

<a id="markdown-更新镜像" name="更新镜像"></a>

### 更新镜像

```bash
docker stop wiz
docker rm wiz
docker pull wiznote/wizserver:latest
docker run --name wiz -it -d -v  ~/wizdata:/wiz/storage -p 8999:80 -e SEARCH=true wiznote/wizserver
```

<a id="markdown-容器名被占用" name="容器名被占用"></a>

### 容器名被占用

创建新 `Docker` 容器时提示容器名被占用

```bash
/usr/bin/docker-current: Error response from daemon: Conflict. The container name "/***" is already in use by container 01405ce586147b3031c1232452d001ee41fb9c938. You have to remove (or rename) that container to be able to reuse that name..
See '/usr/bin/docker-current run --help'.
```

解决办法

```bash
## 查看运行状态下的容器
docker container ls

## 查看所有容器(包含Up运行状态和Exited非运行状态)
docker ps -a

## 移除冲突容器
docker rm <CONTAINER ID>

## 创建新容器
docker run --name wiz -it -d -v  ~/wizdata:/wiz/storage -p 8999:80 -e SEARCH=true wiznote/wizserver
```

<a id="markdown-常见问题" name="常见问题"></a>

## 常见问题

<a id="markdown-💰-该服务如何收费" name="💰-该服务如何收费"></a>

### 💰 该服务如何收费

`5` 用户以下免费使用，超出 `5` 用户，按照用户数的方式按年收取费用

授权价格： `199 元/用户/年`

- 购买后，服务有效期内可享有一次免费数据迁移服务，并可使用线上增值服务，如邮件转发收藏、微信收藏、网页剪辑等
- 一次性购买 `3` 年，可升级为永久授权（含 `3` 年线上增值服务）
- `500` 用户以上团队推荐更可靠的技术架构和集成定制服务，请与我们售前客服联系

<a id="markdown-如何配置-https" name="如何配置-https"></a>

### 如何配置 `https`

[docker-https](https://www.wiz.cn/zh-cn/docker-https)

<a id="markdown-管理员账号是什么" name="管理员账号是什么"></a>

### 管理员账号是什么

默认管理员账号： `admin@wiz.cn` ，密码： `123456` 。请在部署完成后，使用这个账号，登录网页版，然后修改管理员密码。其他用户，请自行注册。免费版本可以注册 `5` 个用户（不包含管理员账号）

<a id="markdown-为知笔记数据保存在哪里" name="为知笔记数据保存在哪里"></a>

### 为知笔记数据保存在哪里

所有数据，都保存在我们前面建立的目录里面。请定时备份该目录，避免数据丢失。

<a id="markdown-重新启动服务器电脑后如何重新启动为知笔记服务" name="重新启动服务器电脑后如何重新启动为知笔记服务"></a>

### 重新启动服务器/电脑后，如何重新启动为知笔记服务

在命令行中窗口/终端中，输入

```bash
docker start wiz
```

就可以重新启动为知笔记服务了。

<a id="markdown-可以使用企业已有用户登录吗" name="可以使用企业已有用户登录吗"></a>

### 可以使用企业已有用户登录吗

可以，请联系我们的客服。

<a id="markdown-数据可以保存在专用的存储设备或者私有云里面吗" name="数据可以保存在专用的存储设备或者私有云里面吗"></a>

### 数据可以保存在专用的存储设备或者私有云里面吗

可以，请联系我们的客服

<a id="markdown-可以使用客户端访问吗" name="可以使用客户端访问吗"></a>

### 可以使用客户端访问吗

可以，您可以直接使用所有的官方客户端，然后在登录的时候，选择登录到企业私有服务器即可。注意：该功能仅限于客户端所在网络可以访问到您的企业私有服务器才可以。例如，手机客户端，在离开公司网络的环境下，通常无法访问私有部署的为知笔记。但是已经离线的数据，则可以正常访问。也可以在离线环境下新建/修改笔记，并在回到公司后进行同步。

<a id="markdown-可以禁止客户端访问吗" name="可以禁止客户端访问吗"></a>

### 可以禁止客户端访问吗

可以禁用客户端访问，确保数据只能通过网页版访问。一旦离开公司网络，就无法访问任何数据。

<a id="markdown-为知笔记服务端有时间限制吗" name="为知笔记服务端有时间限制吗"></a>

### 为知笔记服务端有时间限制吗

没有。在限定的用户数量下，您可以永久免费使用。如果想要更多用户使用，请联系我们购买使用许可。

<a id="markdown-如何升级为知笔记服务端" name="如何升级为知笔记服务端"></a>

### 如何升级为知笔记服务端

我们会经常更新 `docker` 镜像。您只需要下载更新 `docker` 镜像，然后重新启动 `docker` 镜像即可升级为知笔记服务端。无需更多额外操作。

下面是更新镜像命令行：

```bash
docker stop wiz
docker rm wiz
docker pull wiznote/wizserver:latest
```

更新完成后，重新使用前面启动镜像的命令，就可以完成服务端升级。

<a id="markdown-使用一段时间后如果想要将数据从本地硬盘迁移到-nas-或者云存储里面可以吗" name="使用一段时间后如果想要将数据从本地硬盘迁移到-nas-或者云存储里面可以吗"></a>

### 使用一段时间后，如果想要将数据从本地硬盘迁移到 `NAS` 或者云存储里面可以吗

可以。包括数据库，笔记数据内容等，都可以完整的进行迁移。具体方案，请联系我们的客服。

<a id="markdown-如何进行数据备份" name="如何进行数据备份"></a>

### 如何进行数据备份

您可以自己备份用户数据目录，或者将数据保存在 `NAS/云存储` 里面。如有需求，请联系我们的客服。

<a id="markdown-可以部署在路由器里面吗" name="可以部署在路由器里面吗"></a>

### 可以部署在路由器里面吗

由于路由器通常 `CPU` 性能较低，内存也不够大，所以基本无法运行起来。

<a id="markdown-可以支持微信微博邮件收藏吗" name="可以支持微信微博邮件收藏吗"></a>

### 可以支持微信/微博/邮件收藏吗

可以。[点击这里查看使用方式](https://www.wiz.cn/zh-cn/docker-collector-service)

<a id="markdown-服务启动后新建笔记时间不正确" name="服务启动后新建笔记时间不正确"></a>

### 服务启动后新建笔记时间不正确

因为 docker 镜像默认时区不正确。因此需要进入 `docker` 里面手工设置一下时区，命令如下：

```bash
docker exec -it wiz /bin/bash
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
exit
```

上面的命令，会把 `docker` 里面的时区设置为东八区（北京时间）。如果需要设置成其他的时区，请自行修改上面的命令。具体时区的名称，可以搜索 `linux` 时区名称获取。

如果是 `linux` ，则可以通过在命令行里面加入命令，来自动获取当前时区：

```bash
-v  /etc/localtime:/etc/localtime
```

完整命令行：实际使用是，请根据自己的情况调整其他参数，例如映射路径，端口映射等。

```bash
run --name wiz -it -d -v  ~/wizdata:/wiz/storage -p 8088:80 -v  /etc/localtime:/etc/localtime -e SEARCH=true wiznote/wizserver
```

如果是 `mac` 系统，则可以通过下面的命令行来自动设置时区（实际使用是，请根据自己的情况调整其他参数，例如映射路径，端口映射等。）

```bash
-e TZ= `ls -la /etc/localtime | cut -d/ -f8-9`
```

<a id="markdown-群晖-nas-使用-docker-镜像注意问题" name="群晖-nas-使用-docker-镜像注意问题"></a>

### 群晖 NAS 使用 docker 镜像注意问题

1. 内存小于 `4G` 的 `NAS` ，可能无法正常启动 `docker` 镜像。
2. 目录映射，请勿在群晖管理界面建立目录映射，这样目录权限会有问题。请 `ssh` 到 `NAS` 里面，然后按照前面 `linux` 方式建立数据目录。
3. 群晖 `NAS` 无法直接使用 80 端口，请自行选择合适的端口。

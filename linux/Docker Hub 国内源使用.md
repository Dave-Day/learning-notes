---
title: Docker Hub 国内源使用
date: 2019-07-01 12:06:16
categories: Docker
---

<!-- more -->

<!-- TOC -->

- [Docker Hub 国内源使用](#docker-hub-国内源使用)
  - [镜像地址](#镜像地址)
  - [说明](#说明)
  - [使用说明](#使用说明)
    - [Linux](#linux)
      - [方法 1](#方法-1)
      - [方法 2](#方法-2)
      - [方法 3](#方法-3)
    - [macOS](#macos)
    - [Windows](#windows)
    - [Docker Toolbox](#docker-toolbox)
  - [检查 Docker Hub 是否生效](#检查-docker-hub-是否生效)
  - [相关链接](#相关链接)

<!-- /TOC -->

<a id="markdown-docker-hub-国内源使用" name="docker-hub-国内源使用"></a>

# Docker Hub 国内源使用

使用 Docker 的时候，需要经常从官方获取镜像，但是由于显而易见的网络原因，拉取镜像的过程非常耗时，严重影响使用 Docker 的体验。如果您是在国内的网络环境使用 Docker，那么 Docker 镜像加速器一定能帮到您。

<a id="markdown-镜像地址" name="镜像地址"></a>

## 镜像地址

- USTC：`https://docker.mirrors.ustc.edu.cn/`
- HUAWEI：`https://0593f321718026730f10c01bb38d1860.mirror.swr.myhuaweicloud.com`
- Ali：`https://wz099adw.mirror.aliyuncs.com`
- WangYi：`https://hub-mirror.c.163.com`
- DaoCloud：`http://f1361db2.m.daocloud.io`
- Qiniu：`https://reg-mirror.qiniu.com`
- Docker-cn：`https://registry.docker-cn.com`
- Tencent：`https://mirror.ccs.tencentyun.com`
- Azure：`https://dockerhub.azk8s.cn`

<a id="markdown-说明" name="说明"></a>

## 说明

Docker Hub 镜像缓存，提升了国内网络访问 Docker Hub 的速度。

<a id="markdown-使用说明" name="使用说明"></a>

## 使用说明

<a id="markdown-linux" name="linux"></a>

### Linux

<a id="markdown-方法-1" name="方法-1"></a>

#### 方法 1

对于使用 upstart 的系统（Ubuntu 14.04、Debian 7 Wheezy），在配置文件 `/etc/default/docker` 中的 `DOCKER_OPTS` 中配置 Hub 地址：

```bash
DOCKER_OPTS="--registry-mirror=https://docker.mirrors.ustc.edu.cn/"
```

重新启动服务:

```bash
sudo service docker restart
```

对于使用 systemd 的系统（Ubuntu 16.04+、Debian 8+、CentOS 7）， 修改 `/etc/docker/daemon.json` 配置文件：

```bash
## ustc mirrors
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<- 'EOF'
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn/"]
}
EOF

## huawei mirrors
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<- 'EOF'
{
    "registry-mirrors": ["https://0593f321718026730f10c01bb38d1860.mirror.swr.myhuaweicloud.com"]
}
EOF

## ali mirrors
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://wz099adw.mirror.aliyuncs.com"]
}
EOF
```

重新加载配置文件重启 docker：

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

<a id="markdown-方法-2" name="方法-2"></a>

#### 方法 2

```bash
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io
```

该脚本可以将 --registry-mirror 加入到你的 Docker 配置文件 /etc/docker/daemon.json 中。适用于 Ubuntu14.04、Debian、CentOS6 、CentOS7、Fedora、Arch Linux、openSUSE Leap 42.1，其他版本可能有细微不同。更多详情请访问文档。

<a id="markdown-方法-3" name="方法-3"></a>

#### 方法 3

执行以下命令:

```bash
curl -sSL http://oyh1cogl9.bkt.clouddn.com/setmirror.sh | sh -s https://reg-mirror.qiniu.com
```

该脚本将镜像加速地址加入到你的 Docker 配置文件/etc/docker/daemon.json 中。适用于 Ubuntu / Debian / CentOS。

<a id="markdown-macos" name="macos"></a>

### macOS

- 对于 10.10.3 以下的用户 推荐使用 Docker Toolbox
- 对于 10.10.3 以上的用户 推荐使用 Docker for Mac

1. 打开 “Docker.app”
2. 进入偏好设置页面(快捷键 `⌘,` )
3. 打开 “Daemon” 选项卡
4. 在 “Registry mirrors” 中添加 `https://docker.mirrors.ustc.edu.cn/`
5. 点击下方的 “Apply & Restart” 按钮

<a id="markdown-windows" name="windows"></a>

### Windows

在系统右下角托盘 Docker 图标内右键菜单选择 `Settings` ，打开配置窗口后左侧导航菜单选择 `Daemon` 。在 `Registry mirrors` 一栏中填写地址 `https://docker.mirrors.ustc.edu.cn/` ，之后点击 Apply 保存后 Docker 就会重启并应用配置的镜像地址了。

<a id="markdown-docker-toolbox" name="docker-toolbox"></a>

### Docker Toolbox

- 对于 Windows 10 以下的用户，推荐使用 Docker Toolbox
- 对于 Windows 10 以上的用户 推荐使用 Docker for Windows

针对安装了 Docker Toolbox 的用户，您可以参考以下配置步骤：

1. 创建一台安装有 Docker 环境的 Linux 虚拟机，指定机器名称为 default，同时配置 Docker 加速器地址。

   ```bash
   docker-machine create --engine-registry-mirror=https://wz099adw.mirror.aliyuncs.com -d virtualbox default
   ```

2. 查看机器的环境配置，并配置到本地，并通过 Docker 客户端访问 Docker 服务。

   ```bash
   docker-machine env default
   eval "$(docker-machine env default)"
   docker info
   ```

[admonition title="注意" color="red"]

Docker for Windows 和 Docker Toolbox 互不兼容，如果同时安装两者的话，需要使用 hyperv 的参数启动。

```bash
docker-machine create --engine-registry-mirror=https://wz099adw.mirror.aliyuncs.com -d hyperv default
```

Docker for Windows 有两种运行模式，一种运行 Windows 相关容器，一种运行传统的 Linux 容器。同一时间只能选择一种模式运行。

[/admonition]

<a id="markdown-检查-docker-hub-是否生效" name="检查-docker-hub-是否生效"></a>

## 检查 Docker Hub 是否生效

在命令行执行 `docker info` ，如果从结果中看到了镜像加速地址，说明配置成功。

```bash
Registry Mirrors:
    https://docker.mirrors.ustc.edu.cn/
```

<a id="markdown-相关链接" name="相关链接"></a>

## 相关链接

- [Docker 主页](https://www.docker.com)
- [Docker Hub](https://hub.docker.com)
- [Docker 命令参考文档](https://docs.docker.com/engine/reference/commandline/cli/?spm=5176.8351553.0.0.1dd01991cGTHJO)
- [Dockerfile 镜像构建参考文档](https://docs.docker.com/engine/reference/builder/)
- [Docker Hub 源使用帮助 - USTC](http://mirrors.ustc.edu.cn/help/dockerhub.html)
- [华为云容器镜像服务](https://www.huaweicloud.com/product/swr.html)
- [镜像加速器 - 阿里云](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)
- [七牛镜像中心文档](https://kirk-enterprise.github.io/hub-docs/)
- [网易镜像中心](https://c.163yun.com/hub#/home)
- [DaoCloud 镜像站](https://daocloud.io/mirror)
- [使用 DockerHub 加速器 - 腾讯云](https://cloud.tencent.com/document/product/457/9113)
- [AKS on Azure China Best Practices](https://github.com/Azure/container-service-for-azure-china/blob/master/aks/README.md#22-container-registry-proxy)

---
title: CentOS 7 安装 Docker-CE
url: linux-centos-7-insatll-docker-ce
---

## 使用官方安装脚本

使用官方安装脚本自动安装，仅适用于公网环境。

```bash
#安装之前需卸载旧版本
sudo yum remove docker \CE
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine \
                  docker-selinux
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

## 手动 yum 安装

### 卸载旧版本

```bash
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine \
                  docker-selinux

sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine docker-selinux
```

### 安装依赖

```bash
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```

### 下载软件仓库源

```bash
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

# 或者直接使用 Aliyun，可以省略替换国内镜像仓库步骤
sudo yum-config-manager \
    --add-repo \
    http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 禁用
sudo yum-config-manager --disable docker-ce-nightly
sudo yum-config-manager --disable docker-ce-test
```

### 替换为国内镜像仓库

```bash
# tuna
sudo sed -i 's+download.docker.com+mirrors.tuna.tsinghua.edu.cn/docker-ce+' /etc/yum.repos.d/docker-ce.repo

# huawei
sudo sed -i 's+download.docker.com+mirrors.huaweicloud.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo

# tencent
sudo sed -i 's+download.docker.com+mirrors.cloud.tencent.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo
```

### 更新软件包缓存

```bash
sudo yum makecache fast
```

### 安装 Docker Engine

安装最新版本的 Docker Engine-Community 和 containerd。

```bash
sudo yum install -y docker-ce docker-ce-cli containerd.io
```

#### 安装指定版本的Docker-CE

```bash
$ yum list docker-ce --showduplicates | sort -r
 * updates: mirrors.aliyun.com
Loading mirror speeds from cached hostfile
Loaded plugins: fastestmirror, langpacks
Installed Packages
 * extras: mirrors.aliyun.com
docker-ce.x86_64            3:19.03.9-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.8-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.7-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.6-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.5-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.4-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.3-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.2-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.1-3.el7                    docker-ce-stable 
docker-ce.x86_64            3:19.03.12-3.el7                   docker-ce-stable 
……
docker-ce.x86_64            17.03.0.ce-1.el7.centos            docker-ce-stable 
 * base: mirrors.aliyun.com
Available Packages

# sudo yum -y install docker-ce-[VERSION]
$ sudo yum -y install docker-ce-3:19.03.8-3.el7
# 注意：在某些版本之后，docker-ce安装出现了其他依赖包，如果安装失败的话请关注错误信息。例如 docker-ce 17.03 之后，需要先安装 docker-ce-selinux。
# yum list docker-ce-selinux --showduplicates | sort -r
# sudo yum -y install docker-ce-selinux-[VERSION]
```

### 开启 Docker 服务

```bash
sudo systemctl start docker
```

### 查看 Docker 服务的状态

```
sudo systemctl status docker
```

### 设置 Docker 开机启动

```bash
sudo systemctl enable docker
```

### 创建 Docker 工作组

```bash
sudo groupadd docker
```

### 添加用户到 Docker 工作组

Docker 默认只能通过 root 权限执行操作， 但通过将用户添加到 `docker` 用户组可以规避这一点：

```bash
sudo gpasswd -a ${USER} docker
## or 
sudo usermod -aG docker ${USER}
```

### 重启 Docker 服务 

```bash
sudo systemctl restart docker
```

### 安装校验

```bash
$ docker version
Client: Docker Engine - Community
 Version:           19.03.12
 API version:       1.40
 Go version:        go1.13.10
 Git commit:        48a66213fe
 Built:             Mon Jun 22 15:46:54 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.12
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.13.10
  Git commit:       48a66213fe
  Built:            Mon Jun 22 15:45:28 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.2.13
  GitCommit:        7ad184331fa3e55e52b890ea95e65ba581ae3429
 runc:
  Version:          1.0.0-rc10
  GitCommit:        dc9208a3303feef5b3839f4323d9beb36df0a9dd
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
```



## 配置Docker

### 配置国内镜像

#### 常用国内镜像地址

- Netease：`http://hub-mirror.c.163.com`
- Ali1：`https://2h3po24f.mirror.aliyuncs.com`
- Ali2：`https://3laho3y4.mirror.aliyuncs.com`
- Ali3：`https://c0bhpg4f.mirror.aliyuncs.com`
- Ali4：`https://az099ade.mirror.aliyuncs.com`
- USTC：`https://docker.mirrors.ustc.edu.cn`

- DaoCloud ：`http://f1361db2.m.daocloud.io`

> 阿里云专属镜像加速器申请地址：[镜像加速器 - 阿里云](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)

#### 配置镜像加速器

```bash
sudo mkdir -p /etc/docker
sudo tee -a /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

### 修改Docker持久化目录

```bash
test -d /var/lib/docker && \
    mv /var/lib/docker /var/lib/docker_backup && \
    mkdir -p /data/docker && \
    ln -sf /data/docker /var/lib/docker
```

## 参考

- [Install Docker Engine on CentOS](https://docs.docker.com/engine/install/centos/)
- [Docker CE 镜像源站](https://developer.aliyun.com/article/110806)
- [阿里云 - 容器镜像服务](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)
- [Docker Community Edition 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)
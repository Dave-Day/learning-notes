# Manjaro 安装 Docker

## 安装国内镜像源

### 使用国内镜像源

```bash
sudo tee /etc/pacman.d/mirrorlist <<-'EOF'
## Country : China 
Server = https://mirrors.aliyun.com/manjaro/stable/$repo/$arch 

## Country : China 
Server = https://mirrors.ustc.edu.cn/manjaro/stable/$repo/$arch 

## Country : China 
Server = https://mirrors.tuna.tsinghua.edu.cn/manjaro/stable/$repo/$arch

## Country : China
Server = https://mirrors.sjtug.sjtu.edu.cn/manjaro/stable/$repo/$arch

EOF
```

### 刷新缓存

```bash
sudo pacman -Syy
```

### 安装 Docker

### 卸载旧版本

```bash
sudo pacman -R docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine \
                  docker-selinux
```

## Docker 安装配置

### 安装 Docker

```bash
sudo pacman -S docker docker-compose docker-machine
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
sudo gpasswd -a ryanjie docker
## or 
sudo usermod -aG docker ryanjie
```

### 安装校验

```bash
$ docker version
Client:
 Version:           19.03.12-ce
 API version:       1.40
 Go version:        go1.14.5
 Git commit:        48a66213fe
 Built:             Sat Jul 18 01:33:21 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server:
 Engine:
  Version:          19.03.12-ce
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.14.5
  Git commit:       48a66213fe
  Built:            Sat Jul 18 01:32:59 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v1.4.0.m
  GitCommit:        09814d48d50816305a8e6c1a4ae3e2bcc4ba725a.m
 runc:
  Version:          1.0.0-rc92
  GitCommit:        ff819c7e9184c13b7c2607fe6c30ae19403a7aff
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
```

### 配置 Docker 国内镜像

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

## 参考

- [Docker CE 镜像源站](https://developer.aliyun.com/article/110806)
- [阿里云 - 容器镜像服务](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)
- [Docker Community Edition 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)


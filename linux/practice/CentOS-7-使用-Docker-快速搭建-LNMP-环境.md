---
title: CentOS 7 使用 Docker 快速搭建 LNMP 环境
abstract: CentOS 7 使用 Docker 快速搭建 LNMP 环境
url: centos-docker-lnmp-1
permalink: centos-docker-lnmp-1
date: 2021-01-03 23:34:50
category:
  - CentOS
tags:
  - CentOS
  - Docker
  - LNMP
---

## Docker 安装

### 安装 Docker

```bash
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

### 配置国内镜像

```bash
mkdir -p /etc/docker
cat >/etc/docker/daemon.json << EOF
{
  "registry-mirrors": [
      "http://hub-mirror.c.163.com",
      "https://docker.mirrors.ustc.edu.cn"
  ]
}
EOF
```

### 修改 Docker 持久化目录

```bash
test -d /var/lib/docker && \
    mv /var/lib/docker /var/lib/docker_backup && \
    mkdir -p /data/docker && \
    ln -sf /data/docker /var/lib/docker
```

### 创建 Docker 工作组

```bash
groupadd docker
```

### 添加用户到 Docker 工作组

Docker 默认只能通过 root 权限执行操作， 但通过将用户添加到 `docker` 用户组可以规避这一点：

```bash
gpasswd -a ${USER} docker
## or
usermod -aG docker ${USER}
```

### 启动 Docker 并加入开机启动项

```bash
systemctl daemon-reload
systemctl start docker
systemctl enable docker
```

### 安装校验

```bash
docker version
```

## 安装 LNMP

### 搜索镜像

```bash
docker search lnmp
```

### 拉取镜像

```bash
$ docker pull 2233466866/lnmp:latest
```

### 创建相关目录

```bash
mkdir -p /app/lnmp/default /docker/lnmp/
cd /docker/lnmp/
mkdir -p data/mysql conf/vhost
mkdir logs backup temp
```

### 创建相关文件

Nginx/MySQL/PHP 配置文件根据自己情况修改。

#### Nginx 配置文件

```bash
cat >/docker/lnmp/conf/nginx.conf <<EOF
user                    www;
worker_processes        auto;
worker_cpu_affinity     auto;
pid                     logs/nginx.pid;

events {
    worker_connections  102400;
}

http {
    charset             utf-8;
    server_tokens       off;

    log_format  main    '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

    include             mime.types;
    default_type        application/octet-stream;

    client_max_body_size 20M;

    sendfile            on;
    keepalive_timeout   20;

    gzip                on;
    gzip_vary           on;
    gzip_comp_level     1;
    gzip_types          text/css application/javascript application/json image/png image/webp image/apng image/jpeg image/x-icon;

    error_log           /www/z_error.log;
    access_log          /www/z_$host.log main;

    server {
        listen 443 ssl http2;
        server_name www.test.com;
        root        /www;

        # SSL 配置......

        # Allow large attachments
        client_max_body_size 128M;

        location / {
            index   index.php index.html index.htm;
            proxy_pass http://127.0.0.1:8080;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location ~* \.php {
            include                 fastcgi_params;
            fastcgi_index           index.php;
            fastcgi_pass            127.0.0.1:9000;
            fastcgi_split_path_info ^(.+\.php)(.*)$;
            fastcgi_param           PATH_INFO       $fastcgi_path_info;
            fastcgi_param           SCRIPT_NAME     $fastcgi_script_name;
            fastcgi_param           SCRIPT_FILENAME $document_root$fastcgi_script_name;
        }
    }
}
EOF
```

#### MySQL 配置文件

```bash
cat >/docker/lnmp/conf/my.cnf <<EOF
[mysqld]
datadir=/data/mysql
socket=/var/lib/mysql/mysql.sock
symbolic-links=0
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
EOF
```

#### PHP 配置文件

配置文件太大就不贴了，直接下载然后本地修改吧。不会使用 vim 的使用 sed 命令进行替换。

```bash
wget -N https://pic.ryanjie.cn/docker/lnmp/php.ini -O /docker/lnmp/conf/php.ini
wget -N https://pic.ryanjie.cn/docker/lnmp/php-fpm.conf -O /docker/lnmp/conf/php-fpm.conf
## 上面两个文件也可以
wget -N https://pic.ryanjie.cn/docker/lnmp/nginx.conf -O /docker/lnmp/conf/nginx.conf
wget -N https://pic.ryanjie.cn/docker/lnmp/my.cnf -O /docker/lnmp/conf/my.cnf
```

### 备份配置文件

```bash
cp conf/* backup/
```

### 创建自定义网络 lnmp

```bash
$ docker network create lnmp
9d4d47ee3b875cdadf7300182f5de43523efdd0aaecbe37a79ed2cdc75feb777
$ docker network  ls
NETWORK ID     NAME      DRIVER    SCOPE
545f4bdc894a   bridge    bridge    local
753524bb4716   host      host      local
9d4d47ee3b87   lnmp      bridge    local
8623643804ac   none      null      local
```

### 启动容器

```bash
docker run -dit \
-p 8080:80 \
-p 443:443 \
-p 3306:3306 \
-p 9000:9000 \
-e TC="Asia/Shanghai" \
-v /sys/fs/cgroup:/sys/fs/cgroup:ro \
-v /app/lnmp:/www \
-v /docker/lnmp/conf/nginx.conf:/usr/local/nginx/conf/nginx.conf \
-v /docker/lnmp/conf/vhost:/usr/local/nginx/conf/vhost \
-v /docker/lnmp/data/mysql:/data/mysql \
-v /docker/lnmp/conf/my.cnf:/etc/my.cnf \
-v /docker/lnmp/conf/php.ini:/usr/local/php7/lib/php.ini \
-v /docker/lnmp/conf/php-fpm.conf:/usr/local/php7/etc/php-fpm.conf \
-v /docker/lnmp/logs:/logs \
--restart=always \
--net lnmp \
--privileged=true \
--name=mylnmp \
2233466866/lnmp:latest
```

### 连接容器

```bash
# 容器名称与上一步保持一致
docker exec -it lnmp /bin/bash
```

## 配置 LNMP

### 检查 Nginx/MySQL/PHP 状态

```bash
ps aux|grep nginx
ps aux|grep mysql
ps aux|grep php-fpm
# 或者(Or)
systemctl status nginx
systemctl status mysqld
systemctl status php7
```

### 初始密码(Default password)

```bash
cat /var/log/mysqld.log|grep 'A temporary password'
# 或
password=`cat /var/log/mysqld.log|grep 'A temporary password'`;password=${password:91};echo $password
```

### 初始化(initialize)

```bash
# 请及时修改Mysql的密码(默认并未重置密码和初始化)
password=`cat /var/log/mysqld.log|grep 'A temporary password'`
password=${password:91}
echo -e "${password}\n${password}\n${password}\nn\ny\ny\ny\ny\n"
# 以上三条命令的输出为以下命令的输入
mysql_secure_installation
```

### PHP 扩展(PHP extension)

```bash
# 默认已安装部分扩展在目录：/usr/local/php7/lib/php/extensions/no-debug-non-zts-20170718/
# 如果要启用指定扩展，则需要修改php.ini，加上
extension=xxx.so
# xxx为PHP扩展的文件名，然后重启php
systemctl restart php7
```

### 版本(Version)

```bash
# 各版本详细信息请参考
https://github.com/2233466866/lnmp/wiki
```

## 推送镜像

这里使用 Ucloud 的 [**公共镜像库 UHub**](https://docs.ucloud.cn/uhub/README?id=)。UHub 是一种 UCloud 推出的免费的公共镜像库服务。

1. 登录镜像仓库。

   ```bash
   $ docker login uhub.service.ucloud.cn -u ryan@gmail.com
   ```

2. 本地对镜像打 `tag`:

   ```bash
   $ docker tag 2233466866/lnmp:latest uhub.service.ucloud.cn/kongren/2233466866/lnmp:0.0.1
   ```

3. 提交镜像到仓库:

   ```bash
   $ docker push uhub.service.ucloud.cn/kongren/2233466866/lnmp:0.0.1
   ```

## 参考

- [2233466866/lnmp Wiki](https://github.com/2233466866/lnmp/wiki)

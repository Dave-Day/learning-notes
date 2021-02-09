---
title: 在线生成 Nginx 配置文件 - nginxconfig.io
date: 2019-07-02 23:59:00
categories: Website
---

<!-- more -->

<!-- TOC -->

- [在线生成 Nginx 配置文件 - nginxconfig.io](#在线生成-nginx-配置文件---nginxconfigio)
- [nginxconfig.io](#nginxconfigio)
  - [NGINX 优点](#nginx-优点)
- [软件功能](#软件功能)
- [软件部署](#软件部署)
- [相关链接](#相关链接)

<!-- /TOC -->

[github author="digitalocean" project="nginxconfig.io"][/github]

<a id="markdown-在线生成-nginx-配置文件---nginxconfigio" name="在线生成-nginx-配置文件---nginxconfigio"></a>

## 在线生成 Nginx 配置文件 - nginxconfig.io

如果你在使用 NGINX 架设 Web 服务器的过程中为配置而感到头痛的话，那么不妨通过 NGINX Config 这个工具来在线生成。NGINX Config 支持 HTTP、HTTPS、PHP、Python、Node.js、WordPress、Drupal、缓存、逆向代理、日志等各种配置选项。

![nginxconfig.io](https://pic.ryanjie.cn/2019/07/nginx-config.png)

<a id="markdown-nginxconfigio" name="nginxconfigio"></a>

## nginxconfig.io

NGINX 不仅仅是一个网络服务器。

<a id="markdown-nginx-优点" name="nginx-优点"></a>

### NGINX 优点

- 内存使用率低
- 高并发
- 异步事件驱动架构
- 负载均衡
- 反向代理
- 带有缓存的 FastCGI 支持（PHP）
- 快速处理静态文件
- 带有 SNI 的 TLS / SSL

<a id="markdown-软件功能" name="软件功能"></a>

## 软件功能

HTTPS，HTTP / 2，IPv6，certbot，HSTS，安全标头，SSL 配置文件，OCSP 解析器，缓存，gzip，brotli，后备路由，反向代理，www / non-www 重定向，CDN，PHP（TCP / socket， WordPress，Drupal，Magento），Node.js 支持，Python（Django）服务器等。

<a id="markdown-软件部署" name="软件部署"></a>

## 软件部署

1. Clone the repository

   ```bash
   git clone https://github.com/digitalocean/nginxconfig.io.git
   ```

2. Install NPM packages

   ```bash
   npm ci
   ```

3. Run the development server _(with file watchers)_

   ```bash
   npm run dev
   ```

4. Open the development site **[localhost:8080](http://localhost:8080/)**

5. Lint your code _(eslint & sass-lint)_

   ```bash
   npm test
   ```

6. Analyze production bundle size & composition

   ```bash
   npm run analyze
   ```

7. Build for production _(to the `dist` directory)_

   ```bash
   npm run build
   ```

<a id="markdown-相关链接" name="相关链接"></a>

## 相关链接

- [Github](https://github.com/digitalocean/nginxconfig.io)
- [Website](https://nginxconfig.io)
- [NGINX documentation](http://nginx.org/en/docs/)

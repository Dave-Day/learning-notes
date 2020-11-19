---
title: 解决 wordpress 429 问题插件 WP-China-Yes
date: 2020-04-04 06:04:33
categories: WordPress
---

<!-- more -->

<!-- TOC -->

- [解决 wordpress 429 问题插件 WP-China-Yes](#解决-wordpress-429-问题插件-wp-china-yes)
  - [介绍](#介绍)
  - [现状](#现状)
  - [使用方法](#使用方法)
  - [常见问题](#常见问题)
    - [速度为什么这么慢](#速度为什么这么慢)
    - [更新日志](#更新日志)
    - [2.1.0](#210)
    - [2.0.3](#203)
    - [2.0.2](#202)
    - [2.0.0](#200)
    - [1.0.1](#101)
  - [下载地址](#下载地址)

<!-- /TOC -->

<a id="markdown-解决-wordpress-429-问题插件-wp-china-yes" name="解决-wordpress-429-问题插件-wp-china-yes"></a>

# 解决 wordpress 429 问题插件 WP-China-Yes

自去年 10 月份开始，国内无法正常访问 WordPress 官网，一直显示"429 Too Many Requests"，给安装、升级程序和插件等造成极大的不便。为了解决这一问题，国内 WP 爱好者开发了一款可以有效解决国内访问官网慢和无法访问的 WordPress 插件：**WP-China-Yes**。

![WP-China-Yes](https://pic.ryanjie.cn/2020/04/WP-China-Yes.jpg)

<a id="markdown-介绍" name="介绍"></a>

## 介绍

[github author="sunxiyuan" project="wp-china-yes"][/github]

> 因为 WordPress 官方的服务器都在国外，所以中国大陆的用户在访问由 WordPress 官方提供的服务（插件、主题商城，WP 程序版本更新等）时总是很缓慢。
>
> 近期又因为被攻击的原因，WordPress 的 CDN 提供商屏蔽了中国大陆的流量，导致大陆用户访问插件主题商城等服务时报 429 错误。
>
> 为解决上述问题，我在大陆境内架设了基于反向代理的缓存加速节点，用以加快 WordPress 官方服务在中国大陆的访问速度，并规避 429 报错问题。
>
> 此加速节点是直接为你的站点与 WordPress 总部服务器的一切通信做加速，加速范围包括但不限于：插件、主题商城的资源下载、作品图片、作者头像、主题预览等……
>
> 为使更多的使用 WordPress 的同学能够用上大陆加速节点，我开发了 WP-China-Yes 插件，以求帮助大家方便简洁的替换官方服务链接为大陆节点。
>
> 这个是一个公益项目，我始终都不会以任何借口对插件、加速节点的使用权等进行收费。

<a id="markdown-现状" name="现状"></a>

## 现状

该项目目前由又拍云全力赞助支持——提供无限量 CDN 流量及数据存储资源。

后端由各个企业和个人捐助服务器组建反代节点，反代 WordPress 官方服务，前端统一接入到又拍云上，由 CDN 层实现负载均衡和容灾热备，保证高可用性。

目前官方插件、主题、核心程序、作品 LOGO、作品横幅、作品截图、作者头像、主题预览等需要从官方调取的一切静态资源均会在第一次访问后被迁移到又拍云存储上缓存 1 年的时间，日后访问直接从国内云存储调取，速度飞快。

对于动态的 API 请求也有制定专门的加速策略，经测试：从河北秦皇岛移动带宽上直接调用 WP 官方接口检测插件更新情况平均需要耗费 11 秒的时间，而使用中国区仓库源加速后只需要 1 秒。

<a id="markdown-使用方法" name="使用方法"></a>

## 使用方法

- 下载并安装插件后直接启用即可，该插件会自动接收所有 WP 访问境外服务器的流量。
- 插件不会更改你的 WordPress 程序，若不想使用大陆加速节点，直接停用插件即可。
- 插件不会拖累站点的速度，她只有在需要访问官方服务的时候才会被激活，并且核心代码只有 30 行左右，不会对你的站点造成任何负担。

<a id="markdown-常见问题" name="常见问题"></a>

## 常见问题

<a id="markdown-速度为什么这么慢" name="速度为什么这么慢"></a>

### 速度为什么这么慢

加速节点使用 CDN 缓存数据，对于访问人数较少的冷门资源访问速度会慢很多。若遇到访问超时的情况请等 10 分钟再试，这段时间 CDN 会自动去 WordPress 官方服务器拉取资源供使用。

<a id="markdown-更新日志" name="更新日志"></a>

### 更新日志

<a id="markdown-210" name="210"></a>

### 2.1.0

- 取消社区源选择功能，只保留主源和备源
- 去除设置页的 tab
- 在仪表盘放置了赞助者名单展示小部件（可关闭）

<a id="markdown-203" name="203"></a>

### 2.0.3

- 修复修改仓库源后刷新页面无法正确展示源信息的问题

<a id="markdown-202" name="202"></a>

### 2.0.2

- 修复 API 接口编写不规范的问题

<a id="markdown-200" name="200"></a>

### 2.0.0

- 社区源列表 完成
- 自定义源支持 完成

<a id="markdown-101" name="101"></a>

### 1.0.1

- 基本功能 完成

<a id="markdown-下载地址" name="下载地址"></a>

## 下载地址

- [Github](https://github.com/sunxiyuan/wp-china-yes/releases/latest)
- [Wordpress](https://wordpress.org/plugins/wp-china-yes)
- [wordpress 镜像站 1](http://wp101.net/plugins/wp-china-yes)
- [wordpress 镜像站 2](https://wp.hipush.cn/plugins/wp-china-yes)
- [作者博客](https://www.ibadboy.net/archives/3204.html)
- [90 盘](https://www.90pan.com/o129487)

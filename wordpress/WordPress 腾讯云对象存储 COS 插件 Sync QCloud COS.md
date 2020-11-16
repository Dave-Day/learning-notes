---
title: WordPress 腾讯云对象存储 COS 插件 Sync QCloud COS
date: 2020-04-19 07:39:28
categories: WordPress
---

<!-- more -->

<!-- TOC -->

- [WordPress 腾讯云对象存储 COS 插件 Sync QCloud COS](#wordpress-腾讯云对象存储-cos-插件-sync-qcloud-cos)
  - [插件特点](#插件特点)
  - [COS 优点](#cos-优点)
  - [插件安装](#插件安装)
    - [后台安装（推荐使用）](#后台安装推荐使用)
    - [下载源码](#下载源码)
  - [修改配置](#修改配置)
  - [常见问题](#常见问题)
  - [配置指南](#配置指南)
  - [插件下载](#插件下载)

<!-- /TOC -->

<a id="markdown-wordpress-腾讯云对象存储-cos-插件-sync-qcloud-cos" name="wordpress-腾讯云对象存储-cos-插件-sync-qcloud-cos"></a>

# WordPress 腾讯云对象存储 COS 插件 Sync QCloud COS

将 WordPress 站点图片等多媒体文件直接上传到腾讯云对象存储 COS 中，该插件依赖腾讯云对象存储 COS。腾讯云对象存储（Cloud Object Storage，简称：COS）是腾讯云提供的面向非结构化数据，支持 HTTP/HTTPS 协议访问的分布式存储服务，它能容纳海量数据并保证用户对带宽和容量扩充无感知，可以作为大数据计算与分析的数据池。

[github author="sy-records" project="wordpress-qcloud-cos"][/github]

![wordpress-qcloud-cos](https://cdn.jsdelivr.net/gh/sy-records/wordpress-qcloud-cos/screenshot-1.png)

<a id="markdown-插件特点" name="插件特点"></a>

## 插件特点

- 可配置是否上传缩略图和是否保留本地备份
- 本地删除可同步删除腾讯云上面的文件
- 支持腾讯云 COS 存储桶绑定自定义域名
- 支持替换数据库中旧的资源链接地址
- 支持北京、上海、广州、香港、法兰克福等完整地域使用
- 支持同步历史附件到 COS
- 支持验证桶名是否填写正确
- 支持腾讯云数据万象 CI 图片处理

<a id="markdown-cos-优点" name="cos-优点"></a>

## COS 优点

- 在中国大陆地区，使用 COS 标准存储的用户，每月可享受一定量的免费存储空间、免费流量、和免费请求，基本可以满足中小型博客需要
- 标准存储为用户提供了高可靠性，高可用性、高性能的对象存储服务
- 适用场景广泛，支持热点视频、社交图片、移动应用、游戏程序、动态网站等
- 响应时间毫秒级，读写请求费用极低
- 腾讯云对象存储提供整体 99.95% 的可用性，针对标准存储引擎承诺服务可用性不低于 99.95%
- 更多查看 [腾讯云对象存储服务等级协议](https://cloud.tencent.com/document/product/436/6227)

<a id="markdown-插件安装" name="插件安装"></a>

## 插件安装

<a id="markdown-后台安装推荐使用" name="后台安装推荐使用"></a>

### 后台安装（推荐使用）

WordPress 后台安装插件页面搜索`Sync QCloud COS`，点击安装

<a id="markdown-下载源码" name="下载源码"></a>

### 下载源码

从 Github 下载源码，通过 WordPress 后台上传安装，或者直接将源码上传到 WordPress 插件目录`wp-content/plugins`，然后在后台启用

Github 下载节点：[wordpress-qcloud-cos-latest-releases](https://github.com/sy-records/wordpress-qcloud-cos/releases/latest)

<a id="markdown-修改配置" name="修改配置"></a>

## 修改配置

- 方法一：在 WordPress 插件管理页面有设置按钮，进行设置
- 方法二：在 WordPress 后台管理左侧导航栏`设置`下`腾讯云COS设置`，点击进入设置页面

<a id="markdown-常见问题" name="常见问题"></a>

## 常见问题

1. 怎么替换文章中之前的旧资源地址链接

   这个插件已经加上了替换数据库中之前的旧资源地址链接功能，只需要填好对应的链接即可

2. 使用子账户报错`Cos Error Code: AccessDenied, Status Code: 403`

   可以使用子账户，但是 APPID 需要填写为存储桶创建者的 ID，而不是子账户的 ID。例如下文配置指南中的`1250000000`就是 APPID

3. 上传图片提示`图像后期处理失败，请将其缩小到2500像素并重新上传`

   配置的`存储桶名称`填写错误，正确的配置参照下文配置指南中`存储桶名称`

   > `v1.6.1`增强了校验，填写错误会给予提示；同时兼容了桶名称附带`APPID`的情况

4. 从媒体库中删除了图片，但是`COS`中还是存在

   原因是在配置页面选择了`不在本地保留备份`，因为 WordPress 机制问题，无法获取对应的文件信息

5. 在插件中应该如何使用腾讯云数据万象 CI

   参考：[腾讯云对象存储 COS + 数据万象 CI = 完善的图片解决方案](https://cloud.tencent.com/developer/article/1606153) 或 [腾讯云文档 - 使用图片样式](https://cloud.tencent.com/document/product/436/42214#.E4.BD.BF.E7.94.A8.E5.9B.BE.E7.89.87.E6.A0.B7.E5.BC.8F)

<a id="markdown-配置指南" name="配置指南"></a>

## 配置指南

查看 [详细教程](https://qq52o.me/2722.html)

- 存储桶设置

> 访问 [腾讯云控制台](https://console.cloud.tencent.com/cos5/bucket) 创建存储桶，把创建存储桶时要求你填写的**存储桶名称**，把**存储桶名称**填到这里就可以了，没有后面的`-appid` > `examplebucket-1250000000`，其中`examplebucket`为存储桶名称，`1250000000`为 APPID。

- 存储桶地域

> 选择你创建存储桶时所选的地域即可

- APP ID、SecretID、SecretKey

> APP ID 填写上文存储桶设置中所说的`125000000`即可；也可以访问 [腾讯云控制台](https://console.cloud.tencent.com/cos5/key) 获取 APP ID、SecretID、SecretKey

<a id="markdown-插件下载" name="插件下载"></a>

## 插件下载

- [WordPress Plugins](https://wordpress.org/plugins/sync-qcloud-cos/)
- [Github](https://github.com/sy-records/wordpress-qcloud-cos)
- [90 盘](https://www.90pan.com/o129858)
- [(反代)WordPress Plugins](https://wp.hipush.cn/plugins/sync-qcloud-cos/)
- [(反代)WordPress Plugins](http://wp101.net/plugins/sync-qcloud-cos/)

---
title: WordPress 评论内容审核插件 TextCensor For Comments
date: 2020-04-02 19:52:09
categories: WordPress
---

<!-- more -->

<!-- TOC -->

- [WordPress 评论内容审核插件 TextCensor For Comments](#wordpress-评论内容审核插件-textcensor-for-comments)
  - [能力介绍](#能力介绍)
  - [插件安装](#插件安装)
    - [推荐使用](#推荐使用)
    - [下载源码](#下载源码)
  - [插件设置](#插件设置)
  - [更新日志](#更新日志)
    - [v1.0.4](#v104)
    - [v1.0.3](#v103)
    - [v1.0.2](#v102)
    - [v1.0.1](#v101)
    - [v1.0.0](#v100)
  - [插件下载](#插件下载)

<!-- /TOC -->

<a id="markdown-wordpress-评论内容审核插件-textcensor-for-comments" name="wordpress-评论内容审核插件-textcensor-for-comments"></a>

# WordPress 评论内容审核插件 TextCensor For Comments

基于百度文本内容审核技术来提供 WordPress 评论内容审核，对网站用户的评论信息检测，一旦发现用户提交恶意垃圾内容，可以做到文本的自动审核与实时过滤。

[github author="sy-records" project="wp-baidu-textcensor"][/github]

[百度文本内容审核](https://ai.baidu.com/tech/textcensoring)能一站式检测文本中夹杂的色情、推广、辱骂、违禁、涉政、灌水等垃圾内容，净化网络环境，为您的应用提供更可靠的内容安全保障，运用业界领先的深度学习技术，判断一段文本内容是否符合网络发文规范，实现自动化、智能化的文本审核，大幅节省内容审核的人力成本，为您的产品体验保驾护航

![wp-baidu-textcensor](https://cdn.jsdelivr.net/gh/sy-records/wp-baidu-textcensor/screenshot-1.png)

<a id="markdown-能力介绍" name="能力介绍"></a>

## 能力介绍

- 文本色情：对文本中的色情行为描述、色情资源链接、低俗交友、污秽文爱等内容进行识别
- 暴恐违禁：对暴力行为、恐怖描述、赌博、毒品、枪支弹药等违禁内容进行识别
- 政治敏感：对文本中的敏感事件、涉政人物、散布谣言、反动宣传等内容进行识别
- 恶意推广：对文本中带有售卖意向的软文广告，微信、QQ 等个人联系方式等违规内容及变体进行识别
- 低俗辱骂：对文本中的侮辱谩骂、人身攻击、消极宣泄等内容进行识别
- 低质灌水：对网络社区常见的乱码、水帖、刷屏等无意义的灌水信息进行识别

<a id="markdown-插件安装" name="插件安装"></a>

## 插件安装

<a id="markdown-推荐使用" name="推荐使用"></a>

### 推荐使用

在 WordPress 后台安装插件页面搜索 `Baidu TextCensor For Comments`

<a id="markdown-下载源码" name="下载源码"></a>

### 下载源码

从 [Github](https://github.com/sy-records/wp-baidu-textcensor) 或 [WordPress Plugins](https://wordpress.org/plugins/baidu-textcensor/) 下载源码，通过 WordPress 后台上传安装，或者直接将源码上传到 WordPress 插件目录 `wp-content/plugins`，然后在后台启用。

<a id="markdown-插件设置" name="插件设置"></a>

## 插件设置

在百度 Ai 控制台的 [产品服务 / 内容审核 - 应用列表 创建应用](https://console.bce.baidu.com/ai/?fromai=1#/ai/antiporn/app/list) 后获取 AppID、API Key、Secret Key。

<a id="markdown-更新日志" name="更新日志"></a>

## 更新日志

<a id="markdown-v104" name="v104"></a>

### v1.0.4

- 修复 add_submenu_page 参数错误提示

<a id="markdown-v103" name="v103"></a>

### v1.0.3

- 更新 readme.txt 为 markdown 格式
- 更新插件名称为 Baidu TextCensor For Comments
- 修复停用插件删除配置

<a id="markdown-v102" name="v102"></a>

### v1.0.2

- Optimization baiduWpRequest method

<a id="markdown-v101" name="v101"></a>

### v1.0.1

- Updated readme.txt
- Updated pre_comment_approved filter hook

<a id="markdown-v100" name="v100"></a>

### v1.0.0

- First version
- [WordPress Plugins](https://wordpress.org/plugins/baidu-textcensor/)

<a id="markdown-插件下载" name="插件下载"></a>

## 插件下载

- [WordPress Plugins](https://wordpress.org/plugins/baidu-textcensor/)
- [Github](https://github.com/sy-records/wp-baidu-textcensor)
- [90 盘](https://www.90pan.com/o129849)
- [(反代)WordPress Plugins](https://wp.hipush.cn/plugins/baidu-textcensor/)
- [(反代)WordPress Plugins](http://wp101.net/plugins/baidu-textcensor/)

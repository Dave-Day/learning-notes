---
title: Github 镜像访问加速下载脚本
date: 2020-03-21 15:15:49
categories: Plugins
---

<!-- more -->

<!-- TOC -->

- [Github 镜像访问加速下载脚本](#github-镜像访问加速下载脚本)
  - [脚本描述](#脚本描述)
  - [更新日志](#更新日志)
    - [v1.0.4](#v104)
    - [v1.0.2](#v102)
  - [脚本下载](#脚本下载)
  - [使用方法](#使用方法)
    - [安装用户脚本管理器](#安装用户脚本管理器)
    - [安装用户脚本](#安装用户脚本)
    - [使用用户脚本](#使用用户脚本)

<!-- /TOC -->

<a id="markdown-github-镜像访问加速下载脚本" name="github-镜像访问加速下载脚本"></a>

# Github 镜像访问加速下载脚本

GitHub 是一个拥有全球大量用户的开源及私有软件项目的托管平台，因为只支持 git 代码仓库托管，故名 GitHub。众所周知，Github 由于服务器在国外，国内地区访问非常慢，下载项目通常要用代理访问。

[github author="jadezi" project="github-accelerator"][/github]

![img](https://greasyfork.org/system/screenshots/screenshots/000/019/720/original/%E4%B8%BB.png)

![img](https://greasyfork.org/system/screenshots/screenshots/000/019/721/original/%E4%B8%8B.png)

<a id="markdown-脚本描述" name="脚本描述"></a>

## 脚本描述

油猴插件 --- github 访问加速。镜像访问 GitHub。本脚本在 [GitHub 镜像加速下载](https://greasyfork.org/zh-CN/scripts/397419-github-镜像加速下载) 脚本的基础上做了些修改。

<a id="markdown-更新日志" name="更新日志"></a>

## 更新日志

<a id="markdown-v104" name="v104"></a>

### v1.0.4

- 更换镜像网址，移除已失效地址（感谢[@KevinZonda](https://github.com/KevinZonda)提供镜像地址)
- 新增地址[快速克隆 2]不支持 release 加速下载，SSH 克隆

<a id="markdown-v102" name="v102"></a>

### v1.0.2

- 添加了一键复制，样式美化的功能
- 原脚本在克隆地址处添加的快速下载 失效了，我做了一些修改

<a id="markdown-脚本下载" name="脚本下载"></a>

## 脚本下载

- [Greasyfork](https://greasyfork.org/zh-CN/scripts/398278)
- [Github-jsdelivr](https://cdn.jsdelivr.net/gh/jadezi/github-accelerator/Github%20%E5%9B%BD%E5%86%85%E5%8A%A0%E9%80%9F.user.js)
- [Github](https://github.com/jadezi/github-accelerator/raw/master/Github%20%E5%9B%BD%E5%86%85%E5%8A%A0%E9%80%9F.user.js)

<a id="markdown-使用方法" name="使用方法"></a>

## 使用方法

<a id="markdown-安装用户脚本管理器" name="安装用户脚本管理器"></a>

### 安装用户脚本管理器

要使用用户脚本，您首先需要安装一个用户脚本管理器。根据您使用的浏览器不同，可用的用户脚本管理器也有所不同。

- Chrome：[Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) 或 [Violent monkey](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag)
- Firefox：[Greasemonkey](https://addons.mozilla.org/firefox/addon/greasemonkey/)、[Tampermonkey](https://addons.mozilla.org/firefox/addon/tampermonkey/) 或 [Violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/)
- Safari：[Tampermonkey](http://tampermonkey.net/?browser=safari)
- Microsoft Edge：[Tampermonkey](https://www.microsoft.com/store/p/tampermonkey/9nblggh5162s)
- Opera：[Tampermonkey](https://addons.opera.com/extensions/details/tampermonkey-beta/) 或 [Violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/)
- Maxthon：[Violentmonkey](http://extension.maxthon.com/detail/index.php?view_id=1680)
- Dolphin：[Tampermonkey](https://play.google.com/store/apps/details?id=net.tampermonkey.dolphin)
- UC：[Tampermonkey](https://play.google.com/store/apps/details?id=net.tampermonkey.uc)
- Qupzilla：（不需要额外软件）
- AdGuard：（不需要额外软件）

<a id="markdown-安装用户脚本" name="安装用户脚本"></a>

### 安装用户脚本

在您找到想要的用户脚本后，点击用户脚本页面上绿色的安装按钮，您的用户脚本管理器将向您确认是否安装。

<a id="markdown-使用用户脚本" name="使用用户脚本"></a>

### 使用用户脚本

现在您可以访问这个用户脚本所针对的网站，脚本应该已经自动启动和生效。在试用一段时间之后，您可以回到用户脚本发表的页面，给用户脚本的作者留下反馈。

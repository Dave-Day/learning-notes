---
title: Github 镜像加速下载 FastGithub 脚本
date: 2020-03-27 20:56:58
categories: Plugins
---

<!-- more -->

<!-- TOC -->

- [Github 镜像加速下载 FastGithub 脚本](#github-镜像加速下载-fastgithub-脚本)
  - [脚本描述](#脚本描述)
    - [已知的 GitHub 镜像(含失效站点)](#已知的-github-镜像含失效站点)
  - [脚本下载](#脚本下载)
  - [使用方法](#使用方法)
    - [安装用户脚本管理器](#安装用户脚本管理器)
    - [安装用户脚本](#安装用户脚本)
    - [使用用户脚本](#使用用户脚本)

<!-- /TOC -->

<a id="markdown-github-镜像加速下载-fastgithub-脚本" name="github-镜像加速下载-fastgithub-脚本"></a>

# Github 镜像加速下载 FastGithub 脚本

GitHub 是一个拥有全球大量用户的开源及私有软件项目的托管平台，因为只支持 git 代码仓库托管，故名 GitHub。众所周知，Github 由于服务器在国外，国内地区访问非常慢，下载项目通常要用代理访问。

[github author="RC1844" project="FastGithub"][/github]

![img](https://cdn.jsdelivr.net/gh/RC1844/FastGithub/REANDME/releases1.png)

<a id="markdown-脚本描述" name="脚本描述"></a>

## 脚本描述

快速跳转 GitHub 镜像网站的猴油脚本。

<a id="markdown-已知的-github-镜像含失效站点" name="已知的-github-镜像含失效站点"></a>

### 已知的 GitHub 镜像(含失效站点)

| 域名                              | https | 克隆加速 | zip 加速 | releases 加速 | 主机服务商 | 服务器所在地 |
| --------------------------------- | ----- | -------- | -------- | ------------- | ---------- | ------------ |
| `github.com.cnpmjs.org`           | ✓     | ?✓       | ✗        | ✗             | dnspod     | 香港         |
| ~~`github-mirror.bugkiller.org`~~ | ✗     | ✓        | ✗        | ✓             | ?          | 日本         |
| `github.wuyanzheshui.workers.dev` | ✓     | ✗        | ✓        | ✓             | Cloudflare | 美国         |

<a id="markdown-脚本下载" name="脚本下载"></a>

## 脚本下载

- [Greasyfork](https://greasyfork.org/zh-CN/scripts/397419-github-镜像加速下载)
- [Github-jsdelivr](https://cdn.jsdelivr.net/gh/RC1844/FastGithub/FastGithub.js)
- [Github](https://raw.githubusercontent.com/RC1844/FastGithub/master/FastGithub.js)

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

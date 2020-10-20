---
title: HTML5 网页视频播放器增强脚本
date: 2019-12-22 10:04:43
categories: Plugins
---

<!-- more -->

<!-- TOC -->

- [HTML5 网页视频播放器增强脚本](#html5-网页视频播放器增强脚本)
  - [脚本特性](#脚本特性)
  - [快捷键列表](#快捷键列表)
  - [更新日志](#更新日志)
    - [3.0.5](#305)
    - [3.1.0](#310)
    - [3.1.1](#311)
    - [3.1.2](#312)
    - [3.2.0](#320)
    - [3.2.1](#321)
  - [脚本地址](#脚本地址)
  - [使用方法](#使用方法)
    - [安装用户脚本管理器](#安装用户脚本管理器)
    - [安装用户脚本](#安装用户脚本)
    - [使用用户脚本](#使用用户脚本)

<!-- /TOC -->

<a id="markdown-html5-网页视频播放器增强脚本" name="html5-网页视频播放器增强脚本"></a>

# HTML5 网页视频播放器增强脚本

HTML5 视频播放增强脚本，支持所有 H5 视频播放网站，全程快捷键控制，支持：倍速播放/加速播放、视频画面截图、画中画、网页全屏、调节亮度、饱和度、对比度、自定义配置功能增强等功能，提供良好的在线播剧体验

PS：本脚基于：[HTML5 播放器增强插件](https://greasyfork.org/users/49622) 但已远超原脚本提供的功能。

由于之前作者已长期不维护，故接坑自己开干，在原作者的基础上进行了大幅度的代码改造，并采用了全新的项目架构进行开发，维护更加方便，逻辑更加清晰，功能更加强大，兼容更多网站。

[github author="xxxily" project="h5player"][/github]

<a id="markdown-脚本特性" name="脚本特性"></a>

## 脚本特性

- 兼容广泛，所有存在 video 标签的网页均支持 即使嵌在 iframe、shadowdom 下均可兼容
- 支持跨域控制，跨域受限页面下快捷键一样可以无缝衔接
- 支持多实例（如：twitter，instagram 下亦可兼容）
- 支持播放进度记录
- 支持播放速度记录
- 支持视频画面缩放
- 支持画中画功能
- 支持跨 Tab 控制画中画
- 支持视频画面截图功能
- 支持配置式添加自定义功能

<a id="markdown-快捷键列表" name="快捷键列表"></a>

## 快捷键列表

| 快捷键      | 说明                                        |
| ----------- | ------------------------------------------- |
| ctrl+\      | 快捷键是否全网页可用，默认 true             |
| Ctrl+space  | 禁用/启用 该播放插件                        |
| →           | 快进 5 秒                                   |
| ←           | 后退 5 秒                                   |
| Ctrl+→      | 快进 30 秒                                  |
| Ctrl+←      | 后退 30 秒                                  |
| ↑           | 音量升高 10%                                |
| ↓           | 音量降低 10%                                |
| Ctrl+↑      | 音量升高 20%                                |
| Ctrl+↓      | 音量降低 20%                                |
| C           | 加速播放 +0.1                               |
| X           | 减速播放 -0.1                               |
| Z           | 正常速度播放                                |
| shift+C     | 放大视频画面 +0.1                           |
| shift+X     | 缩小视频画面 -0.1                           |
| shift+Z     | 恢复视频画面                                |
| shift+P     | 进入或退画中画功能                          |
| shift+S     | 截图，截取当前画面并保存                    |
| shift+R     | 启用或禁止自动恢复播放进度功能              |
| shift+→     | 画面向右移动 10px                           |
| shift+←     | 画面向左移动 10px                           |
| shift+↑     | 画面向上移动 10px                           |
| shift+↓     | 画面向下移动 10px                           |
| Enter       | 进入全屏                                    |
| shift+Enter | 进入网页全屏                                |
| N           | 下一个/集视频（仅部分网站支持）             |
| D           | 上一帧 (截图时进行微调以找到质量最佳的一帧) |
| F           | 下一帧 (不支持 netflix，因为快捷键冲突)     |
| E           | 亮度增加%                                   |
| W           | 亮度减少%                                   |
| T           | 对比度增加%                                 |
| R           | 对比度减少%                                 |
| U           | 饱和度增加%                                 |
| Y           | 饱和度减少%                                 |
| O           | 色相增加 1 度                               |
| I           | 色相减少 1 度                               |
| K           | 模糊增加 1 px                               |
| J           | 模糊减少 1 px                               |
| Q           | 图像复位                                    |
| S           | 画面旋转 90 度                              |

<a id="markdown-更新日志" name="更新日志"></a>

## 更新日志

<a id="markdown-305" name="305"></a>

### 3.0.5

- 增加 mac 快捷键兼容
- 优化部分代码逻辑

<a id="markdown-310" name="310"></a>

### 3.1.0

- 增加自动恢复播放进度的控制选项
- 修复部分网站 tips 无法正常显示 BUG

<a id="markdown-311" name="311"></a>

### 3.1.1

- 增加部分网站兼容
- 优化提示父节点获取逻辑

<a id="markdown-312" name="312"></a>

### 3.1.2

- 修复火狐下滤镜不兼容导致黑屏的 BUG
- 部分网站增加一键播放下一个视频功能
- 增强部分网站的兼容

<a id="markdown-320" name="320"></a>

### 3.2.0

- 增加跨 Tab 操作画中画视频功能

<a id="markdown-321" name="321"></a>

### 3.2.1

- 自动恢复设置调整为按域名进行控制
- 增加对 A 站的兼容，取消 B 站的自动播放
- 其它功能的部分细节优化

<a id="markdown-脚本地址" name="脚本地址"></a>

## 脚本地址

- 脚本安装地址：[greasyfork-scripts-381682](https://greasyfork.org/scripts/381682)

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

---
title: 哔哩哔哩增强脚本 Bilibili Evolved
date: 2019-12-27 07:23:47
categories: Plugins
---

<!-- more -->

<!-- TOC -->

- [哔哩哔哩增强脚本 Bilibili Evolved](#哔哩哔哩增强脚本-bilibili-evolved)
  - [脚本特性](#脚本特性)
    - [视频](#视频)
    - [样式](#样式)
    - [动态](#动态)
    - [工具](#工具)
    - [触摸](#触摸)
    - [直播](#直播)
    - [消息](#消息)
  - [已知问题](#已知问题)
  - [脚本地址](#脚本地址)
    - [备用安装源](#备用安装源)
  - [使用方法](#使用方法)
    - [安装用户脚本管理器](#安装用户脚本管理器)
    - [安装用户脚本](#安装用户脚本)
    - [使用用户脚本](#使用用户脚本)

<!-- /TOC -->

<a id="markdown-哔哩哔哩增强脚本-bilibili-evolved" name="哔哩哔哩增强脚本-bilibili-evolved"></a>

# 哔哩哔哩增强脚本 Bilibili Evolved

强大的哔哩哔哩增强脚本: 下载视频, 音乐, 封面, 弹幕 / 简化直播间, 评论区, 首页 / 自定义顶栏, 删除广告, 夜间模式 / 触屏设备支持。

[github author="the1812" project="Bilibili-Evolved"][/github]

<a id="markdown-脚本特性" name="脚本特性"></a>

## 脚本特性

<a id="markdown-视频" name="视频"></a>

### 视频

- 下载视频和番剧
- 下载 XML 或 ASS 弹幕
- 查看或下载封面
- 设定默认视频画质/播放器模式/播放速度
- 默认关闭弹幕或特定类型的弹幕
- 播放时自动关灯
- 自动播放视频
- 自动展开弹幕列表
- 自动展开视频简介
- 自动从历史记录点播放
- 逐帧调整视频的进度
- 视频快速截图
- 自动定位到播放器
- 外置稍后再看
- 双击全屏

<a id="markdown-样式" name="样式"></a>

### 样式

- 强大的夜间模式支持
- 自定义顶栏的显示和布局
- 首页换用更紧凑的布局
- 隐藏各种多余的元素
- 简化评论区
- 简化直播间
- 简化首页
- 网页全屏强制保留弹幕栏
- 根据屏幕 DPI 缩放直播间看板娘

<a id="markdown-动态" name="动态"></a>

### 动态

- 解除动态存图限制
- 快速收起动态评论区
- 自动展开动态预览中的长标题
- 自动展开动态正文的全部内容
- 按照关键词/正则表达式/类型来过滤动态

<a id="markdown-工具" name="工具"></a>

### 工具

- 删除各种广告
- 对 B 站界面进行翻译
- 进入直播间自动切换为对应勋章
- 禁止直播首页自动播放
- 重定向稍后再看以使用新版播放器
- 隐藏搜索栏的推荐词
- 使专栏的文字可以选择与复制
- 稍后再看过期提醒
- 下载音频区的音乐
- 使用旧版动态
- 快速跳转到`BiliPlus`对应的页面
- 对图片做高分屏适配
- 快速银瓜子换硬币

<a id="markdown-触摸" name="触摸"></a>

### 触摸

- 优化顶栏触摸体验
- 为播放器开启触摸支持, 能够使用手势控制播放
- 使触屏长按点赞支持素质三连
- 迷你播放器支持触摸拖动

<a id="markdown-直播" name="直播"></a>

### 直播

- 简化直播间
- 缩放直播看板娘
- 收起直播间侧栏
- 删除直播水印
- 禁止直播首页自动播放
- 直播间自动领奖
- 自动选择当前直播间勋章
- 直播弹幕记录器(实验性)

<a id="markdown-消息" name="消息"></a>

### 消息

- 显示消息
- 显示内部错误消息
- 文件命名格式
- 批量命名格式
- 侧栏垂直偏移量
- Ajax Hook API
- 加载模式
- 设置面板停靠位置

<a id="markdown-已知问题" name="已知问题"></a>

## 已知问题

- 和`解除B站区域限制`一同使用时, 两个脚本功能互相没有任何问题, 但有的人会遇到没弹幕的状况. 单独使用各脚本时正常, 目前未找到原因.
- 可能无法很好地适应窄屏幕, 请尽量以 1400px 以上的宽度使用此脚本.
- ASS 弹幕下载不能包含高级弹幕, 字幕弹幕等.
- `简化首页`可能会有无法加载`活动`栏目的情况, 目前未找到原因.

<a id="markdown-脚本地址" name="脚本地址"></a>

## 脚本地址

点击名称即可安装 👇

| [正式版](https://cdn.jsdelivr.net/gh/the1812/Bilibili-Evolved@master/bilibili-evolved.user.js) | [预览版](https://cdn.jsdelivr.net/gh/the1812/Bilibili-Evolved@preview/bilibili-evolved.preview.user.js) | [离线版](https://cdn.jsdelivr.net/gh/the1812/Bilibili-Evolved@master/bilibili-evolved.offline.user.js) | [预览离线版](https://cdn.jsdelivr.net/gh/the1812/Bilibili-Evolved@preview/bilibili-evolved.preview-offline.user.js) |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| 正式发布的版本, 最稳定, 更新频率较低.                                                          | 新增内容测试的地方, 更新频率高, 但功能不稳定.                                                           | 内置所有依赖项, 体积较大, 更新频率高于正式版.                                                          | 兼备预览版和离线版的特点.                                                                                           |

> 使用过程中脚本管理器可能会提示"脚本试图访问跨域资源", 请选择"始终允许".

> 某些破坏性的大更新会使旧版脚本**完全**无法运行, 请及时检查更新.

<a id="markdown-备用安装源" name="备用安装源"></a>

### 备用安装源

如果默认的安装链接无法使用, 可以尝试以下的备用安装源(连接速度从高到低), 内容更新与 GitHub 可能稍有延迟.

|            | 更新延迟 | 正式版                                                                                       | 预览版                                                                                                         | 离线版                                                                                                         | 预览离线版                                                                                                                     |
| ---------- | -------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| jsDelivr   | 24h      | [安装](https://cdn.jsdelivr.net/gh/the1812/Bilibili-Evolved@master/bilibili-evolved.user.js) | [安装](https://cdn.jsdelivr.net/gh/the1812/Bilibili-Evolved@preview/bilibili-evolved.preview.user.js)          | [安装](https://cdn.jsdelivr.net/gh/the1812/Bilibili-Evolved@master/bilibili-evolved.offline.user.js)           | [安装](https://cdn.jsdelivr.net/gh/the1812/Bilibili-Evolved@preview/bilibili-evolved.preview-offline.user.js)                  |
| GreasyFork | 12h      | [安装](https://greasyfork.org/scripts/373563-bilibili-evolved/code/Bilibili Evolved.user.js) | [安装](https://greasyfork.org/scripts/373564-bilibili-evolved-preview/code/Bilibili Evolved (Preview).user.js) | [安装](https://greasyfork.org/scripts/373565-bilibili-evolved-offline/code/Bilibili Evolved (Offline).user.js) | [安装](https://greasyfork.org/scripts/373566-bilibili-evolved-preview-offline/code/Bilibili Evolved (Preview Offline).user.js) |
| GitHub     | <1h      | [安装](https://github.com/the1812/Bilibili-Evolved/raw/master/bilibili-evolved.user.js)      | [安装](https://github.com/the1812/Bilibili-Evolved/raw/preview/bilibili-evolved.preview.user.js)               | [安装](https://github.com/the1812/Bilibili-Evolved/raw/master/bilibili-evolved.offline.user.js)                | [安装](https://github.com/the1812/Bilibili-Evolved/raw/preview/bilibili-evolved.preview-offline.user.js)                       |

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

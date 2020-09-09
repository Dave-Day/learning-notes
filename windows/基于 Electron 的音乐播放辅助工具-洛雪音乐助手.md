---
title: 基于 Electron 的音乐播放辅助工具-洛雪音乐助手
date: 2019-11-13 11:13:56
categories: Program
---

<!-- more -->

<!-- TOC -->

- [基于 Electron 的音乐播放辅助工具-洛雪音乐助手](#基于-electron-的音乐播放辅助工具-洛雪音乐助手)
- [软件特点](#软件特点)
- [本地开发](#本地开发)
  - [源码说明](#源码说明)
  - [源码使用方法](#源码使用方法)
- [常见问题](#常见问题)
  - [软件为什么没有桌面歌词与自定义列表功能](#软件为什么没有桌面歌词与自定义列表功能)
  - [歌曲无法试听与下载](#歌曲无法试听与下载)
  - [软件安装包说明](#软件安装包说明)
  - [软件更新](#软件更新)
  - [Windows 7 下界面异常](#windows-7-下界面异常)
  - [安装版安装失败，提示应用未安装](#安装版安装失败提示应用未安装)
  - [缺少 `xxx.dll`](#缺少-xxxdll)
- [更新日志](#更新日志)
  - [[0.8.2](https://github.com/lyswhut/lx-music-desktop/compare/v0.8.1...v0.8.2) - 2019-10-20](#082httpsgithubcomlyswhutlx-music-desktopcomparev081v082---2019-10-20)
  - [[0.8.1](https://github.com/lyswhut/lx-music-desktop/compare/v0.8.0...v0.8.1) - 2019-10-20](#081httpsgithubcomlyswhutlx-music-desktopcomparev080v081---2019-10-20)
  - [[0.8.0](https://github.com/lyswhut/lx-music-desktop/compare/v0.7.0...v0.8.0) - 2019-10-19](#080httpsgithubcomlyswhutlx-music-desktopcomparev070v080---2019-10-19)
  - [[0.7.0](https://github.com/lyswhut/lx-music-desktop/compare/v0.6.2...v0.7.0) - 2019-10-07](#070httpsgithubcomlyswhutlx-music-desktopcomparev062v070---2019-10-07)
  - [[0.6.2](https://github.com/lyswhut/lx-music-desktop/compare/v0.6.1...v0.6.2) - 2019-10-01](#062httpsgithubcomlyswhutlx-music-desktopcomparev061v062---2019-10-01)
- [软件下载](#软件下载)

<!-- /TOC -->

<a id="markdown-基于-electron-的音乐播放辅助工具-洛雪音乐助手" name="基于-electron-的音乐播放辅助工具-洛雪音乐助手"></a>

## 基于 Electron 的音乐播放辅助工具-洛雪音乐助手

[洛雪音乐助手](https://github.com/lyswhut/lx-music-desktop) 一个基于 `Electron` + `Vue` 开发的 `PC` 上的音乐播放辅助工具。这款洛雪音乐助手功能强大全面，简单易操作，使用后可以帮助用户更轻松便捷的播放音乐。软件支持无损音乐播放和下载，界面清爽绿色。洛雪音乐助手可以免费下载高清无损音乐，基本上集成了多个平台的资源，支持专辑，歌词，封面显示，是专为喜爱音乐的朋友设计的。喜欢听音乐的朋友欢迎来下载使用。

[github author="lyswhut" project="lx-music-desktop"][/github]

![洛雪音乐助手 ](https://pic.ryanjie.cn/2019/11/lxmusic.png)

<a id="markdown-软件特点" name="软件特点"></a>

## 软件特点

- 支持无损格式音乐下载
- 支持智能搜索
- 支持歌词，专辑封面显示
- 支持在线试听
- 多种皮肤界面可选
- 清爽无广告

<a id="markdown-本地开发" name="本地开发"></a>

## 本地开发

<a id="markdown-源码说明" name="源码说明"></a>

### 源码说明

一个基于 `Electron` + `Vue` 开发的音乐软件。

所用技术栈：

- `Electron 6.x`
- `Vue 2.x`

已支持的平台：

- `Windows 7` 及以上
- `Mac OS`
- `Linux`

<a id="markdown-源码使用方法" name="源码使用方法"></a>

### 源码使用方法

环境要求： `Node.js 12.x`

```bash
# 开发模式
npm run dev

# 构建免安装版
npm run pack:dir

# 构建安装包（windows 版）
npm run pack
```

<a id="markdown-常见问题" name="常见问题"></a>

## 常见问题

在阅读本常见问题后，仍然无法解决您的问题，请提交 `issue` 或者加企鹅群 `830125506` 反馈，反馈时请**注明**已阅读常见问题！

<a id="markdown-软件为什么没有桌面歌词与自定义列表功能" name="软件为什么没有桌面歌词与自定义列表功能"></a>

### 软件为什么没有桌面歌词与自定义列表功能

洛雪音乐的最初定位不是作为播放器开发的，它主要用于**查找歌曲**，软件的播放功能仅用于试听，不建议用作为常用播放器使用，因此无桌面、界面歌词，不可自定义列表。

<a id="markdown-歌曲无法试听与下载" name="歌曲无法试听与下载"></a>

### 歌曲无法试听与下载

该问题解决顺序如下：

1. 尝试更新到最新版本
2. 尝试切换其他歌曲（或直接搜索该歌曲），若全部歌曲都无法试听与下载则进行下一步
3. 尝试到设置-接口来源切换到其他接口
4. 尝试切换网络，比如用手机开热点（目前存在某些网络无法访问接口服务器的情况）
5. 若还不行请到这个链接查看详情：[lx-music-desktop-issues-5](https://github.com/lyswhut/lx-music-desktop/issues/5)
6. 若没有在第 `5` 条链接中的第一条评论中看到接口无法使用的说明，则应该是您网络无法访问接口服务器的问题，如果接口有问题我会在那里说明。

想要知道是不是自己网络的问题可以看看 `https://ts.tempmusic.tk` 能不能在浏览器打开，浏览器显示 404 是正常的，如果不是 `404` 那就证明所在网络无法访问接口服务器。
若网页无法打开或打来不是 `404` ，则应该是 `DNS` 的问题，可以尝试以下办法：

1. 改成自动获取试试;
2. 手动把 `DNS` 改一下，不要用 `360` 的 `DNS` ，可以把 DNS 改成 `114.114.114.114` 、 `8.8.8.8` ;
3. 软件设置里面的代理不要勾起来;

<a id="markdown-软件安装包说明" name="软件安装包说明"></a>

### 软件安装包说明

软件发布页及网盘中有多个类型的安装文件，以下是对这些类型文件的说明：

- 文件名带 `win_` 的是在 `Windows` 系统上运行的版本，
- 其中安装版（ `Setup` ）可自动更新软件，
- 绿色版（ `green` ）为免安装版，自动更新功能不可用；
- 以 **`.dmg`** 结尾的文件为 MAC 版本；
- 以 **`.AppImage`**、**`.deb`** 结尾的为 `Linux` 版本。
- 带有 `x64` 的为 64 位的系统版本，带 `x86` 的为 `32` 位的系统版本；若两个都带有的则为集合版，安装时会自动根据系统位数选择对应的版本安装。

<a id="markdown-软件更新" name="软件更新"></a>

### 软件更新

软件启动时若发现新版本时会自动从本仓库下载安装包，下载完毕会弹窗提示更新。
若下载未完成时软件被关闭，下次启动软件会再次自动下载。
若还是**更新失败**，可能是无法访问 `GitHub` 导致的，这时需要手动更新，即下载最新安装包直接覆盖安装即可。
注意：**绿色版**的软件自动更新功能**不可用**，建议使用安装版！！
注意：**Mac 版**、**Linux deb**版不支持自动更新！

<a id="markdown-windows-7-下界面异常" name="windows-7-下界面异常"></a>

### Windows 7 下界面异常

当 win7 没有开启**透明效果**时界面将会显示异常，开启方法请自行百度。
对于一些开启透明效果后仍然无法正常显示界面的系统，我也不知道是什么原因导致的，只能说正常的系统是没有这个问题的，如果您知道原因导致的欢迎反馈！

<a id="markdown-安装版安装失败提示应用未安装" name="安装版安装失败提示应用未安装"></a>

### 安装版安装失败，提示应用未安装

对于部分电脑出现安装失败的问题我也不懂什么原因，，可以尝试清理下安装文件，或者重启电脑试试。

<a id="markdown-缺少-xxxdll" name="缺少-xxxdll"></a>

### 缺少 `xxx.dll`

这个是电脑缺少某些 dll 导致的，正常的系统是没有这个问题的，解决办法需自行百度弹出的错误信息看下别人是怎么解决的。

<a id="markdown-更新日志" name="更新日志"></a>

## 更新日志

<a id="markdown-082httpsgithubcomlyswhutlx-music-desktopcomparev081v082---2019-10-20" name="082httpsgithubcomlyswhutlx-music-desktopcomparev081v082---2019-10-20"></a>

### [0.8.2](https://github.com/lyswhut/lx-music-desktop/compare/v0.8.1...v0.8.2) - 2019-10-20

**修复**

- 兼容旧版酷我源搜索列表过滤 `128k` 音质的 `bug` （注： `0.8.1` 版本仅修复了酷我源的歌曲过滤问题，该修复仅对以后添加的歌曲有效，如果是之前添加的歌曲仍会出现这个问题，现修复对之前旧列表数据的兼容处理）

<a id="markdown-081httpsgithubcomlyswhutlx-music-desktopcomparev080v081---2019-10-20" name="081httpsgithubcomlyswhutlx-music-desktopcomparev080v081---2019-10-20"></a>

### [0.8.1](https://github.com/lyswhut/lx-music-desktop/compare/v0.8.0...v0.8.1) - 2019-10-20

**修复**

- 修复酷我源搜索歌曲结果未添加 `128k` 音质导致播放 `128k` 音质时显示“该歌曲没有可播放的音频”的问题

<a id="markdown-080httpsgithubcomlyswhutlx-music-desktopcomparev070v080---2019-10-19" name="080httpsgithubcomlyswhutlx-music-desktopcomparev070v080---2019-10-19"></a>

### [0.8.0](https://github.com/lyswhut/lx-music-desktop/compare/v0.7.0...v0.8.0) - 2019-10-19

**新增**

- 新增网易云源歌曲搜索
- 新增网易云源歌单
- 新增各平台通过输入歌单链接或歌单 `ID` 打开歌单详情列表，目前只适配了**网页版歌单链接**，其他方式的歌单链接可能无法解析，但您可想办法获取歌单 `ID` 后输入打开。注：各平台歌单 `ID` 均为纯数字，若遇到链接里存在歌单 `ID` 但无法解析的歌单链接，可以到 `GitHub` 提交 `issue` 或发送邮件或加群 `830125506` 反馈！
- 新增音量调整滑动功能，现在支持鼠标左右拖动调整音量了

**优化**

- 优化搜索框搜索体验
- 优化音量条交互视觉效果
- 缓存歌单详情列表数据

**修复**

- 修复 `QQ` 源歌单无法翻页 `Bug`
- 修复默认列表没有创建时无法显示收藏列表的 `Bug`
- 修复网易云 `128k` 直接试听
- 修复歌曲音质不存在时仍然播放或下载的 `Bug`
- 修复调整音量时，调整的位置与鼠标点击的位置不一致的问题

<a id="markdown-070httpsgithubcomlyswhutlx-music-desktopcomparev062v070---2019-10-07" name="070httpsgithubcomlyswhutlx-music-desktopcomparev062v070---2019-10-07"></a>

### [0.7.0](https://github.com/lyswhut/lx-music-desktop/compare/v0.6.2...v0.7.0) - 2019-10-07

**新增**

- 新增“我的收藏”本地播放列表
- 新增缓存清理功能，可到**设置-其他**查看与清理软件缓存
- 新增 `QQ` 音乐源搜索
- 新增咪咕源搜索
- 新增咪咕源歌单
- 新增咪咕源排行榜
- 新增我的音乐列表歌曲源显示，默认关闭，可到**设置-列表设置**开启

**优化**

- 优化选择框动画效果
- 尝试优化选我的音乐列表内容很多时多选的卡顿问题

**修复**

- 修复列表延迟显示的 `Bug`
- 修复 `QQ` 音源 `128k` 音质试听

<a id="markdown-062httpsgithubcomlyswhutlx-music-desktopcomparev061v062---2019-10-01" name="062httpsgithubcomlyswhutlx-music-desktopcomparev061v062---2019-10-01"></a>

### [0.6.2](https://github.com/lyswhut/lx-music-desktop/compare/v0.6.1...v0.6.2) - 2019-10-01

祝贺祖国成立 `70` 周年~！

**新增**

- 新增 `QQ` 音乐源歌单

**修复**

- 修正火影皮肤名字
- 修复当试听列表为空时，无法切到其他界面的 Bug
- 修复百度源搜索结果为空时的接口处理 Bug
- 恢复**酷狗**其他音质播放

<a id="markdown-软件下载" name="软件下载"></a>

## 软件下载

- [Github - Release](https://github.com/lyswhut/lx-music-desktop/releases/latest)
- [蓝奏云](https://www.lanzous.com/b906260/#glqw) 密码：glqw
- [90 盘](https://www.90pan.com/o129389)
- [本站分流](https://pan.ryanjie.cn/Excellent/lxmusic)

[admonition title="免责声明" color="indigo"]

本项目**不开发或者破解直接获取音频数据**的功能，所有音频数据均来自**第三方接口**！
本软件仅用于**测试 `electron 8` 在各种系统上的兼容性**及用于**对比各大音乐平台歌单、排行榜等数据列表的差异性**，使用本软件产生的**任何涉及版权相关的数据**请于**24 小时内删除**。
本软件仅用于学习交流使用，禁止用于商业用途，使用本软件所造成的的后果由使用者承担！
若对此有疑问请 mail to: [lyswhut@qq.com](mailto:lyswhut@qq.com)

[/admonition]

[admonition title="文件校验" icon="flag" color="indigo"]

文件名称: **lx-music-desktop-v0.8.2-x64_x86-Setup.exe**
文件大小: 83.3 MB (87,375,892 字节)
MD5: `ac295cb1830f5d50370082799aa5ff4e`
SHA1: `cc6ae9a2bf429a2d082042eadad91b3d8e5eb0d9`

文件名称: **lx-music-desktop-v0.8.2-win_x64-green.7z**
文件大小: 39.3 MB (41,253,945 字节)
MD5: `84611b3ad8bcca80a4a0f81e01870eb3`
SHA1: `712fcc37f9ee4c9b8d45450902d3be299d98706c`

文件名称: **lx-music-desktop-0.8.2.dmg**
文件大小: 62.1 MB (65,177,866 字节)
MD5: `0f85adeeb62c42fea2a292661e5068e3`
SHA1: `b3b1960174c9d523e8f55a152c20b137bf117e69`

文件名称: **lx-music-desktop.v0.8.2.x64.deb**
文件大小: 43.9 MB (46,051,328 字节)
MD5: `5016e35e2495702ab6f186b305125908`
SHA1: `296b1405057d6f9df9e3b518338351a4bbf05e55`

文件名称: **lx-music-desktop-v0.8.2-x64.AppImage**
文件大小: 63.4 MB (66,483,139 字节)
MD5: `e8c87790c3da31f0c62c3ac3ffbabf70`
SHA1: `9fa545596b0136cc3ffb03e626d861b80e030ab6`

[/admonition]

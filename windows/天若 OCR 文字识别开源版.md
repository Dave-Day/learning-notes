---
title: 天若 OCR 文字识别开源版
date: 2019-10-18 06:59:48
categories: Program
---

<!-- more -->

<!-- TOC -->

- [天若 OCR 文字识别开源版](#天若-ocr-文字识别开源版)
  - [软件使用](#软件使用)
  - [软件说明](#软件说明)
  - [更新日志](#更新日志)
    - [V5.0.0](#v500)
  - [软件下载](#软件下载)

<!-- /TOC -->

<a id="markdown-天若-ocr-文字识别开源版" name="天若-ocr-文字识别开源版"></a>

# 天若 OCR 文字识别开源版

有些图片或视频中的信息想复制下来，这就要求我们要将这些图片或视频上的的信息截图后转换成可以编辑的文字，解决这个问题有些人知道用专业的 OCR 识别软件，而对于假如只想复制小部分文字，又不想安装大型 OCR 识别软件的人来说，下面这款天若 OCR 文字识别工具就非常实用方便，OCR 接口多，且识别率高。

天若 ocr 文字识别工具，集合百度、腾讯、有道、搜狗，调用了各大网站的 ocr 接口，免费不限次数。（有道免费接口有 ip 限制仅供娱乐）。

[github author="AnyListen" project="tianruoocr"][/github]

天若 OCR 文字识别开源版是基于 @天若幽心 [开源的代码](https://github.com/tianruoyouxin/tianruoocr_last) 进行完善制作而成。

[github author="tianruoyouxin" project="tianruoocr_last"][/github]

- 对于搜狗的接口调用的还是[ocr-shouji-sogou](http://ocr.shouji.sogou.com/v2/ocr/json)，这个接口识别效果很好，但对于图片的尺寸有规定。本人对截取图片进行了尺寸上的优化，保证较小文字也能识别。具体自行测试。
- 腾讯 ocr 接口，也比较准确，但是速度比较慢。
- 百度 ocr 接口，精确度还可以，但是标点符号识别不准确，速度一般。
- 有道 ocr 接口，速度很快平均 0.3-0.4 秒就可识别出来。但是接口受 ip 请求的限制。

<a id="markdown-软件使用" name="软件使用"></a>

## 软件使用

[admonition title="使用说明" color="indigo"]

1. 默认 F4 进行截图识别（托盘右键设置可自定义快捷键）。
2. 默认 F7 进行选择文本自动翻译（托盘右键设置可自定义快捷键）。
3. 默认 F8 浏览最近识别的文本（托盘右键设置可自定义快捷键）。
4. 有识别模式、翻译模式、文本模式（托盘右键设置可进行切换）。
   - 识别模式：识别文本后弹窗。
   - 翻译模式：识别文本后弹窗，并自动翻译。
   - 文本模式：识别文本后不弹窗，自动复制文本到粘贴板。
5. 快捷键以及截图保存位置，可以鼠标右键点击按钮进行禁用。
6. 截图时按 Tab 键可以切换识别还是截图。
7. 快捷键支持 2 个键的组合键。

[/admonition]

<a id="markdown-软件说明" name="软件说明"></a>

## 软件说明

[admonition title="软件不能使用原因" color="red"]

- 缺少.net 框架，最低需要安装.net4.0。原则上你只要安装了这个版本的框架 xp 系统也可以使用。
- 快捷键冲突更换快捷键。
- 出现按下截图键，屏幕放大情况的请右键属性，禁用 dpi 的显示缩放。如下图所示：

[/admonition]

<a id="markdown-更新日志" name="更新日志"></a>

## 更新日志

<a id="markdown-v500" name="v500"></a>

### V5.0.0

新版本的主要特性：

1. 对原来的代码结构进行了简单重构；
2. 移除了 V4.49 版本的提示更新的弹窗；
3. 实现了新版的程序自动更新。

总体来讲没有带来什么新功能，后期主要对目前的功能代码进行重构； 然后逐步跟进新版本的功能。

最后，希望有兴趣的可以共同推动开源版本的发展。

<a id="markdown-软件下载" name="软件下载"></a>

## 软件下载

- [Github - release](https://github.com/AnyListen/tianruoocr_last/releases)
- [百度网盘](https://pan.baidu.com/s/17T1MR6R7EQ4zvgeokTMFeA)
- [90 盘](https://www.90pan.com/o128796)

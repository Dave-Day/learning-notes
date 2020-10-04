---
title: 蓝奏云客户端 GUI 版 lanzou-gui
date: 2020-02-16 07:49:53
categories: Program
---

<!-- more -->

<!-- TOC -->

- [蓝奏云客户端 GUI 版 lanzou-gui](#蓝奏云客户端-gui-版-lanzou-gui)
  - [软件说明](#软件说明)
  - [使用说明](#使用说明)
  - [更新日志](#更新日志)
    - [v0.0.7](#v007)
    - [v0.0.6](#v006)
    - [v0.0.5](#v005)
  - [软件下载](#软件下载)

<!-- /TOC -->

<a id="markdown-蓝奏云客户端-gui-版-lanzou-gui" name="蓝奏云客户端-gui-版-lanzou-gui"></a>

# 蓝奏云客户端 GUI 版 lanzou-gui

蓝奏云客户端，采用蓝奏云 API 项目使用 PyQt5 实现图形界面，完成蓝奏云的大部分功能。蓝奏云 API 项目封装了蓝奏网盘的基础功能: 登录、注销、获取文件(夹)列表、下载文件、上传文件、删除文件(夹)、 移动文件、清空回收站、恢复文件(夹)、创建文件夹、设置文件(夹)访问密码、设置文件(夹)描述。解决了蓝奏云的上传格式限制和单文件大小限制，同时增加了以下功能: 批量上传/下载文件、 上传/下载时断点续传、清理"幽灵"文件夹、移动文件夹、获取下载直链。

[github author="rachpt" project="lanzou-gui"][/github]

![img](https://img.shields.io/badge/support-Windows-blue?logo=Windows) ![img](https://img.shields.io/badge/support-Linux-yellow?logo=Linux) ![img](https://img.shields.io/badge/support-MacOS-green?logo=apple)![img](https://img.shields.io/github/v/release/rachpt/lanzou-gui.svg?logo=iCloud) ![img](https://img.shields.io/github/last-commit/rachpt/lanzou-gui.svg)

[admonition title="lanzou-gui" color="indigo"]

- 本项目使用`PyQt5`实现图形界面，可以完成蓝奏云的大部分功能
- 得益于 API 的功能，可以间接突破单文件最大 100MB 的限制，同时增加了批量上传/下载的功能
- `Python` 依赖见[requirements.txt](https://github.com/rachpt/lanzou-gui/blob/master/requirements.txt)，[releases](https://github.com/rachpt/lanzou-gui/releases) 有打包好了的 Windows 可执行程序，但**可能不是最新的**

[/admonition]

![lanzou-gui](https://pic.ryanjie.cn/2020/02/lanzou-gui.jpg)

<a id="markdown-软件说明" name="软件说明"></a>

## 软件说明

- 目前默认并发下载任务为 3，可以自行设置，单个文件还是单线程的；
- 文件可以直接拖拽到软件界面上传，也可以使用对话框选择；
- 文件夹最多 4 级，这是蓝奏云的限制；
- 文件上传后不能改名，同时最好不要创建相同名字的文件夹；
- 更多说明与界面预览详见 [WiKi](https://github.com/rachpt/lanzou-gui/wiki)。

<a id="markdown-使用说明" name="使用说明"></a>

## 使用说明

1. 无需账号，即可使用链接提取与下载功能；
2. 首次登录后，下次打开软件会自动登录(已经实现异步登录 ![:zap:](https://gitee.com/assets/emoji/zap-414cd56e51886412a1db3c4ce4089442.png))，对了登录信息直接使用二进制存储在 `config.pkl` 文件中(v0.0.8 与以前的版本不兼容！)；
3. 如果提示登录成功，但是没有显示文件，可能需要手动重新登录以下；
4. 单个文件下载是单线程的，对于批量下载，默认同时下载文件数为 3，文件夹与文件一样在一个线程里面下载；
5. 文件上传功能除了通过窗口对话框选择文件，还可以直接拖拽文件到软件界面。和下载一样只有一个较简单的状态栏提示状态，后期会做一个独立的任务管理界面；
6. 如果需要上传大于 100MB 文件：对于 windows 用户，直接从源码运行，需要自己下载 [rar.exe](https://www.lanzous.com/i8m39mj) 放置软件根目录，非 windows 用户需要确保 `rar` 的安装路径是 `/usr/bin/rar`，或者自己设置 rar 的路径(v0.0.9 及以后不需要)；
7. 回收站已经完成(v0.1.0)，支持批量删除与还原；
8. 软件关闭到系统托盘需要自行设置开启，默认未开启；
9. 用户文件界面、回收站可以使用 `F5` 键快速刷新，其他快捷键见软件界面；
10. 软件启动后，会后台检查是否有新版本，有则会提示，也可以在关于界面手动点击版本号，检测更新；
11. 界面预览 [Linux-KDE-Interface-Preview](https://gitee.com/rachpt/lanzou-gui/wikis/Linux-KDE-Interface-Preview)
12. 开发功能与进度：[lanzou-gui-projects](https://github.com/rachpt/lanzou-gui/projects/1)

<a id="markdown-更新日志" name="更新日志"></a>

## 更新日志

<a id="markdown-v007" name="v007"></a>

### v0.0.7

- 修复上传接口 bug，[#5](https://github.com/rachpt/lanzou-gui/issues/5)
- 允许文件中有空格，[#6](https://github.com/rachpt/lanzou-gui/issues/6)
- 保存 cookie 至 config.pkl 文件，登录复用
- API 同步更新

<a id="markdown-v006" name="v006"></a>

### v0.0.6

本次更新除了升级 api 版本外，最重要的就是彻底将网络请求与 GUI 分离，从而确保不会因为网络质量差导致程序主线程崩溃。

此外：

- 修复修改与设置密码对话框信息残留 bug，
- 修复 Windows 平台 因 rar.exe 一直占用文件导致上传大文件失败的 bug，
- 新增 支持批量移动文件至新的文件夹，
- 修改下载上传进度条样式，
- 其它 请自行探索。

**对了，打包文件变大，可能是因为升级了 python3.8.1 的原因。**

<a id="markdown-v005" name="v005"></a>

### v0.0.5

- 新增 鼠标悬停提示 描述与提取码（大小列前面的钥匙图标也是表示有提取码）
- 全选快捷键 `Alt + A`，或者 `Ctrl + A`，推荐前者
- UI 更新，包括：tab 栏居中，使用 QSS 改变控件样式，文件夹导航栏美化
- 状态栏优化，使用不同颜色表明状态，后期会加入动画
- 文件上传目前几乎没有什么问题了
- 优化 登录登出逻辑，比如没有登录就不能打开上传对话框等
- 登录使用异步进程，软件打开速度明显变快

对了，添加了背景图片，加入了半透明效果，更新了 WiKi 软件截图。

<a id="markdown-软件下载" name="软件下载"></a>

## 软件下载

- [github-releases](https://github.com/rachpt/lanzou-gui/releases/latest)
- [gitee-releases](https://gitee.com/rachpt/lanzou-gui/releases)
- [90 盘](https://www.90pan.com/o128463)

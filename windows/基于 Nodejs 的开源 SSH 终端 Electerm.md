---
title: 基于 Nodejs 的开源 SSH 终端 Electerm
date: 2019-10-25 12:45:20
categories: Program
---

<!-- more -->

<!-- TOC -->

- [基于 Nodejs 的开源 SSH 终端 Electerm](#基于-nodejs-的开源-ssh-终端-electerm)
- [软件特色](#软件特色)
- [软件下载](#软件下载)
- [软件升级](#软件升级)

<!-- /TOC -->

[github author="electerm" project="electerm"][/github]

<a id="markdown-基于-nodejs-的开源-ssh-终端-electerm" name="基于-nodejs-的开源-ssh-终端-electerm"></a>

## 基于 Nodejs 的开源 SSH 终端 Electerm

electerm 是一个 terminal/ssh/sftp 客户端(支持 linux, mac, win), 基于 electron/ssh2/node-pty/xterm/antd 等组件.

![Electerm](https://pic.ryanjie.cn/2019/10/electerm.jpg)

![img](https://cdn.jsdelivr.net/gh/electerm/electerm-resource/static/images/electerm.gif)

<a id="markdown-软件特色" name="软件特色"></a>

## 软件特色

- 可作为终端/文件管理器或 ssh / sftp 客户端（类似于 xshell）
- 全局热键以切换窗口可见性（类似于 guake，默认值为`ctrl + 2`）
- 多平台（Linux，Mac，Win）
- 🇺🇸 🇨🇳 🇧🇷 🇷🇺 🇪🇸 🇫🇷 🇹🇷 支持多国语言（[electerm-locales](https://github.com/electerm/electerm-locales)，欢迎提供/修复问题）
- 双击直接编辑远程文件（小文件）。
- 使用内置编辑器编辑本地文件（小文件）。
- 使用公钥+密码进行身份验证。
- Zmodem（rz，sz）。
- 透明窗口（Mac，Win）。
- 终端背景图像。
- 全局/会话代理。
- 快速命令
- 将书签/主题/快速命令同步到 GitHub Secret Gist
- 串口支持

<a id="markdown-软件下载" name="软件下载"></a>

## 软件下载

- [Github Release](https://github.com.cnpmjs.org/electerm/electerm/releases)
- Mac： `brew cask install electerm`
- Linux： `sudo snap install electerm`
- Deepin：可以在 App Store 中找到它。
- npm：

  ```shell
  npm i -g electerm

  # after install it will open at once for windows and linux,
  # for mac, will open the drag to install panel
  ```

<a id="markdown-软件升级" name="软件升级"></a>

## 软件升级

- 自动升级：发布新版本后，再次启动 electerm 后，您将收到升级通知，然后单击升级按钮进行升级。
- 下载：只需下载最新版本，然后重新安装。
- Npm：如果从 npm 安装，则再次运行`npm i -g electerm`升级。

---
title: 谷歌浏览器 Google Chrome 便携增强版
date: 2019-11-03 19:51:42
categories: Program
---

<!-- more -->

<!-- TOC -->

- [谷歌浏览器 Google Chrome 便携增强版](#谷歌浏览器-google-chrome-便携增强版)
- [增强功能](#增强功能)
- [软件使用](#软件使用)
- [软件更新](#软件更新)
- [注意事项](#注意事项)
  - [其它说明](#其它说明)
- [软件下载](#软件下载)

<!-- /TOC -->

<a id="markdown-谷歌浏览器-google-chrome-便携增强版" name="谷歌浏览器-google-chrome-便携增强版"></a>

## 谷歌浏览器 Google Chrome 便携增强版

Google Chrome 是一款由 Google 公司开发的网页浏览器，该浏览器基于其他开源软件撰写，包括 WebKit，目标是提升稳定性、速度和安全性，并创造出简单且有效率的使用者界面。

[admonition title="软件官网" color="indigo"]

- [Google Chrome 国内](https://www.google.cn/chrome)
- [Google Chrome 国外](https://www.google.com/chrome)

[/admonition]

Google Chrome 浏览器增强版，由 shuax 基于官方正式版打包而成，加入便携化注入模块 Chrome++增强软件，强制实现 flash 插件支持，解除 Adobe Flash Player 地区不相容限制和移除警告提示，增强标签页功能。

![Chrome](https://pic.ryanjie.cn/2019/11/chrome.jpg)

<a id="markdown-增强功能" name="增强功能"></a>

## 增强功能

- 双击关闭标签页
- 保留最后标签页（点 X 不行）（防止关闭最后一个标签页时关闭浏览器）
- 鼠标悬停标签栏滚动
- 按住右键时滚轮滚动标签栏
- 移除 flash 锁区，移除 2020 年过期警告（下载、加载 flash 需要你自己处理）
- 移除开发者模式警告
- 便携设计，程序放在 App 目录，数据放在 Data 目录（不兼容原版数据，可以重装系统换电脑不丢数据）
- 移除更新错误警告（因为是绿色版没有自动更新功能）

<a id="markdown-软件使用" name="软件使用"></a>

## 软件使用

- 解压后运行 App/chrome.exe 即可。
- 由于是便携版，不会和其它版本冲突，不想用了可以直接删掉整个文件夹。

<a id="markdown-软件更新" name="软件更新"></a>

## 软件更新

1. 升级先把老版本 App 重命名为 App2。
2. 然后把新下载的所有文件覆盖到老文件夹内。
3. 包括 App、Data 和说明.txt。
4. 运行测试正常后可以安全删除 App2 老版本。
5. 建议保留上个版本压缩包以便出问题时还原。

<a id="markdown-注意事项" name="注意事项"></a>

## 注意事项

1. 增强功能通过 App/verison.dll 实现，通过 dll 劫持方式启动。
2. 鼠标手势推荐使用全局手势软件，比如 MouseInc。
3. 软件发现了问题欢迎加 QQ 群：703641632 进行反馈。

<a id="markdown-其它说明" name="其它说明"></a>

### 其它说明

1. v80 开启新增的隐藏功能拦截高负载的广告

   ```
   chrome://flags/#enable-heavy-ad-intervention //更改为Enabled重启；
   ```

2. v79 开启多线程下载功能（Parallel downloading）

   ```
   chrome://flags/#enable-parallel-downloading //更改为Enabled重启；
   ```

3. v77 开始又增加了 1 个隐藏地址栏中 URL 的 HTTP、HTTPS 及 WWW 前缀选项；

   ```
   chrome://flags/#omnibox-ui-hide-steady-state-url-trivial-subdomains //更改为Enabled重启；
   ```

4. v76 开始隐藏地址栏中 URL 的 HTTP、HTTPS 及 WWW 前缀（恢复方法）

   ```
   chrome://flags/#omnibox-ui-hide-steady-state-url-scheme-and-subdomains //更改为Enabled重启；
   ```

5. v73 开始禁止本地拖拽本地 crx 安装（仍然可通过扩展程序，加载已解压的扩展程序安装）
6. v71 开始永久禁用了 PPAPI f.lash 插件（强制启用方法如下，或用 Chrome ＋＋增强插件）

   ```
   chrome://flags/#enable-ephemeral-flash-permission //改为Enabled重启。
   ```

7. v57 开始弃用 `chrome://plugins/` 命令行进入界面；
8. v54 开始不再内置 PPAPI f.lash 插件；
9. v50 开始不再支持 Windows&reg; XP；

<a id="markdown-软件下载" name="软件下载"></a>

## 软件下载

- [增强版官网](https://shuax.com/project/chrome/)
- [蓝奏云（密码: hgkw）](https://www.lanzous.com/b00t3vkmb)

---
title: Git 代码树扩展
date: 2020-06-04 12:34:34
categories: Plugins
---

<!-- more -->

<!-- TOC -->

- [Git 代码树扩展](#git-代码树扩展)
  - [安装](#安装)
  - [特性](#特性)
  - [设置](#设置)
    - [Access Token](#access-token)
    - [快捷键](#快捷键)

<!-- /TOC -->

[github author="ineo6" project="git-master"][/github]

<a id="markdown-git-代码树扩展" name="git-代码树扩展"></a>

# Git 代码树扩展

Git 代码目录树浏览工具，支持 GitHub 通知，Git 文件历史可视化。

| Github                                                                     | Git History                                                                          | Gitee                                                                    |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| ![git-master-github](https://pic.ryanjie.cn/2020/06/git-master-github.png) | ![git-master-git-history](https://pic.ryanjie.cn/2020/06/git-master-git-history.png) | ![git-master-gitee](https://pic.ryanjie.cn/2020/06/git-master-gitee.png) |

<a id="markdown-安装" name="安装"></a>

## 安装

- [Github](https://github.com/ineo6/git-master)
- [Chrome Web Store](https://chrome.google.com/webstore/detail/git-master/klmeolbcejnhefkapdchfhlhhjgobhmo)
- [Edge Web Store](https://microsoftedge.microsoft.com/addons/detail/pcpkfgepcjdmdfelbabogmgoadgmiocg)
- [Firefox Addon](https://addons.mozilla.org/zh-CN/firefox/addon/git-master/)

<a id="markdown-特性" name="特性"></a>

## 特性

- 🚀 代码树支持`GitHub`、`GitLab`、`Gitee`
- 🖊️ 支持私有部署页面，一键标记
- 🗂️ 支持文件提交历史可视化 (GitHub && GitLab)
- 🔔 `GitHub`通知提醒
- 🌗 `GitHub`支持黑暗模式
- ⬇️ `GitHub`支持文件、目录下载
- 📦 展示`GitHub`仓库和文件大小

<a id="markdown-设置" name="设置"></a>

## 设置

<a id="markdown-access-token" name="access-token"></a>

### Access Token

默认情况下，`GitMaster`使用开放请求获取仓库信息，有以下两种情况需要配置`Access Token`:

- 访问私有仓库
- 接口请求达到上限

如果你使用`GitHub`，可以[点此创建](https://github.com/settings/tokens/new?scopes=repo&description=Git%20Master%20extension), 为了保证基本使用，切记勾选`public_repo` 和 `repo`.

`GitLab` 和 `Gitee`的操作是类似的。

**Access tokens 仅被存在浏览器本地存储中, 只有你自己能够访问.**

<a id="markdown-快捷键" name="快捷键"></a>

### 快捷键

边栏可以使用快捷键控制显隐，多个快捷键使用逗号`,`分隔。

- 支持的修饰键: `⇧`, `shift`, `option`, `⌥`, `alt`, `ctrl`, `control`, `command`, and `⌘`.
- 支持的功能键: `backspace`, `tab`, `clear`, `enter`, `return`, `esc`, `escape`, `space`, `up`, `down`, `left`, `right`, `home`, `end`, `pageup`, `pagedown`, `del`, `delete` , `f1` 到 `f19`.

进一步了解可以访问 [keymaster](https://github.com/madrobby/keymaster#supported-keys).

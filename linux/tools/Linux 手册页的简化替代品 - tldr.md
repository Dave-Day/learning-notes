---
title: Linux 手册页的简化替代品 - tldr
date: 2019-07-03 22:12:34
categories: Linux
---

<!-- more -->

<!-- TOC -->

- [Linux 手册页的简化替代品 - tldr](#linux-手册页的简化替代品---tldr)
- [软件特点](#软件特点)
- [软件安装](#软件安装)
  - [二进制安装包](#二进制安装包)
  - [使用 NPM 安装](#使用-npm-安装)
  - [macOS using brew](#macos-using-brew)
  - [其他方式](#其他方式)
- [软件使用](#软件使用)
  - [在线使用](#在线使用)
  - [本地使用](#本地使用)
- [相关链接](#相关链接)

<!-- /TOC -->

[github author="isacikgoz" project="tldr"][/github]

[github author="tldr-pages" project="tldr"][/github]

<a id="markdown-linux-手册页的简化替代品---tldr" name="linux-手册页的简化替代品---tldr"></a>

## Linux 手册页的简化替代品 - tldr

TLDR 页的 GitHub 仓库将其描述为简化的、社区驱动的手册页集合。在实际示例的帮助下，努力让使用手册页的体验变得更简单。如果还不知道，TLDR 取自互联网的常见俚语：Too Long Didn’t Read（太长没读）。

通过智能用户交互改进了社区驱动的手册页。 tldr 通过便利的用户指导功能将自己与任何其他 tldr 客户端区分开。

![alt-text](https://isacikgoz.me/tldr/images/screenplay.gif)

<a id="markdown-软件特点" name="软件特点"></a>

## 软件特点

- 完全互动（轻松填写命令参数）
- 从命令中搜索以找到所需的命令（精确+模糊搜索）
- 智能文件建议（将添加更多建议）
- 实施简单
- 最快的客户之一，甚至最快（请参阅基准）
- 易于安装。 支持所有主流操作系统和平台（Linux，MacOS，Windows）（arm，x86）
- Pure-go（甚至包含内置的 git）

<a id="markdown-软件安装" name="软件安装"></a>

## 软件安装

<a id="markdown-二进制安装包" name="二进制安装包"></a>

### 二进制安装包

从 [Release Page](https://github.com/isacikgoz/tldr/releases) 下载安装包，解压缩文件(如有必要，给程序添加执行权限)并添加进环境变量 `$PATH` 中。

例如：

linux

```bash
$ curl -OL https://github.com/isacikgoz/tldr/releases/download/v0.5.0/tldr_0.5.0_linux_amd64.tar.gz
$ tar xzf tldr_0.5.0_linux_amd64.tar.gz
$ chmod +x tldr
$ sudo mv tldr /usr/local/bin
```

<a id="markdown-使用-npm-安装" name="使用-npm-安装"></a>

### 使用 NPM 安装

```bash
npm install -g tldr
```

<a id="markdown-macos-using-brew" name="macos-using-brew"></a>

### macOS using brew

```bash
brew install isacikgoz/taps/tldr
```

<a id="markdown-其他方式" name="其他方式"></a>

### 其他方式

| Client                                                              | Installation instructions                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [Web client](https://github.com/ostera/tldr.jsx)                    | Visit [https://tldr.ostera.io](https://tldr.ostera.io/)                             |
| [Node.js client](https://github.com/tldr-pages/tldr-node-client)    | `npm install -g tldr`                                                               |
| [Ruby client](https://github.com/YellowApple/tldrb)                 | `gem install tldrb`                                                                 |
| [Haskell client](https://github.com/psibi/tldr-hs)                  | `stack install tldr`                                                                |
| [Perl client](https://github.com/skaji/perl-tldr)                   | `cpanm App::tldr`                                                                   |
| [Python client](https://github.com/tldr-pages/tldr-python-client)   | `pip install tldr` / `pacman -S tldr`                                               |
| [C client](https://github.com/tldr-pages/tldr-c-client)             | `brew install tldr`                                                                 |
| [Rust client](https://github.com/dbrgn/tealdeer/)                   | `cargo install tealdeer` / `yaourt -S tealdeer`                                     |
| [iOS client](https://github.com/freesuraj/TLDR)                     | [TLDR Man Page on App Store](https://appsto.re/sg/IQ0-_.i)                          |
| [Dash for macOS](https://github.com/Moddus/tldr-python-dash-docset) | open `Preferences > Downloads > User Contributed` and find `tldr pages` in the list |
| [Bash client](https://github.com/pepa65/tldr-bash-client)           | `bpkg install pepa65/tldr`                                                          |
| [Go client](https://github.com/isacikgoz/tldr)                      | `go get -u github.com/isacikgoz/tldr`                                               |

<a id="markdown-软件使用" name="软件使用"></a>

## 软件使用

<a id="markdown-在线使用" name="在线使用"></a>

### 在线使用

- [https://tldr.ostera.io/{Command name}](https://tldr.ostera.io/{Command name})

  - eg: [https://tldr.ostera.io/dd](https://tldr.ostera.io/dd)

- [https://tldr.ooops.me/](https://tldr.ooops.me/)
  - eg: [https://tldr.ooops.me/?windows/zh/rmdir](https://tldr.ooops.me/?windows/zh/rmdir)
  - eg: [https://tldr.ooops.me/?common/it/dd](https://tldr.ooops.me/?common/it/dd)

<a id="markdown-本地使用" name="本地使用"></a>

### 本地使用

```bash
$ tldr {Command name}
```

![tldr-pages](https://cdn.jsdelivr.net/gh/tldr-pages/tldr/images/screenshot.png)

<a id="markdown-相关链接" name="相关链接"></a>

## 相关链接

- [tldr Github](https://github.com/isacikgoz/tldr)
- [tldr Website](https://isacikgoz.me/tldr/)
- [tldr-pages Github](https://github.com/tldr-pages/tldr)
- [tldr-pages Website](https://tldr.sh/)

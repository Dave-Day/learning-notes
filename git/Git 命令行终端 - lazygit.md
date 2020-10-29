---
title: Git 命令行终端 - lazygit
date: 2019-01-04 18:06:26
categories: Github
---

<!-- more -->

<!-- TOC -->

- [Git 命令行终端 - lazygit](#git-命令行终端---lazygit)
- [软件特点](#软件特点)
- [软件安装](#软件安装)
  - [Github Releases](#github-releases)
  - [Homebrew](#homebrew)
  - [MacPorts](#macports)
  - [Ubuntu](#ubuntu)
  - [Void Linux](#void-linux)
  - [Scoop (Windows)](#scoop-windows)
  - [Fedora and CentOS 7](#fedora-and-centos-7)
- [软件使用](#软件使用)
  - [使用](#使用)
  - [快捷键](#快捷键)
  - [文档](#文档)
  - [介绍视频](#介绍视频)
- [相关链接](#相关链接)

<!-- /TOC -->

[github author="jesseduffield" project="lazygit"][/github]

<a id="markdown-git-命令行终端---lazygit" name="git-命令行终端---lazygit"></a>

## Git 命令行终端 - lazygit

[lazygit](https://github.com/jesseduffield/lazygit) 是一个用于 Git 命令行的简单终端 UI，使用 Go 语言编写，用到了 gocui 库，目的是在命令行提供 Git 的图形界面。

![lazygit](https://pic.ryanjie.cn/2019/01/lazygit.gif)

<a id="markdown-软件特点" name="软件特点"></a>

## 软件特点

- 轻松添加文件
- 解决合并冲突
- 轻松检出最近的分支
- 滚动查看 branches/commits/stash 的日志和差异信息
- 快速进行 pushing/pulling 操作
- 压缩并重命名 commits 信息

<a id="markdown-软件安装" name="软件安装"></a>

## 软件安装

<a id="markdown-github-releases" name="github-releases"></a>

### Github Releases

- [https://github.com/jesseduffield/lazygit/releases](https://github.com/jesseduffield/lazygit/releases)

<a id="markdown-homebrew" name="homebrew"></a>

### Homebrew

Tap:

```bash
brew install jesseduffield/lazygit/lazygit
```

Core:

```bash
brew install lazygit
```

<a id="markdown-macports" name="macports"></a>

### MacPorts

```bash
sudo port install lazygit
```

<a id="markdown-ubuntu" name="ubuntu"></a>

### Ubuntu

```bash
sudo add-apt-repository ppa:lazygit-team/release
sudo apt-get update
sudo apt-get install lazygit
```

<a id="markdown-void-linux" name="void-linux"></a>

### Void Linux

```bash
sudo xbps-install -S lazygit
```

<a id="markdown-scoop-windows" name="scoop-windows"></a>

### Scoop (Windows)

```bash
# Add the extras bucket
scoop bucket add extras

# Install lazygit
scoop install lazygit
```

<a id="markdown-fedora-and-centos-7" name="fedora-and-centos-7"></a>

### Fedora and CentOS 7

```bash
sudo dnf copr enable atim/lazygit -y
sudo dnf install lazygit
```

<a id="markdown-软件使用" name="软件使用"></a>

## 软件使用

<a id="markdown-使用" name="使用"></a>

### 使用

```bash
$ lazygit
```

添加别名

```bash
$ echo "alias lg='lazygit'" >> ~/.zshrc
```

<a id="markdown-快捷键" name="快捷键"></a>

### 快捷键

- [https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings)

<a id="markdown-文档" name="文档"></a>

### 文档

- https://github.com/jesseduffield/lazygit/blob/master/docs

<a id="markdown-介绍视频" name="介绍视频"></a>

### 介绍视频

- [Video Tutorial](https://youtu.be/VDXvbHZYeKY)
- [Rebase Magic Video Tutorial](https://youtu.be/4XaToVut_hs)
- [Twitch Stream](https://www.twitch.tv/jesseduffield)

<a id="markdown-相关链接" name="相关链接"></a>

## 相关链接

- Github：[https://github.com/jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)
- Doc：[https://github.com/jesseduffield/lazygit/blob/master/docs](https://github.com/jesseduffield/lazygit/blob/master/docs)

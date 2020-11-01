---
title: 模块化的 Vim IDE - SpaceVim
date: 2019-02-03 15:16:05
categories: Github
---

<!-- more -->

<!-- TOC -->

- [模块化的 Vim IDE - SpaceVim](#模块化的-vim-ide---spacevim)
- [安装指南](#安装指南)
  - [Linux 或 macOS](#linux-或-macos)
  - [Windows](#windows)
  - [Docker 支持](#docker-支持)
- [基本配置](#基本配置)
- [在线教程](#在线教程)
- [其他资源](#其他资源)

<!-- /TOC -->

[github author="SpaceVim" project="SpaceVim"][/github]

<a id="markdown-模块化的-vim-ide---spacevim" name="模块化的-vim-ide---spacevim"></a>

## 模块化的 Vim IDE - SpaceVim

SpaceVim 是一个社区驱动的模块化的 Vim IDE，以模块的方式组织管理插件以及相关配置， 为不同的语言开发量身定制了相关的开发模块，该模块提供代码自动补全， 语法检查、格式化、调试、REPL 等特性。用户仅需载入相关语言的模块即可得到一个开箱即用的 Vim IDE。

- [主页](https://spacevim.org/cn/)
- [入门指南](https://spacevim.org/cn/quick-start-guide/)
- [使用文档](https://spacevim.org/cn/documentation/)

<a id="markdown-安装指南" name="安装指南"></a>

## 安装指南

在安装 SpaceVim 之前，你需要确保电脑上已经安装了 `Git` 和 `cURL`。这两个工具用来 下载插件以及字体。

如果在终端中使用 Vim 或 Neovim，还需要设置终端的字体。

<a id="markdown-linux-或-macos" name="linux-或-macos"></a>

### Linux 或 macOS

```bash
curl -sLf https://spacevim.org/cn/install.sh | bash
```

安装结束后，初次打开 `Vim` 或者 `gVim` 时，SpaceVim 会**自动**下载并安装插件。

如果需要获取安装脚本的帮助信息，可以执行如下命令，包括定制安装、更新和卸载等。

```bash
curl -sLf https://spacevim.org/cn/install.sh | bash -s -- -h
```

<a id="markdown-windows" name="windows"></a>

### Windows

Windows 下最快捷的安装方法是下载安装脚本 [install.cmd](https://spacevim.org/cn/install.cmd) 并运行。

<a id="markdown-docker-支持" name="docker-支持"></a>

### Docker 支持

```bash
docker pull spacevim/spacevim
docker run -it --rm spacevim/spacevim nvim
```

也可以通过挂载的方式载入本地配置：

```bash
docker run
  \ -it -v
  \ ~/.SpaceVim.d:/home/spacevim/.SpaceVim.d
  \ --rm
  \ spacevim/spacevim nvim
```

<a id="markdown-基本配置" name="基本配置"></a>

## 基本配置

SpaceVim 的默认配置文件为 `~/.SpaceVim.d/init.toml`。下面为一简单的配置示例。 如果需要查阅更多 SpaceVim 配置相关的信息，请阅读 SpaceVim 用户文档。

```ini
# 这是一个基础的 SpaceVim 配置示例

# 所有的 SpaceVim 选项都列在 [options] 之下
[options]
    # 设置 SpaceVim 主题及背景，默认的主题是 gruvbox，如果你需要使用更
    # 多的主题，你可以载入 colorscheme 模块
    colorscheme = "gruvbox"
    # 背景可以取值 "dark" 或 "light"
    colorscheme_bg = "dark"
    # 启用/禁用终端真色，在目前大多数终端下都是支持真色的，当然也有
    # 一小部分终端不支持真色，如果你的 SpaceVim 颜色看上去比较怪异
    # 可以禁用终端真色，将下面的值设为 false
    enable_guicolors = true
    # 设置状态栏上分割符号形状，如果字体安装失败，可以将值设为 "nil" 以
    # 禁用分割符号，默认为箭头 "arrow"
    statusline_separator = "nil"
    statusline_inactive_separator = "bar"
    # 设置顶部标签列表序号类型，有以下五种类型，分别是 0 - 4
    # 0: 1 ➛ ➊
    # 1: 1 ➛ ➀
    # 2: 1 ➛ ⓵
    # 3: 1 ➛ ¹
    # 4: 1 ➛ 1
    buffer_index_type = 4
    # 显示/隐藏顶部标签栏上的文件类型图标，这一图标需要安装 nerd fonts，
    # 如果未能成功安装这一字体，可以隐藏图标
    enable_tabline_filetype_icon = true
    # 是否在状态栏上显示当前模式，默认情况下，不显示 Normal/Insert 等
    # 字样，只以颜色区分当前模式
    enable_statusline_mode = false

# SpaceVim 模块设置，主要包括启用/禁用模块

# 启用 autocomplete 模块，启用模块时，可以列出一些模块选项，并赋值，
# 关于模块的选项，请阅读各个模块的文档
[[layers]]
    name = "autocomplete"
    auto-completion-return-key-behavior = "complete"
    auto-completion-tab-key-behavior = "cycle"

# 禁用 shell 模块，禁用模块时，需要加入 enable = false
[[layers]]
    name = "shell"
    enable = false

# 添加自定义插件
[[custom_plugins]]
    name = "lilydjwg/colorizer"
    merged = false
```

<a id="markdown-在线教程" name="在线教程"></a>

## 在线教程

以下主要为 SpaceVim 的基本使用教程，侧重于各种语言开发环境的搭建，可以理解为 SpaceVim 用户文档的精简版，主要包括以下内容：

- [使用 SpaceVim 搭建基本的开发环境](https://spacevim.org/cn/use-vim-as-ide/)：涵盖一些窗口及文件的常规操作。

针对不同语言，一些基础的配置及使用技巧：

- [使用 Vim 搭建 TypeScript 开发环境](https://spacevim.org/cn/use-vim-as-a-typescript-ide/)
- [使用 Vim 搭建 Rust 开发环境](https://spacevim.org/cn/use-vim-as-a-rust-ide/)
- [使用 Vim 搭建 C/C++ 开发环境](https://spacevim.org/cn/use-vim-as-a-c-cpp-ide/)
- [使用 Vim 搭建 PHP 开发环境](https://spacevim.org/cn/use-vim-as-a-php-ide/)
- [使用 Vim 搭建 Ruby 开发环境](https://spacevim.org/cn/use-vim-as-a-ruby-ide/)
- [使用 Vim 搭建 Perl 开发环境](https://spacevim.org/cn/use-vim-as-a-perl-ide/)
- [使用 Vim 搭建 CoffeeScript 开发环境](https://spacevim.org/cn/use-vim-as-a-coffeescript-ide/)
- [使用 Vim 搭建 JavaScript 开发环境](https://spacevim.org/cn/use-vim-as-a-javascript-ide/)
- [使用 Vim 搭建 Lua 开发环境](https://spacevim.org/cn/use-vim-as-a-lua-ide/)
- [使用 Vim 搭建 Go 开发环境](https://spacevim.org/cn/use-vim-as-a-go-ide/)
- [使用 Vim 搭建 Python 开发环境](https://spacevim.org/cn/use-vim-as-a-python-ide/)
- [使用 Vim 搭建 Java 开发环境](https://spacevim.org/cn/use-vim-as-a-java-ide/)

<a id="markdown-其他资源" name="其他资源"></a>

## 其他资源

- [Hack-SpaceVim](https://github.com/Gabirel/Hack-SpaceVim). Tell you how to hack SpaceVim.
- [SpaceVim 入门教程](https://everettjf.gitbooks.io/spacevimtutorial/content/)：everettjf 所著的 SpaceVim 入门教程。

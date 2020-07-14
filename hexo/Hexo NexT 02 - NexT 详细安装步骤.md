---
title: Hexo NexT 02 - NexT 详细安装步骤
date: 2018-11-11 02:13:30
categories: Hexo
---

<!-- more -->

## Hexo NexT 02 - NexT 详细安装步骤

> **原文地址：<https://theme-next.org/docs/getting-started/installation>**

## 进入站点根目录

进入 Hexo **站点根目录**。这一目录中应当有 `node_modules`、`source`、`themes` 等若干子目录：

```bash
$ cd hexo
$ ls
_config.yml  node_modules  package.json  public  scaffolds  source  themes
```

## 获取 `NexT`

从 GitHub 下载主题。为了下载 `NexT` 主题，共有 **3 种方案**可选。您需要选择其中**任意一个方式**。

### 下载[开发版(最新 master 分支)](https://github.com/theme-next/hexo-theme-next/archive/master.zip)

可能**不稳定**，但包含最新的特性。推荐进阶用户和开发者按此方式进行。

#### 方式 1：Git

```bash
$ git clone https://github.com/theme-next/hexo-theme-next themes/next
```

这一方式将为您下载**完整仓库**（其中包含 `.git` 目录）。
您可以随时[使用 git 更新至最新版本](https://github.com/theme-next/hexo-theme-next/blob/master/docs/zh-CN/README.md#update)并切换至任何有 tag 标记的 release 版本、最新的 master 分支版本、甚至其他分支。
在绝大多数情况下对用户和开发者友好。

获取 tags 列表：

```bash
$ cd themes/next
$ git tag -l
…
v6.0.0
v6.0.1
v6.0.2
```

例如，假设您想要切换到 `v6.0.1` 这一 [tag 指向的 release 版本](https://github.com/theme-next/hexo-theme-next/tags)。输入如下指令：

```bash
$ git checkout tags/v6.0.1
Note: checking out 'tags/v6.0.1'.
…
HEAD is now at da9cdd2... Release v6.0.1

# If you want to switch on latest release version without defining tag (optional)
$ git checkout $(git describe --tags $(git rev-list --tags --max-count=1))
```

然后，假设您想要切换回 [master 分支](https://github.com/theme-next/hexo-theme-next/commits/master)，输入如下指令即可：

```bash
$ git checkout master
```

**更新**

您可以通过如下命令更新到最新的 master 分支：

```bash
$ cd themes/next
$ git pull
```

如果您在此过程中收到了任何错误报告 (例如 **«Commit your changes or stash them before you can merge»**)，我们推荐您使用 [Hexo 数据文件](https://github.com/theme-next/hexo-theme-next/blob/master/docs/zh-CN/DATA-FILES.md)特性。
然而您也可以通过提交（`Commit`）、贮藏（`Stash`）或忽视（`Discard`）本地更改以绕过这种更新错误。具体方法请参考[这里](https://stackoverflow.com/a/15745424/5861495)。

#### 方式 2：下载解压方式 curl 和 tar

```bash
$ mkdir themes/next
$ curl -L https://api.github.com/repos/theme-next/hexo-theme-next/tarball | tar -zxv -C themes/next --strip-components=1
```

和上述的 `curl、tar 和 wget` 方法相同，但只会下载**最新 master 分支版本**。
在有些情况对开发者有所帮助。

### 下载 [tag 指向的 release 版本](https://github.com/theme-next/hexo-theme-next/releases)

在少数情况下将有所帮助，但这并非推荐方式。
您必须指定一个版本：使用 [tags 列表](https://github.com/theme-next/hexo-theme-next/tags)中的任意 tag 替换 `v6.0.0`。

#### 方式 1：Git

```bash
$ git clone --branch v6.0.0 https://github.com/theme-next/hexo-theme-next themes/next
```

这一方式将为您下载**指定的 release 版本**（其中包含 `.git` 目录）。
并且，您可以随时切换到任何已定义的版本号所对应的 tag 的版本。

#### 方式 2：下载解压方式 curl 和 tar

```bash
$ mkdir themes/next
$ curl -L https://api.github.com/repos/theme-next/hexo-theme-next/tarball/v6.0.0 | tar -zxv -C themes/next --strip-components=1
```

和上述的 `curl、tar 和 wget` 方法相同，但只会下载**指定的 release 版本**。

### 下载 [稳定版(最新 release 版本)](https://github.com/theme-next/hexo-theme-next/releases/latest)

通常情况下请选择 **stable** 版本。推荐不熟悉的用户按此方式进行。

#### 下载解压方式 curl 和 tar

```bash
$ mkdir themes/next
$ curl -s https://api.github.com/repos/theme-next/hexo-theme-next/releases/latest | grep tarball_url | cut -d '"' -f 4 | wget -i - -O- | tar -zx -C themes/next --strip-components=1
```

这种方式将**仅提供最新的 release 版本**（其中不附带 `.git` 目录）。
因此，将来您将不可能通过 `git` 更新这一方式安装的主题。
取而代之的，为了能不丢失您的自定义配置，您可以使用独立的配置文件（例如 [数据文件](https://github.com/theme-next/hexo-theme-next/blob/master/docs/zh-CN/DATA-FILES.md)）并下载最新版本到旧版本的目录中（或者下载到新的主题目录中并修改**站点配置文件** `Hexo` 配置中的主题名），以免丢失您原来的配置。

### 配置

`NexT` 下载完成后，我们必须返回到之前的指南并阅读 [启用`NexT` 主题](https://theme-next.org/docs/getting-started/#Enabling-NexT) 说明。

---
title: Hexo NexT 01 - NexT 入门
date: 2018-11-10 02:13:07
categories: Hexo
---

<!-- more -->

## Hexo NexT 01 - NexT 入门

> **原文地址：<https://theme-next.org/docs/getting-started/>**

[HEXO](https://hexo.io/) 是一个快速而强大的静态博客生成框架，它是基于 `Node.js` 的，通过使用`Hexo`，您可以用`Markdown`轻松地写文章，您还可以使用`Hexo`提供的[标记插件](https://hexo.io/docs/tag-plugins)简单地插入特殊格式的内容。在这个页面中，我们假设您已经安装[HEXO](https://hexo.io/docs/tag-plugins)，并创建了一个网站。

> 您可以访问[`Hexo`官方文档](https://hexo.io/docs/)以了解如何安装`Hexo`。

## 文档变量

### \_config.yml

在 Hexo 中有两份主要的配置文件，其名称都是 `_config.yml`。

1. 第一个是在**站点根目录**下，其中包含`Hexo`的配置。
2. 第二个是在**主题根目录**下，由`NexT`提供，包含主题的配置。

为了描述方便，在以下说明中，将前者称为 **站点配置文件**， 后者称为 **主题配置文件**。

## NexT 安装

Hexo 的主题安装过程很简单。您只需要下载`NexT`主题，然后将**主题文件夹**复制到**站点根目录**下的主题目录，并在**站点配置文件**中指定您的**主题根目录**。具体步骤如下：

### 下载 NexT

#### 最新版（开发版）

如果您了解 Git，您可以克隆整个存储库，并使用 Git pull 命令随时更新它，而不必手动下载更新。

打开终端，切换到`Hexo`站点根目录，克隆`NexT`主题的最新`master`分支：

```bash
$ cd hexo
$ git clone https://github.com/theme-next/hexo-theme-next themes/next
```

#### 稳定版

1. 转到[`NexT`稳定版发布页](https://github.com/theme-next/hexo-theme-next/releases/latest)。
2. 选择所需的版本并下载源代码（zip）。例如 `v6.0.0`。
3. 将`zip`文件解压缩到站点的主题目录，并将解压缩的文件夹（`hexo-theme-next-6.0.0`）重命名为`next`。

> **此外，如果您想要使用其他方式，您也可以阅读 [详细安装步骤](https://theme-next.org/docs/getting-started/installation)。**
>
> **如果您还在用 v5.x 版本，您可以阅读 [如何从 v5.x 更新到 v6.x](https://theme-next.org/docs/getting-started/update-from-v5) 这篇文档。**

### 启用主题

打开 **站点配置文件**，找到 `theme` 字段，并将其值更改为 `next` 。

**hexo/\_config.yml**

```yaml
theme: next
```

到此，`NexT` 主题安装完成。下一步我们将验证主题是否正确启用。在切换主题之后、验证之前，我们最好使用 `hexo clean` 来清除 `Hexo` 的缓存。

```bash
λ sed -i 's/theme: landscape/theme: next/g' _config.yml
λ hexo clean
```

### 验证主题

首先启动 `Hexo` 本地站点，并开启调试模式（即加上 `--debug` ），整个命令是 `hexo s --debug` 。在服务启动的过程，注意观察命令行输出是否有任何异常信息，如果您碰到问题，这些信息将帮助他人更好的定位错误。当命令行输出中提示出：

```bash
INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.
DEBUG Database saved
```

此时即可使用浏览器访问 `http://localhost:4000` ，检查站点是否正确运行。

> 如果您发现您的网站看起来像这张图片，说明您已经正确安装了它。 这是 `NexT`默认的风格 - Muse 。
>
> ![Default Scheme – Muse](https://d33wubrfki0l68.cloudfront.net/90fa9a4a64b8ddf623b4b88c59f821f60500655a/6bf8d/images/docs/next-default-scheme-linux.png)

现在您已经安装并启用`NexT`。在接下来的步骤中，我们将改变一些设置，包括个性化和第三方服务集成。

### 安装插件

有 2 个方法加载`NexT`插件：

- 本地安装（插件脚本会从您的网站加载）。
- CDN 链接（插件脚本会从远程主机加载）。

> **如果您的站点托管在带有 nginx 配置的 VPS（ openvz、kvm、独服 ）上，建议使用本地安装。**
>
> **如果您的文件部署到任何免费托管服务（Github 上、Coding、Gitee、Gitlab 等），建议使用 CDN 链接。**

#### 本地加载

在 `NexT`配置中有一些第三方插件，它们已经被移至外部仓库。您可以在[组织主页](https://github.com/theme-next)中找到它们。

例如，您想要在您的站点中使用 `pjax` 插件，请进入 `NexT`**主题配置文件**，您会看到如下内容：

```yaml
# Easily enable fast Ajax navigation on your website.
# Dependencies: https://github.com/theme-next/theme-next-pjax
pjax: false
```

启用 `pjax` 配置项，打开它上面的 [«Dependencies» 链接](https://github.com/theme-next/theme-next-pjax) 查看它的安装步骤。

#### 设置 CDN

如果您想要通过 CDN 来加载插件脚本，那么需要设置相关的 CDN 链接。

例如，您使用了 `mediumzoom` 插件并且配置了 CDN 加载链接，进入 Next 配置文件，您会看到如下内容：

```yaml
vendors:
  # ...
  # Some contents...
  # ...
  mediumzoom: # Set or update mediumzoom CDN URL.
```

这里我们推荐使用 **jsdeliver CDN**，因为它在任何地方都很快，并且拥有中国政府颁发的有效 ICP 许可证。它不仅能从 npm 包中抓取 js 文件，还能从 GitHub Releases 中抓取！我们可以使用下面的链接来引用 js 文件，就像其他 cdn 一样。

```yaml
//cdn.jsdelivr.net/gh/user/repo@version/file
```

您只需使用`filename.min.js`或`filename.min.css`来替换上面的文件。它可以自动压缩 JS 和 CSS 文件，即使您没有简化版。

我们还提供其他可选的 CDN，包括著名的[CDNJS](https://cdnjs.com/)和在中国访问速度非常快的[Bootcss](https://www.bootcdn.cn/)。

## 配置 `NexT` 主题

### 选择 风格

风格是 `NexT` 提供的一种特性，借助于 Scheme，`NexT` 为您提供多种不同的外观。同时，几乎所有的配置都可以在各种风格之间共用。

- **`Muse`** → 默认方案，这是`NexT` 的初始版本。采用黑白色调，主要看起来干净。
- `Mist` → 紧密版的`Muse`，具有整齐单列视图。
- `Pisces` → 双列风格，像您邻居的女儿一样清新。
- `Gemini` → 看起来像`Pisces` ，但相比于`Pisces` 有更明显的阴影效果。

风格切换通过更改 **主题配置文件**，搜索 scheme 关键字。您会看到有四行 scheme 的配置，将您需用启用的 scheme 前面注释 `#` 去除即可，然后在之前的 scheme 前面添加注释 `#` 。

```yaml
#scheme: Muse
#scheme: Mist
#scheme: Pisces
scheme: Gemini
```

```bash
λ sed -i 's/scheme: Muse/#scheme: Muse/g' themes/next/_config.yml
λ sed -i 's/#scheme: Gemini/scheme: Gemini/g' themes/next/_config.yml
```

#### 主题风格预览

- 💟 Muse scheme: [LEAFERx](https://leaferx.online/) | [Alex LEE](http://saili.science/) | [Miaia](https://11.tt/)
- 🔯 Mist scheme: [uchuhimo](https://uchuhimo.me/) | [xirong](http://www.ixirong.com/)
- ♓️ Pisces scheme: [Vi](https://notes.iissnan.com/) | [Acris](https://acris.me/) | [Jiaxi He](https://jiaxi.io/)
- ♊️ Gemini scheme: [Ivan. Nginx](https://almostover.ru/) | [Raincal](https://raincal.com/) | [Dandy](https://dandyxu.me/) | [Mimi](https://zhangshuqiao.org/)

### 设置 语言

编辑 **站点配置文件**， 将 `language` 设置成您所需要的语言。建议明确设置您所需要的语言，例如选用 English ，配置如下：

```bash
language: en
```

目前 `NexT` 支持的语言如以下表格所示：

| Language                  | Example               | Code    |
| :------------------------ | :-------------------- | :------ |
| 🇨🇳 Chinese (Simplified)   | 简体中文              | `zh-CN` |
| 🇹🇼 Chinese (Traditional)  | 繁體中文              | `zh-TW` |
| 🇭🇰 Chinese (Hong Kong)    | 繁體中文-香港         | `zh-HK` |
| 🇧🇶 Dutch                  | Niederländisch        | `nl`    |
| 🇺🇸 English                | English               | `en`    |
| 🇹🇫 French                 | Français              | `fr`    |
| 🇩🇪 German                 | Deutsch               | `de`    |
| 🇮🇩 Indonesian             | Indonesia             | `id`    |
| 🇮🇹 Italian                | Italiano              | `it`    |
| 🇯🇵 Japanese               | 日本語                | `ja`    |
| 🇰🇷 Korean                 | 한국어                | `ko`    |
| 🇮🇷 Persian                | فارسی                 | `fa`    |
| 🇵🇹 Portuguese             | Português             | `pt`    |
| 🇧🇷 Portuguese (Brazilian) | Português (Brazilian) | `pt-BR` |
| 🇷🇺 Russian                | Русский               | `ru`    |
| 🇪🇸 Spanish                | Español               | `es`    |
| 🇹🇷 Turkish                | Türk                  | `tr`    |
| 🇺🇦 Ukrainian              | Український           | `uk`    |
| 🇻🇳 Vietnamese             | Tiếng Việt            | `vi`    |

如果您想为`NexT` 题添加或修改语言，可以使用[crowdin](https://crwd.in/theme-next) service 轻松实现。

```bash
λ sed -i 's/language: en/language: zh-Hans/g' _config.yml
```

### 配置 菜单导航

菜单导航配置包括三个部分，第一是菜单导航（名称和链接），第二是菜单导航的显示文本，第三是菜单导航对应的图标。 `NexT` 使用的是 [Font Awesome](http://fontawesome.io/) 提供的图标， `Font Awesome` 提供了 600+ 的图标，可以满足绝大的多数的场景，同时无须担心在 `Retina` 屏幕下图标模糊的问题。

编辑 **主题配置文件**，修改以下内容：

#### 配置 菜单导航内容

设置菜单导航内容，对应的字段是 `menu` 。菜单内容的设置格式是： `Key: /link/ || icon` 。

- `Key` 是菜单导航名称，例如： `home` , `archives` 等等。注意： `Key` 是敏感的，也就是区分大小写， 键值（如 `home`）的大小写要严格匹配 。
- `||` 分隔符 之后的 ( `/link/` ) → 是菜单导航链接，指向您网站内相对网址的目标链接。
- `||` 分隔符 之后的 ( `icon` ) → 是菜单导航图标， `FontAwesome` 图标的名称。这些图标的名字可以在 [Font Awesome](https://fontawesome.com/) 网站上找到。

```yaml
menu:
  home: / || home
  tags: /tags/ || tags
  categories: /categories/ || th
  archives: /archives/ || archive
  about: /about/ || user
  # schedule: /schedule/ || calendar
  # sitemap: /sitemap.xml || sitemap
  # commonweal: /404/ || heartbeat
```

`NexT` 主题默认提供 首页 `home` 和 归档 `archives` 两个菜单导航，需要其他菜单导航请自定义相关页面。

> **若您的站点运行在子目录中，请将链接前缀的 `/` 去掉** 。

> **请注意键值（如 `home`）的大小写要严格匹配** 。

#### 自定义 导航相关页面

##### 添加 新导航页面

例如添加 `Tags` 和 `Categories` 导航页面。

```bash
cd your-hexo-site
hexo new page tags
hexo new page categories
```

##### 设置 导航页面类型

**tags/index.md**

```md
---
title: Tags
date: 2018-06-06 17:25:30
type: "tags"
comments: false
---
```

**categories/index.md**

```md
---
title: Categories
date: 2018-06-06 17:25:30
type: "categories"
comments: false
---
```

##### 编辑 菜单导航

```yaml
menu:
  tags: /tags/ || tags
  categories: /categories/ || th
```

#### 配置 菜单导航图标

- `icons` ：是否显示菜单导航图标
- `badges` ：是否显示菜单导航页面计数。

> **默认情况下，`NexT`不显示菜单导航页面计数。**

```yaml
# Enable / Disable menu icons / item badges.
menu_settings:
  icons: true
  badges: true
```

### 配置 网站图标

默认情况下，`Hexo` 站点使用 `hexo-site/themes/next/source/images/` 目录中的 `NexT` favicons，不同的设备有不同的尺寸。您可以用您自己的图标来代替它们。

例如，您可以把您的站点图标放在 `hexo-site/source/images/` 目录下。然后您需要重命名它们并在**主题配置文件**中更改`favicon`部分的设置。否则，`NexT` 的图标将重写`Hexo`中的自定义图标。

您还可以将自定义图标放入 `hexo-site/source/` 目录 。如果这样的话，您必须从路径中**删除** `/images` 前缀。

如果您想要自定义网站图标，可以访问网站 [Favicon 生成器](https://realfavicongenerator.net/)。

**hexo/\_config.yml**

```yaml
favicon:
  small: /images/favicon-16x16-next.png
  medium: /images/favicon-32x32-next.png
  apple_touch_icon: /images/apple-touch-icon-next.png
  safari_pinned_tab: /images/logo.svg
  android_manifest: /images/manifest.json
  ms_browserconfig: /images/browserconfig.xml
```

### 设置 头像

默认情况下，`NexT` 在边栏中不显示头像。您可以通过编辑\*\*主题配置文件，修改字段 `avatar`， 值设置成头像的链接地址。

#### url 头像路径

- url 可以通过以下方式之一来指定您自己的头像。

| 地址                   | 值                                                                                                                         |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **站点根目录**         | 把您的头像放在**网站根目录** `source/uploads/` (如果不存在则创建目录)。<br/>然后将选项改为 `avatar: /uploads/avatar.png`。 |
| **`NexT` 主题目录**    | 把您的头像放在**主题目录** `source/images/`。<br/>然后将选项改为 `avatar: /images/avatar.png`。                            |
| **互联网上的绝对路径** | 您还可以指定任何外部 URL，其绝对路径为 : `http(s)://example.com/avatar.png` 。                                             |

> 当前站点使用**主题目录**下的 avatar 来自 `next/source/images/apple-touch-icon-next.png` 文件，配置如下:
>
> **hexo/\_config.yml**
>
> ```yaml
> theme_config:
>   avatar:
>     url: /images/apple-touch-icon-next.png
>     rounded: true
>     rotated: false
> ```

#### rounded 头像圆角化

通过改变 `avatar.rounded`的值来设置头像是否圆角化。

- `true` → 头像为圆的。
- **`false`** → 头像为方的。

#### rotated 鼠标悬停旋转

通过改变 `avatar.rotated`值来设置鼠标悬停是否旋转头像。

- `true` → 鼠标悬停旋转头像。
- **`false`** → 鼠标悬停不旋转头像。

### 配置 网站作者昵称

编辑 **站点配置文件**， 设置 `author` 为您的昵称。

**hexo/\_config.yml**

```yaml
# Siteauthor:
```

### 站点描述

编辑 **站点配置文件**， 设置 `description` 字段为您的站点描述。站点描述可以是您喜欢的一句签名。

**hexo/\_config.yml**

```yaml
# Sitedescription:
```

接下来我们开始 [配置部署](https://theme-next.org/docs/getting-started/deployment)。

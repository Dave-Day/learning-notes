---
title: Hexo NexT 06 - NexT 主题配置 - Footer 页脚
date: 2018-11-15 18:04:57
categories: Hexo
---

<!-- more -->

## Hexo NexT 06 - NexT 主题配置 - Footer

> 原文地址：<https://theme-next.org/docs/theme-settings/footer>
>
> **网站页脚设置**

## 站点建立时间

默认情况下，`NexT`在页脚显示当前年份，如 `© 2018` 。 您可以将其配置为显示时间间隔，例如`© 2015 - 2018`。 编辑 **主题配置文件**中的 `since`字段部分。

```yaml
footer:
  # Specify the date when the site was setup. If not defined, current year will be used.
  since: 2018
```

## 网站页脚图标

默认情况下，`NexT`会在页脚显示黑色用户图标，而不显示年份和版权信息之间的动画。您可以通过编辑**主题配置文件**中的 `icon` 字段的值来配置它。

### name 页脚图标名称

页脚图标名称 可以在网站 [Font Awesome](https://fontawesome.com/) 找到。建议 `heart` 。

### animated 页脚图标动画

通过修改 `icon.animated` 的值来设置是否加载页脚图标的动画。

- `true` → 加载页脚图标的动画。

- **`false`** → 不加载页脚图标的动画。

### color 页脚图标颜色

通过修改`icon.color`的值设置页脚图标的颜色。请使用十六进制代码， `heart` 图标建议使用红色（`#ff0000`）。

```yaml
name: heart
    # If you want to animate the icon, set it to true.
    animated: true
    # Change the color of icon, using Hex Code.
    color: "#d43f57"
```

## 网站版权名称

默认情况下，`NexT`显示来自**站点配置文件**的作者 `author` 的名称。您可以通过编辑**主题配置文件**中的 `copyright` 字段的值来配置它。

```yaml
# If not defined, `author` from Hexo `_config.yml` will be used.
copyright:
```

## 网站平台信息

默认情况下，`NexT`显示`Hexo`和 `Theme & scheme` 信息，例如 `Powered by Hexo v3.7.1 | Theme — NexT.Muse v6.3.0` 。您可以通过在**主题配置文件**的`powered`和`theme`字段的值来配置它。

### powered Hexo 信息

#### enable Hexo 平台信息

- **`true`** → 显示 `Powered by Hexo` 信息。
- `false` → 不显示 `Powered by Hexo` 信息。

#### version Hexo 版本

- **`true`** → 显示 Hexo 版本信息。
- `false` → 不显示 Hexo 版本信息。

```yaml
powered:
  # Hexo link (Powered by Hexo).
  enable: true
  # Version info of Hexo after Hexo link (vX.X.X).
  version: true
```

### theme 主题信息

#### enable 主题风格信息

- **`true`** → 显示 `Theme & Scheme` 信息。
- `false` → 不显示 `Theme & Scheme` 信息。

#### version 主题风格版本

- **`true`** → 显示 主题风格 版本信息。
- `false` → 不显示 主题风格 版本信息。

```yaml
theme:
  # Theme & scheme info link (Theme - NexT.scheme).
  enable: true
  # Version info of NexT after scheme info (vX.X.X).
  version: true
```

## 站点备案信息

备案信息是为中国用户提供的。默认情况下`NexT`不会显示`beian`的信息。您可以通过编辑**主题配置文件**中的`beian`字段的值来配置它。

```yaml
beian:
  enable: true
  icp: 京ICP备 1234567890号-1
  # The digit in the num of gongan beian.
  gongan_id: 1234567890
  # The full num of gongan beian.
  gongan_num: 京公网安备 1234567890号
  # The icon for gongan beian. See: http://www.beian.gov.cn/portal/download
  gongan_icon_url: /uploads/beian.png
```

## `footer` 完整配置文件

```yaml
footer:
  # Specify the date when the site was setup. If not defined, current year will be used.
  since: 2018

  # Icon between year and copyright info.
  icon:
    # Icon name in Font Awesome. See: https://fontawesome.com/v4.7.0/icons/
    # `heart` is recommended with animation in red (#ff0000).
    name: heart
    # If you want to animate the icon, set it to true.
    animated: true
    # Change the color of icon, using Hex Code.
    color: "#d43f57"

  # If not defined, `author` from Hexo `_config.yml` will be used.
  copyright:

  powered:
    # Hexo link (Powered by Hexo).
    enable: true
    # Version info of Hexo after Hexo link (vX.X.X).
    version: true

  theme:
    # Theme & scheme info link (Theme - NexT.scheme).
    enable: true
    # Version info of NexT after scheme info (vX.X.X).
    version: true

  # Beian ICP and gongan information for Chinese users. See: http://www.beian.miit.gov.cn, http://www.beian.gov.cn
  beian:
    enable: true
    icp: 京ICP备 1234567890号-1
    # The digit in the num of gongan beian.
    gongan_id: 1234567890
    # The full num of gongan beian.
    gongan_num: 京公网安备 1234567890号
    # The icon for gongan beian. See: http://www.beian.gov.cn/portal/download
    gongan_icon_url: /uploads/beian.png
```

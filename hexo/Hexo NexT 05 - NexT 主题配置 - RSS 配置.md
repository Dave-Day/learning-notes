---
title: Hexo NexT 05 - NexT 主题配置 - RSS 配置
date: 2018-11-14 17:28:41
categories: Hexo
---

<!-- more -->

## Hexo NexT 05 - NexT 主题配置 - RSS

`NexT` 中 `RSS` 有三个设置选项，满足特定的使用场景。 更改 **主题配置文件**，设定 `rss` 字段的值：

- `false`：禁用 `RSS`，不在页面上显示 RSS 连接。
- 留空：使用 `Hexo` 生成的 `Feed` 链接。 您可以需要先安装 [hexo-generator-feed](https://github.com/hexojs/hexo-generator-feed) 插件。
- 具体的链接地址：适用于已经烧制过 `Feed` 的情形。

## hexo-generator-feed

> Feed generator for Hexo. <http://hexo.io>
>
> <https://github.com/hexojs/hexo-generator-feed>

### 安装

`Hexo` 站点根目录运行：

```bash
$ npm install hexo-generator-feed --save
```

- Hexo 3: 1.x
- Hexo 2: 0.x

### 使用

在文章的前面，您可以选择添加描述、简介或摘录设置来为文章撰写摘要。否则，摘要将默认为摘录或文章的前 140 个字符。

您可以在**站点配置文件**配置这个插件。

```yaml
feed:
  # Generate atom feed
  type: atom

  # Generate both atom and rss2 feeds
  type:
    - atom
    - rss2
  path:
    - atom.xml
    - rss2.xml
  limit: 20
  hub:
  content:
  content_limit: 140
  content_limit_delim: ' '
  order_by: -date
  icon: icon.png
  autodiscovery: true
```

- **type** - Feed type. `atom` or `rss2`. Specify `['atom', 'rss2']` to output both types. (Default: `atom`)
- **path** - Feed path. When both types are specified, path must follow the order of type value. (Default: atom.xml/rss2.xml)
- **limit** - Maximum number of posts in the feed (Use `0` or `false` to show all posts)
- **hub** - URL of the PubSubHubbub hubs (Leave it empty if you don't use it)
- **content** - (optional) set to 'true' to include the contents of the entire post in the feed.
- **content_limit** - (optional) Default length of post content used in summary. Only used, if **content** setting is false and no custom post description present.
- **content_limit_delim** - (optional) If **content_limit** is used to shorten post contents, only cut at the last occurrence of this delimiter before reaching the character limit. Not used by default.
- **order_by** - Feed order-by. (Default: -date)
- **icon** - (optional) Custom feed icon. Defaults to a gravatar of email specified in the main config.
- **autodiscovery** - Add feed [autodiscovery](http://www.rssboard.org/rss-autodiscovery). (Default: `true` )
  - Many themes already offer this feature, so you may also need to adjust the theme's config if you wish to disable it.

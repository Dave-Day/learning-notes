---
title: 浏览器沉浸式阅读扩展 - 简悦 (SimpRead)
url: ijllcpnolfcooahcekpamkbidhejabll
---

# 浏览器沉浸式阅读扩展 - 简悦 (SimpRead)

[简悦](http://ksria.com/simpread/) 是一个浏览器扩展，主要做的是：给你提供 **无干扰的沉浸式阅读体验。** 这款基于浏览器的插件可以实现自动提取标题、描述、正文、媒体 （ 图片 / 视频 ） 等资源；生成符合中文阅读习惯的页面，具备零干扰、沉浸式特点，适合深入阅读。

[![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=Kenshin&repo=simpread&show_owner=true&locale&hide_border)](https://github.com/Kenshin/simpread)

软件官网：[http://ksria.com/simpread](http://ksria.com/simpread)

## 软件功能

- [聚焦模式](http://ksria.com/simpread/docs/#/聚焦模式)
  不改变当前页面的结构，仅仅高亮需要阅读的部分，不分散用户的注意力；适合 `临时阅读` 或者 `未适配阅读模式` 的网站

- [阅读模式](http://ksria.com/simpread/docs/#/阅读模式)
  简悦 `原创` 功能，逐一适配了 [数百种类型](https://simpread.ksria.cn/sites/) 的网站，自动提取 `标题` `描述` `正文` `媒体资源（ 图片/ 视频 ）` 等，生成 `符合中文阅读` 的页面

  - 支持 [自动生成目录](http://ksria.com/simpread/docs/#/目录)
  - 支持 [论坛类页面及分页](http://ksria.com/simpread/docs/#/论坛类页面及分页) 如：知乎 · 百度贴吧等
  - 支持 [代码段的高亮](https://github.com/Kenshin/simpread/issues/500)，包含了大部分常见的网站
  - 支持 [TXT 阅读器](http://ksria.com/simpread/docs/#/TXT-阅读器) · 支持 [LaTeX 解析](http://ksria.com/simpread/docs/#/LaTeX-阅读器) · [Markdown 阅读器](http://ksria.com/simpread/docs/#/Markdown-阅读器)
  - 更符合 `中文阅读` 习惯的设置，包括：`字间距` `行间距` 等 以及 `自定义 CSS` ，详细请看 [自定义样式](http://ksria.com/simpread/docs/#/自定义样式)

- 主动适配
  通过简单的一个步骤，就可以让 `非适配页面` 支持阅读模式，详细请看 [主动适配](http://ksria.com/simpread/docs/#/主动适配阅读模式) 以及 [操作](http://ksria.com/simpread/welcome/version_1.0.5.html#mate-read-mode)

- 智能适配

  全新的 `词法分析引擎`，更智能、更精准的提取正文，辅以精准适配，任意网页均「不在话下」，不仅能自动识别出 Wordpress · Hexo · Ghost · Discuz 等博客 / 论坛的页面，甚至于只要是结构良好的页面，（无需适配）自动生成阅读模式，详细请看 [词法分析引擎](http://ksria.com/simpread/docs/#/词法分析引擎)

- 智能感知

  当生成的阅读模式出现问题时，简悦会自动重新获取正文，详细说明请看 [智能感知](http://ksria.com/simpread/docs/#/智能感知)

- 手动框选适配
  针对 `未适配` 或 `智能识别` 失败的情况，简悦可以使用手动框选的方式，生成阅读模式，详细请看 [手动框选](http://ksria.com/simpread/docs/#/手动框选)

- 站点适配源
  包括：`官方适配源` `第三方适配源` `站点集市适配源` `自定义适配源`，详细请看 [站点适配源](http://ksria.com/simpread/docs/#/站点适配源)

- 站点编辑器
  页面任意元素，均可隐藏，`可编程，定制化`，详细请看 [站点编辑器](http://ksria.com/simpread/docs/#/站点编辑器)

- 站点管理器
  可管理全部的适配站点，详细请看 [站点管理器](http://ksria.com/simpread/docs/#/站点管理器)

- 站点集市
  上传并共享自己的适配站点，一键分享临时阅读模式，适配失败的站一键提交，详细请看 [站点集市](https://simpread.ksria.cn/sites)

- 插件系统
  现在开始可以使用 JavaScript 编写基于 `简悦` 的插件了，更上线了 [插件中心](https://simpread.ksria.cn/plugins/) ，如何编写插件请看 → [说明文档](http://ksria.com/simpread/docs/#/插件系统)

- 多种主题
  `白练、白磁、卯之花色、丁子色、娟鼠、月白、百合、紺鼠、黒鸢` 等

- 丰富的导出功能

  - 导出 [Markdown](https://github.com/Kenshin/simpread#感谢) · `HTML` · `PNG` · `PDF` · [epub](http://ksria.com/simpread/docs/#/发送到-Epub)
  - 发送阅读模式优化后的页面到 `Kindle`，详细配置 [请看这里](http://ksria.com/simpread/docs/#/发送到-Kindle)
  - 导出到 `Pocket` `Linnk` `Instapaper` 的功能，包括：`当前页面的链接` `稍后读`
  - 导出到生产力工具，包括：`坚果云` `语雀` `有道云笔记` `为知笔记` `Dropbox` `Notion` `Onenote` `Google Drive` `印象笔记 / Evernote`，详细请看 [导出到生产力](http://ksria.com/simpread/docs/#/导出到生产力工具)

- 同步 · 上传/下载 配置 · 同步适配列表 · [快捷键支持](http://ksria.com/simpread/docs/#/快捷键) 等；

- 高级定制，包括：`右键菜单` `控制栏可隐藏` `阅读进度可隐藏` `自动进入阅读模式` [白名单](http://ksria.com/simpread/docs/#/FAQ?id=白名单) 以及 [排除列表](http://ksria.com/simpread/docs/#/FAQ?id=排除列表) 等

- 稍后读

## 相关链接

- [更新日志](http://ksria.com/simpread/changelog.html)
- [帮助中心](http://ksria.com/simpread/docs/#)
- [新手入门](http://ksria.com/simpread/guide)
- [常见问题](http://ksria.com/simpread/docs/#/FAQ)

## 软件下载

- [Chrome 应用商店](https://chrome.google.com/webstore/detail/%E7%AE%80%E6%82%A6-simpread/ijllcpnolfcooahcekpamkbidhejabll) 或者 [离线下载](http://ksria.com/simpread/crx/1.1.4/simpread.crx)
- [Firefox 扩展中心](https://addons.mozilla.org/zh-CN/firefox/addon/simpread)
- [支持 UserScript 的浏览器](https://greasyfork.org/zh-CN/scripts/39998) 如：Apple Safari · Microsoft Edge · Opera · Dolphin 详细 [请看这里](https://github.com/Kenshin/simpread-little)
- [iPhone / iPad 版](https://xteko.com/redir?url=http://sr.ksria.cn/jsbox/simpread-1.0.0.box?201805251238&name=%E7%AE%80%E6%82%A6) 详细 [请看这里](http://ksria.com/simpread/docs/#/JSBox)
- [Android 版](http://ksria.com/simpread/docs/#/Android) 详细 [请看这里](http://ksria.com/simpread/docs/#/Android)

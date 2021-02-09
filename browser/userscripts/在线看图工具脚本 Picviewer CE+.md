---
title: 在线看图工具脚本 Picviewer CE+
url: 24204
---

# 在线看图工具脚本 Picviewer CE+

基于[ywzhaiqi](https://greasyfork.org/users/145) 的 [picviewer CE](https://greasyfork.org/scripts/5199) 2015.7.10.0 NLF 的围观图修改版，增加高清原图查找显示（在线看图工具，支持图片翻转、旋转、缩放、弹出大图、批量保存、查找原图、聚合所有分页大图、图片在线编辑）。

[![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=hoothin&repo=UserScripts&show_owner=true&locale&hide_border&theme=vue-dark)](https://github.com/hoothin/UserScripts)

## 脚本特性

- 查看原始图片：旋转、放大、缩小、水平翻转、垂直翻转；
- 查看当前：悬浮在网页上单独浏览，可拖拽移动；
- 放大镜
- 批量保存
- 查找原图
- 聚合所有分页大图
- 图片在线编辑

## 脚本说明

- 修改內容
  - 修复部分情景下工具栏以及图框错位导致无法点击的问题
  - 修复 _chrome_ 上直接修改 _innerHTML_ 造成引用丢失的问题
  - 修复消息传递后原页面和 _frame_ 接收两次导致 _frame_ 与父页显示俩框的问题
  - 滚动条缓动改为 sin
  - 适配国产奇葩浏览器，如傲游搜狗等
  - 修复新浪微博相册大图
  - 修复淘宝大图规则
  - 修正父级重复链接显示原图按钮的问题
  - _iframe_ 内进入图库加载图片范围由 _iframe_ 内改为整页（不能突破同源限制）
  - 修复按键响应（`loadPrefs()`前`floatBar.keys.enable`始终为 _false_）
  - 修复自动重载（汤不热页面高度可能远大于 99999，且自动重载图片可能不限于本页）

---

#

- 新增內容
  - 批量下载库中筛选显示的图片
  - 图片导出页面点击选择复制
  - 图片导出页面按住 _Ctrl_ 展示完整大图
  - 添加尺寸筛选滑条
  - r 键旋转
  - 查找原图：在"图集"按钮后与图片展示框上添加"查找原图"按钮，在 _tineye_ 查找尺寸最大的 3 张图并显示首张成功加载的，如果没有找到，就用 _google_ 识图（you need fanqiang），还找不到就去百度图片找，可在设置里配置首选搜图引擎
  - 读取下一页图片：在图库上方工具栏里点击"加载更多"即可读取下一页图片，[案例](https://www.meitulu.com/item/11952.html)，可设置是否读取全部分页的图片
  - 增加 _nvshens、aisimeinv、24tupian_ 等站规则
  - 增加图库全局快捷键，按住 _Ctrl_ 加上图库快捷键（默认 g）即可
  - 增加自动打开图库选项，设置里输入相应网址正则则访问对应网站时会自动打开图库
  - 在图库命令菜单中增加下载按钮
  - 按住 _alt_ 不显示浮动工具栏
  - 增加对被 _div_ 覆盖的图片的支持，例如 [_Dribbble_](https://dribbble.com/)
  - 增加对元素背景的支持，例如 [_Acfun_](http://www.acfun.cn/u/1121228.aspx)，浮动栏显示设置同"缩放过的图片"
  - 增加图库大图滚动到底进行图片切换的功能，其中返回上一张从长图底部开始，可设置启用与否
  - 浮动工具栏显示位置的正上方与正下方选项
  - 图片导出页面增加瀑布流排序、列表排序并居中与原图平铺功能
  - 图片导出页面默认排序设置功能
  - 浮动工具栏图标排序设置
  - 图库内图片张数显示
  - 图库内小图筛选设置
  - 兼容 _wordpress_ 通配规则，例： _www.acg.tf_
  - 兼容中转缩略图跳转规则，例： _acg18.us_
  - _dribbble_ 与 _deviantart_ 大图规则
  - 百度贴吧用户头像高清大图规则
  - 百度百科原图规则
  - _instagram_ 大图规则
  - _pixiv_ 大图规则
  - _tumblr_ 大图规则
  - 微博外链图片大图规则
  - 天猫以及 _alicdn_ 大图规则
  - 京东大图规则
  - 一号店大图规则
  - _itunes_ 大图规则
  - 豆瓣图片大图规则
  - _steam_ 大图规则
  - 半次元大图规则
  - 知乎大图规则
  - 汽车之家大图规则
  - 易车大图规则
  - 爱卡大图规则
  - 太平洋汽车大图规则
  - _gravatar_ 头像大图规则
  - 基于 1024 图床网站的大图规则

## 脚本地址

- [Picviewer CE+](https://greasyfork.org/zh-CN/scripts/24204-picviewer-ce)

## 使用方法

### 安装用户脚本管理器

要使用用户脚本，您首先需要安装一个用户脚本管理器。根据您使用的浏览器不同，可用的用户脚本管理器也有所不同。

- Chrome：[Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) 或 [Violent monkey](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag)
- Firefox：[Greasemonkey](https://addons.mozilla.org/firefox/addon/greasemonkey/)、[Tampermonkey](https://addons.mozilla.org/firefox/addon/tampermonkey/) 或 [Violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/)
- Safari：[Tampermonkey](http://tampermonkey.net/?browser=safari)
- Microsoft Edge：[Tampermonkey](https://www.microsoft.com/store/p/tampermonkey/9nblggh5162s)
- Opera：[Tampermonkey](https://addons.opera.com/extensions/details/tampermonkey-beta/) 或 [Violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/)
- Maxthon：[Violentmonkey](http://extension.maxthon.com/detail/index.php?view_id=1680)
- Dolphin：[Tampermonkey](https://play.google.com/store/apps/details?id=net.tampermonkey.dolphin)
- UC：[Tampermonkey](https://play.google.com/store/apps/details?id=net.tampermonkey.uc)
- Qupzilla：（不需要额外软件）
- AdGuard：（不需要额外软件）

### 安装用户脚本

在您找到想要的用户脚本后，点击用户脚本页面上绿色的安装按钮，您的用户脚本管理器将向您确认是否安装。

### 使用用户脚本

现在您可以访问这个用户脚本所针对的网站，脚本应该已经自动启动和生效。在试用一段时间之后，您可以回到用户脚本发表的页面，给用户脚本的作者留下反馈。

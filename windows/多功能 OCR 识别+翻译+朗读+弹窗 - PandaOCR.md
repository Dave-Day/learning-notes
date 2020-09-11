---
title: 多功能 OCR 识别+翻译+朗读+弹窗 - PandaOCR
date: 2019-06-30 17:04:58
categories: Program
---

<!-- more -->

<!-- TOC -->

- [多功能 OCR 识别+翻译+朗读+弹窗 - PandaOCR](#多功能-ocr-识别翻译朗读弹窗---pandaocr)
  - [软件介绍](#软件介绍)
  - [使用技巧](#使用技巧)
  - [软件说明](#软件说明)
  - [使用教程](#使用教程)
  - [API 版接口申请 (不需申请也能用)](#api-版接口申请-不需申请也能用)
  - [更新日志](#更新日志)
    - [[PandaOCR.v2.43](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.43)](#pandaocrv243httpsgithubcommiaomiaosoftpandaocrreleasestag243)
    - [[PandaOCR.v2.42](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.42)](#pandaocrv242httpsgithubcommiaomiaosoftpandaocrreleasestag242)
    - [[PandaOCR.v2.41](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.41)](#pandaocrv241httpsgithubcommiaomiaosoftpandaocrreleasestag241)
    - [[PandaOCR.v2.40](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.40)](#pandaocrv240httpsgithubcommiaomiaosoftpandaocrreleasestag240)
    - [[PandaOCR.v2.39](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.39)](#pandaocrv239httpsgithubcommiaomiaosoftpandaocrreleasestag239)
    - [[PandaOCR.v2.38](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.38)](#pandaocrv238httpsgithubcommiaomiaosoftpandaocrreleasestag238)
    - [[PandaOCR.v2.37](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.37)](#pandaocrv237httpsgithubcommiaomiaosoftpandaocrreleasestag237)
    - [[PandaOCR.v2.36](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.36)](#pandaocrv236httpsgithubcommiaomiaosoftpandaocrreleasestag236)
    - [[PandaOCR.v2.35](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.35)](#pandaocrv235httpsgithubcommiaomiaosoftpandaocrreleasestag235)
    - [[PandaOCR.v2.34](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.34)](#pandaocrv234httpsgithubcommiaomiaosoftpandaocrreleasestag234)
    - [[PandaOCR.v2.33](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.33)](#pandaocrv233httpsgithubcommiaomiaosoftpandaocrreleasestag233)
    - [[PandaOCR.v2.32](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.32)](#pandaocrv232httpsgithubcommiaomiaosoftpandaocrreleasestag232)
    - [[PandaOCR.v2.31](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.31)](#pandaocrv231httpsgithubcommiaomiaosoftpandaocrreleasestag231)
    - [[PandaOCR.v2.30](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.3)](#pandaocrv230httpsgithubcommiaomiaosoftpandaocrreleasestag23)
  - [下载地址](#下载地址)
    - [问题反馈](#问题反馈)
    - [已知问题](#已知问题)

<!-- /TOC -->

<a id="markdown-多功能-ocr-识别翻译朗读弹窗---pandaocr" name="多功能-ocr-识别翻译朗读弹窗---pandaocr"></a>

# 多功能 OCR 识别+翻译+朗读+弹窗 - PandaOCR

![PandaOCR](https://pic.ryanjie.cn/2019/06/PandaOCR.jpg)

[github author="miaomiaosoft" project="PandaOCR"][/github]

<a id="markdown-软件介绍" name="软件介绍"></a>

## 软件介绍

- 支持识别引擎：搜狗 OCR/API+腾讯 OCR/API+百度 OCR/API+有道 OCR/API+京东 OCR
- 支持翻译引擎：搜狗翻译/API+腾讯翻译/API+百度翻译/API+有道翻译/API+谷歌翻译+词霸翻译+必应翻译+沪江翻译+剑桥翻译+奇虎翻译+海词翻译+彩云翻译
- 支持朗读引擎：搜狗朗读+腾讯朗读+百度朗读+必应朗读+讯飞朗读+谷歌朗读+京东朗读
- 支持快捷键和屏幕边角触发截图识别功能，方便快速
- 支持截取识别固定区域，例如可帮助翻译英文游戏/软件中的单词或队友聊天记录 [固定截图识别使用参考](https://www.bilibili.com/video/av56168758)
- 支持右侧小弹窗显示信息，快速查看识别/翻译内容
- 支持智能合并修正识别/翻译文本，让排版更合理
- 支持设置最多十条固定截图规则，让一键识别更方便快捷
- 支持监听图像和文本复制操作，快速识别图像文本或翻译复制文本
- 支持简单的窗口汉化功能，帮助翻译纯英文类软件界面文字
- 还有很多奇怪的没有列在程序界面上的功能，可以编辑程序目录下的 CONFIG. INI 文件试试

<a id="markdown-使用技巧" name="使用技巧"></a>

## 使用技巧

- 将鼠标移到各功能组件或按钮上会显示简单的悬停提示帮助你理解程序操作。
- 配置文件内已添加各功能注释说明，如果想要实现某种功能但在程序界面上没找到相关设置，可以先翻一翻配置文件或许它已经在那里等着你（程序目录下 CONFIG.ini 即是配置文件）。
- 如果你有两块屏幕，请勾选“高级截图方式”以解决无法截取第二块屏的问题。
- 如果你是高分屏或修改了系统 DPI 缩放，可能出现截图不全或弹窗位置偏移的问题，此时你需要在此程序文件的属性中取消系统 DPI 设置。
- 程序界面上存在的设置多数是可以实时生效的不需要频繁点击保存按钮，比如设置语言、更换引擎此类。
- 有时手工更改了配置文件又不想重启软件可以试试右键点击界面左上角图标重载配置，不要点左键。
- 从演示版引擎临时更改为 API 版引擎可以右键点击引擎选择组合框。
- 鼠标党如果觉得按快捷键识别麻烦可以把鼠标移到屏幕左上角来触发识别，默认配置已启用，也可以编辑配置文件关闭或改为其他位置。
- 在截图时按住 CTRL 键可以临时取消识别，只截图并复制至剪贴板。
- 在截图时按住 ALT 键可以临时取消修正文本，当识别图像的文本中不包含任何标点符号时建议这样使用。
- 在文本区输入文本后按 CTRL+回车键会直接翻译，不需要再用鼠标点翻译按钮。
- 在文本区输入文本后按 ALT+回车键会直接朗读。
- 将图片直接拖入至程序界面上会自动开始识别。
- 在识别或是朗读进行中如果想中止任务可以双击界面右上方“线程”字样处，或按住空格键的同时点击托盘图标。
- 鼠标右键点击“保存设置”按钮可缩小或展开程序界面。
- 如果觉得文本区域过小，可以双击文本区使用大窗口浏览或简单编辑。
- 有些不太用的上的功能建议关闭以减少识别等待时间，比如朗读文本。
- 在启用了监听复制功能时临时不想执行识别或翻译可以在复制的同时按住空格键。

<a id="markdown-软件说明" name="软件说明"></a>

## 软件说明

- 程序使用压缩壳减小文件体积，如有误报请自行解决无恶意代码，程序访问的所有服务器都是上面这些引擎需要调用的，可自行验证
- 程序的开发与发布均在受保护的环境中完成，如果使用过程中，您系统中某种"安全"软件称「发现木马」，那么此种情形将考验您的判断力
- 已知在高分辨率/高分屏下截图功能异常 [尝试解决方法](https://github.com/miaomiaosoft/PandaOCR/issues/17)
- 如需使用自己申请的 ID 和 KEY，用文本编辑器打开程序目录下的 CONFIG.ini 文件，在[数据配置]项，将各版本后面数值设为 1（0 为演示版），并修改下面相应的 ID 和 KEY
- 各引擎精准度推荐：OCR 推荐搜狗，翻译推荐搜狗或腾讯，朗读推荐搜狗或腾讯，讯飞只适合短句也不太稳定
- 右击<保存设置>按钮可以收缩/展开界面，弹窗上的小按钮单击隐藏，右击弹出菜单
- 开源？好的，马上就开！咕咕咕~

<a id="markdown-使用教程" name="使用教程"></a>

## 使用教程

- [游戏机翻](https://www.bilibili.com/video/BV1Vt4y1U7Es/)
- [基础操作](https://www.bilibili.com/video/BV1UV411d7zh)

<a id="markdown-api-版接口申请-不需申请也能用" name="api-版接口申请-不需申请也能用"></a>

## API 版接口申请 (不需申请也能用)

- 搜狗 OCR/翻译： `http://deepi.sogou.com`
- 腾讯 OCR： `https://ai.qq.com` 腾讯云翻译： `https://cloud.tencent.com` 腾讯翻译君： `https://ai.qq.com`
- 百度 OCR： `https://cloud.baidu.com` 百度翻译： `http://api.fanyi.baidu.com`
- 有道 OCR/翻译： `http://ai.youdao.com`

<a id="markdown-更新日志" name="更新日志"></a>

## 更新日志

[admonition title="更新日志" color="indigo"]

<a id="markdown-pandaocrv243httpsgithubcommiaomiaosoftpandaocrreleasestag243" name="pandaocrv243httpsgithubcommiaomiaosoftpandaocrreleasestag243"></a>

### [PandaOCR.v2.43](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.43)

- 主要优化多线程，旧版滥用多线程可能会导致一些卡死问题
- 修复其他 BUG 和增加一些功能和配置项，具体懒的写了

<a id="markdown-pandaocrv242httpsgithubcommiaomiaosoftpandaocrreleasestag242" name="pandaocrv242httpsgithubcommiaomiaosoftpandaocrreleasestag242"></a>

### [PandaOCR.v2.42](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.42)

- 增加 网易 OCR 演示版
- 增加 小牛翻译演示版
- 增加 更多知声朗读引擎，现在总共有近 30 个
- 增加 翻译来源语言支持 AUTO+方式，使用百度或谷歌在线检测文本语言
- 增加 朗读语言支持 AUTO+方式，使用百度或谷歌在线检测文本语言
- 增加 首次启动时显示提示信息
- 增加 五种加载动画，共十种
- 增加 弹窗关闭方式 配置项，如果程序偶尔卡死请尝试改为 0 [默认 1=隐藏 | 0=销毁]
- 增加 截图隐藏窗口 配置项，如果截图时主窗口处于显示状态将被暂时隐藏 [默认 1=启用]
- 增加 其他一些不太常用的配置项
- 优化 自制并替换了非高级截图时的十字形鼠标指针样式
- 优化 调整了截图时的提示音
- 优化 一些引擎的失效重试逻辑
- 优化 在截图中按住空格键将临时不修正/排版识别文本改为按住 ALT 键
- 修复 搜狗翻译演示版
- 修复 一些您可能注意不到的小 BUG

<a id="markdown-pandaocrv241httpsgithubcommiaomiaosoftpandaocrreleasestag241" name="pandaocrv241httpsgithubcommiaomiaosoftpandaocrreleasestag241"></a>

### [PandaOCR.v2.41](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.41)

- 增加 编辑框右键支持手动朗读和保存朗读音频文件
- 增加 智能朗读+自定 [1=依次 2=随机 | 自定朗读编号请手工编辑配置文件 "智能朗读自定排序"，以|号分隔]
- 增加 华为 OCR 演示版
- 增加 为某些 OCR 或翻译引擎增加备用接口 [备用返回的文本最后带"_"字符]
- 增加 截图时按住某些按键将实现不同功能 [CTRL=不识别只截图并复制到剪贴板 | 空格=识别后不修正文本]
- 增加 鼠标单击任务栏图标时按住某些按键将实现不同功能 [CTRL=复制识别文本 | ALT=复制翻译文本 | 空格=强行结束任务]
- 增加 为主程序图片区和文本区增加一些快捷操作方式，具体参见鼠标悬停提示
- 增加 右键点击引擎选择组合框将能临时更改引擎版本 [只限带*号的引擎]
- 修复 搜狗翻译演示版
- 调整 增加了程序界面宽度

<a id="markdown-pandaocrv240httpsgithubcommiaomiaosoftpandaocrreleasestag240" name="pandaocrv240httpsgithubcommiaomiaosoftpandaocrreleasestag240"></a>

### [PandaOCR.v2.40](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.40)

- 增加 智能识别+ [依次使用所有的演示版 OCR 引擎进行识别，直到识别成功]
- 增加 智能翻译+ [依次使用所有的演示版翻译引擎进行翻译，直到翻译成功]
- 增加 智能朗读+依次 [依次使用所有的朗读引擎进行朗读，直到朗读成功 | 依次 1=只用边下边播 | 依次 2=优先边下边播]
- 增加 智能朗读+随机 [随机使用所有的朗读引擎进行朗读，直到朗读成功 | 随机 1=只用边下边播 | 随机 2=优先边下边播]
- 增加 朗读方式 配置项 [0=先下再播 | 1=边下边播 | 2=优先尝试边下边播，如不可用再使用先下再播方式]
- 增加 搜狗朗读 2 台语女声
- 增加 有道翻译 演示版 2
- 增加 朗读语言 配置项 [指定文本朗读语言：auto | zh | en | ja | 并不是所有引擎都支持，请逐个尝试，默认 auto]
- 增加 自动保存音频 配置项 [注意：只支持 朗读方式=0 下可用，并且不支持智能朗读，设置路径即启用，默认 0=禁用]
- 增加 新特性：截图识别过程中按住空格键将临时放弃修正文本
- 增加 现在可以在程序界面直接更改识别语言和朗读语言

<a id="markdown-pandaocrv239httpsgithubcommiaomiaosoftpandaocrreleasestag239" name="pandaocrv239httpsgithubcommiaomiaosoftpandaocrreleasestag239"></a>

### [PandaOCR.v2.39](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.39)

- 修复 腾讯朗读 1 [因腾讯增加了验证，所以此引擎不再支持边下边播方式]
- 修复 搜狗翻译 演示版
- 增加 新窗查看 编辑框右键菜单 [使用更大和可调的新窗口显示识别和翻译文本]

<a id="markdown-pandaocrv238httpsgithubcommiaomiaosoftpandaocrreleasestag238" name="pandaocrv238httpsgithubcommiaomiaosoftpandaocrreleasestag238"></a>

### [PandaOCR.v2.38](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.38)

- 修复 固定截图热键 在 WIN10 系统上的识别错误
- 增加 检查版本 配置项，如不想每次运行时都检查是否有新版可以自行关闭，1=启用，0=禁用，默认启用

<a id="markdown-pandaocrv237httpsgithubcommiaomiaosoftpandaocrreleasestag237" name="pandaocrv237httpsgithubcommiaomiaosoftpandaocrreleasestag237"></a>

### [PandaOCR.v2.37](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.37)

- 增加 SpaceOCR [默认识别中文，需要识别其他语言请在配置中更改：识别语言]
- 增加 图像转换 配置项 [1=慢速，高质量 2=快速，低质量 | 如想提升识别质量请使用 1，默认 2]
- 变更 将 复制提示 配置项改为 提示方式 [支持提示音、托盘、弹窗等方式，0=禁用提示，包括启动和截图提示音效]
- 修复 腾讯 OCR 演示版 [并增加一个演示版，新增的演示版可能需要登陆，程序界面会提供登陆按钮，具体参考配置说明]
- 修复 必应翻译
- 移除 必应朗读

<a id="markdown-pandaocrv236httpsgithubcommiaomiaosoftpandaocrreleasestag236" name="pandaocrv236httpsgithubcommiaomiaosoftpandaocrreleasestag236"></a>

### [PandaOCR.v2.36](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.36)

- 增加 识别和翻译文本区右键菜单功能 [复制/翻译/朗读/搜索/符号替换]
- 增加 边角触发禁用 配置项，当焦点停留在设定的进程列表中时不启用边角触发截图，示例：GTA5. EXE|KFGame. EXE [用|分隔]，0=不启用
- 修复 腾讯朗读 1
- 修复 其他一些 BUG

<a id="markdown-pandaocrv235httpsgithubcommiaomiaosoftpandaocrreleasestag235" name="pandaocrv235httpsgithubcommiaomiaosoftpandaocrreleasestag235"></a>

### [PandaOCR.v2.35](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.35)

- 增加 显示统计数据 配置项 [启用后将在窗口上方显示一些信息，默认启用，0=关闭]
- 优化 将程序启动时的提示音量降至 50
- 修复 当用户网络不稳定时初始化引擎数据可能导致的正则报错

<a id="markdown-pandaocrv234httpsgithubcommiaomiaosoftpandaocrreleasestag234" name="pandaocrv234httpsgithubcommiaomiaosoftpandaocrreleasestag234"></a>

### [PandaOCR.v2.34](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.34)

- 修复 腾讯翻译多出空行
- 修复 谷歌翻译在启用行首空格时可能出现乱码
- 优化 为弹窗逐行显示增加空行
- 优化 截图热键 注册方式，现在支持组合键，如：CTRL+F 键
- 增加 识别语言 配置项，可指定 OCR 识别语言，目前只支持 API 版识别引擎 [腾讯暂不支持]

<a id="markdown-pandaocrv233httpsgithubcommiaomiaosoftpandaocrreleasestag233" name="pandaocrv233httpsgithubcommiaomiaosoftpandaocrreleasestag233"></a>

### [PandaOCR.v2.33](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.33)

- 增加 弹窗字体风格 配置项，可加粗或斜体显示文本
- 增加 定时重载数据 配置项，定时刷新统计和演示引擎 COOKIES，数值为分钟，默认 30 分钟，0=不启用
- 增加 自动保存文本 配置项，可将识别翻译文本保存到特定文本文件，0=不启用
- 增加 只读中/英文 朗读项，当启用自动翻译时，取识别和译文的中/英文数，哪边多读哪个
- 增加 只显中/英文 弹窗项，当启用自动翻译时，取识别和译文的中/英文数，哪边多显哪个
- 优化 行首空格 配置项，0=不启用| 1=启用 | 2=当选择智能合并时才启用
- 优化 自动复制和监听复制同时启用时的死循环问题
- 优化 减少可能的崩溃错误

<a id="markdown-pandaocrv232httpsgithubcommiaomiaosoftpandaocrreleasestag232" name="pandaocrv232httpsgithubcommiaomiaosoftpandaocrreleasestag232"></a>

### [PandaOCR.v2.32](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.32)

- 优化 尝试减少截图时屏幕闪烁
- 优化 启动时初始化时间过长
- 优化 某些功能运行逻辑
- 增加 弹窗背景功能，具体请查看配置说明
- 增加 智能合并 2 规则，效果比旧的好一点，但性能可能会慢一些，自行对比选择
- 增加 逐行对照显示弹窗内容
- 修复 部分 OCR 忽略换行的问题
- 修复 百度 OCR 演示版
- 修复 其他小 BUG

<a id="markdown-pandaocrv231httpsgithubcommiaomiaosoftpandaocrreleasestag231" name="pandaocrv231httpsgithubcommiaomiaosoftpandaocrreleasestag231"></a>

### [PandaOCR.v2.31](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.31)

- 增加 京东 OCR 演示版
- 增加 京东朗读 [音质优美，推荐]
- 增加 朗读方式 [0=先下载再播放，慢 | 1=边下载边播放，快，但不是全都支持 | 默认 0]
- 增加 符号替换 功能，当一段文本中多数为中文时将标点符号替换为全角，需要编辑配置文件启用
- 增加 进度动画 提示，共五种动画效果，默认启用，可以编辑配置文件更换或关闭
- 优化 只有当启用 智能合并 时 行首空格 才生效
- 优化 删除不再使用的模块
- 优化 程序执行逻辑

<a id="markdown-pandaocrv230httpsgithubcommiaomiaosoftpandaocrreleasestag23" name="pandaocrv230httpsgithubcommiaomiaosoftpandaocrreleasestag23"></a>

### [PandaOCR.v2.30](https://github.com/miaomiaosoft/PandaOCR/releases/tag/2.3)

- 优化 高级截图方式，勾选后将调用微信截图模块 [也许能解决高分屏下截图异常的问题]
- 优化 减少程序界面边框，使之更简洁
- 增加 程序启动时初始化完成提示音
- 增加 有道 OCR 的 API 版 [测试可用]
- 增加 有道翻译的 API 版 [未测试可用性，因为没 KEY]
- 增加 搜狗 OCR 的 API 版 [共三版本，0=演示版，1=API 版，2=另一种演示版]
- 增加 腾讯翻译的 API 版 [共三版本，0=演示版，1=腾讯云翻译，2=腾讯 AI 翻译君]

PS：以上增加的各引擎如有错误请反馈，也许还需要您提供 KEY 给我测试

[/admonition]

<a id="markdown-下载地址" name="下载地址"></a>

## 下载地址

**因增加了配置项，从旧版升级前请先删除 CONFIG.ini 配置文件**

- [PandaOCR/releases](https://github.com/miaomiaosoft/PandaOCR/releases/latest)
- [百度网盘(提取码: `yxxn`)](https://pan.baidu.com/s/1UpEbyzC3vn6i9kNDQrjOwA#yxxn)

<a id="markdown-问题反馈" name="问题反馈"></a>

### 问题反馈

- [Github issues](https://github.com/miaomiaosoft/PandaOCR/issues)

<a id="markdown-已知问题" name="已知问题"></a>

### 已知问题

1. 英文或繁体系统下整个程序界面中文将可能会乱码
2. 韩文同样会乱码，即使 OCR 支持识别韩文也显示不了
3. 不支持高分屏或者系统 DPI 缩放，截图将不完整，弹窗按钮无法点击，除非您将本程序的属性设置为不使用系统 DPI
4. 只支持 WIN 系统，MAC 之类的不会有
5. 文本朗读建议在 500 字以内，太长的文本需要更长的下载等待时间影响体验，也不打算利用分割多段的方式支持长文本朗读
6. 不会增加表格或公式识别，我真的一点都用不到
7. 普通截图方式不支持多屏幕，可以试试勾选高级截图尝试解决

以上如有遇到或符合自己的情况就不用反馈或建议了

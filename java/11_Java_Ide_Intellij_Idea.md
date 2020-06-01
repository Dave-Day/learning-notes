---
title: Java 集成开发环境 - IntelliJ IDEA
---

<!-- TOC -->

- [IDEA 概述](#idea-概述)
  - [IDEA 与 Eclipse 对比](#idea-与-eclipse-对比)
  - [IDEA 简介](#idea-简介)
  - [IDEA 特性](#idea-特性)
    - [高度智能](#高度智能)
    - [安装即用](#安装即用)
    - [智能代码补全](#智能代码补全)
    - [框架针对性辅助](#框架针对性辅助)
    - [促进生产力](#促进生产力)
    - [开发者人体工程学](#开发者人体工程学)
    - [深化内隐的智能设计](#深化内隐的智能设计)
- [IDEA 下载安装](#idea-下载安装)
  - [IDEA 下载](#idea-下载)
  - [IDEA 安装](#idea-安装)
    - [Windows 环境](#windows-环境)
    - [Linux 环境](#linux-环境)
- [参考](#参考)

<!-- /TOC -->

<a id="markdown-idea-概述" name="idea-概述"></a>

## IDEA 概述

<a id="markdown-idea-与-eclipse-对比" name="idea-与-eclipse-对比"></a>

### IDEA 与 Eclipse 对比

> [为何 IntelliJ IDEA 比 Eclipse 更适合于专业 java 开发者](https://www.cnblogs.com/wangzhongqiu/p/6698880.html)

<a id="markdown-idea-简介" name="idea-简介"></a>

### IDEA 简介

> IntelliJ IDEA 是一种商业化销售的 Java 集成开发环境（Integrated Development Environment，IDE）工具软件，由 JetBrains 软件公司（前称为 IntelliJ）开发，提供 Apache 2.0 开放式授权的社区版本以及专有软件的商业版本，开发者可选择其所需来下载使用。
>
> 最初版于 2001 年 1 月时推出，当时是少数使用前阶代码浏览及代码重构的 Java 集成开发环境之一。
>
> 在 2010 年的 Infoworld 报告中，比较当时市面上的主流 Java 集成开发环境，包括：Eclipse、IntelliJ、NetBeans、JDeveloper，IntelliJ 获得该媒体实测中的最高评比。
>
> 2014 年 12 月，Google 宣布其旗下专用于发展 Android 操作系统的首版 Android Studio，即基于 IntelliJ IDEA 的社区版本发展而成，用以取代原来提供 Android 开发者使用的 Eclipse ADT。开发者除了可直接下载 Android Studio 外，原 IntelliJ 用户亦可下载其相关插件来进行开发程序。
>
> IntelliJ 对个别编程语言所开发的集成环境，如 AppCode、CLion、PhpStorm、PyCharm、RubyMine、WebStorm 和 MPS 等，皆可由插件的方式加载 IntelliJ IDEA 来使用。
>
> ​ -- [IDEA - Wikipedia](https://zh.wikipedia.org/wiki/IntelliJ_IDEA)

> IDEA 全称 IntelliJ IDEA，是 java 编程语言开发的集成环境。IntelliJ 在业界被公认为最好的 java 开发工具，尤其在智能代码助手、代码自动提示、重构、JavaEE 支持、各类版本工具(git、svn 等)、JUnit、CVS 整合、代码分析、 创新的 GUI 设计等方面的功能可以说是超常的。IDEA 是 JetBrains 公司的产品，这家公司总部位于捷克共和国的首都布拉格，开发人员以严谨著称的东欧程序员为主。它的旗舰版本还支持 HTML，CSS，PHP，MySQL，Python 等。免费版只支持 Java,Kotlin 等少数语言。
>
> ​ -- [IDEA - BaiduBaike](https://baike.baidu.com/item/IntelliJ%20IDEA/9548353?fr=aladdin)

<a id="markdown-idea-特性" name="idea-特性"></a>

### IDEA 特性

<a id="markdown-高度智能" name="高度智能"></a>

#### 高度智能

当 IntelliJ IDEA 为源码建好索引后，即可为各种上下文提供相关建议， 使开发者体验到无与伦比的快速和智能： 快速的智能代码补全功能、实时代码分析和可靠的重构工具。

<a id="markdown-安装即用" name="安装即用"></a>

#### 安装即用

任务关键型工具，如集成版本控制系统、 多种支持的语言和框架都随时可用— 无需另外安装插件。

<a id="markdown-智能代码补全" name="智能代码补全"></a>

#### 智能代码补全

基本代码补全在可见范围内为类、方法、属性和关键字提供名称建议， 而智能代码补全专注在当前 上下文并提供需要的类型建议。

<a id="markdown-框架针对性辅助" name="框架针对性辅助"></a>

#### 框架针对性辅助

虽然 IntelliJ IDEA 是一种适用于 Java 的 IDE，但它也理解大量其他语言（例如 SQL、JPQL、HTML、JavaScript 等）并提供智能编码辅助，即使当语言表达式被注入到 Java 代码的字符串文字中也能够辨识。

<a id="markdown-促进生产力" name="促进生产力"></a>

#### 促进生产力

IDE 可以预测您的需求，然后自动完成开发工作中繁琐而又重复的任务，使您可以专注于处理更重要的工作。

<a id="markdown-开发者人体工程学" name="开发者人体工程学"></a>

#### 开发者人体工程学

我们深刻的了解打断开发者工作流程所产生的风险，因此在制定 每一项设计和实施决策时都尽力消除或降低这类情况的发生。

IDE 根据您的开发内容并 自动调用相关工具。

<a id="markdown-深化内隐的智能设计" name="深化内隐的智能设计"></a>

#### 深化内隐的智能设计

IntelliJ IDEA 中的编码辅助不仅仅体现在编辑器中，它还可以帮助您在处理其他工作时同样保持生产力：例如，填写属性、搜索元素列表、访问工具窗口或切换配置，等等。

<a id="markdown-idea-下载安装" name="idea-下载安装"></a>

## IDEA 下载安装

<a id="markdown-idea-下载" name="idea-下载"></a>

### IDEA 下载

- [官网](https://www.jetbrains.com/zh-cn/idea/)
- [历史版本](https://www.jetbrains.com/zh-cn/idea/download/other.html)
- [Toolbox App](https://www.jetbrains.com/zh-cn/toolbox-app/)
- [IDEA Community - snapcraft](https://snapcraft.io/intellij-idea-community)
- [IDEA Educational - snapcraft](https://snapcraft.io/intellij-idea-educational)
- [IDEA Ultimate - snapcraft](https://snapcraft.io/intellij-idea-ultimate)

<a id="markdown-idea-安装" name="idea-安装"></a>

### IDEA 安装

<a id="markdown-windows-环境" name="windows-环境"></a>

#### Windows 环境

安装包集成 32 位和 64 位，双击 `ideaIU-****.exe` 安装包进行安装 IDEA。

- 欢迎界面

  ![idea_install_01](https://pic.ryanjie.cn/learn/java/idea/idea_install_01.png)

- 选择 IDEA 安装路径

  ![idea_install_02](https://pic.ryanjie.cn/learn/java/idea/idea_install_02.png)

- 配置安装选项：创建应用程序快捷方式、添加系统环境变量、添加文件资源管理器右键菜单、相应格式文件关联以及下载 32 位的 JetBrains JRE

  ![idea_install_03](https://pic.ryanjie.cn/learn/java/idea/idea_install_03.png)

- 选择开始菜单文件夹

  ![idea_install_04](https://pic.ryanjie.cn/learn/java/idea/idea_install_04.png)

- 应用程序正在安装

  ![idea_install_05](https://pic.ryanjie.cn/learn/java/idea/idea_install_05.png)

- 安装结束：如果之前选择添加系统环境变量，现在需要重启之后才能生效

  ![idea_install_06](https://pic.ryanjie.cn/learn/java/idea/idea_install_06.png)

<a id="markdown-linux-环境" name="linux-环境"></a>

#### Linux 环境

使用 Snap 安装：

```bash
# 社区版
sudo snap install intellij-idea-community --classic
# 旗舰版
sudo snap install intellij-idea-ultimate --classic
# 教育版
sudo snap install intellij-idea-educational --classic
```

<a id="markdown-参考" name="参考"></a>

## 参考

- [IDEA - Wikipedia](https://zh.wikipedia.org/wiki/IntelliJ_IDEA)
- [IDEA - BaiduBaike](https://baike.baidu.com/item/IntelliJ%20IDEA/9548353?fr=aladdin)
- [为何 IntelliJ IDEA 比 Eclipse 更适合于专业 java 开发者](https://www.cnblogs.com/wangzhongqiu/p/6698880.html)

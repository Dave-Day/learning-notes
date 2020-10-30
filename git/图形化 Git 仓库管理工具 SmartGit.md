---
title: 图形化 Git 仓库管理工具 SmartGit
date: 2020-03-25 06:16:29
categories: Program
---

<!-- more -->

<!-- TOC -->

- [图形化 Git 仓库管理工具 SmartGit](#图形化-git-仓库管理工具-smartgit)
    - [使用说明](#使用说明)
    - [软件下载](#软件下载)
        - [SmartGit（Version 20.1.1）](#smartgitversion-2011)
        - [smartgit-agent](#smartgit-agent)
    - [特别声明](#特别声明)

<!-- /TOC -->


<a id="markdown-图形化-git-仓库管理工具-smartgit" name="图形化-git-仓库管理工具-smartgit"></a>
# 图形化 Git 仓库管理工具 SmartGit

**SmartGit** 是一个图形化的 Git 和 Mercurial 客户端，它也可以连接到 SVN 存储库。 SmartGit 可在 Linux，MacOS 和 Windows（7 或更高版本）上运行。 Git 和 Mercurial（Hg）是分布式版本控制系统（DVCS）。

**Smartgit**是一个易于使用的图形化 Git 客户端应用程序，它能在您的工作上满足您的需求，快速的管理您的 Git、SVN 软件。smartgit 是一个企业级的 Git、Mercurial、以及 Subversion 图形化客户端软件，采用图像化的显示界面，使您的观看更加的直观，也可以快速的了解您的问题，简单快速的实现 Git 及 Mercurial 中的版本控制工作，非常的适合开发人员在进行管理项目时使用，使开发人员的工作效率提高。

**SmartGit**允许您访问联机存储库、进行更改和以最小的工作量推送新提交。旨在提供对本地存储库的访问，并促进与存储项目资源的服务器的连接。因此，您可以从服务器中提取内容，进行修改并选择要推送到服务器的提交。主窗口允许您查看项目结构和文件，以便使用源代码。该程序还包括一个文件比较工具和合并文件的能力，这在处理多个版本时非常有用。其他功能包括提交文件的一部分并查看其他同事所做的修改。还可以通过启动 git shell 并在 windows 资源管理器或终端窗口中打开它来浏览代码。尽管该包不包含脱机帮助文件，但您可以通过阅读联机文档来熟悉 git 概念和可用的命令。此外，该应用程序还为某些操作（如克隆存储库）提供了逐步说明。

![smartgit](https://tva1.sinaimg.cn/large/006pYIPbly1gdq9k4svi9j31ka16ddn9.jpg)


<a id="markdown-使用说明" name="使用说明"></a>
## 使用说明

[admonition title="**by zhile.io**" color="indigo"]

本项目在 SmartGit 20.1.1、SmartSVN 11.0.4、SmartSynchronize 4.0.3 上测试通过

使用方法:

0. 先安装 SmartGit/SmartSVN/SmartSynchronize，打开试用。

1. 先下载压缩包解压后得到 smartgit-agent.jar，把它放到你认为合适的文件夹内。
   下载页面：[smartgit-license-crack](https://zhile.io/2020/03/27/smartgit-license-crack.html)

2. SmartGit：编辑 smartgit.vmoptions 文件。文件所在文件夹分别是：
   mac: ~/Library/Preferences/SmartGit/
   linux: ~/.config/smartgit/
   windows: %APPDATA%\syntevo\SmartGit\ 或者你直接在 bin 目录下改。

   SmartSVN：编辑 smartsvn.vmoptions 文件。文件所在文件夹分别是：
   mac: ~/Library/Preferences/SmartSVN/
   linux: ~/.config/smartsvn/
   windows: %APPDATA%\syntevo\SmartSVN\ 或者你直接在 bin 目录下改。

   SmartSynchronize：编辑 smartsynchronize.vmoptions 文件。文件所在文件夹分别是：
   mac: ~/Library/Preferences/SmartSynchronize/
   linux: ~/.config/smartsynchronize/
   windows: %APPDATA%\syntevo\SmartSynchronize\ 或者你直接在 bin 目录下改。

3. 在打开的 smartgit.vmoptions 编辑窗口末行添加："-javaagent:/absolute/path/to/smartgit-agent.jar"
   一定要自己确认好路径，填错会导致 SmartGit 打不开！！！最好使用绝对路径，不要使用中文路径。
   示例:
   mac: -javaagent:/Users/neo/smartgit-agent.jar
   linux: -javaagent:/home/neo/smartgit-agent.jar
   windows: -javaagent:C:\Users\neo\smartgit-agent.jar

4. 启动 SmartGit/SmartSVN/SmartSynchronize，注册使用压缩包内的"license.zip"文件（不需解压）即可。

5. 如果提示错误:
   "Error opening zip file or JAR manifest missing : smartgit-agent.jar"
   这种情况请试着填上 jar 文件的绝对路径.

[/admonition]


<a id="markdown-软件下载" name="软件下载"></a>
## 软件下载


<a id="markdown-smartgitversion-2011" name="smartgitversion-2011"></a>
### SmartGit（Version 20.1.1）

- [**Windows 7+ (64-bit), Git, Installer**](https://www.syntevo.com/downloads/smartgit/smartgit-win-20_1_1.zip)

- [**Windows 7+ (64-bit), Git, Archive (7z)**](https://www.syntevo.com/downloads/smartgit/smartgit-portable-20_1_1.7z)

- [**macOS 10.11 - 10.15, Git, Archive (dmg)**](https://www.syntevo.com/downloads/smartgit/smartgit-macosx-20_1_1.dmg)

- [**Linux (64-bit), Archive (tar.gz)**](https://www.syntevo.com/downloads/smartgit/smartgit-linux-20_1_1.tar.gz)

- [**Linux (64-bit), Archive (deb)**](https://www.syntevo.com/downloads/smartgit/smartgit-20_1_1.deb)

- [**90 盘不限速下载**](https://www.90pan.com/o128582)

[admonition title="shasum（Version 20.1.1）" color="indigo"]

Windows 7+ (64-bit), Git, Archive (7z)

- Size: 93,381,638 Bytes
- SHA-1: 7360c876dfffd66f17fa9b932a5ebc1c84a4d537

Windows 7+ (64-bit), Git, Installer

- Size: 84,980,419 Bytes
- SHA-1: b6e330add8fcdd9f3c1639bd9e772cfcd48273fa

macOS 10.11 - 10.15, Git, Archive (dmg)

- Size: 92,886,460 Bytes
- SHA-1: 94726347a125dbebc7a22dd90aa4e52b0ce11ddd

Linux (64-bit), Archive (tar.gz)

- Size: 50,251,992 Bytes
- SHA-1: fd39b9b547c932ef39752b98c3c8d25cddce8f0c

Linux (64-bit), Archive (deb)

- Size: 50,248,490 Bytes
- SHA-1: 92db5a7397be4b99828d6ddf5c3bd80d14d46cae

[/admonition]


<a id="markdown-smartgit-agent" name="smartgit-agent"></a>
### smartgit-agent

- [**百度云下载(download link)**](https://pan.baidu.com/s/1EhzM1_5xE8w5mk38tfcpSg)，提取码：`bb4i`
- [**OneDrive(download link)**](https://1drv.ms/u/s!Atf-z4aXHKwch1BZun0X8xxBHs0X?e=m1wc1l)

[admonition title="shasum" color="indigo"]

smartgit-agent.jar 88c24b89539fd7f52b013c82517439854fcb5d6e

[/admonition]

[admonition title="注意" color="red"]

- 请使用`SmartGit`/`SmartSynchronize`的`jre`替换 SmartSVN 的`jre`，因为 SmartSVN 的`jre`是阉割版。

[/admonition]


<a id="markdown-特别声明" name="特别声明"></a>
## 特别声明

1. 本项目只做学习研究之用，不得用于商业用途！
2. 若资金允许，请购买正版，谢谢合作！

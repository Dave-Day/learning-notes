---
title: Linux 简介
---

<!-- TOC -->

- [Linux 历史](#linux-历史)
  - [UNIX 渊源](#unix-渊源)
  - [GNU 计划](#gnu-计划)
  - [Unix 和类 Unix 系统演化](#unix-和类-unix-系统演化)
  - [Linux 创立](#linux-创立)
  - [Linux 命名](#linux-命名)
  - [关于 GNU/Linux 命名方式的争议](#关于-gnulinux-命名方式的争议)
  - [Linux 发展现状](#linux-发展现状)
- [Linux 系统架构](#linux-系统架构)
- [Linux 发行版](#linux-发行版)
  - [流行的发行版](#流行的发行版)
    - [基于 Dpkg (Debian 系)](#基于-dpkg-debian-系)
    - [基于 RPM (Red Hat 系)](#基于-rpm-red-hat-系)
    - [基于其他包格式](#基于其他包格式)
  - [Android](#android)
  - [Arch Linux](#arch-linux)
  - [Debian](#debian)
  - [Red Hat](#red-hat)
  - [Gentoo Linux](#gentoo-linux)
  - [Slackware](#slackware)
  - [openSUSE](#opensuse)
- [Linux 学习](#linux-学习)
  - [为什么要学习 Linux](#为什么要学习-linux)
  - [推荐 Linux 发行版(个人学习)](#推荐-linux-发行版个人学习)
    - [Red Hat 系](#red-hat-系)
    - [Debian 系](#debian-系)
    - [Arch 系](#arch-系)
- [参考](#参考)

<!-- /TOC -->

> **发音**
>
> ---
>
> 根据林纳斯·托瓦兹的说法，Linux 的发音和“Minix”是押韵的。“Li”中“i”的发音类似于“Minix”中“i”的发音，而“nux”中“u”的发音类似于英文单词“profess”中“o”的发音。依照国际音标应该是['linэks][ˈlɪnəks]。
>
> 此外有一份林纳斯·托瓦兹本人说话的录音，录音内容为“Hello, this is Linus Torvalds, and I pronounce Linux as Linux”，也表明了作者对单词的读法。
>
> <audio controls>
> <source src="https://pic.ryanjie.cn/learn/linux/00/Linus-linux.ogg" type="audio/ogg" />
> Your browser does not support this audio format.
> </audio>

Linux（/ˈlɪnəks/ LIN-əks）是一种自由和开放源码的类 UNIX 操作系统。该操作系统的内核由林纳斯·托瓦兹在 1991 年 10 月 5 日首次发布，在加上用户空间的应用程序之后，成为 Linux 操作系统。Linux 也是自由软件和开放源代码软件发展中最著名的例子。只要遵循 GNU 通用公共许可证（GPL），任何个人和机构都可以自由地使用 Linux 的所有底层源代码，也可以自由地修改和再发布。大多数 Linux 系统还包括像提供 GUI 的 X Window 之类的程序。除了一部分专家之外，大多数人都是直接使用 Linux 发行版，而不是自己选择每一样组件或自行设置。

Linux 严格来说是单指操作系统的内核，因操作系统中包含了许多用户图形接口和其他实用工具。如今 Linux 常用来指基于 Linux 的完整操作系统，内核则改以 Linux 内核称之。由于这些支持用户空间的系统工具和库主要由理查德·斯托曼于 1983 年发起的 GNU 计划提供，自由软件基金会提议将其组合系统命名为 GNU/Linux，但 Linux 不属于 GNU 计划，这个名称并没有得到社群的一致认同。

Linux 最初是作为支持英特尔 x86 架构的个人电脑的一个自由操作系统。目前 Linux 已经被移植到更多的计算机硬件平台，远远超出其他任何操作系统。Linux 可以运行在服务器和其他大型平台之上，如大型计算机和超级计算机。世界上 500 个最快的超级计算机已 100％运行 Linux 发行版或变种。Linux 也广泛应用在嵌入式系统上，如手机（Mobile Phone）、平板电脑（Tablet）、路由器（Router）、电视（TV）和电子游戏机等。在移动设备上广泛使用的 Android 操作系统就是创建在 Linux 内核之上。

通常情况下，Linux 被打包成供个人计算机和服务器使用的 Linux 发行版，一些流行的主流 Linux 发布版，包括 Debian（及其派生版本 Ubuntu、Linux Mint）、Fedora（及其相关版本 Red Hat Enterprise Linux、CentOS）和 openSUSE 等。Linux 发行版包含 Linux 内核和支撑内核的实用程序和库，通常还带有大量可以满足各类需求的应用程序。个人计算机使用的 Linux 发行版通常包含 X Window 和一个相应的桌面环境，如 GNOME 或 KDE。桌面 Linux 操作系统常用的应用程序，包括 Firefox 网页浏览器、LibreOffice 办公软件、GIMP 图像处理工具等。由于 Linux 是自由软件，任何人都可以创建一个符合自己需求的 Linux 发行版。

<a id="markdown-linux-历史" name="linux-历史"></a>

## Linux 历史

<a id="markdown-unix-渊源" name="unix-渊源"></a>

### UNIX 渊源

UNIX 操作系统（英语：UNIX），是美国 AT&T 公司贝尔实验室于 1969 年完成的操作系统。最早由肯·汤普逊（Ken Thompson），丹尼斯·里奇（Dennis Ritchie），道格拉斯·麦克罗伊（Douglas McIlroy），和乔伊·欧桑纳于 1969 年在 AT&T 贝尔实验室开发。于 1971 年首次发布，最初是完全用汇编语言编写。后来，在 1973 年用一个重要的开拓性的方法，Unix 被丹尼斯·里奇用编程语言 C（内核和 I/O 例外）重新编写。高级语言编写的操作系统具有更佳的兼容性，能更容易地移植到不同的计算机平台。

1983 年，理查德·马修·斯托曼创立 GNU 计划。这个计划有一个目标，是为了发展一个完全自由的类 Unix 操作系统。自 1984 年发起这个计划以来，在 1985 年，理查德·马修·斯托曼发起自由软件基金会并且在 1989 年撰写 GPL。1990 年代早期，GNU 开始大量地产生或收集各种系统所必备的组件，像是——库、编译器、调试工具、文本编辑器，以及一个 Unix 的用户界面（Unix shell）——但是像一些底层环境，如硬件驱动、守护进程、系统内核（kernel）仍然不完整和陷于停顿，GNU 计划中是在 Mach 微内核的架构之上开发系统内核，也就是所谓的 GNU Hurd，但是这个基于 Mach 的设计异常复杂，发展进度则相对缓慢。林纳斯·托瓦兹曾说过如果 GNU 内核在 1991 年时可以用，他不会自己去写一个。

386BSD 涉及的法律问题直到 1992 年还没有解决，NetBSD 和 FreeBSD 是 386BSD 的后裔，早于 Linux。林纳斯·托瓦兹曾说，当时如果有可用的 386BSD，他就可能不会编写 Linux。

MINIX 是一个轻量小型并采用微内核(Micro-Kernel)架构的类 Unix 操作系统，是安德鲁·斯图尔特·塔能鲍姆为在计算机科学用作教学而设计的。

<a id="markdown-gnu-计划" name="gnu-计划"></a>

### GNU 计划

GNU 计划（英语：GNU Project），又译为革奴计划，是一个自由软件集体协作计划，1983 年 9 月 27 日由理查德·斯托曼在麻省理工学院公开发起。它的目标是创建一套完全自由的操作系统，称为 GNU。理查德·斯托曼最早在 net.unix-wizards 新闻组上公布该消息，并附带一份《GNU 宣言》等解释为何发起该计划的文章，其中一个理由就是要“重现当年软件界合作互助的团结精神”。

GNU 是“GNU is Not Unix”的递归缩写。

UNIX 是一种广泛使用的商业操作系统的名称。由于 GNU 将要实现 UNIX 系统的接口标准，因此 GNU 计划可以分别开发不同的操作系统。GNU 计划采用了部分当时已经可自由使用的软件，例如 TeX 排版系统和 X Window 视窗系统等。不过 GNU 计划也开发了大批其他的自由软件，这些软件也被移植到其他操作系统平台上，例如 Microsoft Windows、BSD 家族、Solaris 及 Mac OS。

为保证 GNU 软件可以自由地“使用、复制、修改和发布”，所有 GNU 软件都包含一份在禁止其他人添加任何限制的情况下，授权所有权利给任何人的协议条款，GNU 通用公共许可证（GNU General Public License，GPL）。这个就是被称为“公共著作权”的概念。GNU 也针对不同场合，提供 GNU 宽通用公共许可证与 GNU 自由文档许可证这两种协议条款。

1990 年代早期，GNU 开始大量地产生或收集各种系统所必备的组件，像是——库、编译器、调试工具、文本编辑器，以及一个 Unix 的用户界面（Unix shell）——但是像一些底层环境，如硬件驱动、守护进程、系统内核（kernel）仍然不完整和陷于停顿，GNU 计划中是在 Mach 微内核的架构之上开发系统内核，也就是所谓的 GNU Hurd，但是这个基于 Mach 的设计异常复杂，发展进度则相对缓慢。

<a id="markdown-unix-和类-unix-系统演化" name="unix-和类-unix-系统演化"></a>

### Unix 和类 Unix 系统演化

> [File: Unix history-simple.svg](https://zh.wikipedia.org/wiki/File:Unix_history-simple.svg)

![Unix history-simple](https://pic.ryanjie.cn/learn/linux/00/Unix_history-simple.svg)

<a id="markdown-linux-创立" name="linux-创立"></a>

### Linux 创立

1991 年，林纳斯·托瓦兹在赫尔辛基大学上学时，对操作系统很好奇。他对 MINIX 只允许在教育上使用很不满（在当时 MINIX 不允许被用作任何商业使用），于是他便开始写他自己的操作系统，这就是后来的 Linux 内核。

林纳斯·托瓦兹开始在 MINIX 上开发 Linux 内核，为 MINIX 写的软件也可以在 Linux 内核上使用。后来使用 GNU 软件代替 MINIX 的软件，因为使用从 GNU 系统来的源代码可以自由使用，这对 Linux 的发展有益。使用 GNU GPL 协议的源代码可以被其他项目所使用，只要这些项目使用同样的协议发布。为了让 Linux 可以在商业上使用，林纳斯·托瓦兹决定更改他原来的协议（这个协议会限制商业使用），以 GNU GPL 协议来代替。之后许多开发者致力融合 GNU 元素到 Linux 中，做出一个有完整功能的、自由的操作系统。

<a id="markdown-linux-命名" name="linux-命名"></a>

### Linux 命名

Linux 的第一个版本在 1991 年 9 月被大学 FTP server 管理员 Ari Lemmke 发布在 Internet 上，最初 Torvalds 称这个内核的名称为"Freax"，意思是自由（"free"）和奇异（"freak"）的结合字，并且附上"X"这个常用的字母，以配合所谓的类 Unix 的系统。但是 FTP 服务器管理员嫌原来的命名“Freax”的名称不好听，把内核的称呼改成“Linux”，当时仅有 10000 行代码，仍必须运行于 Minix 操作系统之上，并且必须使用硬盘引导；随后在 10 月份第二个版本（0.02 版）发布，同时这位芬兰赫尔辛基的大学生在 comp.os.minix 上发布一则消息：

> Hello everybody out there using minix- I'm doing a (free) operation system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones.

Linux 的标志和吉祥物是一只名字叫做 Tux 的企鹅，标志的由来有一说是因为 Linus 在澳洲时曾被一只动物园里的企鹅咬了一口，便选择企鹅作为 Linux 的标志，但更容易被接受的说法是：企鹅代表南极，而南极又是全世界所共有的一块陆地。这也就代表 Linux 是所有人的 Linux。

<a id="markdown-关于-gnulinux-命名方式的争议" name="关于-gnulinux-命名方式的争议"></a>

### 关于 GNU/Linux 命名方式的争议

“Linux”这个名称一开始只被 Torvalds 用于 Linux 内核。但是这个内核却常和其他软件一起使用，尤其是 GNU 计划的软件。这很快就成为最受欢迎的 GNU 软件。1994 年六月，在 GNU 的期刊中，Linux 被称作“自由 Unix 克隆版”，Debian 计划也开始把它的产品叫做“Debian GNU/Linux”。1996 年 5 月，Richard Stallman 发布了编辑器 Emacs 的 19.31 版本，其中系统的名称从 Linux 变成了 Lignux。这种拼法为的是明确指出 GNU 和 Linux 的结合。但是这不久就被“GNU/Linux”所代替了。

对这个名称，不同人有不同的反应。GNU 和 Debian 项目使用那个名字，但是，多数开发者仍然简单地用“Linux”来指代它们的结合。

<a id="markdown-linux-发展现状" name="linux-发展现状"></a>

### Linux 发展现状

1994 年 3 月，Linux1.0 版正式发布，Marc Ewing 成立 Red Hat 软件公司，成为最著名的 Linux 经销商之一。早期 Linux 的引导管理程序（boot loader）使用 LILO（Linux Loader），早期的 LILO 存在着一些难以容忍的缺陷，例如无法识别 1024 柱面以后的硬盘空间，后来的 GRUB（GRand Unified Bootloader）克服这些缺点，具有‘动态搜索内核文件’的功能，可以让用户在引导的时候，自行编辑引导设置系统文件，透过 ext2 或 ext3 文件系统中加载 Linux Kernel（GRUB 通过不同的文件系统驱动可以识别几乎所有 Linux 支持的文件系统，因此可以使用很多文件系统来格式化内核文件所在的扇区，并不局限于 ext 文件系统）。

今天由 Linus Torvalds 带领下，众多开发共同参与开发和维护 Linux 内核。理查德·斯托曼领导的自由软件基金会，继续提供大量支持 Linux 内核的 GNU 组件。一些个人和企业开发的第三方的非 GNU 组件也提供对 Linux 内核的支持，这些第三方组件包括大量的作品，有内核模块和用户应用程序和库等内容。Linux 社区或企业都推出一些重要的 Linux 发行版，包括 Linux 内核、GNU 组件、非 GNU 组件，以及其他形式的软件包管理系统软件。

> - 1983：Richard Stallman 发起以创建一个自由的操作系统为目标的 GNU 计划。
> - 1989：Richard Stallman 撰写第一版的 GNU GPL。
> - 1991：Linux 内核在 8 月 25 日由 21 岁的芬兰学生 Linus Benedict Torvalds 公开发布。
> - 1992：在 GNU GPL 下 Linux 内核被重新授权使用，产生第一个“Linux 发行版本”。
> - 1993：超过 100 个开发者致力于 Linux 内核开发。在他们的努力下，内核逐渐适应 GNU 的环境，这个为 Linux 创造巨大的应用空间的广阔环境。Slackware 首次发布。后来在同一年，Debian 项目设立，现已成为最大的社区发布项目。
> - 1994: 3 月, Torvalds 认为内核的所有组件已经完全成熟，他放出了 Linux 的 1.0 版本。XFree86 项目组提供了一个图形化用户界面（GUI）. 同年 Red Hat 公司和 SUSE 发行他们各自的 Linux 1.0 分发版本。
> - 1995: Linux 被移植到 DEC Alpha 和 Sun 公司的 SPARC 平台上，而在接下来的几年里它又被广泛地移植到更多的平台上。
> - 1996: Linux 内核 2.0 版本发布。此时内核已经支持多处理器，因而成为各大公司的绝佳选择。
> - 1998：很多大公司，诸如 IBM、Compaq ，Oracle 表示支持 Linux 系统。另外，一部分程序员开始图形化用户界面 KDE 的开发。
> - 1999：一些程序员开始致力于开发图形化环境 GNOME，它可以替代依靠 Qt 工具包才能工作的 KDE。在这一年里 IBM 宣布一项支持 Linux 的浩大的工程。
> - 2004: XFree86 小组分裂，同现有的 X Windows 标准组织 共同成立 X. Org 基金会，促使了 X Window ServerLinux 版本极其快速而迅猛的发展。

<a id="markdown-linux-系统架构" name="linux-系统架构"></a>

## Linux 系统架构

已安装 Linux 操作系统包含的一些组件：

- 启动程序：例如 GRUB 或 LILO。该程序在计算机开机启动的时候运行，并将 Linux 内核加载到内存中。
- init 程序：init 是由 Linux 内核创建的第一个进程，称为根进程，所有的系统进程都是它的子进程，即所有的进程都是通过 init 启动。init 启动的进程如系统服务和登录提示（图形或终端模式的选择）。
- 软件库包含代码：可以通过运行的进程在 Linux 系统上使用 ELF 格式来执行文件，负责管理库使用的动态链接器是“ld-linux.so”。Linux 系统上最常用的软件库是 GNU C 库。
- 用户界面程序：如命令行 Shell 或窗口环境。

> [File: Linux kernel ubiquity.svg](https://zh.wikipedia.org/wiki/File:Linux_kernel_ubiquity.svg)

![Linux kernel ubiquity](https://pic.ryanjie.cn/learn/linux/00/Linux_kernel_ubiquity.svg)

Linux 内核支持各种硬件架构，为软件（包括可能的专有软件）提供公共平台。

<a id="markdown-linux-发行版" name="linux-发行版"></a>

## Linux 发行版

通常说的 Linux 操作系统指的是 Linux 发行版。

广义地说， Linux 发行版可能是：

- 商业或非商业的;
- 给企业或家庭使用的;
- 服务器，台式机或嵌入式设备专用的;
- 针对普通用户或高级用户;
- 为一般用途或特殊功能的机器定制的，例如防火墙，网络路由器和计算机集群;
- 甚至是为特定的硬件和计算机架构设计的;
- 针对特定的用户群体，例如国际化和本地化，或加入许多音乐制作或科学计算软件包。
- 不同配置的安全性，可用性，便携性，或全面性
- 支持不同类型的硬件

Linux 发行版的多样性是由于不同用户和厂商的技术、哲学和用途差异。在宽松的自由软件许可证下，任何有足够的知识和兴趣的用户可以自定义现有的发行版，以适应自己的需要。

一个典型的发行版包括：Linux 内核，GNU 库和各种系统工具，命令行 Shell，图形界面底层的 X 窗口系统和上层的桌面环境等。桌面环境有如 KDE 或 GNOME 等，并包含数千种从办公包，编译器，文本编辑器，小游戏，儿童教育软件，到科学工具的应用软件。

![linux-distribution](https://pic.ryanjie.cn/learn/linux/00/linux-distribution.png)

<a id="markdown-流行的发行版" name="流行的发行版"></a>

### 流行的发行版

<a id="markdown-基于-dpkg-debian-系" name="基于-dpkg-debian-系"></a>

#### 基于 Dpkg (Debian 系)

**商业发行版**

- Ubuntu，一个非常流行的桌面发行版，由 Canonical 维护。

**社群发行版**

- Debian，一个强烈信奉自由软件，并由志愿者维护的系统。
- Kubuntu, 使用 KDE 桌面的 Ubuntu。
- Linux Mint，使用 Cinnamon 桌面系统的 Ubuntu 派生版。
- Knoppix，第一个 Live CD 发行版，可以从可移动介质运行，Debian 的派生版。
- OpenGEU，Ubuntu 的派生版。
- Elementary OS：基于 Ubuntu，图形界面酷似 Mac OS X。
- gOS 和其他上网本用的系统。

<a id="markdown-基于-rpm-red-hat-系" name="基于-rpm-red-hat-系"></a>

#### 基于 RPM (Red Hat 系)

**商业发行版**

- Red Hat Enterprise Linux，Fedora 的商业版，由 Red Hat 维护和提供技术支持。
- openSUSE，最初由 Slackware 分离出来，现在由 Novell 维护。
- Loongnix，从 Fedora 发展而来的发行版。

**社群发行版**

- Fedora，是 Red Hat 的社区版，会经常引入新特性进行测试。
- PCLinuxOS，Mandriva 的派生版本，由社区维护的非常流行的发行版。
- CentOS，从 Red Hat 发展而来的发行版，由志愿者维护，旨在提供开源的，并与 Red Hat 100%兼容的系统。
- Mageia，从 Mandriva 发展而来的发行版。
- Loongnix，从 Fedora 发展而来的发行版。

<a id="markdown-基于其他包格式" name="基于其他包格式"></a>

#### 基于其他包格式

- ArchLinux，一个基于 KISS（Keep It Simple and Stupid）的滚动更新的操作系统。
- Chakra，一个从 ArchLinux 派生出来，只使用 KDE 桌面的半滚动更新发行版。
- Gentoo，一个面向高级用户的发行版，所有软件的源代码需要自行编译。
- Slackware，最早的发行版之一，1993 年创建，由 Patrick J. Volkerding 维护。

在 [DistroWatch](https://distrowatch.com) 网站可以看到很多发行版的排名和信息。

<a id="markdown-android" name="android"></a>

### Android

Android（读音：英：['ændrɔɪd]，美：[ˈænˌdrɔɪd]），常见的非官方中文名称为安卓，官方译名是安致，是一个基于 Linux 内核的开放源代码移动操作系统，由谷歌成立的开放手持设备联盟持续领导与开发，主要设计用于触摸屏移动设备如智能手机和平板电脑与其他便携式设备。

常见衍生版：[Android](https://zh.wikipedia.org/wiki/Android) | [Android-IA](https://zh.wikipedia.org/w/index.php?title=Android-IA&action=edit&redlink=1) | [Android-x86](https://zh.wikipedia.org/wiki/Android-x86) | [LineageOS](https://zh.wikipedia.org/wiki/LineageOS) | [CyanogenMod](https://zh.wikipedia.org/wiki/CyanogenMod) | [Remix OS](https://zh.wikipedia.org/wiki/Remix_OS) | [Replicant](https://zh.wikipedia.org/wiki/Replicant)

<a id="markdown-arch-linux" name="arch-linux"></a>

### Arch Linux

Arch Linux（或 Arch /ˈɑːrtʃ/)）是一款基于 x86-64 架构的 Linux 发行版。系统主要由自由和开源软件组成，支持社区参与。系统设计以 KISS 原则（保持简单和愚蠢）为总体指导原则，注重代码正确、优雅和极简主义，期待用户愿意去理解系统的运作。Arch Linux 采用 pacman 作为默认的软件包管理器。针对 x86-64 的 CPU 做了优化，以.pkg.tar.xz 格式打包并由包管理器进行跟踪维护，特别适合动手能力强的 Linux 用户。

常见基于 pacman（Arch 系）衍生版：[Antergos](https://zh.wikipedia.org/wiki/Antergos) | [ArchBang](https://zh.wikipedia.org/wiki/ArchBang) | [ArchLabs](https://zh.wikipedia.org/w/index.php?title=ArchLabs&action=edit&redlink=1) | [Chakra](https://zh.wikipedia.org/wiki/Chakra_GNU/Linux) | [Manjaro Linux](https://zh.wikipedia.org/wiki/Manjaro_Linux) | [Parabola GNU/Linux-libre](https://zh.wikipedia.org/wiki/Parabola_GNU/Linux-libre)

<a id="markdown-debian" name="debian"></a>

### Debian

Debian（/ˈdɛbiən/）是完全由自由软件组成的类 UNIX 操作系统，其包含的多数软件使用 GNU 通用公共许可协议授权，并由 Debian 计划的参与者组成团队对其进行打包、开发与维护。

Debian GNU / Linux 是一种强调使用自由软件的发行版。它支持多种硬件平台。Debian 及其派生发行版使用[deb](https://zh.wikipedia.org/wiki/Deb)软件包格式，并使用 dpkg 及其前端作为包管理器。

常见基于 Dpkg（Debian 系）发行版：

- Adamantix：基于 Debian，特别关注安全。
- Anthon GNU/Linux：即安同 OS，是直接从源码构建的开源 Linux 操作系统，但采用 Dpkg 包管理系统，遵循 LGPL 授权协议，使用 KDE 桌面环境，由安同开源操作系统社区社区成员共同开发。
- B2D Linux：基于 Debian，希望可以由“做中学”来产生一个小而美的中文 Linux 包的计划。
- Debian GNU/Linux：由大批社区志愿者收集的包，拥有庞大的软件包可供选择（29000 个以上），支持大量的硬件平台（12 个计算机系统结构）。Debian 强调开源和自由。
- Deepin：原基于 Ubuntu，现基于 Debian，使用自行开发的 Deepin DE 桌面环境的发行版，启动迅速，简洁美观，开发了深度文件管理器，深度音乐，深度截图，深度终端等特色软件，还与软件厂商合作开发了有道词典、网易云音乐等 Linux 原生应用。
- MX Linux 是一个中量级的 GNU/Linux 发行版。其基于 Debian 稳定版本开发，使用了 antiX 的核心组件，并可安装 MX 社区开发或打包的软件。MX Linux 是 antiX 和早前的 MEPIS 社区合作开发的产物，旨在使用各自系统中最优秀的工具和软件。MX 社区的既定目标是“将优雅而高效的桌面与简单的配置、高度的稳定性、可靠的性能和中等的大小相结合”。MX Linux 使用 Xfce 作为默认桌面环境。
- Ubuntu：是以桌面应用为主的 Linux 发行版。Ubuntu 的开发由英国 Canonical 有限公司主导，南非企业家 Mark Shuttleworth 所创立。Canonical 通过销售与 Ubuntu 相关的技术支持和其他服务来产生收益。Ubuntu 项目公开承诺开源软件开发的原则；鼓励人们使用自由软件，研究它的运作原理，改进和分发。
  - 官方：[Edubuntu](https://zh.wikipedia.org/wiki/Edubuntu) | [Kubuntu](https://zh.wikipedia.org/wiki/Kubuntu) | [Lubuntu](https://zh.wikipedia.org/wiki/Lubuntu) | [Ubuntu Budgie](https://zh.wikipedia.org/w/index.php?title=Ubuntu_Budgie&action=edit&redlink=1) | [Ubuntu GNOME](https://zh.wikipedia.org/wiki/Ubuntu_GNOME) | [Ubuntu Kylin](https://zh.wikipedia.org/wiki/优麒麟) | [Ubuntu MATE](https://zh.wikipedia.org/wiki/Ubuntu_MATE) | [Ubuntu Studio](https://zh.wikipedia.org/wiki/Ubuntu_Studio) | [Xubuntu](https://zh.wikipedia.org/wiki/Xubuntu)
  - 其它：[Asturix](https://zh.wikipedia.org/w/index.php?title=Asturix&action=edit&redlink=1) | [BackTrack](https://zh.wikipedia.org/wiki/BackTrack) | [Bodhi Linux](https://zh.wikipedia.org/wiki/Bodhi_Linux) | [elementary OS](https://zh.wikipedia.org/wiki/Elementary_OS) | [KDE neon](https://zh.wikipedia.org/wiki/KDE_neon) | [Linux Mint](https://zh.wikipedia.org/wiki/Linux_Mint) | [Peppermint Linux OS](https://zh.wikipedia.org/wiki/Peppermint_Linux_OS) | [Pinguy OS](https://zh.wikipedia.org/w/index.php?title=Pinguy_OS&action=edit&redlink=1) | [Trisquel](https://zh.wikipedia.org/wiki/Trisquel) | [Uruk](https://zh.wikipedia.org/w/index.php?title=Uruk_GNU/Linux&action=edit&redlink=1) | [Zorin OS](https://zh.wikipedia.org/wiki/Zorin_OS)

<a id="markdown-red-hat" name="red-hat"></a>

### Red Hat

Red Hat Linux 和 SUSE Linux 是最早使用 RPM 格式软件包的发行版，如今 RPM 格式已广泛运用于众多的发行版。这两种发行版后来都分为商业版本和社区支持版本。Red Hat Linux 的社区支持版本现称为 Fedora，商业版本则称为 Red Hat Enterprise Linux。

基于 RPM（Red Hat 系）发行版：

- Asianux Server：由中国红旗、日本 Miracle、韩国 Hannsoft 三家联合开发，主要市场针对亚洲地区，对中文、日文、韩文的支持比较好。
- CentOS：由社群支持的包，旨在 100%地与 Red Hat Linux 企业版兼容，但不包含 Red Hat 的商业软件。
- Fedora：可用作工作站、桌面以及服务器，由红帽公司及其社群开发。
- Magic Linux：一个易用的中文包，基于 Fedora 和 KDE 桌面环境。
- Red Hat Enterprise Linux：红帽 Linux 家族中唯一的商业分支。
- Turbo Linux：在亚洲较流行的一个包，基于 Red Hat，是 United Linux 的成员。
- Vine Linux：基于 Red Hat 的一个日本包。

<a id="markdown-gentoo-linux" name="gentoo-linux"></a>

### Gentoo Linux

Gentoo Linux（发音为/ˈdʒɛntuː/）是一种 Linux 操作系统，基于 Portage 包管理系统，而拥有几乎无限制的适应性特性，被官方称作元发行版（meta-distribution），支持多达 10 种以上的电脑系统结构平台。此项目和它的产品以巴布亚企鹅命名。Gentoo 包管理系统的设计是模块化、可移植、易维护、灵活以及针对用户机器优化的。软件包从源代码构建，这延续了 ports 的传统。但是为了方便，也提供一些大型软件包在多种架构的预编译二进制文件，用户亦可自建或使用第三方二进制包镜像来直接安装二进制包。

常见发行版：[Calculate Linux](https://zh.wikipedia.org/wiki/Calculate_Linux) | [Chromium OS](https://zh.wikipedia.org/wiki/Chromium_OS) [Chrome OS](https://zh.wikipedia.org/wiki/Chrome_OS) | [Funtoo Linux](https://zh.wikipedia.org/wiki/Funtoo_Linux) | [Sabayon Linux](https://zh.wikipedia.org/wiki/Sabayon_Linux)

<a id="markdown-slackware" name="slackware"></a>

### Slackware

Slackware 是 Slackware Linux, Inc 的 Patrick Volkerding 制作的 Linux 发行版本。Slackware 走了一条与其他的发行版本（Red Hat、Debian、Gentoo、SuSE、Mandriva、Ubuntu 等）不同的道路，它力图成为“UNIX 风格”的 Linux 发行版本。它的方针是只吸收稳定版本的应用程序，并且缺少其他 Linux 版本中那些为发行版本定制的配置工具。

常见发行版：[Austrumi Linux](https://zh.wikipedia.org/w/index.php?title=Austrumi_Linux&action=edit&redlink=1) | [DeLi Linux](https://zh.wikipedia.org/w/index.php?title=DeLi_Linux&action=edit&redlink=1) | [DNALinux](https://zh.wikipedia.org/w/index.php?title=DNALinux&action=edit&redlink=1) | [Kongoni](<https://zh.wikipedia.org/w/index.php?title=Kongoni_(操作系统)&action=edit&redlink=1>) | [NimbleX](https://zh.wikipedia.org/w/index.php?title=NimbleX&action=edit&redlink=1) | [Platypux](https://zh.wikipedia.org/w/index.php?title=Platypux&action=edit&redlink=1) | [Porteus](<https://zh.wikipedia.org/w/index.php?title=Porteus_(操作系统)&action=edit&redlink=1>) | [Salix OS](https://zh.wikipedia.org/w/index.php?title=Salix_OS&action=edit&redlink=1) | [Slax](https://zh.wikipedia.org/wiki/Slax) | [TopologiLinux](https://zh.wikipedia.org/w/index.php?title=TopologiLinux&action=edit&redlink=1) | [VectorLinux](https://zh.wikipedia.org/w/index.php?title=VectorLinux&action=edit&redlink=1) | [Zenwalk](https://zh.wikipedia.org/w/index.php?title=Zenwalk&action=edit&redlink=1)

<a id="markdown-opensuse" name="opensuse"></a>

### openSUSE

openSUSE（/ˌoʊpənˈsuːzə/），前身为 SUSE Linux 和 SuSE Linux Professional，是一个 Linux 发行版与项目，由 SUSE Linux GmBH 与其他公司赞助。openSUSE 在全世界被广泛使用，尤其是在德国。它的开发重心是为软件开发者和系统管理者创造适用的开放源代码的工具，并提供易于使用的桌面环境和功能丰富的服务器环境。openSUSE 针对桌面环境进行了一系列的优化，是一个对 Linux 新手较为友好的 Linux 发行版。

<a id="markdown-linux-学习" name="linux-学习"></a>

## Linux 学习

<a id="markdown-为什么要学习-linux" name="为什么要学习-linux"></a>

### 为什么要学习 Linux

Windows 系统很好用，而且也可足以满足日常工作需求，为什么还需要学习 Linux？

- 个人使用很少有著作权问题，绝大多数都是免费使用，几乎无所谓盗版问题。
- 新的 Linux 发行版大多数软件都有服务器的服务，只要点击就可以自动下载、安装经过认证的软件，不需要到市面购买、安装。
- 强大的 Shell 及脚本支持，容易组合出符合需求的环境或创造自动程序。
- 默认安全设置相对于目前主流的 Windows 操作系统安全很多。Windows 操作系统为了非专业用户降低了默认安全性的设置，导致系统容易受到木马、病毒的侵害。盗版的 Windows 更糟糕，可能随盗版操作系统捆绑木马、恶意程序，部分默认超级用户（Administrator）登录、关闭安全更新等问题导致安全性更差。
- 性能上相对不耗资源，适合于小内存的机器使用。

- 几乎可以使用键盘进行一切操作。

<a id="markdown-推荐-linux-发行版个人学习" name="推荐-linux-发行版个人学习"></a>

### 推荐 Linux 发行版(个人学习)

推荐使用 [全球开源操作系统排行榜（distrowatch 排名）](https://distrowatch.com) 作为参考。排行榜排名靠前的一定有着自己的特色。

<a id="markdown-red-hat-系" name="red-hat-系"></a>

#### Red Hat 系

- CentOS：推荐服务器安装(日常使用安装软件需要找第三方源或者编译安装)。Centos 作为老牌的 redhat 亲信，采用的组件和内核版本都比较保守，因此稳定性也要好得多，而且出现安全时间时，会第一时间内推出安全补丁，对于长时间运行不重启的服务器来说相对更合适。

<a id="markdown-debian-系" name="debian-系"></a>

#### Debian 系

- MX Linux：符合用户使用习惯，被开发者调试得非常出色。体积不大，却继承了大多数发行版都有的东西。
- Deepin：美工设计可以说是 Linux 系列中的佼佼者，许多优秀轮子。

<a id="markdown-arch-系" name="arch-系"></a>

#### Arch 系

- Manjaro：硬件支持特别好，软件最新最齐全，稳定性方面也还不错。

<a id="markdown-参考" name="参考"></a>

## 参考

- [UNIX Wikipedia](https://zh.wikipedia.org/wiki/UNIX)
- [File: Unix history-simple.svg](https://zh.wikipedia.org/wiki/File:Unix_history-simple.svg)
- [GUN 计划 Wikipedia](https://zh.wikipedia.org/wiki/GNU%E8%A8%88%E5%8A%83)
- [MINIX Wikipedia](https://zh.wikipedia.org/wiki/MINIX)
- [Linux Wikipedia](https://zh.wikipedia.org/wiki/Linux)
- [File: Linux kernel ubiquity.svg](https://zh.wikipedia.org/wiki/File:Linux_kernel_ubiquity.svg)

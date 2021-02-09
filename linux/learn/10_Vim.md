---
title: Vim
---




## Vim


### Vim 简介

Vim 是从 vi 发展出来的一个文本编辑器。其代码补完、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用。和 Emacs 并列成为类 Unix 系统用户最喜欢的编辑器。

Vim 的第一个版本由布莱姆·米勒在 1991 年发布。最初的简称是 Vi IMitation，随着功能的不断增加，正式名称改成了 Vi IMproved。现在是在开放源代码方式下发行的自由软件。


### Vim 历史

布莱姆·米勒在 80 年代末购入他的 Amiga 计算机时，Amiga 上还没有他最常用的编辑器 vi。Bram 从一个开源的 vi 复制 Stevie 开始，开发了 Vim 的 1.0 版本。最初的目标只是完全复制 vi 的功能，那个时候的 Vim 是 Vi IMitation（模拟）的简称。1991 年 Vim 1.14 版被"Fred Fish Disk #591"这个 Amiga 用的免费软件集所收录了。1992 年 1.22 版本的 Vim 被移植到了 UNIX 和 MS-DOS 上。从那个时候开始，Vim 的全名就变成 Vi IMproved（改良）了。

在这之后，Vim 加入了不计其数的新功能。做为第一个里程碑的是 1994 年的 3.0 版本加入了多窗口编辑（分割视窗）模式，可以在同一终端中同时编辑多个文件。1996 年发布的 Vim 4.0 是第一个利用 GUI（图形用户界面）的版本。1998 年 5.0 版本的 Vim 加入了 highlight（语法高亮）功能。2001 年的 Vim 6.0 版本加入了代码折叠、插件、多国语言支持、垂直分割视窗等功能。2006 年 5 月发布的 Vim 7.0 版更加入了拼字检查、上下文相关补全，标签页编辑等新功能。2008 年 8 月发布的 Vim 7.2，合并了 Vim 7.1 以来的所有修正补丁，并且加入了脚本的浮点数支持。现在最新的版本是 Vim 8。


### Vim 协议

目前，VIM 是按照 VIM 许可证发布的开源软件，这个协议兼容 GPL。它的协议中包含一些慈善条款，建议用户向荷兰 ICCF 捐款，用于帮助乌干达的艾滋病患者。VIM 启动时会显示「Help poor children in Uganda!」的字样，在中文版本中则是「请帮助乌干达的可怜孩童!」。


### Vim 键盘图

> 英文原图：[www.viemu.com](https://www.viemu.com)
>
> 中文翻译：fdl(linuxsir)

<img style="display:inline-block" src=""><img style="display:inline-block" src="">


### Vim 和 Vi 比较

Vim = Vi + IMproved

- 多级撤销
- 代码语法高亮和代码自动补全
- 支持多种插件
- 通过网络协议（HTTP/SSH）编辑文件
- 多文件编辑
- Vim 可以编辑压缩格式文件（gzip、zip 等）


## Vimrc


### Vimrc 概述

Vimrc 是 Vim 的配置文件。Vim 编辑器相关的所有功能开关都可以通过.vimrc 文件进行设置。

- rc = run command

- 系统级 vimrc 和用户级 vimrc。系统 vimrc 配置文件存放在 Vim 的安装目录，默认路径为`/usr/share/vim/.vimrc`。可以使用命令`echo $VIM`来确定 Vim 的安装目录。用户 vimrc 文件，存放在用户主目录下`~/.vimrc`。可以使用命令`echo $HOME`确定用户主目录。

  注意：用户配置文件优先于系统配置文件，Vim 启动时会优先读取当前用户根目录下的.vimrc 文件。所以与个人用户相关的个性化配置一般都放在`~/.vimrc`中。

- 每一行作为一个命令执行


## 基本模式

> **技巧提示：** 当你不知道自己到底处于什么模式下， 可以按两下 `<Esc>` 返回普通模式下。不过不能在 Ex 模式里这么做（用 ":visual" 返回普通模式）。如果在你按下 <Esc> 后发现屏幕闪烁或者听到响声，这证明你已经回到普通模式。然而，在插入模式里按下 CTRL-O 后再按下 <Esc> 也会听到喇叭的响声，此时你仍然处于插入模式，再按一下 <Esc> 即可。

在 `Vim` 命令模式下输入 `:h vim-modes-intro` 即可进入 Vim 官方内置模式的文档。


### 普通模式 Normal mode / 命令模式 Command mode

按键盘左上角的 `Esc` 键，就会从其他任意模式退回到普通模式。

在普通模式中，用的编辑器命令，比如移动光标，删除文本等等。这也是 Vim 启动后的默认模式。这正好和许多新用户期待的操作方式相反（大多数编辑器默认模式为插入模式）。

Vim 强大的编辑能力来自于其普通模式命令。普通模式命令往往需要一个操作符结尾。例如普通模式命令"dd"删除当前行，但是第一个"d"的后面可以跟另外的移动命令来代替第二个"d"，比如用移动到下一行的"j"键就可以删除当前行和下一行。另外还可以指定命令重复次数，"2dd"（重复"dd"两次），和"dj"的效果是一样的。用户学习了各种各样的文本间移动／跳转的命令和其他的普通模式的编辑命令，并且能够灵活组合使用的话，能够比那些没有模式的编辑器更加高效的进行文本编辑。

在普通模式中，有很多方法可以进入插入模式。比较普通的方式是按"a"（append／追加）键或者"i"（insert／插入）键。


### 可视化模式 Visual mode

按键盘上的 `v` 键，就会从普通模式切换为 VISUAL 可视化模式。处于 VISUAL 模式时，在左下角会显示 `-- VISUAL --`。 该 (visual) 模式与普通模式相似，但是移动光标的命令会扩展高亮的区域。非移动命令作用于高亮的区域。见|Visual-mode|。

这个模式与普通模式比较相似，主要为了用户便于选取文本。

- 用 `v` 命令进入的字符可视化模式（Characterwise visual mode)。文本选择是以字符为单位的。
- 用 `V` 命令进入的行可视化模式（Linewise visual mode)。文本选择是以行为单位的。
- 用 `ctrl-V` 进入的块可视化模式（Blockwise visual mode）。可以选择一个矩形内的文本。

按 `Esc` 键，回到普通模式。


### 选择模式 Select mode

处于 选择模式时，在左下角会显示 `-- SELECT --`。这个模式和无模式编辑器的行为比较相似（Windows 标准文本控件的方式）。这个模式中，可以用鼠标或者光标键高亮选择文本，不过输入任何字符的话，Vim 会用这个字符替换选择的高亮文本块，并且自动进入插入模式。


### 插入模式 Insert mode

按键盘上的 `i, I, a, A, o, O` 键，就会从普通模式切换为插入模式。处于插入模式时，在左下角会显示 `--INSERT--`。

- i : 在光标所在字符前面进入插入模式
- a : 在光标所在字符后面进入插入模式
- shift + I : 在光标所在行的开头进入插入模式
- shift + A : 在光标所在行的末尾进入插入模式
- o : 在光标所在行的下面插入新的一行，光标移动到新插入的这一行，并进入插入模式
- shift + O : 在光标所在行的上面插入新的一行，光标移动到新插入的这一行，并进入插入模式。

在这个模式中，大多数按键都会向文本缓冲区中插入文本。大多数新用户希望文本编辑器编辑过程中一直保持这个模式。

在插入模式中，可以按`ESC`键回到普通模式。


### 命令行模式 Command-line mode

在命令行模式中可以输入会被解释成并执行的文本。例如执行命令（":"键），搜索（"/"和"?"键）或者过滤命令（"!"键）。在命令执行之后，Vim 返回到命令行模式之前的模式，通常是普通模式。


## 推荐


### Vim 配置方案

- [dofy / **7th-vim**](https://github.com/dofy/7th-vim)
- [kepbod / **ivim**](https://github.com/kepbod/ivim)
- [chxuan / **vimplus**](https://github.com/chxuan/vimplus)
- [SpaceVim / **SpaceVim**](https://github.com/SpaceVim/SpaceVim)


### Vim 文本教程

- 控制台运行 `vimtutor` 这是 Vim 官方实操教程
- [简明 Vim 练级攻略](http://coolshell.cn/articles/5426.html) 很不错的入门教程
- [Vim Galore](https://github.com/mhinz/vim-galore) 更新频繁，Vim 进阶必读
- [每日一 Vim](http://liuzhijun.iteye.com/category/270228) 共 30 篇，内容比较全
- [Vim 教程网](https://vimjc.com/) 一个女生维护的 Vim 中文教程网站，持续更新中


### Vim 视频教程

- [优雅玩转 Vim - Imooc](https://www.imooc.com/learn/1049)
- [玩转 Vim 从放弃到爱不释手 - Imooc](https://www.imooc.com/learn/1129)


### Vim 速查表

- [Vim Cheat Sheet](https://vim.rtorr.com/)
-


## 参考

- [Vim - 维基百科](https://zh.wikipedia.org/wiki/Vim)
- [Linux vi/vim - 菜鸟教程](https://www.runoob.com/linux/linux-vim.html)
- [Vim 实操教程（Learning Vim）](https://github.com/dofy/learn-vim)

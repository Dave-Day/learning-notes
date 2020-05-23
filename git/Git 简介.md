---
title: Git 简介
abstract: Git 是什么以及 Git 的来源。
url: git-1
permalink: git-1
date: 2020-03-05 18:35:43
category:
  - [Git]
tags:
  - [Git]
---

## Git 简介

### 什么是 Git

Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的分布式版本控制系统。

与常用的版本控制工具 CVS, Subversion 等不同，它采用了分布式版本库的方式，不必服务器端软件支持（注：这得分是用什么样的服务端，使用http协议或者git协议等不太一样。并且在push和pull的时候和服务器端还是有交互的），使源代码的发布和交流极其方便。 Git 的速度很快，这对于诸如 Linux kernel 这样的大项目来说自然很重要。 Git 最为出色的是它的合并跟踪（merge tracing）能力。

同生活中的许多伟大事件一样，Git 诞生于一个极富纷争大举创新的年代。Linux 内核开源项目有着为数众广的参与者。绝大多数的 Linux 内核维护工作都花在了提交补丁和保存归档的繁琐事务上（1991－2002年间）。到 2002 年，整个项目组开始启用分布式版本控制系统 BitKeeper 来管理和维护代码。

到了 2005 年，开发 BitKeeper 的商业公司同 Linux 内核开源社区的合作关系结束，他们收回了免费使用 BitKeeper 的权力。这就迫使 Linux 开源社区（特别是 Linux 的缔造者 Linus Torvalds ）不得不吸取教训，只有开发一套属于自己的版本控制系统才不至于重蹈覆辙。他们对新的系统制订了若干目标：

- 速度
- 简单的设计
- 对非线性开发模式的强力支持（允许上千个并行开发的分支）
- 完全分布式
- 有能力高效管理类似 Linux 内核一样的超大规模项目（速度和数据量）

自诞生于 2005 年以来，Git 日臻成熟完善，在高度易用的同时，仍然保留着初期设定的目标。它的速度飞快，极其适合管理大项目，它还有着令人难以置信的非线性分支管理系统，可以应付各种复杂的项目开发需求。

### 什么是仓库

在 Git 的概念中，仓库，就是你存在`.git`目录的那个文件夹内的所有文件，包括隐藏的文件，Git程序会再当前目录以及上级目录查找是否存在`.git`文件，如果存在，则会将`.git`目录存在的文件夹开始下的所有文件当成你需要管理的文件，所以，我们如果想将某个文件夹当做一个Git仓库，你可以在那个文件夹下通过终端(Window为Cmd或者PoewrShell或者Bash)来执行

```bash
git init
```

这样，你所期望的那个文件夹就成为了一个Git管理的仓库了

### 什么是版本

严格来讲，Git并不存在版本的概念，但人们也硬是发展出了这么个玩意，在Git中，计数基础是提交，即我们常说的Commit，我们每做一点更改便可以产生一次提交，当提交累计起来，可以作为产品定型时，就在当前的Commit上打上一个标记，将这个标记我们称之为版本多少多少，那么就算完成了一个版本，标记本身被称之为Tag，请注意，在Git中，版本仅仅只是某一个提交的标签，并没有其他意义，Git本身也仅有打标签的功能，并没有版本功能，版本功能是根据Tag来扩展的，Git本身并没有

### 什么是分支

这是Git中最重要的也是最常用的概念和功能之一，分支功能解决了正在开发的版本与上线版本稳定性冲突的问题在Git使用过程中，我们的默认分支一般是Master，当然，这是可以修改的，我们在Master完成一次开发，生成了一个稳定版本，那么当我们需要添加新功能或者做修改时，只需要新建一个分支，然后在该分支上开发，完成后合并到主分支即可

### 什么是提交

提交在Git中同样是非常重要的概念，Git对于版本的管理其实是对于提交的管理，在整个Git仓库中，代码存在的形式并不是一分一分的代码，而是一个一个的提交，Git使用四十个字节长度的16进制字符串来标识每一个提交，这基本保证了每一个提交的标识是唯一的，然后通过组织一个按照时间排序的提交列表，就组成了我们所说的分支，请注意，分支在本质上只是一个索引，所以，我们可以任意回退，修正，即使因为某些原因丢失了，也可以重建另外，关于Git的储存方式:Git是仅仅只储存有修改的部分，并不会储存整个文件，所以，请不要删除文件夹整个文件夹的内容，除非你确定你不再需要他，否则请勿删除

### 什么是同步

同步，也可以称之为拉取，在Git中是非常频繁的操作，和SVN不同，Git的所有仓库之间是平等的，所以，为了保证代码一致性，尽可能的在每次操作前进行一次同步操作，具体的为在工作目录下执行如下命令:

```bash
git pull origin main
```

其中`origin`代表的是你远程的仓库，可以通过命令 `git remote -v` 查看，`main`是分支名，如果你本地是其他分支，请换成其他分支的名字，另，因为远程仓库与你本地仓库可能存在冲突，故当存在冲突时，请参考进阶篇的如何处理冲突

### 什么是推送

和拉取一样，也是一个非常频繁的操作，当你代码有更新时，你需要更新到远程仓库，这个动作被称之为推送，执行的命令与拉取一样，只是将其中的`pull`这个单词改成`push`，同样，如果远程仓库存在你本地仓库没有的更新，则在推送前你需要先进行一次同步，如果你确定你不需要远程的更新，则在推送时加上 `-f` 选项，则可以强制推送，注: 在协同开发中，不建议这么做，因为这样很可能覆盖别人的代码。

推送代码示例:

```bash
git push origin main
```

强制推送代码示例:

```bash
git push origin main -f
```

### 什么是冲突

在使用Git开发时，如果只是一个人使用，那么基本不会产生冲突，但是在多人合作开发的情况下，产生冲突是很正常的一件事情，关于如何处理冲突，请参考进阶篇的[如何处理代码冲突](https://gitee.com/help/articles/%24{domain}?v=%24{version}&t=83148) 这一小节

### 什么是合并

合并这个命令通常情况下是用于两个分支的合并，一般用于本地分支，远程分支多用Pull命令，该命令的功能是将待合并分支与目标分支合并在一起，注意，这个命令只会合并当前版本之前的差异，两个分支的提交历史会根据提交时间重新组织索引，故只可能会产生一次冲突但是会生成一个提交，如果你不想生成这次提交，加上 `--base`参数即可。

### 什么是暂存

这个既是一个概念也是一个命令，其含义就是字面上的，作用就是可以将你当前正在进行的工作暂时存起来，然后在此基础上干别的事情，等你别的事情干完后，再转回来继续，注意，暂存只是针对你最后一次改动而言，即针对当前所在的版本的所有改动都算具体执行命令为:

将当前改动暂存起来:

```bash
git stash
```

恢复最后一次暂存的改动

```bash
git stash pop
```

查看有多少暂存

```bash
git stash list
```

### 什么是撤销

撤销命令使用是非常频繁的，因为某些原因，我们不再需要我们的改动或者新的改动有点问题，我们需要回退到某个版本，这时就需要用到撤销命令，或者说这个应该翻译成重置更加恰当。具体命令如下:

撤销当前的修改:

```bash
git reset --hard
```

请注意:以上命令会完全重置你的修改，如果你想保留某些文件，请使用checkout +文件路径 命令来逐一撤销修改

如果你想重置到某一版本，可以将 `--hard` 改为具体的Commit的id如:

```bash
git reset 1d7f5d89346
```

请注意，这时你的修改仍然存在，只是你的最近一次提交的版本号变成了你要重置的版本，如果说你想完全丢弃修改，只需要加上 --hard参数就可以



## 安装 Git

最早Git是在Linux上开发的，很长一段时间内，Git只能在Linux/Unix系统上运行。随着Git的使用逐渐普及，一些开发者也慢慢将Git移植到了Windows平台上。目前Git已经发展为可以在 Windows/macOS/Linux/Unix 上运行的跨平台工具。

### 下载

你可以从 [官网](https://git-scm.com) 获得Git在Windows/macOS/Linux三个操作系统相关的安装包。也可以通过以下方式安装。

### 安装

#### Window 

从 [官网](http://git-scm.com/download)/ [华为镜像站](https://repo.huaweicloud.com/git-for-windows/) 上下载window版的客户端，以管理员身份运行后，一直选择下一步安装即可，请注意，如果你不熟悉每个选项的意思，请保持默认的选项

#### Ubuntu 

```bash
apt install git 
```

#### Centos/Redhat 

```bash
yum install git
```

#### Fedora23

```bash
dnf install git
# or
yum install git
```

#### Fedora22/21 

```bash
yum install git
```

#### SUSE/OPENSUSE

```bash
zypper install git
```

#### Mac OS X

从 [官网](http://git-scm.com/download)/ [华为镜像站](https://repo.huaweicloud.com/git-for-macos/) 上下载Git的macOS客户端进行安装或者使用下面命令：

```bash
brew install git
```

#### 编译安装(注:仅适合非window系统)

从 https://github.com/git/git/releases 上选取一个版本下载，解压缩后进入到 Git 的目录然后依次执行以下代码:

```bash
make configure
./configure
make all
sudo make install
```

注意:如果遇上无法编译的问题，请自行通过搜索引擎来查找 Git 所需的依赖

如果以上一切正常，打开终端(Window下请打开安装git时一并安装的bash) 输入 git --version 应该会显示如下类似的信息

```bash
git version 2.5.0
```

## 配置 Git

在新的系统上，我们一般都需要先配置下自己的 Git 工作环境。配置工作只需一次，以后升级时还会沿用现在的配置。当然，如果需要，你随时可以用相同的命令修改已有的配置。

Git 提供了一个叫做 `git config` 的工具（译注：实际是 git-config 命令，只不过可以通过 git 加一个名字来呼叫此命令。），专门用来配置或读取相应的工作环境变量。而正是由这些环境变量，决定了 Git 在各个环节的具体工作方式和行为。这些变量可以存放在以下三个不同的地方：

> - /etc/gitconfig 文件：系统中对所有用户都普遍适用的配置。若使用 git config 时用 --system 选项，读写的就是这个文件。
> - ~/.gitconfig 文件：用户目录下的配置文件只适用于该用户。若使用 git config 时用 --global 选项，读写的就是这个文件。
> - 当前仓库的 Git 目录中的配置文件（也就是工作目录中的 .git/config 文件）：这里的配置仅仅针对当前仓库有效。每一个级别的配置都会覆盖上层的相同配置，所以 .git/config 里的配置会覆盖 /etc/gitconfig 中的同名变量。

在 Windows 系统上，Git 会找寻用户主目录下的 .gitconfig 文件。主目录即 $HOME 变量指定的目录，一般都是 `C:\Documents and Settings\$USER`。此外，Git 还会尝试找寻 /etc/gitconfig 文件，只不过看当初 Git 装在什么目录，就以此作为根目录来定位。

### 用户信息配置

第一个要配置的是你个人的用户名称和电子邮件地址。这两条配置很重要，每次 Git 提交时都会引用这两条信息，说明是谁提交了更新，所以会随更新内容一起被永久纳入历史记录：

```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

如果用了 --global 选项，那么更改的配置文件就是位于你用户主目录下的那个，以后你所有的仓库都会默认使用这里配置的用户信息。如果要在某个特定的仓库中使用其他名字或者电邮，只要去掉 --global 选项重新配置即可，新的设定保存在当前仓库的 .git/config 文件里。

如果你是使用 `https` 进行仓库的推拉，你可能需要配置客户端记住密码，避免每次都输入密码

```bash
$ git config --global credential.helper store
```

### 文本编辑器配置

接下来要设置的是默认使用的文本编辑器。Git 需要你输入一些额外消息的时候，会自动调用一个外部文本编辑器给你用。默认会使用操作系统指定的默认编辑器，一般可能会是 Vi 或者 Vim。如果你有其他偏好，比如 Emacs 的话，可以重新设置：

```bash
$ git config --global core.editor emacs
```

差异分析工具
还有一个比较常用的是，在解决合并冲突时使用哪种差异分析工具。比如要改用 vimdiff 的话：

```bash
$ git config --global merge.tool vimdiff
```

Git 可以理解 kdiff3，tkdiff，meld，xxdiff，emerge，vimdiff，gvimdiff，ecmerge，和 opendiff 等合并工具的输出信息。当然，你也可以指定使用自己开发的工具。

### 查看配置信息

要检查已有的配置信息，可以使用 git config --list 命令：

```bash
$ git config --list
user.name=Scott Chacon
user.email=schacon@gmail.com
color.status=auto
color.branch=auto
color.interactive=auto
color.diff=auto
...
```

有时候会看到重复的变量名，那就说明它们来自不同的配置文件（比如 /etc/gitconfig 和 ~/.gitconfig），不过最终 Git 实际采用的是最后一个。

也可以直接查阅某个环境变量的设定，只要把特定的名字跟在后面即可，像这样：

```bash
$ git config user.name
Scott Chacon
```

## 获取 Git 帮助

想了解 Git 的各式工具该怎么用，可以阅读它们的使用帮助，方法有三：

```bash
$ git help <verb>
$ git <verb> --help
$ man git-<verb>
```

比如，要学习 config 命令可以怎么用，运行：

```bash
$ git help config
```

## 参考 

- [Git - Git 简史](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-Git-%E7%AE%80%E5%8F%B2)

- [Git 的官方文档](https://git-scm.com/book/zh/v2)
---
title: Git 工作流
abstract: Git 工作流。
url: git-flow
permalink: git-flow
date: 2020-09-05 18:35:43
category:
  - Git
tags:
  - Git
---

## Git 工作流

提到版本控制管理系统，很多人会第一时间才能想到 SVN 和 Git。而 SVN 和 Git 除了集中式和分布式的区别外，就是分支管理。相比 SVN，Git 提供更丰富的分支特性。

Git 工作流如下图所示：

![git-flow](https://img.zxj.guru/2020/09/git-flow.png)

现在让我们来看一个最简单的分支管理的例子。

1. 开发某个网站，为实现某个新的需求，创建一个分支并在这个分支上开展工作。

2. 此时，你突然接到一个电话说有个 Bug 需要紧急修补。
3. 返回到原先已经发布到生产服务器上的分支，为这次紧急修补建立一个新分支，并在其中修复问题。
4. 通过测试后，回到生产服务器所在的分支，将修补分支合并进来，然后再推送到生产服务器上。
5. 切换到之前实现新需求的分支，将修补分支合并进来，然后继续工作。

这里我们参考 [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/) 一文来学习Git 的分支管理。

## 主分支

主分支包括 `master` 分支和 `develop` 分支。

- `master ` 分支
- `develop` 分支

`master` 分支用来发布，`HEAD` 就是当前线上的运行代码。`develop` 分支就是我们的日常开发。使用这两个分支就具有了最简单的开发模式：`develop` 分支用来开发功能，开发完成并且测试没有问题则将 `develop` 分支的代码合并到 `master` 分支并发布。

![main-branches](https://img.zxj.guru/2020/09/main-branches.png)

## 辅助分支

主要介绍的辅助分支如下：

- `feature` 分支
- `release` 分支
- `hotfix` 分支

通过这些分支，我们可以做到：团队成员之间并行开发，`feature track` 更加容易，开发和发布并行以及线上问题修复。辅助分支与主分支的不同点：辅助分支是有限的生命期，他们最终会被移除。

### Feature 分支

`feature` 分支用来开发具体的功能，一般 fork 自 `develop` 分支，最终可能会合并到 `develop` 分支。比如我们要在下一个版本增加功能1、功能2、功能3。那么我们就可以起三个 `feature` 分支：`feature1` 、 `feature2 ` 和 `feature3`。（`feature` 分支命名最好能够自解释，这并不是一种好的命名。）随着我们开发，功能1和功能2都被完成了，而功能3因为某些原因完成不了，那么最终 `feature1` 和 `feature2` 分支将被合并到 `develop` 分支，而 `feature3` 分支将被干掉。

![feature-branches](https://img.zxj.guru/2020/09/feature-branches.png)

从 `develop` 分支建一个 `feature` 分支，并切换到 `feature` 分支。

```bash
$ git checkout -b myfeature develop
Switched to a new branch "myfeature"
```

合并 `feature` 分支到 `develop`

```bash
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff myfeature
Updating ea1b82a..05e9557
(Summary of changes)
$ git branch -d myfeature
Deleted branch myfeature
$ git push origin develop
```

上面我们 merge 分支的时候使用了参数 `--no-ff`，ff 是`fast-forward` 的意思，`--no-ff`就是禁用`fast-forward`。关于这两种模式的区别如下图。（可以使用 `sourceTree` 或者命令`git log --graph`查看。）

![merge-without-ff](https://img.zxj.guru/2020/09/merge-without-ff.png)

看了上面的图，那么使用非`fast-forward`模式来 `merge` 的好处就不言而喻了：我们知道哪些 `commit` 是某些 `feature` 相关的。虽然 `git merge` 的时候会自动判断是否使用`fast-farward`模式，但是有时候为了更明确，我们还是要加参数`--no-ff`或者`--ff`。

### Release 分支

`release` 分支在我看来是 `pre-master`。`release` 分支从 `develop` 分支 `fork` 出来，最终会合并到 `develop` 分支和 `master` 分支。合并到 `master` 分支上就是可以发布的代码了。有人可能会问那为什么合并回 `develop` 分支呢？很简单，有了 `release` 分支，那么相关的代码修复就只会在 `release` 分支上改动了，最后必然要合并到 `develop` 分支。下面细说。

我们最初所有的开发工作都在 `develop` 分支上，当我们这一期的功能开发完毕的时候，我们基于 `develop` 分支开一个新的 `release` 分支。这个时候我们就可以对 `release` 分支做统一的测试了，另外做一些发布准备工作：比如版本号之类的。

如果测试工作或者发布准备工作和具体的开发工作由不同人来做，比如国内的 `RD` 和 `QA`，这个 `RD` 就可以继续基于 `develop` 分支继续开发了。再或者说公司对于发布有严格的时间控制，开发工作提前并且完美的完成了，这个时候我们就可以在 `develop` 分支上继续我们下一期的开发了。同时如果测试有问题的话，我们将直接在 `release` 分支上修改，然后将修改合并到 `develop` 分支上。

待所有的测试和准备工作做完之后，我们就可以将 `release` 分支合并到 `master` 分支上，并进行发布了。

一些相关命令如下。

新建 `release` 分支

```
$ git checkout -b release-1.2 develop
Switched to a new branch "release-1.2"
$ ./bump-version.sh 1.2
File modified successfully, version bumped to 1.2.
$ git commit -a -m "Bumped version number to 1.2"
[release-1.2 74d9424] Bumped version number to 1.2
1 files changed, 1 insertions(+), 1 deletions(-)
```

`release` 分支合并到 `master` 分支

```
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff release-1.2
Merge made by recursive.
(Summary of changes)
$ git tag -a 1.2
```

`release` 分支合并到 `develop` 分支

```
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff release-1.2
Merge made by recursive.
(Summary of changes)
```

最后，删除 `release` 分支

```
$ git branch -d release-1.2
Deleted branch release-1.2 (was ff452fe).
```

### Hotfix 分支

顾名思义，`hotfix` 分支用来修复线上 `bug`。当线上代码出现 `bug` 时，我们基于 `master` 分支开一个 `hotfix` 分支，修复 bug 之后再将 hotfix 分支合并到 master 分支并进行发布，同时 develop 分支作为最新最全的代码分支，hotfix 分支也需要合并到 develop 分支上去。仔细想一想，其实 hotfix 分支和 release 分支功能类似。hotfix 的好处是不打断 develop 分支正常进行，同时对于现实代码的修复貌似也没有更好的方法了.

![hotfix-branches](https://img.zxj.guru/2020/09/hotfix-branches.png)

一些相关的命令。

新建 hotfix 分支

```
$ git checkout -b hotfix-1.2.1 master
Switched to a new branch "hotfix-1.2.1"
$ ./bump-version.sh 1.2.1
Files modified successfully, version bumped to 1.2.1.
$ git commit -a -m "Bumped version number to 1.2.1"
[hotfix-1.2.1 41e61bb] Bumped version number to 1.2.1
1 files changed, 1 insertions(+), 1 deletions(-)
```

Fix bug

```
$ git commit -m "Fixed severe production problem"
[hotfix-1.2.1 abbe5d6] Fixed severe production problem
5 files changed, 32 insertions(+), 17 deletions(-)
```

buf fix 之后，hotfix 合并到 master

```
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff hotfix-1.2.1
Merge made by recursive.
(Summary of changes)
$ git tag -a 1.2.1
```

hotfix 合并到 develop 分支

```
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff hotfix-1.2.1
Merge made by recursive.
(Summary of changes)
```

删除 hotfix 分支

```
$ git branch -d hotfix-1.2.1
Deleted branch hotfix-1.2.1 (was abbe5d6).
```

## 总结

- `master` 分支：主分支，主要存放已经发布到生产服务器上的代码。
- `develop` 分支：日常开发分支，该分支从 `master` 分支拉取，主要存放着在实现新的产品需求时开发的代码。

- `feature` 分支：日常开发特性分支。一般从 `develop` 分支拉取，主要存放着在实现新产品需求具体功能时开发的代码。具体功能开发完成之后将合并到 `develop` 分支。
- `release` 分支：产品发布测试分支。主要存放着从 `develop` 分支合并过来的代码。 `develop` 分支的代码在新的产品需求全部实现后会合并到 `release` 分支进行测试，测试没有问题后（到了发布日期）将会合并到 `master` 分支并发布。测试有问题将会在 `release` 分支修改，修改测试没问题后将会合并到 `master` 分支和 `develop` 分支。
- `hotfix` 分支：线上 bug 修复分支。主要存放这在紧急修补中为修复问题开发的代码，在测试没有问题后将会合并到 `master` 分支和 `develop` 分支。



## 参考

- [A successful Git branching model » nvie.com](https://nvie.com/posts/a-successful-git-branching-model/)
- [git最佳实践: 分支管理 | Legendtkl](http://legendtkl.com/2016/12/31/git-good-practice-gitflow/)
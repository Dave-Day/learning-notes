---
title: 部署虚拟环境安装 RHEL 7 系统
url: linux-install-rhel-7
---

> 原文地址： <https://www.linuxprobe.com/chapter-01.html>

## 工具下载

> [https://www.linuxprobe.com/tools](https://www.linuxprobe.com/tools)

### RHEL 7

- 百度网盘 1：[https://pan.baidu.com/s/1eGfv3_E9dtAGuLc0iJaEOw#3e6m](https://pan.baidu.com/s/1eGfv3_E9dtAGuLc0iJaEOw#3e6m) 验证码 3e6m
- 百度网盘 2：[http://pan.baidu.com/s/1dEWdcch#j94c](http://pan.baidu.com/s/1dEWdcch#j94c) 验证码 j94c
- 本站分流 1：[https://file.ryanjie.cn/ISO/Red.Hat.Enterprise.Linux](https://file.ryanjie.cn/ISO/Red.Hat.Enterprise.Linux)
- 本站分流 2：[https://pan.ryanjie.cn](https://pan.ryanjie.cn) 路径：`/ISO/Red.Hat.Enterprise.Linux`

> **文件校验**
>
> ```ini
> 文件名称: RHEL-server-7.0-x86_64-LinuxProbe.Com.iso
> 文件大小: 3.48 GB (3,743,416,320 字节)
> MD5: 08961a5cb32d2cdf72026bec43876b7f
> SHA1: ce5b360b8ef96fa2105a13cf981f2e3d148931d6
> SHA256: 85a9fedc2bf0fc825cc7817056aa00b3ea87d7e111e0cf8de77d3ba643f8646c
> ```

### RHEL 8

- 百度网盘 1：[https://pan.baidu.com/s/1B1NH0SM7TIYW9HSmgrf50g](https://pan.baidu.com/s/1B1NH0SM7TIYW9HSmgrf50g) 验证码 brik
- 百度网盘 2：[https://pan.baidu.com/s/1BpE-ggM7cCdqmztvBE74Og#y5hw](https://pan.baidu.com/s/1BpE-ggM7cCdqmztvBE74Og#y5hw) 验证码 y5hw
- 本站分流 1：[https://file.ryanjie.cn/ISO/Red.Hat.Enterprise.Linux](https://file.ryanjie.cn/ISO/Red.Hat.Enterprise.Linux)
- 本站分流 2：[https://pan.ryanjie.cn](https://pan.ryanjie.cn) 路径：`/ISO/Red.Hat.Enterprise.Linux`

> **文件校验**
>
> ```ini
> 文件名称: rhel-8.0-x86_64-linuxprobe.com.iso
> 文件大小: 6.61 GB (7,103,053,824 字节)
> MD5: 8a0bca1c323ad8628b09d0a7cce43f39
> SHA1: 66cad03832dbc99206d2dddd935c3174f8b3cff5
> SHA256: 005d4f88fff6d63b0fc01a10822380ef52570edd8834321de7be63002cc6cc43
> ```

## 安装配置 VM 虚拟机

VMware WorkStation 虚拟机软件是一款桌面计算机虚拟软件，让用户能够在单一主机上同时运行多个不同的操作系统。每个虚拟操作系统的硬盘分区、数据配置都是独立的，而且多台虚拟机可以构建为一个局域网。Linux 系统对硬件设备的要求很低，我们没有必要再买一台电脑，课程实验用虚拟机完全可以搞定，而且 VM 还支持实时快照、虚拟网络、拖曳文件以及 PXE（Preboot Execute Environment，预启动执行环境）网络安装等方便实用的功能。

> 可能会有读者有疑问"为什么要用收费的虚拟机产品来搭建实验环境，而不是用一些免费的开源虚拟机软件呢？"本书前言中讲到，我们学习 Linux 系统的原因不是因为它免费，也不是因为它开源，而是因为 Linux 系统真的很好用，这个结论同样也适用于 VMware Workstation 这款产品。虽然网上总能找到免费的序列号，但刘遄老师真的很不推荐用盗版软件，因为既然您眼前的这本《Linux 就该这么学》可以从网上免费下载到（ [pdf 电子版下载地址](https://www.linuxprobe.com/book) ），就请把原本要买书的钱多捐助一些给开源组织和真正用心做产品的公司吧，愿世界美好的脚步更快一些。

第 1 步：运行下载完成的 Vmware Workstation 虚拟机软件包，将会看到如图 1-1 所示的虚拟机程序安装向导初始界面。

![图2-1 虚拟机软件的安装向导初始界面](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤1.jpg)

第 2 步：在虚拟机软件的安装向导界面单击"下一步"按钮，如图 1-2 所示。

![图2-2 虚拟机的安装向导](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤2.jpg)

第 3 步：在最终用户许可协议界面选中"我接受许可协议中的条款"复选框，然后单击"下一步"按钮，如图 1-3 所示。

![图2-3 接受许可条款](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤3.jpg)

第 4 步：选择虚拟机软件的安装位置（可选择默认位置），选中"增强型键盘驱动程序"复选框后单击"下一步"按钮，如图 1-4 所示。

![图2-4 选择虚拟机软件的安装路径](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤4.jpg)

第 5 步：根据自身情况适当选择"启动时检查产品更新"与"帮助完善 VMware Workstation Pro"复选框，然后单击"下一步"按钮，如图 1-5 所示。

![图2-5 虚拟机的用户体验设置](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤5.jpg)

第 6 步：选中"桌面"和"开始菜单程序文件夹"复选框，然后单击"下一步"按钮，如图 1-6 所示。

![图2-6 虚拟机图标的快捷方式生成位置](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤6.jpg)

第 7 步：一切准备就绪后，单击"安装"按钮，如图 1-7 所示。

![图2-7 准备开始安装虚拟机](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤7.jpg)

第 8 步：进入安装过程，此时要做的就是耐心等待虚拟机软件的安装过程结束，如图 1-8 所示。

![图2-8 等待虚拟机软件安装完成](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤8.jpg)

第 9 步：大约 5 ～ 10 分钟后，虚拟机软件便会安装完成，然后再次单击"完成"按钮，如图 1-9 所示。

![图2-9 虚拟机软件安装向导完成界面](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤9.jpg)

第 10 步：双击桌面上生成的虚拟机快捷图标，在弹出的如图 1-10 所示的界面中，输入许可证密钥，或者选择试用之后，单击"继续"按钮（这里选择的是"我希望试用 VMware Worksatation 12 30 天"复选框）。

![图2-10 虚拟机软件许可验证界面](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤10.jpg)

第 11 步：在出现"欢迎使用 VMware Workstation 12"界面后，单击"完成"按钮，如图 1-11 所示。

![ 图2-11 虚拟机软件的感谢界面](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤11.jpg)

第 12 步：在桌面上再次双击快捷方式，此时便看到了虚拟机软件的管理界面，如图 1-12 所示。

![图2-12 虚拟机软件的管理界面](https://img.zxj.guru/learn/linux/02/虚拟机安装步骤12.jpg)

> 注意，在安装完虚拟机之后，不能立即安装 Linux 系统，因为还要在虚拟机内设置操作系统的硬件标准。只有把虚拟机内系统的硬件资源模拟出来后才可以正式步入 Linux 系统安装之旅。VM 虚拟机的强大之处在于不仅可以调取真实的物理设备资源，还可以模拟出多网卡或硬盘等资源，因此完全可以满足大家对学习环境的需求，再次强调，真的不用特意购买新电脑。

## 创建 RHEL 7 虚拟机

第 1 步：在图 1-12 中，单击"创建新的虚拟机"选项，并在弹出的"新建虚拟机向导"界面中选择"典型"单选按钮，然后单击"下一步"按钮，如图 1-13 所示。

![图2-13 新建虚拟机向导](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程1.jpg)

第 2 步：选中"稍后安装操作系统"单选按钮，然后单击"下一步"按钮，如图 1-14 所示。

> 在近几年的讲课过程中真是遇到了很多不听话的学生，明明要求选择"稍后安装操作系统"单选按钮，结果非要选择"安装程序光盘镜像文件"单选按钮，并把下载好的 RHEL 7 系统的镜像选中。这样一来，虚拟机会通过默认的安装策略为您部署最精简的 Linux 系统，而不会再向您询问安装设置的选项。
>
> 如果您是购买图书自行学习的话，请一定不要低估后续实验的难度和 Linux 知识体系的难度，更不要高估自己的自学和排错能力，否则可能会因为系统长期报错而丧失学习兴趣，得不偿失。对于经济条件允许、有意愿深入了解 Linux 系统并考取红帽 RHCE 的同学，可以看一下刘遄老师主讲的培训介绍：[https://www.linuxprobe.com/training](https://www.linuxprobe.com/training)。

![图2-14 选择虚拟机的安装来源](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程2.jpg)

第 3 步：在图 1-15 中，将客户机操作系统的类型选择为"Linux"，版本为"Red Hat Enterprise Linux 7 64 位"，然后单击"下一步"按钮。

![图2-15 选择操作系统的版本](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程3.jpg)

第 4 步：填写"虚拟机名称"字段，并在选择安装位置之后单击"下一步"按钮，如图 1-16 所示。

![图2-16 命名虚拟机及设置安装路径](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程4.jpg)

第 5 步：将虚拟机系统的"最大磁盘大小"设置为 20.0GB（默认即可），然后单击"下一步"按钮，如图 1-17 所示。

![ 图2-17 虚拟机最大磁盘大小](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程5.jpg)

第 6 步：单击"自定义硬件"按钮，如图 1-18 所示。

![图2-18 虚拟机的配置界面](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程6.jpg)

第 7 步：在出现的图 1-19 所示的界面中，建议将虚拟机系统内存的可用量设置为 2GB，最低不应低于 1GB。如果自己的真机设备具有很强的性能，那么也建议将内存量设置为 2GB，因为将虚拟机系统的内存设置得太大没有必要。

![图2-19 设置虚拟机的内存量](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程7.jpg)

第 8 步：根据您真机的性能设置 CPU 处理器的数量以及每个处理器的核心数量，并开启虚拟化功能，如图 1-20 所示。

![图2-20 设置虚拟机的处理器参数](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程8.jpg)

第 9 步：光驱设备此时应在"使用 ISO 镜像文件"中选中了下载好的 RHEL 系统镜像文件，如图 1-21 所示。

![图2-21 设置虚拟机的光驱设备](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程9.jpg)

第 10 步：VM 虚拟机软件为用户提供了 3 种可选的网络模式，分别为桥接模式、NAT 模式与仅主机模式。这里选择"仅主机模式"，如图 1-22 所示。

> **桥接模式：** 相当于在物理主机与虚拟机网卡之间架设了一座桥梁，从而可以通过物理主机的网卡访问外网。
> **NAT 模式：** 让 VM 虚拟机的网络服务发挥路由器的作用，使得通过虚拟机软件模拟的主机可以通过物理主机访问外网，在真机中 NAT 虚拟机网卡对应的物理网卡是 VMnet8。
> **仅主机模式：** 仅让虚拟机内的主机与物理主机通信，不能访问外网，在真机中仅主机模式模拟网卡对应的物理网卡是 VMnet1。

![图2-22 设置虚拟机的网络适配器](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程10.jpg)

第 11 步：把 USB 控制器、声卡、打印机设备等不需要的设备统统移除掉。移掉声卡后可以避免在输入错误后发出提示声音，确保自己在今后实验中思绪不被打扰。然后单击"关闭"按钮，如图 1-23 所示。

![图2-23 最终的虚拟机配置情况](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程11.jpg)

第 12 步：返回到虚拟机配置向导界面后单击"完成"按钮，如图 1-24 所示。虚拟机的安装和配置顺利完成。

![图2-24 结束虚拟机配置向导](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程12.jpg)

第 13 步：当看到如图 1-25 所示的界面时，就说明您的虚拟机已经被配置成功了。接下来准备步入属于您的 Linux 系统之旅吧。

![图2-25 虚拟机配置成功的界面](https://img.zxj.guru/learn/linux/02/虚拟机硬件的配置过程13步.jpg)

## 安装 RHEL 7 系统

安装 RHEL 7 或 CentOS 7 系统时，您的电脑的 CPU 需要支持 VT（Virtualization Technology，虚拟化技术）。所谓 VT，指的是让单台计算机能够分割出多个独立资源区，并让每个资源区按照需要模拟出系统的一项技术，其本质就是通过中间层实现计算机资源的管理和再分配，让系统资源的利用率最大化。其实只要您的电脑不是五六年前买的，价格不低于三千元，它的 CPU 就肯定会支持 VT 的。如果开启虚拟机后依然提示"CPU 不支持 VT 技术"等报错信息，请重启电脑并进入到 BIOS 中把 VT 虚拟化功能开启即可。

第 1 步：在虚拟机管理界面中单击"开启此虚拟机"按钮后数秒就看到 RHEL 7 系统安装界面，如图 1-26 所示。在界面中，Test this media & install Red Hat Enterprise Linux 7.0 和 Troubleshooting 的作用分别是校验光盘完整性后再安装以及启动救援模式。此时通过键盘的方向键选择 Install Red Hat Enterprise Linux 7.0 选项来直接安装 Linux 系统。

![图2-26 RHEL 7系统安装界面](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-30-36.jpg)

第 2 步：接下来按回车键后开始加载安装镜像，所需时间大约在 30 ～ 60 秒，请耐心等待，如图 1-27 所示。

![图2-27 安装向导的初始化界面](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-30-48.jpg)

第 3 步：选择系统的安装语言后单击 Continue 按钮，如图 1-28 所示。

> 请读者不用担心英语基础的问题，因为 Linux 系统中用的 Linux 命令具有特定的功能和意义，而非英语单词本身的意思。比如 free 的意思是"自由"、"免费"，而 free 命令在 Linux 系统中的作用是查看内存使用量。因此即便是英语水平很高，只要没有任何 Linux 基础知识，在看到这些 Linux 命令后也需要重新学习。再者，把系统设置成英文后还可以锻炼一下英语阅读能力，不知不觉地就把 Linux 系统和英文一起学了，岂不是更好？！如果您执意选择中文安装语言，也可以在图 1-28 中进行选择。

![图2-28 选择系统的安装语言](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-31-32.jpg)

第 4 步：在安装界面中单击 SOFTWARE SELECTION 选项，如图 1-29 所示。

![图2-29 安装系统界面](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-32-05.jpg)

第 5 步：RHEL 7 系统的软件定制界面可以根据用户的需求来调整系统的基本环境，例如把 Linux 系统用作基础服务器、文件服务器、Web 服务器或工作站等。此时您只需在界面中单击选中 Server with GUI 单选按钮，然后单击左上角的 Done 按钮即可，如图 1-30 所示。

> 之前看过一个新闻，说是苹果公司某员工在 iOS 系统的用户说明书末尾加了一句"反正你们也不会去看"。其实这件事情有时候也可以用来调侃部分读者的学习状态，刘遄老师绝不会把没用的知识写到本书中，但就是这样一张如此醒目的截图也总是有同学视而不见，结果采用了默认的 Minimal Install 单选按钮安装 RHEL 7 系统，最终导致很多命令不能执行，服务搭建不成功。请一定留意！
> **刘遄老师亲自上课的培训课程视频介绍：[https://www.linuxprobe.com/training](https://www.linuxprobe.com/training)**

![图2-30 选择系统软件类型](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-31-54.jpg)

第 6 步：返回到 RHEL 7 系统安装主界面，单击 NETWORK & HOSTNAME 选项后，将 Hostname 字段设置为 linuxprobe.com，然后单击左上角的 Done 按钮，如图 1-31 所示。

![图2-31 配置网络和主机名](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-32-31.jpg)

第 7 步：返回到安装主界面，单击 INSTALLATION DESTINATION 选项来选择安装媒介并设置分区。此时不需要进行任何修改，单击左上角的 Done 按钮即可，如图 1-32 所示。

> 读者可能会有这样的疑问"为什么我们不像其他 Linux 图书那样，讲一下手动分区的方法呢"？原因很简单，因为 Linux 系统根据 FHS（Filesystem Hierarchy Standard，文件系统层次结构标准）把不同的目录定义了相应的不同功能，这部分内容会在第 6 章中详细介绍。并且通过刘遄老师最近这几年的教学经验来看，即便现在写出了操作步骤，读者们大多也只是点点鼠标，并不能真正理解其中的知识，效果不一定好，更何况在接下来的实验中，手动分区相对于自动分区来说也没有明显的好处。所以读者大可不必担心学不到，我们书籍的规划课程章节是非常科学的。

![图2-32 系统安装媒介的选择](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-32-17.jpg)

第 8 步：返回到安装主界面，单击 Begin Installation 按钮后即可看到安装进度，在此处选择 ROOT PASSWORD，如图 1-33 所示。

![图2-33 RHEL 7系统的安装界面](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-32-37.jpg)

第 9 步：然后设置 root 管理员的密码。若坚持用弱口令的密码则需要单击 2 次左上角的 Done 按钮才可以确认，如图 1-34 所示。这里需要多说一句，当您在虚拟机中做实验的时候，密码无所谓强弱，但在生产环境中一定要让 root 管理员的密码足够复杂，否则系统将面临严重的安全问题。

![图2-34 设置root管理员的密码](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-32-42.jpg)

第 10 步：Linux 系统安装过程一般在 30 ～ 60 分钟，在安装过程期间耐心等待即可。安装完成后单击 Reboot 按钮，如图 1-35 所示。

![图2-35 系统安装完成](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-15-56-54.jpg)

第 11 步：重启系统后将看到系统的初始化界面，单击 LICENSE INFORMATION 选项，如图 1-36 所示。

![图2-36 系统初始化界面](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-00-32.jpg)

第 12 步：选中 I accept the license agreement 复选框，然后单击左上角的 Done 按钮，如图 1-37 所示。

![图2-37 同意许可说明书](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-00-37.jpg)

第 13 步：返回到初始化界面后单击 FINISH CONFIGURATION 选项，即可看到 Kdump 服务的设置界面。如果暂时不打算调试系统内核，也可以取消选中 Enable kdump 复选框，然后单击 Forward 按钮，如图 1-38 所示。

![图2-38 禁用Kdump服务](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-00-59.jpg)

第 14 步：在如图 1-39 所示的系统订阅界面中，选中 No, I prefer to register at a later time 单选按钮，然后单击 Finish 按钮。此处设置为不注册系统对后续的实验操作和生产工作均无影响。

![图2-39 暂时不对系统进行注册](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-01-07.jpg)

第 15 步：虚拟机软件中的 RHEL 7 系统经过又一次的重启后，我们终于可以看到系统的欢迎界面，如图 1-40 所示。在界面中选择默认的语言 English (United States)，然后单击 Next 按钮。

![图2-40 系统的语言设置](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-18-46.jpg)

第 16 步：将系统的输入来源类型选择为 English (US)，然后单击 Next 按钮，如图 1-41 所示。

![图2-41 设置系统的输入来源类型](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-18-58.jpg)

第 17 步：为 RHEL 7 系统创建一个本地的普通用户，该账户的用户名为 linuxprobe，密码为 redhat，然后单击 Next 按钮，如图 1-42 所示。

![图2-42 创建本地的普通用户](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-19-26.jpg)

第 18 步：按照图 1-43 所示的设置来设置系统的时区，然后单击 Next 按钮。

![图2-43 设置系统的时区](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-19-56.jpg)

第 19 步：在图 1-44 所示的界面中单击 Start using Red Hat Enterprise Linux Server 按钮，出现如图 1-45 所示的界面。至此，RHEL 7 系统完成了全部的安装和部署工作。准备开始学习 Linux 系统吧。

![图2-44 系统初始化结束界面](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-20-00.jpg)

![图2-45 系统的欢迎界面](https://img.zxj.guru/learn/linux/02/红帽企业版RHEL7_x86_64-2015-01-27-16-20-37.jpg)

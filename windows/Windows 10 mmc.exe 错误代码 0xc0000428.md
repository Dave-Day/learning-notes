---
title: Windows 10 mmc.exe 错误代码 0xc0000428
date: 2019-01-11 13:11:49
categories: Windows
---

<!-- more -->

<!-- TOC -->

- [Windows 10 mmc.exe 错误代码 0xc0000428](#windows-10-mmcexe-错误代码-0xc0000428)
  - [问题 : Windows10 mmc.exe 错误代码 0xc0000428](#问题--windows10-mmcexe-错误代码-0xc0000428)
  - [解决方法](#解决方法)
  - [解决方法 2](#解决方法-2)

<!-- /TOC -->

<a id="markdown-windows-10-mmcexe-错误代码-0xc0000428" name="windows-10-mmcexe-错误代码-0xc0000428"></a>

# Windows 10 mmc.exe 错误代码 0xc0000428

<a id="markdown-问题--windows10-mmcexe-错误代码-0xc0000428" name="问题--windows10-mmcexe-错误代码-0xc0000428"></a>

## 问题 : Windows10 mmc.exe 错误代码 0xc0000428

系统 win10 版本 `10.0.17134.285` 。

在桌面右键点击此电脑的 `管理` 菜单，就会提示 `mmc.exe应用程序错误` 。

`应用程序无法正常启动(0xc0000428).请点击“确定”关闭应用程序。`

![mmc.exe错误.jpg](https://pic.ryanjie.cn/2019/01/windows10-0xc0000428-pro.jpg)

<a id="markdown-解决方法" name="解决方法"></a>

## 解决方法

> 当时一共找到两种解决办法，自己使用第一个方法成功解决，所以第二种我没有尝试过。第一种方法不能解决的可以使用第二种方法，记得提前备份文件。

1. 快捷键 `『Windows + R』` 输入 `regedit` 打开注册表。
2. 依次找到 `计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\Manage\command` (可以直接复制粘贴在地址栏里回车就能跳转到文件夹) ;
3. 右键 `默认` 字符串值修改 `数值数据` ;
4. 输入 `%SystemRoot%\system32\mmc.exe /s %SystemRoot%\system32\compmgmt.msc` , 回车确认即可。

![mmc.exe错误-解决方法.jpg](https://pic.ryanjie.cn/2019/01/windows10-0xc0000428.jpg)

<a id="markdown-解决方法-2" name="解决方法-2"></a>

## 解决方法 2

1. 找一台和您自己相同系统版本和位数的电脑;
2. 在 `C:\Windows\System32` 目录下将 `mmc.exe` 程序拷贝至您的电脑中替换原文件( _记得备份好之前的文件_ );
3. 以管理员运行 cmd，粘贴输入 `sfc /scannow` 命令，进行修复操作。
4. 修复完成重启就行。

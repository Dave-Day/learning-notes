---
title: Linux 服务器综合测试工具 LemonBench
date: 2019-10-11 14:26:58
categories: Linux
---

<!-- more -->

<!-- TOC -->

- [Linux 服务器综合测试工具 LemonBench](#linux-服务器综合测试工具-lemonbench)
  - [快速测试](#快速测试)
  - [完整测试](#完整测试)
  - [测试项目](#测试项目)

<!-- /TOC -->

<a id="markdown-linux-服务器综合测试工具-lemonbench" name="linux-服务器综合测试工具-lemonbench"></a>

# Linux 服务器综合测试工具 LemonBench

LemonBench 工具 (别名 LBench、柠檬 Bench )，是一款针对 Linux 服务器设计的服务器性能测试工具。通过综合测试，可以快速评估服务器的综合性能，为使用者提供服务器硬件配置信息。

[github author="LemonBench" project="LemonBench"][/github]

LemonBench 目前涵盖了如下测试：

- **服务器基础信息** (CPU 信息/内存信息/Swap 信息/磁盘空间信息/网络信息等)
- **流媒体解锁测试** (目前支持 HBO Now/动画疯/B 站港澳台/B 站台湾限定)
- **系统性能测试 (CPU/内存/磁盘)**
- **Speedtest 网速测试** (本地到最近源及国内各地域不同线路的网速)
- **路由追踪测试** (追踪到国内和海外不同线路的路由信息)

LemonBench 使用起来非常简单，只需要复制粘贴再来个回车就可以轻松启动测试。

<a id="markdown-快速测试" name="快速测试"></a>

## 快速测试

如果您的服务器上安装有 curl 工具，请使用以下命令执行脚本：

```bash
curl -fsSL https://ilemonrain.com/download/shell/LemonBench.sh | bash -s fast
```

如果您的服务器上安装有 wget 工具，请使用以下命令执行脚本：

```bash
wget -qO- https://ilemonrain.com/download/shell/LemonBench.sh | bash -s fast
```

<a id="markdown-完整测试" name="完整测试"></a>

## 完整测试

如果您的服务器上安装有 curl 工具，请使用以下命令执行脚本：

```bash
curl -fsSL https://ilemonrain.com/download/shell/LemonBench.sh | bash -s full
```

如果您的服务器上安装有 wget 工具，请使用以下命令执行脚本：

```bash
wget -qO- https://ilemonrain.com/download/shell/LemonBench.sh | bash -s full
```

<a id="markdown-测试项目" name="测试项目"></a>

## 测试项目

以下测试项目列表，为 20191007 版本的项目列表！测试内容随时可能发生变化，以实际版本为准！

- **系统信息收集**
  - 系统名称 (包括版本号、系统位数)
  - CPU 信息 (型号、缓存大小)
  - CPU 数量检测 (自适应识别区分虚拟机 (即 VPS) 与独立服务器)
  - 内存使用率
  - Swap 使用率
  - 引导设备 (开机磁盘)
  - 系统负载 (1 分钟/5 分钟/15 分钟，测试结果取启动测试时的实时结果)
- **网络信息收集**
  - 本机 IPV4 地址及相关信息（ASN/归属地/运营商）
  - 本机 IPV6 地址及相关信息（ASN/归属地/运营商）
- **流媒体解锁测试 (Beta)**
  - HBO Now 解锁测试
  - 巴哈姆特动画疯解锁测试
  - 哔哩哔哩 港澳台 及 台湾限定 解锁测试
- **系统性能测试**
  - CPU 性能测试
  - 内存性能测试
  - 磁盘性能测试 (4K 测试结果适用于 SSD 介质磁盘，1M 测试结果适用于 SSD 介质与 HDD 介质磁盘)
- **Speedtest 网速测试**
  - 最近测速点
  - 中国东北地区 (联通/移动)
  - 中国华北地区 (联通/移动)
  - 中国华中地区 (联通/电信)
  - 中国华东地区 (联通/移动)
  - 中国华南地区 (电信/移动)
  - 中国西南地区 (联通/移动)
  - 中国西北地区 (联通/电信/移动)
- **路由追踪测试** (回程测试)
  - 国内部分：联通/电信/移动/联通精品网/电信 CN2/鹏博士/教育网/科技网/广电网
  - 香港部分：CU/CT/CN2/HGC/HKBN/PCCW/TGT/WTT
  - 新加坡部分：CT/CN2/Singtel/StarHub/M1/AWS
  - 日本部分：NTT/IIJ/SoftBank/KDDI/CT/CN2/AWS
  - 韩国部分：KT/SK/LG/CN2/AWS
  - 台湾部分：Chief/APTG/CHT/TFN/FET/KBT/TAIFO
  - 美国部分：CT/CN2/PCCW/HE/GTT/ATT/TATA/NTT/Level3/ZAYO/Cogentco
  - 欧洲部分：Telekom/O2/Vodafont/CT/CN2/GTT/Cogentco/BT/TATA/RT/TTK/MTS
  - IPV6 部分：联通/电信/移动/教育网 (CERNET2)

> 工具发布地址： [极光星空 (iLemonrain)](https://blog.ilemonrain.com/linux/LemonBench.html)
>
> LemonBench TG 交流群： [LemonBench](https://t.me/LemonBench)

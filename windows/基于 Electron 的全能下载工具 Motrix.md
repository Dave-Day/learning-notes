---
title: 基于 Electron 的全能下载工具 Motrix
date: 2019-06-24 09:04:30
categories: Program
---

<!-- more -->

## 基于 Electron 的全能下载工具 Motrix

Motrix 支持下载 HTTP、FTP、BT、磁力链、百度网盘等资源。

[github author="agalwood" project="Motrix"][/github]

![motrix](https://pic.ryanjie.cn/2019/06/Motrix.png)

## 软件特性

- 🕹 简洁明了的图形操作界面
- 🦄 支持 BT 和磁力链任务
- ☑️ 支持选择性下载 BT 部分文件
- 💾 支持下载百度云盘资源
- 🎛 最高支持 10 个任务同时下载
- 🚀 单任务最高支持 64 线程下载
- 🚥 设置上传/下载限速
- 🕶 模拟用户代理 UA
- 🔔 下载完成后通知
- 💻 支持触控栏快捷键 (Mac 专享)
- 🤖 常驻系统托盘，操作更加便捷
- 🌑 深色模式
- 🗑 移除任务时可同时删除相关文件
- 🌍 国际化
- 🎏 ...

## 更新日志

- 添加种子任务时可选择下载部分文件
- 手动停止 BT 任务做种
- 恢复下载失败的任务
- 开机自动启动
- 恢复上次退出时窗口的大小和位置
- 设置限速
- RPC 密钥设置
- 设置下载协议默认客户端
- 保存偏好设置不再需要重启应用

## 本地开发

### 克隆代码

```bash
git clone git@github.com:agalwood/Motrix.git
```

### 安装依赖

```bash
cd Motrix
npm install
```

大陆用户建议使用淘宝的 npm 源

```bash
npm config set registry 'https://registry.npm.taobao.org'
export ELECTRON_MIRROR='https://npm.taobao.org/mirrors/electron/'
export SASS_BINARY_SITE='https://npm.taobao.org/mirrors/node-sass'
```

如果喜欢 [Yarn](https://yarnpkg.com/)，也可以使用 `yarn` 安装依赖

### 开发模式

```bash
npm run dev
```

### 编译打包

```bash
npm run build
```

完成之后可以在项目的 `release` 目录看到编译打包好的应用文件

## 常见问题

**有其他问题请到 [GitHub](https://github.com/agalwood/Motrix) 提 [issue](https://github.com/agalwood/Motrix/issues)**

### Q：BT/Magnet 下载无速度

**A:** 使用 Motrix 下载 BT/Magnet 任务之前，建议找个热门种子（ **不是磁力链接 Magnet**
！），下载一波，挂着做种，过几个小时后退出，用于生成 dht.dat 缓存数据。这样之后下载 BT/Magnet 任务时速度会比较正常。

BT 下载速度受多重因素影响，比如 **没人做种** ，部分网络运营商禁封了 BT 的连接端口，还有不可抗力的网络原因无法连接国外的 tracker 服务器等（请自备酸酸乳等饮品），请务必有点耐心！

**更新：Motrix v1.3.8 版新增了更新 tracker 服务器的功能，打开「偏好设置-进阶设置-
Tracker 服务器」，点击右上角的「同步按钮」，Motrix 会从 [ngosang-trackerslist](https://github.com/ngosang/trackerslist) 同步数据。建议经常更新，保持最新的数据，能显著改善 BT 的下载速度和体验。**

### Q：BT/Magnet 下载到 100%之后，没有自动结束，下载速度一直为 0 KB/s

**A:** BT 任务下载之后会自动开始做种，您可以手动停止任务结束做种（分享率达到 1.0 自动结束）
「人人为我，我为人人」

### Q：迅雷链接下载失败以及迅雷为什么可能可以下载

**A:** 迅雷链接解析出来的源地址可能是已经失效的地址，所有使用 Motrix
会下载失败；迅雷能下载是因为它可以去迅雷自家的服务器上去查找相同的资源，如果能查到，所以有可能可以下载。

### Q：新建任务时导入 Cookie

**A:** Motrix 新建任务的弹层——「显示高级选项」—— 填写 Cookie 字段

![Motrix-Cookie](https://pic.ryanjie.cn//2019/06/Motrix-pro1.png)

### Q：国际化 i18n

**A:** v1.1.3 + 版本已支持

![Motrix-i18n](https://pic.ryanjie.cn/2019/06/Motrix-pro2.png)

## 下载地址

- [Github - releases](https://github.com/agalwood/Motrix/releases/latest)
- 本站分流：[Motrix/](https://pan.ryanjie.cn/Excellent/Motrix/)

[admonition title="文件校验" color="indigo"]

文件名称: Motrix-1.4.1-win.zip
文件大小: 59.8 MB (62,751,633 字节)
MD5: 23b96d9f3a8c8b336b0c565967edf9e5
SHA1: 4cc847d2eb43a6b01b94136ef452761223e9885d
SHA256: d42f72ea029fc29a38a1fb9439eae8cb677fc243e8d9afe35f2f6576f7f7dfba

文件名称: Motrix-Setup-1.4.1.exe
文件大小: 77.5 MB (81,272,178 字节)
MD5: a3e562dcdd99e6ba9949bd9eecce28e4
SHA1: 4eb0dedaaddf7967396caf53fbbfba42030e6696
SHA256: fa78a33628485dc760840ef648a948327c67b0595951c41c82b0923710210f90

文件名称: Motrix-1.4.1-mac.zip
文件大小: 60.1 MB (63,088,420 字节)
MD5: 119d42e5a1dfb5c050709bc40b26ca58
SHA1: 76adc3f9807041f77facbd4575985c9b38b3753f
SHA256: e46a03775d25d455e234fd5770133c38469b020a6a63869fb0431519c6318f60

文件名称: Motrix-1.4.1.dmg.blockmap
文件大小: 67.4 KB (69,089 字节)
MD5: 3a83601b13f423e61f4c647b635c0f28
SHA1: 5aeb459d29ed24fdcf8e4fc1633ff53674ba7358
SHA256: 09c2a614cefb7e2474631998e9e5672bc0d9198e6be240e0d3ea801abb174cd1

文件名称: Motrix-1.4.1.dmg
文件大小: 63.0 MB (66,112,269 字节)
MD5: 385ce974bf9cd7d1f5431ef4494fbbf3
SHA1: 891e4c72233408cb5da0dfcd9805935602851c2a
SHA256: e2250db04b7dcb93fb5fde90ea82fee2cfd6c621c6253cd7535a2630b9a5632c

文件名称: Motrix_1.4.1_amd64.deb
文件大小: 46.5 MB (48,843,228 字节)
MD5: 2817c7cc6ffa66b7db54898d7d8f3b16
SHA1: ee5a4fe4f5b70d31585a8d37c834f89bbff08fee
SHA256: ace42023f1bd6b69626f27838c752ee8c60bcbd372341e4d9056e7229a53fb99

文件名称: Motrix-1.4.1-x86_64.AppImage
文件大小: 67.8 MB (71,186,963 字节)
MD5: 96f2aea1332517fb645347d5033fbabf
SHA1: 56cf99416a902e0a208130797e44b4608d77813a
SHA256: 54ba6a41e58e186118f7b1944327cb2fe02036611f7f99661879c5fcff4cd4d3

[/admonition]

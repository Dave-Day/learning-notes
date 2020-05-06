##  Dell  Inspiron 7590 安装  Manjaro KDE  记录

切记：

> 1. 一块硬盘安装多系统时（Windows + RHEL/CentOS + Debain/Ubuntu/Deepin + Arch/Manjaro），一定要注意安装顺序为：最先安装Windows ，其次安装 RHEL/CentOS ，最后安装 Debain/Ubuntu/Deepin 或者 Arch/Manjaro 。原因是 Windows 和 RHEL/CentOS 会重写系统引导分区；
> 2. 安装多系统时记得关闭 BIOS 中的 `secure boot`；
> 3. UEFI 模式下 `/boot/efi`分区挂载点不能选择格式化；
> 4. Intel 9560 无线网卡（Intel(R) Wireless-AC 9560 160MHz (WLAN)）用户在安装 Manjaro 系统（内核版本 >= 5.4），请提前下载备份 linux419内核 。原因是系统安装之后无线网卡会加载失败，连不到WiFi。

## 桌面环境选择

> 官方介绍：[Manjaro - Download](https://manjaro.org/download)

常用桌面环境：XFCE、GNOME、KDE Plasma。

- GNOME：对 Fcitx 框架支持不好。对于经常输入中文的而言，输入法只能选择 ibus而不能选择搜狗输入法，所以直接PASS；
- KDE Plasma：功能丰富，提供多种主题、小部件等（类似于Windows）。缺点是：开启动画模式下占用内存会偏高。
- XFCE：Xfce是一个快速、轻量级的类unix操作系统的桌面环境。占用内存低，内存小的可以选择。

总结：正常情况下推荐使用 KDE Plasma，内存小的用户推荐使用 XFCE。



## 制作安装启动盘

Linux 下使用 `dd` 制作启动盘。

```bash
sudo dd bs=4M if=/path/to/manjaro.iso of=/dev/sd[drive letter] status=progress oflag=sync
```

Windows 下使用官方推荐的 [ImageWriter](https://launchpad.net/win32-image-writer/) 或者 [Rufus](https://rufus.akeo.ie/) 。如果在安装多系统时，不想反复地格式化U盘的可以使用 [Ventoy](https://ventoy.net/en/index.html) ，然后只需要把ISO文件拷贝到U盘里面就可以启动。

-  [ImageWriter](https://launchpad.net/win32-image-writer/)
- [Rufus](https://rufus.akeo.ie/) 
- [Ventoy](https://ventoy.net/en/index.html)

## 删除分区

安装双系统的需要在当前硬盘内给 manjaro 分出一片磁盘空间用于安装 manjaro 系统。只安装manjaro 系统的可以跳过此步骤。

1. 使用 Windows自带的磁盘整理软件进行操作；
2. 在 PE 下使用 DiskGenius 等分区软件进行操作。

- [Wepe](https://pan.ryanjie.cn/?path=/ISO/wepe)



## 系统安装

1. 插入 U 盘， 开机之后进入 BIOS 将 U盘 设置为第一启动项；

2. 重启之后就开始安装 manjaro 系统，安装过程中注意下面几点，其它的就一路 Enter 就行。（推荐在安装之前先阅读桌面上的 `Manjaro-User-Guide.pdf`文件）

### 驱动选择

驱动选择闭源驱动（driver-no-free）。

### 磁盘分区(挂载点)

磁盘分区在 BIOS 模式 和 UEFI 分区下有差异，具体可以阅读官方 `Manjaro-User-Guide.pdf`文档。以下为UEFI + GPT 模式下的分区建议。当然如果感觉麻烦也可以选择系统自动分区。

- `swap` (交换分区，可选)：根据内存而定，内存大小小于4GB的交换分区设置为为内存大小的2倍，内存大小在 4GB - 16GB的交换分区设置为内存大小，内存大于16GB的交换分区随便设置（可不分配）。文件系统为 `linuxswap`。
- `/boot/efi` (EFI分区)：大小 300MB -500MB。文件系统为 `fat32`，Flags 选择 `boot` 和`ESP`。**切记：此分区不能选择格式化。**
- `/`  (根分区)：将剩余空间全部分配给根分区。文件系统为 `EXT4`。

> 关于`/boot/efi`分区： 先建立efi分区，和/分区，根分区下新建boot目录。然后将efi分区挂载到/boot下就行了。

## 系统配置

```bash
 ██████████████████  ████████     ryanjie@ryanjie
 ██████████████████  ████████     OS: Manjaro 20.0.3 Lysia
 ██████████████████  ████████     Kernel: x86_64 Linux 4.19.133-1-MANJARO
 ██████████████████  ████████     Uptime: 3h 47m
 ████████            ████████     Packages: 1104
 ████████  ████████  ████████     Shell: bash 5.0.18
 ████████  ████████  ████████     Resolution: 1920x1080
 ████████  ████████  ████████     DE: KDE 5.72.0 / Plasma 5.19.3
 ████████  ████████  ████████     WM: KWin
 ████████  ████████  ████████     GTK Theme: Breath [GTK2/3]
 ████████  ████████  ████████     Icon Theme: breath2
 ████████  ████████  ████████     Disk: 28G / 121G (24%)
 ████████  ████████  ████████     CPU: Intel Core i5-9300H @ 8x 4.1GHz [76.0°C]
 ████████  ████████  ████████     GPU: Mesa Intel(R) UHD Graphics 630 (CFL GT2)
                                  RAM: 3851MiB / 15805MiB
```



### 配置国内源

####  Arch Linux 软件源

```bash
sudo pacman-mirrors -i -c China -m rank
```

根据排序选择一个镜像仓库即可。

或者直接编辑 `/etc/pacman.d/mirrorlist` ，在文件的最顶端添加下面中的一条即可。

```bash
## USTC
Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch

## TUNA
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
```

然后更新软件包缓存：

```bash
sudo pacman -Syy
```

#### ArchlinuxCN 镜像

在 `/etc/pacman.conf` 文件末尾添加以下两行：

```bash
## TUNA
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

## USTC
[archlinuxcn]
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

## BFSU
[archlinuxcn]
Server = https://mirrors.bfsu.edu.cn/archlinuxcn/$arch
```

更新软件包缓存：

```bash
sudo pacman -Syy
```

安装 `archlinuxcn-keyring` 包导入 GPG key：

```bash
sudo pacman -S archlinuxcn-keyring
```

#### Arch4edu 镜像

在 `/etc/pacman.conf` 文件末尾添加以下两行：

```bash
## TUNA
[arch4edu]
Server = https://mirrors.tuna.tsinghua.edu.cn/arch4edu/$arch

## BFSU
[arch4edu]
Server = https://mirrors.bfsu.edu.cn/arch4edu/$arch
```

更新软件包缓存：

```bash
sudo pacman -Syy
```

安装 `archlinuxcn-keyring` 包导入 GPG key：

```bash
sudo pacman-key --Secv-keys 7931B6D628C8D3BA
sudo pacman-key --finger 7931B6D628C8D3BA
sudo pacman-key --lsign-key 7931B6D628C8D3BA
```

#### AUR 镜像

安装 yay：

```bash
sudo pacman -S yay
```

修改镜像配置：

```bash
yay --aururl "https://aur.tuna.tsinghua.edu.cn" --save
```

修改的配置文件位于 `~/.config/yay/config.json` ，还可通过以下命令查看修改过的配置：

```bash
yay -P -g
```

### 安装输入法

#### fcitx-sogoupinyin

```bash
sudo yay -S fcitx-sogoupinyin fcitx-configtool sogoupinyin-skin-roulan
```

关于搜狗输入法无法启动的，在命令行中输入`sogou-qimpanel`，查看错误提示信息。

#### 常见错误信息

- 提示缺少 icui18n.so ：`sudo pacman -S icu`
- 无法启动：`rm -rf ~/.sogouinput`
- 任然无法工作：` rm -rf ~/.sogouinput ~/.config/SogouPY* `，注销重新登录。

#### fcitx-sogouimebs

> 2020-08-09 更新:
>
> 今天在逛 fcitx-sogoupinyin 的 AUR 仓库时发现有人推荐 fcitx-sogouimebs。

**依赖对比**

```bash
## fcitx-sogoupinyin
Depends On      : fcitx  opencc  libidn11  lsb-release  xorg-xprop  qtwebkit

## fcitx-sogouimebs
Depends On      : fcitx  opencc  libidn11  lsb-release  xorg-xprop  qt5-webkit  fcitx-qt5
```

**下载地址**

- [码云下载](https://gitee.com/laomocode/fcitx-sogouimebs/releases)

- [Github下载](https://github.com/laomocode/fcitx-sogouimebs/releases)
- [AUR下载](https://aur.archlinux.org/packages/fcitx-sogouimebs/)

**安装**

```bash
## github 
wget -O ~/Downloads/fcitx-sogouimebs-2.0.0.38+0428.1-1-x86_64.pkg.tar.xz https://github.com/laomocode/fcitx-sogouimebs/releases/download/2.0.0.38_0428.1-1/fcitx-sogouimebs-2.0.0.38+0428.1-1-x86_64.pkg.tar.xz

## fastgit
wget -O ~/Downloads/fcitx-sogouimebs-2.0.0.38+0428.1-1-x86_64.pkg.tar.xz https://download.fastgit.org/laomocode/fcitx-sogouimebs/releases/download/2.0.0.38_0428.1-1/fcitx-sogouimebs-2.0.0.38+0428.1-1-x86_64.pkg.tar.xz

## Install
sudo pacman -U ~/Downloads/fcitx-sogouimebs-2.0.0.38+0428.1-1-x86_64.pkg.tar.xz
sudo pacman -S fcitx-configtool 
```

**配置**

在  fcitx-configtool  中添加 sogouimebs 输入法即可。

### 字体

> 原文链接：[manjaro中文字体安装与设置](https://www.jianshu.com/p/26fa3a803439)

#### 安装字体

```bash
## adobe 
sudo pacman -S adobe-source-han-mono-cn-fonts nerd-fonts-fira nerd-fonts-fira-code adobe-source-han-mono-tw-fonts adobe-source-han-mono-jp-fonts 

sudo pacman -S ttf-roboto noto-fonts ttf-dejavu

# 文泉驿
sudo pacman -S wqy-bitmapfont wqy-microhei wqy-microhei-lite wqy-zenhei

# 思源字体
sudo pacman -S noto-fonts-cjk adobe-source-han-sans-cn-fonts adobe-source-han-serif-cn-fonts
```

#### 安装 fontconfig

```bash
sudo pacman -S fontconfig
```

#### 编辑配置文件

编辑配置文件`~/.config/fontconfig/fonts.conf`，然后重新登录。

```properties
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

<fontconfig>

    <its:rules xmlns:its="http://www.w3.org/2005/11/its" version="1.0">
        <its:translateRule translate="no" selector="/fontconfig/*[not(self::description)]"/>
    </its:rules>

    <description>Manjaro Font Config</description>

    <!-- Font directory list -->
    <dir>/usr/share/fonts</dir>
    <dir>/usr/local/share/fonts</dir>
    <dir prefix="xdg">fonts</dir>
    <dir>~/.fonts</dir> <!-- this line will be removed in the future -->

    <!-- 自动微调 微调 抗锯齿 内嵌点阵字体 -->
    <match target="font">
        <edit name="autohint"> <bool>false</bool> </edit>
        <edit name="hinting"> <bool>true</bool> </edit>
        <edit name="antialias"> <bool>true</bool> </edit>
        <edit name="embeddedbitmap" mode="assign"> <bool>false</bool> </edit>
    </match>

    <!-- 英文默认字体使用 Roboto 和 Noto Serif ,终端使用 DejaVu Sans Mono. -->
    <match>
        <test qual="any" name="family">
            <string>serif</string>
        </test>
        <edit name="family" mode="prepend" binding="strong">
            <string>Noto Serif</string>
        </edit>
    </match>
    <match target="pattern">
        <test qual="any" name="family">
            <string>sans-serif</string>
        </test>
        <edit name="family" mode="prepend" binding="strong">
            <string>Roboto</string>
        </edit>
    </match>
    <match target="pattern">
        <test qual="any" name="family">
            <string>monospace</string>
        </test>
        <edit name="family" mode="prepend" binding="strong">
            <string>DejaVu Sans Mono</string>
        </edit>
    </match>

    <!-- 中文默认字体使用思源宋体,不使用 Noto Sans CJK SC 是因为这个字体会在特定情况下显示片假字. -->
    <match>
        <test name="lang" compare="contains">
            <string>zh</string>
        </test>
        <test name="family">
            <string>serif</string>
        </test>
        <edit name="family" mode="prepend">
            <string>Source Han Serif CN</string>
        </edit>
    </match>
    <match>
        <test name="lang" compare="contains">
            <string>zh</string>
        </test>
        <test name="family">
            <string>sans-serif</string>
        </test>
        <edit name="family" mode="prepend">
            <string>Source Han Sans CN</string>
        </edit>
    </match>
    <match>
        <test name="lang" compare="contains">
            <string>zh</string>
        </test>
        <test name="family">
            <string>monospace</string>
        </test>
        <edit name="family" mode="prepend">
            <string>Noto Sans Mono CJK SC</string>
        </edit>
    </match>

    <!-- 把Linux没有的中文字体映射到已有字体，这样当这些字体未安装时会有替代字体 -->
    <match target="pattern">
        <test qual="any" name="family">
            <string>SimHei</string>
        </test>
        <edit name="family" mode="assign" binding="same">
            <string>Source Han Sans CN</string>
        </edit>
    </match>
    <match target="pattern">
        <test qual="any" name="family">
            <string>SimSun</string>
        </test>
        <edit name="family" mode="assign" binding="same">
            <string>Source Han Serif CN</string>
        </edit>
    </match>
    <match target="pattern">
        <test qual="any" name="family">
            <string>SimSun-18030</string>
        </test>
        <edit name="family" mode="assign" binding="same">
            <string>Source Han Serif CN</string>
        </edit>
    </match>
    <!--
    <match target="pattern">
        <test qual="any" name="family">
            <string>Microsoft YaHei</string>
        </test>
        <edit name="family" mode="assign" binding="same">
            <string>Source Han Sans CN</string>
        </edit>
    </match>
    -->
    
    <!-- Load local system customization file -->
    <include ignore_missing="yes">conf.d</include>
    <!-- Font cache directory list -->
    <cachedir>/var/cache/fontconfig</cachedir>
    <cachedir prefix="xdg">fontconfig</cachedir>
    <!-- will be removed in the future -->
    <cachedir>~/.fontconfig</cachedir>

    <config>
        <!-- Rescan in every 30s when FcFontSetList is called -->
        <rescan> <int>30</int> </rescan>
    </config>

</fontconfig>
```

### 配置开发环境

#### Proxy

```bash
## Qt GUI Client qv2ray
sudo pacman -S qv2ray qv2ray-plugin-command qv2ray-plugin-naiveproxy-git qv2ray-plugin-ssr-dev-git qv2ray-plugin-trojan


qv2ray-plugin-command-dev-git qv2ray-plugin-naiveproxy-git qv2ray-plugin-ssr-dev-git qv2ray-plugin-trojan-dev-git
wget -O ~/Downloads/v2ray-linux-64.zip https://hub.fastgit.org/v2ray/v2ray-core/releases/download/v4.27.5/v2ray-linux-64.zip
sudo unzip -od /usr/lib/v2ray ~/Downloads/v2ray-linux-64.zip
sudo chmod +x /usr/lib/v2ray/v2ray /usr/lib/v2ray/v2ctl

## 终端代理工具 proxychains-ng
sudo pacman -S proxychains-ng

## trojan-go
sudo pacman -S trojan-go-git

## Browser Extensions
Chrome：Proxy SwitchyOmega (https://chrome.google.com/webstore/detail/padekgcemlokbadohgkifijomclgjgif)
```

#### C

```bash
sudo pacman -S make gcc g++
```

#### Java

```bash
sudo pacman -S jdk intellij-idea-ultimate-edition
```

#### Python

```bash
sudo pacman -S python3 pycharm-professional
```

#### NodeJS

```bash
## sudo pacman -S nvm
## Init 
## source /usr/share/nvm/nvm.sh
## source /usr/share/nvm/bash_completion
## source /usr/share/nvm/install-nvm-exec

## yarn 
sudo pacman -S yarn

## githubusercontent
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash

## jsdelivr
wget -O $HOME/Downloads/nvm_install.sh https://cdn.jsdelivr.net/gh/nvm-sh/nvm@master/install.sh 
sed -i 's+raw.githubusercontent.com+raw.fastgit.org+' $HOME/Downloads/nvm_install.sh
sed -i 's+github.com+hub.fastgit.org+' $HOME/Downloads/nvm_install.sh
bash $HOME/Downloads/nvm_install.sh

## Activate NVM
chmod +x $HOME/.nvm/nvm.sh
. $HOME/.nvm/nvm.sh

## 编辑 $HOME/.zshrc 
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

## Install latest LTS
nvm ls-remote --lts
nvm install --lts
nvm use --lts

## 淘宝 NPM 镜像
npm config set registry http://registry.npm.taobao.org/
yarn config set registry http://registry.npm.taobao.org/
```

#### Git

```bash
sudo pacman -S git github-desktop-bin gitkraken

## Config
git config --global user.name "Ryanjie"
git config --global user.email ryanjiena@foxmail.com
ssh-keygen -o
cat ~/.ssh/id_rsa.pub
```

#### Vim

```bash
sudo pacman -S vim

## vimrc
git clone --depth=1 https://hub.fastgit.org/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh

```

2020-08-09 更新： Use [Vim Plugin Manager](https://github.com/junegunn/vim-plug) Install Plugins.

```bash
## Create your .vimrc：https://vim-bootstrap.com/
curl 'https://vim-bootstrap.com/generate.vim' --data 'editor=vim&frameworks=vuejs&langs=c&langs=go&langs=html&langs=javascript&langs=lua&langs=php&langs=perl&langs=python&langs=ruby&langs=rust&langs=typescript' > ~/.vimrc

## Set up plug.vim
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://cdn.jsdelivr.net/gh/junegunn/vim-plug@master/plug.vim

## Install Plugins： Launch vim and run :PlugInstall
vim +PlugInstall +qall
vim +VimBootstrapUpdate +qall
proxychains4 vim +PlugInstall +qall
proxychains4 vim +VimBootstrapUpdate +qall
```

#### Oh My Zsh

```bash
## sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

sudo pacman -S zsh oh-my-zsh-git zsh-syntax-highlighting 
# sudo git clone --depth=1 https://hub.fastgit.org/zsh-users/zsh-syntax-highlighting.git /usr/share/zsh/plugins/zsh-syntax-highlighting
sudo git clone --depth=1 https://hub.fastgit.org/zsh-users/zsh-completions.git /usr/share/zsh/plugins/zsh-completions
sudo git clone --depth=1 https://hub.fastgit.org/zsh-users/zsh-autosuggestions.git /usr/share/zsh/plugins/zsh-autosuggestions
sudo git clone --depth=1 https://hub.fastgit.org/zsh-users/zsh-history-substring-search.git /usr/share/zsh/plugins/zsh-history-substring-search
```



```bash
chsh -s /bin/zsh
sudo chsh -s /bin/zsh
```

#### Editor

```bash
sudo pacman -S  typora visual-studio-code-bin wps-office-cn
```

#### Audio & Video

```bash
sudo pacman -S electron-netease-cloud-music vlc
## sudo pacman -S netease-cloud-music netease-cloud-music-gtk
```

#### Browser

```bash
sudo pacman -S google-chrome
```

#### IM

```bash
sudo pacman -S telegram-desktop-megumifox deepin.com.qq.im deepin.com.qq.office
```

#### Launcher

```bash
sudo pacman -S ulauncher
```

#### Download Manager

```bash
sudo pacman -S motrix
```

#### Grub2 Theme

```bash
cd ~/Downloads && wget -O grub2-themes.zip https://hub.fastgit.org/vinceliuice/grub2-themes/archive/master.zip
unar grub2-themes.zip && cd grub2-themes
chmod +x install.sh
sudo ./install.sh -b -t -2
sudo update-grub
```












# Manjaro 配置国内镜像源

## Manjaro 源 

> Manjaro Linux 软件源。

### 配置镜像源 

```bash
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
sudo tee /etc/pacman.d/mirrorlist <<-'EOF'
## Country : China 
Server = https://mirrors.aliyun.com/manjaro/stable/$repo/$arch 

## Country : China 
Server = https://mirrors.ustc.edu.cn/manjaro/stable/$repo/$arch 

## Country : China 
Server = https://mirrors.tuna.tsinghua.edu.cn/manjaro/stable/$repo/$arch

## Country : China
Server = https://mirrors.sjtug.sjtu.edu.cn/manjaro/stable/$repo/$arch

## Country : China
Server = https://mirrors.cloud.tencent.com/manjaro/stable/$repo/$arch

## Country : China
Server = https://mirrors.dgut.edu.cn/manjaro/stable/$repo/$arch

## Country : China
Server = https://mirrors.huaweicloud.com/manjaro/stable/$repo/$arch

EOF
```

或者使用下面命令

```bash
sudo pacman-mirrors -i -c China -m rank
```

根据排序选择镜像仓库即可。

### 刷新软件包缓存

```bash
sudo pacman -Syy
```

## AUR 源

> [Arch 用户软件仓库](https://aur.archlinux.org/)（Arch User Repository，AUR）是为用户而建、由用户主导的 Arch 软件仓库。AUR 中的软件包以软件包生成脚本（[PKGBUILD](https://wiki.archlinux.org/index.php/PKGBUILD_(简体中文))）的形式提供，用户自己通过 [makepkg](https://wiki.archlinux.org/index.php/Makepkg_(简体中文)) 生成包，再由 [pacman](https://wiki.archlinux.org/index.php/Pacman_(简体中文)) 安装。创建 AUR 的初衷是方便用户维护和分享新软件包，并由官方定期从中挑选软件包进入 [community](https://wiki.archlinux.org/index.php/Community_repository) 仓库。本文介绍用户访问和使用 AUR 的方法。
>
> 许多官方仓库软件包都来自 AUR。通过 AUR，大家相互分享新的软件包生成脚本（[PKGBUILD](https://wiki.archlinux.org/index.php/PKGBUILD_(简体中文)) 和其他相关文件）。用户还可以为软件包投票。如果一个软件包投票足够多、没有协议问题、打包质量好，那么它就很有希望被收录进官方 *community* 仓库（以后就可以直接通过 [pacman](https://wiki.archlinux.org/index.php/Pacman) 或 [abs](https://wiki.archlinux.org/index.php/ABS) 安装了）。
>
> **警告： AUR 中的软件包是由其他用户编写的，使用这些文件的风险由您自行承担。**

Arch 的包管理器 pacman 不直接支持 AUR，支持 AUR 的工具常常被称之为 `AUR 助手`。早期使用的是 [yaourt](https://github.com/archlinuxfr/yaourt)，不过其已经不再维护，所以切换到 [yay](https://github.com/Jguer/yay)。

### 配置镜像源 - yaourt

```bash
sudo cp /etc/yaourtrc /etc/yaourtrc.bak
sudo tee /etc/yaourtrc <<-'EOF'
AURURL="https://aur.tuna.tsinghua.edu.cn"

EOF
```

### 配置镜像源 - yay

执行以下命令修改 aururl :

```bash
sudo cp ~/.config/yay/config.json ~/.config/yay/config.json.bak
yay --aururl "https://aur.tuna.tsinghua.edu.cn" --save
```

修改的配置文件位于 `~/.config/yay/config.json` ，还可通过以下命令查看修改过的配置：

```bash
yay -P -g
```

## ArchlinuxCN 源

> **Arch Linux 中文社区仓库**是由 Arch Linux 中文社区驱动的非官方软件仓库，包含许多官方仓库未提供的额外的软件包（中文用户常用软件、工具、字体/美化包等），以及已有软件的 git 版本等变种。一部分软件包的打包脚本来源于 AUR，但也有许多包与 AUR 不一样。
>
> 查看打包脚本、可用包列表、报告问题，请[访问我们在 GitHub 上的项目](https://github.com/archlinuxcn/repo)。
>
> 仓库主地址：`https://repo.archlinuxcn.org/`
>
> （仓库服务器位于欧洲。我们在中国大陆、香港、美国有[镜像](https://github.com/archlinuxcn/mirrorlist-repo)。）
>
> 安装 archlinuxcn-mirrorlist-git 包可以获得一份镜像列表，以便在 pacman.conf 中直接引入。
>
> 社区仓库镜像：`https://github.com/archlinuxcn/mirrorlist-repo`。强烈推荐中国大陆用户选取一个速度快的镜像，以获得良好的安装体验。

### 配置镜像源

```bash
sudo cp /etc/pacman.conf /etc/pacman.conf.bak
sudo tee -a /etc/pacman.conf <<-'EOF'
[archlinuxcn]
# ## ArchLinuxCN (ipv4, ipv6, http, https)
# Server = https://repo.archlinuxcn.org/$arch

# ## 浙江大学 (浙江杭州) (ipv4, ipv6, http, https)
# Server = https://mirrors.zju.edu.cn/archlinuxcn/$arch

# ## 中国科学技术大学 (安徽合肥) (ipv4, ipv6, http, https)
# Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

# ## 清华大学 (北京) (ipv4, ipv6, http, https)
# Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

# ## xTom (Hong Kong server) (Hong Kong) (ipv4, ipv6, http, https)
# ## xTom Hong Kong Mirror
# Server = https://mirror.xtom.com.hk/archlinuxcn/$arch

# ## xTom (US server) (Fremont, CA, United States) (ipv4, ipv6, http, https)
# ## xTom US Mirror
# Server = https://mirror.xtom.com/archlinuxcn/$arch

# ## xTom (Netherlands server) (Amsterdam, the Netherlands) (ipv4, ipv6, http, https)
# ## xTom Netherlands Mirror
# Server = https://mirror.xtom.nl/archlinuxcn/$arch

# ## Open Computing Facility, UC Berkeley (Berkeley, CA, United States) (ipv4, ipv6, http, https)
# Server = https://mirrors.ocf.berkeley.edu/archlinuxcn/$arch

# ## 北京外国语大学 (北京) (ipv4, ipv6, http, https)
# Server = https://mirrors.bfsu.edu.cn/archlinuxcn/$arch

# ## 网易 (浙江杭州) (ipv4, http, https)
# Server = https://mirrors.163.com/archlinux-cn/$arch

# ## 重庆大学 (重庆) (ipv4, http, https)
# Server = https://mirrors.cqu.edu.cn/archlinuxcn/$arch

# ## SJTUG 软件源镜像服务 (上海) (ipv4, https)
# Server = https://mirrors.sjtug.sjtu.edu.cn/archlinux-cn/$arch

# ## 莞工 GNU/Linux 协会 开源软件镜像站 (广东东莞) (ipv4, https)
# Server = https://mirrors.dgut.edu.cn/archlinuxcn/$arch

# ## 腾讯云 (上海) (ipv4, https)
# Server = https://mirrors.cloud.tencent.com/archlinuxcn/$arch

## 阿里云 (Global CDN) (ipv4, http, https)
Server = https://mirrors.aliyun.com/archlinuxcn/$arch

EOF
```

### 导入  GPG 密钥

```bash
sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring
```

### 刷新软件包缓存

```bash
sudo pacman -Syy
```

## Arch4edu 源

> Arch4edu 是面向高校用户推出的非官方软件仓库， 支持 Arch Linux 和 Arch Linux ARM， 主要包含高校用户常用的科研、教学及开发软件。
>
> 项目地址：`https://github.com/arch4edu/arch4edu`

### 导入 GPG 密钥

```bash
sudo pacman-key --recv-keys 7931B6D628C8D3BA
sudo pacman-key --finger 7931B6D628C8D3BA
sudo pacman-key --lsign-key 7931B6D628C8D3BA
```

### 配置镜像源

```bash
sudo tee -a /etc/pacman.conf <<-'EOF'
[arch4edu]
## 清华大学 (Source)
Server = https://mirrors.tuna.tsinghua.edu.cn/arch4edu/$arch

# ## 阿里云
# Server = https://mirrors.aliyun.com/arch4edu/$arch

# ## 北京外国语大学
# Server = https://mirrors.bfsu.edu.cn/arch4edu/$arch

# ## 南京大学
# Server = https://mirrors.nju.edu.cn/arch4edu/$arch

# ## 平安云
# Server = https://mirrors.pinganyun.com/arch4edu/$arch

# ## 腾讯云
# Server = https://mirrors.tencent.com/arch4edu/$arch

# ## 云南大学
# Server = https://mirrors.ynu.edu.cn/arch4edu/$arch

# ## Keybase
# Server = https://keybase.pub/arch4edu/$arch

EOF
```

### 刷新软件包缓存

```bash
sudo pacman -Syy
```

## 参考

- [AUR 镜像使用帮助](https://mirrors.bfsu.edu.cn/help/AUR/)
- [Arch Linux 中文社区仓库](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/)
- [Arch Linux Chinese Community Repository](https://github.com/archlinuxcn/repo)
- [Arch Linux CN Community repo mirrors list](https://github.com/archlinuxcn/mirrorlist-repo)

- [Archlinux Repository for Education](https://github.com/arch4edu/arch4edu)
- [Unofficial user repositories](https://wiki.archlinux.org/index.php/Unofficial_user_repositories)


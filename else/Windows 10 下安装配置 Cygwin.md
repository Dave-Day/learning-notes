# Windows 10 下安装配置 Cygwin

2019-12-03

## Cygwin 简介

### Cygwin 是什么

Cygwin 是一个可原生运行于 Windows 系统上的 POSXI 兼容环境，GNU 在 Windows 系统上的移植版，是许多自由软件的集合，最初由 Cygnus Solutions 开发，用于各种版本的 Microsoft Windows 上，运行类 UNIX 系统。Cygwin 的主要目的是通过重新编译，将 POSIX 系统上的软件移植到 Windows 上。

> Cygwin是许多自由软件的集合，最初由Cygnus Solutions开发，用于各种版本的Microsoft Windows上，运行类UNIX系统。Cygwin的主要目的是通过重新编译，将POSIX系统（例如Linux、BSD，以及其他Unix系统）上的软件移植到Windows上。Cygwin移植工作在Windows NT上比较好，在Windows 95和Windows 98上，相对差劲一些。目前Cygwin由Red Hat等负责维护。
>
> ​	-- [Cygwin - Wikipedia](https://zh.wikipedia.org/wiki/Cygwin)

> Cygwin是一个在windows平台上运行的类UNIX模拟环境，是cygnus solutions公司开发的自由软件（该公司开发的著名工具还有eCos，不过现已被Redhat收购）。它对于学习UNIX/Linux操作环境，或者从UNIX到Windows的应用程序移植，或者进行某些特殊的开发工作，尤其是使用GNU工具集在Windows上进行嵌入式系统开发，非常有用。随着嵌入式系统开发在国内日渐流行，越来越多的开发者对Cygwin产生了兴趣。
> Cygwin 提供一个UNIX 模拟 DLL 以及在其上层构建的多种可以在 Linux 系统中找到的软件包，在 Windows XP SP3 以上的版本提供良好的支持。Cygwin主要由Red Hat及其下属社区负责维护。
>
> ​	-- [Cygwin - 百度百科](https://baike.baidu.com/item/Cygwin)

更多关于 Cygwin 的介绍可以查看 [Cygwin 系列（一）：Cygwin 是什么 - silaoA](https://zhuanlan.zhihu.com/p/56692626) 。

### Cygwin 优缺点

#### Cygwin 优点

- 首先自然是近乎一致的 UNIX/Linux 体验；
- 完备且相对轻量，普通用户不必安装整个 Linux 系统或虚拟机，就可以获得近乎一致的体验，Cygwin 的程序运行与 Windows 互不干扰，高效的命令行工具与 Windows 图形界面各有所长、形成互补；
- 开源免费，`cygwin1.dll`本身是按照 GPLv3 协议发布的，其他的应用程序有 GPL、LGPL、X11 等多种协议；
- 安装卸载方便，Cygwin 提供了包管理工具，可按需安装/卸载软件包，一个能运行起来的最小 Cygwin 系统只需要几十上百 MB，而完全的 Cygwin 系统需要几十 GB；
- 源码级兼容性，GNU、UNIX、Linux 软件的源代码几乎不用修改就可以在 Cygwin 环境中编译构建成功；
- 与 Windows 互操作，Cygwin 把 Windows 的磁盘挂载到/cygdrive 下，如 c 盘就是`/cygdrive/c`、d 盘就是`/cygdrive/d`，Cygwin 中的应用程序可以读写 Windows 磁盘中的文件，Windows 应用程序也可以读写 Cygwin 目录中的文件（但要注意不要把文件搞乱了）；Cygwin 的 shell 中可以启动 Windows 程序，Windows 的 cmd 中也可以启动 Cygwin 的程序，但由于字符编码不同可能造成乱码；
- 多一套可用的 API，对于 Windows 开发者，程序代码既可以调用 Win32 API，又可以调用 Cygwin API，甚至混合。

#### Cygwin 缺点

- 效率相对低，由于是在 Win32 系统之上模拟实现 POSIX 兼容层，应用程序在底层就多了一个层级的函数调用，效率比 UNIX/Linux 系统上原生的应用程序肯定低，不过这也是在效率和兼容性之间选择的一个平衡；
- 未实现二进制文件级别的兼容，Cygwin 系统上的应用程序编译后仍然是 Windows PE 格式的可执行文件，**UNIX/Linux 系统上的二进制可执行文件在 Cygwin 上不能运行**。
- 与 Windows 互操作不足，Windows 原生程序并不能利用`cygwin1.dll`提供的与 UNIX/Linux 兼容的信号、pty 设备等，除非改写程序代码重新编译，但这样新的程序就依赖于`cygwin1.dll`，就不是“Windows 原生程序”了。

### 相关链接

- [官方主页](http://cygwin.com/)
- [邮件列表](http://cygwin.com/lists.html)
- [镜像列表](http://cygwin.com/mirrors.html)
- [官方文档](http://cygwin.com/docs.html)

## Cygwin 下载安装

### 下载 Cygwin

从 [Cygwin 官网](http://www.cygwin.com/) 下载 [setup-x86.exe](https://cygwin.com/setup-x86.exe)或 [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) 文件。

[setup-x86.exe](https://cygwin.com/setup-x86.exe)或 [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) 文件主要用于安装、更新、卸载应用程序（组件），类似于 GNU/Linux 下的包管理器。

### 安装 Cygwin

1. 双击之前下载的[setup-x86.exe](https://cygwin.com/setup-x86.exe)或 [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) 文件，点击 <kbd>Next(下一步)</kbd> 进行安装。

   ![cygwin_install_01](https://pic.ryanjie.cn/learn/windows/cygwin_install_01.png)

2. 选择`Install from Internet`。如图显示 3种安装方式：

   - `Install from Internet` 是从Internet下载并安装，下载的安装包同时也保留在硬盘中并不删除；

   - `Download Without Installing` 是仅下载，供后期再安装；

   - `Install Local Directory` 是从本地安装，如果前期选择了仅下载，现在选择本地安装即可。然后点击 <kbd>Next(下一步)</kbd> 。![cygwin_install_02](https://pic.ryanjie.cn/learn/windows/cygwin_install_02.png)



3. 选择 cygwin 安装路径。建议默认，如果 C 盘空间不足可以更换到别的盘。例如：`D:\cygwin64`。然后点击 <kbd>Next(下一步)</kbd> 。

   ![cygwin_install_03](https://pic.ryanjie.cn/learn/windows/cygwin_install_03.png)

4. 选择 cygwin 组件包的下载路径。默认下载到用户桌面。建议更改到其他路径。例如：`C:\cygwin_packages`。然后点击 <kbd>Next(下一步)</kbd> 。

   ![cygwin_install_04](https://pic.ryanjie.cn/learn/windows/cygwin_install_04.png)

5. 设置网络代理。没有的点击 <kbd>Next(下一步)</kbd> 。

   ![cygwin_install_055](https://pic.ryanjie.cn/learn/windows/cygwin_install_05.png)

6. 选择官方软件包仓库下载站。从列表中选择以下任意一个官方推荐的国内镜像站即可。

   - 阿里云：`https://mirrors.aliyun.com/cygwin/`
   - USTC：`http://mirrors.ustc.edu.cn/cygwin/`
   - SJTUG：`https://mirrors.sjtug.sjtu.edu.cn/cygwin/`
   - 网易：`http://mirrors.163.com/cygwin/`

   或者在 `User URL` 处输入以下地址：

   - TUNA：`https://mirrors.tuna.tsinghua.edu.cn/cygwin/`
   - BIT：`http://mirror.bit.edu.cn/cygwin/`
   - HUAWEI：`https://mirrors.huaweicloud.com/cygwin/`

   然后点击 <kbd>Next(下一步)</kbd> 。

   ![cygwin_install_06](https://pic.ryanjie.cn/learn/windows/cygwin_install_06.png)

7. 从下载站更新软件包数据，更新完之后点击 <kbd>Next(下一步)</kbd> 。

   ![cygwin_install_07](https://pic.ryanjie.cn/learn/windows/cygwin_install_07.png)

8. 安装需要的组件(软件)，之后点击 <kbd>Next(下一步)</kbd> 。

   ![cygwin_install_08](https://pic.ryanjie.cn/learn/windows/cygwin_install_08.png)

9. 确认需要安装的组件，之后点击 <kbd>Next(下一步)</kbd> 。

![cygwin_install_09](https://pic.ryanjie.cn/learn/windows/cygwin_install_09.png)

10. 创建桌面快捷方式以及开始菜单快捷方式，最后点击 <kbd>Finish(完成)</kbd> 完成 Cygwin 的安装。

![cygwin_install_10](https://pic.ryanjie.cn/learn/windows/cygwin_install_10.png)

## Cygwin 配置

### 选择下载镜像站

选择 Cygwin 官方软件包仓库国内镜像站。以下是官方推荐的国内镜像站。

- 阿里云：`https://mirrors.aliyun.com/cygwin/`
- USTC：`http://mirrors.ustc.edu.cn/cygwin/`
- SJTUG：`https://mirrors.sjtug.sjtu.edu.cn/cygwin/`
- 网易：`http://mirrors.163.com/cygwin/`

或者在 `User URL` 处输入以下地址：

- TUNA：`https://mirrors.tuna.tsinghua.edu.cn/cygwin/`
- BIT：`http://mirror.bit.edu.cn/cygwin/`
- HUAWEI：`https://mirrors.huaweicloud.com/cygwin/`

点击 <kbd>Add</kbd> , 然后选中`https://mirrors.tuna.tsinghua.edu.cn`, 点击 <kbd>下一步 </kbd>进行安装。

> 更多关于 Cygwin 的镜像站内容可以查看官方文档： [Cygwin 镜像列表](https://cygwin.com/mirrors.html)

### 安装配置 ohmyzsh

[![ohmyzsh](https://github-readme-stats.vercel.app/api/pin/?username=ohmyzsh&repo=ohmyzsh&show_owner=true&theme=nightowl)](https://github.com/ohmyzsh/ohmyzsh)

> Oh My Zsh is a delightful, open source, community-driven framework for managing your Zsh configuration. It comes bundled with thousands of helpful functions, helpers, plugins, themes, and a few things that make you shout...

#### 安装 ohmyzsh

双击之前下载的[setup-x86.exe](https://cygwin.com/setup-x86.exe)或 [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) 文件，安装必需的 Cygwin 组件：

- `curl` or `wget`
- `git` （v2.4.11 或更高版本）
- `zsh` （v4.3.9 或更高版本）

```bash
# 克隆 ohmyzsh 仓库
git clone --depth=1 https://hub.fastgit.org/ohmyzsh/ohmyzsh.git /usr/share/oh-my-zsh

# 安装 zsh 插件
git clone --depth=1 https://hub.fastgit.org/zsh-users/zsh-syntax-highlighting.git /usr/share/zsh/plugins/zsh-syntax-highlighting
git clone --depth=1 https://hub.fastgit.org/zsh-users/zsh-completions.git /usr/share/zsh/plugins/zsh-completions
git clone --depth=1 https://hub.fastgit.org/zsh-users/zsh-autosuggestions.git /usr/share/zsh/plugins/zsh-autosuggestions
git clone --depth=1 https://hub.fastgit.org/zsh-users/zsh-history-substring-search.git /usr/share/zsh/plugins/zsh-history-substring-search

# 备份 zsh 配置文件(.zshrc)
cp ~/.zshrc ~/.zshrc.bak

# 生成 zsh 配置文件(.zshrc)
cp /usr/share/oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

# 更换默认 shell
# chsh -s $(which zsh)
# chsh -s /bin/zsh
echo "exec zsh" >> .bashrc
```

1. 因为国内网络原因，导致在安装过程中访问下载 Github 资源的速度不是很理想，所以在这里选择了手动安装。如果有网络代理可以直接直接使用以下命令安装。

   | Method    | Command                                                      |
   | --------- | ------------------------------------------------------------ |
   | **curl**  | `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` |
   | **wget**  | `sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` |
   | **fetch** | `sh -c "$(fetch -o - https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` |

2. 因为 Cygwin 中没有 chsh ，不能执行 `chsh -s $(which zsh)` 命令。所以选择在 `.bashrc` 中添加执行 zsh 终端的命令手动启动 zsh。

3. 在执行完上面命令之后需要重启终端。终端重启之后会自动加载 zsh 的配置文件。

#### 配置 ohmyzsh

下面是 我的 zsh 配置文件(.zshrc)。

```bash
# Path to your oh-my-zsh installation.
export ZSH="/usr/share/oh-my-zsh"

# Case-sensitive completion.
CASE_SENSITIVE="true"

# Disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Disable auto-setting terminal title.
DISABLE_AUTO_TITLE="true"

# Disable marking untracked files under VCS as dirty.
DISABLE_UNTRACKED_FILES_DIRTY="true"

# History.
HIST_STAMPS="yyyy-mm-dd"

# Themes
# See https://github.com/ohmyzsh/ohmyzsh/wiki
ZSH_THEME="agnoster"

# Would you like to use another custom folder than $ZSH/custom?
ZSH_CUSTOM=/usr/share/zsh
## Plugins section: Enable fish style features
# # Use Auto suggestions
# source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
# # Use completions
# source /usr/share/zsh/plugins/zsh-completions/zsh-completions.plugin.zsh
# # Use syntax highlighting
# source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
# # Use history substring search
# source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
# # bind UP and DOWN arrow keys to history substring search
zmodload zsh/terminfo
# bindkey "$terminfo[kcuu1]" history-substring-search-up
# bindkey "$terminfo[kcud1]" history-substring-search-down
# bindkey '^[[A' history-substring-search-up			
# bindkey '^[[B' history-substring-search-down

# Plugins
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins
plugins=(extract git docker-compose git-flow git-hubflow git-prompt gitignore zsh-syntax-highlighting zsh-completions zsh-autosuggestions zsh-history-substring-search) 
 
source $ZSH/oh-my-zsh.sh

# Aliases.
# source ~/.aliases

# Environment variables.
# source ~/.exports

# Functions.
# source ~/.functions

# dircolors.
if [ -x "$(command -v dircolors)" ]; then
    eval "$(dircolors -b ~/.dircolors)"
fi

# You may need to manually set your language environment
# export LANG=zh_CN.UTF-8

## Options section
setopt correct                                                  # Auto correct mistakes
setopt extendedglob                                             # Extended globbing. Allows using regular expressions with *
setopt nocaseglob                                               # Case insensitive globbing
setopt rcexpandparam                                            # Array expension with parameters
setopt nocheckjobs                                              # Don't warn about running processes when exiting
setopt numericglobsort                                          # Sort filenames numerically when it makes sense
setopt nobeep                                                   # No beep
setopt appendhistory                                            # Immediately append history instead of overwriting
setopt histignorealldups                                        # If a new command is a duplicate, remove the older one
setopt autocd  
# enable substitution for prompt
setopt prompt_subst                                                 # if only directory path is entered, cd there.

zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'       # Case insensitive tab completion
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"         # Colored completion (different colors for dirs/files/etc)
zstyle ':completion:*' rehash true                              # automatically find new executables in path 
# Speed up completions
zstyle ':completion:*' accept-exact '*(N)'
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache
HISTFILE=~/.zhistory
HISTSIZE=1000
SAVEHIST=500
#export EDITOR=/usr/bin/nano
#export VISUAL=/usr/bin/nano
WORDCHARS=${WORDCHARS//\/[&.;]}                                 # Don't consider certain characters part of the word

## Keybindings section
bindkey -e
bindkey '^[[7~' beginning-of-line                               # Home key
bindkey '^[[H' beginning-of-line                                # Home key
if [[ "${terminfo[khome]}" != "" ]]; then
  bindkey "${terminfo[khome]}" beginning-of-line                # [Home] - Go to beginning of line
fi
bindkey '^[8~' end-of-line                                     # End key
bindkey '^[[F' end-of-line                                     # End key
if [[ "${terminfo[kend]}" != "" ]]; then
  bindkey "${terminfo[kend]}" end-of-line                       # [End] - Go to end of line
fi
bindkey '^[[2~' overwrite-mode                                  # Insert key
bindkey '^[[3~' delete-char                                     # Delete key
bindkey '^[[C'  forward-char                                    # Right key
bindkey '^[[D'  backward-char                                   # Left key
bindkey '^[[5~' history-beginning-search-backward               # Page up key
bindkey '^[[6~' history-beginning-search-forward                # Page down key

# Navigate words with ctrl+arrow keys
bindkey '^[Oc' forward-word                                     #
bindkey '^[Od' backward-word                                    #
bindkey '^[[1;5D' backward-word                                 #
bindkey '^[[1;5C' forward-word                                  #
bindkey '^H' backward-kill-word                                 # delete previous word with ctrl+backspace
bindkey '^[[Z' undo     

# Theming section  
autoload -U compinit colors zcalc
compinit -d
colors
```

### 安装配置 vim

#### 安装 vim

双击之前下载的[setup-x86.exe](https://cygwin.com/setup-x86.exe)或 [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) 文件，安装 vim 组件即可。

#### 配置 vim

```bash
# Create your .vimrc：https://vim-bootstrap.com/
curl 'https://vim-bootstrap.com/generate.vim' --data 'editor=vim&frameworks=vuejs&langs=c&langs=go&langs=html&langs=javascript&langs=lua&langs=php&langs=perl&langs=python&langs=ruby&langs=rust&langs=typescript' > ~/.vimrc

# Set up plug.vim
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://cdn.jsdelivr.net/gh/junegunn/vim-plug@master/plug.vim

# Install Plugins： Launch vim and run :PlugInstall
vim +PlugInstall +qall
vim +VimBootstrapUpdate +qall
```

vim 的配置文件(.vimrc)，我是使用 [Vim Bootstrap](https://github.com/editor-bootstrap/vim-bootstrap) 生成工具自动生成。

[![Vim Bootstrap](https://github-readme-stats.vercel.app/api/pin/?username=editor-bootstrap&repo=vim-bootstrap&show_owner=true&theme=nightowl)](https://github.com/editor-bootstrap/vim-bootstrap)

> vim-bootstrap：一个简单、易用的 `.vimrc` 配置文件生成工具，也可通过网站点选生成。支持 Vim、NeoVim、NeoVim-Qt、MacVim 和 GVim。

- Gitee Gist：[hellozxj / init.vim](https://gitee.com/helloryan/codes/3d25qcxfo6tswia4ghepk72)

- Vim Bootstrap：[https://vim-bootstrap.com](https://vim-bootstrap.com)

- Vim Bootstrap Github：[https://github.com/editor-bootstrap/vim-bootstrap](https://github.com/editor-bootstrap/vim-bootstrap)

- 本地备份

  ```bash
  " vim-bootstrap
  
  "*****************************************************************************
  "" Vim-Plug core
  "*****************************************************************************
  let vimplug_exists=expand('~/.vim/autoload/plug.vim')
  if has('win32')&&!has('win64')
    let curl_exists=expand('C:\Windows\Sysnative\curl.exe')
  else
    let curl_exists=expand('curl')
  endif
  
  let g:vim_bootstrap_langs = "c,elixir,elm,erlang,go,haskell,html,javascript,lisp,lua,ocaml,perl,php,python,ruby,rust,scala,typescript"
  let g:vim_bootstrap_editor = "vim"				" nvim or vim
  let g:vim_bootstrap_theme = "molokai"
  let g:vim_bootstrap_frams = "vuejs"
  
  if !filereadable(vimplug_exists)
    if !executable(curl_exists)
      echoerr "You have to install curl or first install vim-plug yourself!"
      execute "q!"
    endif
    echo "Installing Vim-Plug..."
    echo ""
    silent exec "!"curl_exists" -fLo " . shellescape(vimplug_exists) . " --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
    let g:not_finish_vimplug = "yes"
  
    autocmd VimEnter * PlugInstall
  endif
  
  " Required:
  call plug#begin(expand('~/.vim/plugged'))
  
  "*****************************************************************************
  "" Plug install packages
  "*****************************************************************************
  Plug 'scrooloose/nerdtree'
  Plug 'jistr/vim-nerdtree-tabs'
  Plug 'tpope/vim-commentary'
  Plug 'tpope/vim-fugitive'
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  Plug 'airblade/vim-gitgutter'
  Plug 'vim-scripts/grep.vim'
  Plug 'vim-scripts/CSApprox'
  Plug 'Raimondi/delimitMate'
  Plug 'majutsushi/tagbar'
  Plug 'dense-analysis/ale'
  Plug 'Yggdroot/indentLine'
  Plug 'editor-bootstrap/vim-bootstrap-updater'
  Plug 'tpope/vim-rhubarb' " required by fugitive to :Gbrowse
  Plug 'tomasr/molokai'
  
  
  if isdirectory('/usr/local/opt/fzf')
    Plug '/usr/local/opt/fzf' | Plug 'junegunn/fzf.vim'
  else
    Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --bin' }
    Plug 'junegunn/fzf.vim'
  endif
  let g:make = 'gmake'
  if exists('make')
          let g:make = 'make'
  endif
  Plug 'Shougo/vimproc.vim', {'do': g:make}
  
  "" Vim-Session
  Plug 'xolox/vim-misc'
  Plug 'xolox/vim-session'
  
  "" Snippets
  Plug 'SirVer/ultisnips'
  Plug 'honza/vim-snippets'
  
  "*****************************************************************************
  "" Custom bundles
  "*****************************************************************************
  
  " c
  Plug 'vim-scripts/c.vim', {'for': ['c', 'cpp']}
  Plug 'ludwig/split-manpage.vim'
  
  
  " elixir
  Plug 'elixir-lang/vim-elixir'
  Plug 'carlosgaldino/elixir-snippets'
  
  
  " elm
  "" Elm Bundle
  Plug 'elmcast/elm-vim'
  
  
  " erlang
  Plug 'jimenezrick/vimerl'
  
  
  " go
  "" Go Lang Bundle
  Plug 'fatih/vim-go', {'do': ':GoInstallBinaries'}
  
  
  " haskell
  "" Haskell Bundle
  Plug 'eagletmt/neco-ghc'
  Plug 'dag/vim2hs'
  Plug 'pbrisbin/vim-syntax-shakespeare'
  
  
  " html
  "" HTML Bundle
  Plug 'hail2u/vim-css3-syntax'
  Plug 'gko/vim-coloresque'
  Plug 'tpope/vim-haml'
  Plug 'mattn/emmet-vim'
  
  
  " javascript
  "" Javascript Bundle
  Plug 'jelera/vim-javascript-syntax'
  
  
  " lisp
  "" Lisp Bundle
  Plug 'vim-scripts/slimv.vim'
  
  
  " lua
  "" Lua Bundle
  Plug 'xolox/vim-lua-ftplugin'
  Plug 'xolox/vim-lua-inspect'
  
  
  " ocaml
  "" OCaml Bundle
  Plug 'def-lkb/ocp-indent-vim'
  
  
  " perl
  "" Perl Bundle
  Plug 'vim-perl/vim-perl'
  Plug 'c9s/perlomni.vim'
  
  
  " php
  "" PHP Bundle
  Plug 'phpactor/phpactor', {'for': 'php', 'do': 'composer install --no-dev -o'}
  Plug 'stephpy/vim-php-cs-fixer'
  
  
  " python
  "" Python Bundle
  Plug 'davidhalter/jedi-vim'
  Plug 'raimon49/requirements.txt.vim', {'for': 'requirements'}
  
  
  " ruby
  Plug 'tpope/vim-rails'
  Plug 'tpope/vim-rake'
  Plug 'tpope/vim-projectionist'
  Plug 'thoughtbot/vim-rspec'
  Plug 'ecomba/vim-ruby-refactoring', {'tag': 'main'}
  
  
  " rust
  " Vim racer
  Plug 'racer-rust/vim-racer'
  
  " Rust.vim
  Plug 'rust-lang/rust.vim'
  
  " Async.vim
  Plug 'prabirshrestha/async.vim'
  
  " Vim lsp
  Plug 'prabirshrestha/vim-lsp'
  
  " Asyncomplete.vim
  Plug 'prabirshrestha/asyncomplete.vim'
  
  " Asyncomplete lsp.vim
  Plug 'prabirshrestha/asyncomplete-lsp.vim'
  
  
  " scala
  if has('python')
      " sbt-vim
      Plug 'ktvoelker/sbt-vim'
  endif
  " vim-scala
  Plug 'derekwyatt/vim-scala'
  
  
  " typescript
  Plug 'leafgarland/typescript-vim'
  Plug 'HerringtonDarkholme/yats.vim'
  
  
  " vuejs
  Plug 'posva/vim-vue'
  Plug 'leafOfTree/vim-vue-plugin'
  
  
  
  "*****************************************************************************
  "*****************************************************************************
  
  "" Include user's extra bundle
  if filereadable(expand("~/.vimrc.local.bundles"))
    source ~/.vimrc.local.bundles
  endif
  
  call plug#end()
  
  " Required:
  filetype plugin indent on
  
  
  "*****************************************************************************
  "" Basic Setup
  "*****************************************************************************"
  "" Encoding
  set encoding=utf-8
  set fileencoding=utf-8
  set fileencodings=utf-8
  set ttyfast
  
  "" Fix backspace indent
  set backspace=indent,eol,start
  
  "" Tabs. May be overridden by autocmd rules
  set tabstop=4
  set softtabstop=0
  set shiftwidth=4
  set expandtab
  
  "" Map leader to ,
  let mapleader=','
  
  "" Enable hidden buffers
  set hidden
  
  "" Searching
  set hlsearch
  set incsearch
  set ignorecase
  set smartcase
  
  set fileformats=unix,dos,mac
  
  if exists('$SHELL')
      set shell=$SHELL
  else
      set shell=/bin/sh
  endif
  
  " session management
  let g:session_directory = "~/.vim/session"
  let g:session_autoload = "no"
  let g:session_autosave = "no"
  let g:session_command_aliases = 1
  
  "*****************************************************************************
  "" Visual Settings
  "*****************************************************************************
  syntax on
  set ruler
  set number
  
  let no_buffers_menu=1
  colorscheme molokai
  
  
  set mousemodel=popup
  set t_Co=256
  set guioptions=egmrti
  set gfn=Monospace\ 10
  
  if has("gui_running")
    if has("gui_mac") || has("gui_macvim")
      set guifont=Menlo:h12
      set transparency=7
    endif
  else
    let g:CSApprox_loaded = 1
  
    " IndentLine
    let g:indentLine_enabled = 1
    let g:indentLine_concealcursor = 0
    let g:indentLine_char = '┆'
    let g:indentLine_faster = 1
  
    
    if $COLORTERM == 'gnome-terminal'
      set term=gnome-256color
    else
      if $TERM == 'xterm'
        set term=xterm-256color
      endif
    endif
    
  endif
  
  
  if &term =~ '256color'
    set t_ut=
  endif
  
  
  "" Disable the blinking cursor.
  set gcr=a:blinkon0
  
  set scrolloff=3
  
  
  "" Status bar
  set laststatus=2
  
  "" Use modeline overrides
  set modeline
  set modelines=10
  
  set title
  set titleold="Terminal"
  set titlestring=%F
  
  set statusline=%F%m%r%h%w%=(%{&ff}/%Y)\ (line\ %l\/%L,\ col\ %c)\
  
  " Search mappings: These will make it so that going to the next one in a
  " search will center on the line it's found in.
  nnoremap n nzzzv
  nnoremap N Nzzzv
  
  if exists("*fugitive#statusline")
    set statusline+=%{fugitive#statusline()}
  endif
  
  " vim-airline
  let g:airline_theme = 'powerlineish'
  let g:airline#extensions#branch#enabled = 1
  let g:airline#extensions#ale#enabled = 1
  let g:airline#extensions#tabline#enabled = 1
  let g:airline#extensions#tagbar#enabled = 1
  let g:airline_skip_empty_sections = 1
  
  "*****************************************************************************
  "" Abbreviations
  "*****************************************************************************
  "" no one is really happy until you have this shortcuts
  cnoreabbrev W! w!
  cnoreabbrev Q! q!
  cnoreabbrev Qall! qall!
  cnoreabbrev Wq wq
  cnoreabbrev Wa wa
  cnoreabbrev wQ wq
  cnoreabbrev WQ wq
  cnoreabbrev W w
  cnoreabbrev Q q
  cnoreabbrev Qall qall
  
  "" NERDTree configuration
  let g:NERDTreeChDirMode=2
  let g:NERDTreeIgnore=['\.rbc$', '\~$', '\.pyc$', '\.db$', '\.sqlite$', '__pycache__']
  let g:NERDTreeSortOrder=['^__\.py$', '\/$', '*', '\.swp$', '\.bak$', '\~$']
  let g:NERDTreeShowBookmarks=1
  let g:nerdtree_tabs_focus_on_files=1
  let g:NERDTreeMapOpenInTabSilent = '<RightMouse>'
  let g:NERDTreeWinSize = 50
  set wildignore+=*/tmp/*,*.so,*.swp,*.zip,*.pyc,*.db,*.sqlite
  nnoremap <silent> <F2> :NERDTreeFind<CR>
  nnoremap <silent> <F3> :NERDTreeToggle<CR>
  
  " grep.vim
  nnoremap <silent> <leader>f :Rgrep<CR>
  let Grep_Default_Options = '-IR'
  let Grep_Skip_Files = '*.log *.db'
  let Grep_Skip_Dirs = '.git node_modules'
  
  " terminal emulation
  nnoremap <silent> <leader>sh :terminal<CR>
  
  
  "*****************************************************************************
  "" Commands
  "*****************************************************************************
  " remove trailing whitespaces
  command! FixWhitespace :%s/\s\+$//e
  
  "*****************************************************************************
  "" Functions
  "*****************************************************************************
  if !exists('*s:setupWrapping')
    function s:setupWrapping()
      set wrap
      set wm=2
      set textwidth=79
    endfunction
  endif
  
  "*****************************************************************************
  "" Autocmd Rules
  "*****************************************************************************
  "" The PC is fast enough, do syntax highlight syncing from start unless 200 lines
  augroup vimrc-sync-fromstart
    autocmd!
    autocmd BufEnter * :syntax sync maxlines=200
  augroup END
  
  "" Remember cursor position
  augroup vimrc-remember-cursor-position
    autocmd!
    autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g`\"" | endif
  augroup END
  
  "" txt
  augroup vimrc-wrapping
    autocmd!
    autocmd BufRead,BufNewFile *.txt call s:setupWrapping()
  augroup END
  
  "" make/cmake
  augroup vimrc-make-cmake
    autocmd!
    autocmd FileType make setlocal noexpandtab
    autocmd BufNewFile,BufRead CMakeLists.txt setlocal filetype=cmake
  augroup END
  
  set autoread
  
  "*****************************************************************************
  "" Mappings
  "*****************************************************************************
  
  "" Split
  noremap <Leader>h :<C-u>split<CR>
  noremap <Leader>v :<C-u>vsplit<CR>
  
  "" Git
  noremap <Leader>ga :Gwrite<CR>
  noremap <Leader>gc :Gcommit<CR>
  noremap <Leader>gsh :Gpush<CR>
  noremap <Leader>gll :Gpull<CR>
  noremap <Leader>gs :Gstatus<CR>
  noremap <Leader>gb :Gblame<CR>
  noremap <Leader>gd :Gvdiff<CR>
  noremap <Leader>gr :Gremove<CR>
  
  " session management
  nnoremap <leader>so :OpenSession<Space>
  nnoremap <leader>ss :SaveSession<Space>
  nnoremap <leader>sd :DeleteSession<CR>
  nnoremap <leader>sc :CloseSession<CR>
  
  "" Tabs
  nnoremap <Tab> gt
  nnoremap <S-Tab> gT
  nnoremap <silent> <S-t> :tabnew<CR>
  
  "" Set working directory
  nnoremap <leader>. :lcd %:p:h<CR>
  
  "" Opens an edit command with the path of the currently edited file filled in
  noremap <Leader>e :e <C-R>=expand("%:p:h") . "/" <CR>
  
  "" Opens a tab edit command with the path of the currently edited file filled
  noremap <Leader>te :tabe <C-R>=expand("%:p:h") . "/" <CR>
  
  "" fzf.vim
  set wildmode=list:longest,list:full
  set wildignore+=*.o,*.obj,.git,*.rbc,*.pyc,__pycache__
  let $FZF_DEFAULT_COMMAND =  "find * -path '*/\.*' -prune -o -path 'node_modules/**' -prune -o -path 'target/**' -prune -o -path 'dist/**' -prune -o  -type f -print -o -type l -print 2> /dev/null"
  
  " The Silver Searcher
  if executable('ag')
    let $FZF_DEFAULT_COMMAND = 'ag --hidden --ignore .git -g ""'
    set grepprg=ag\ --nogroup\ --nocolor
  endif
  
  " ripgrep
  if executable('rg')
    let $FZF_DEFAULT_COMMAND = 'rg --files --hidden --follow --glob "!.git/*"'
    set grepprg=rg\ --vimgrep
    command! -bang -nargs=* Find call fzf#vim#grep('rg --column --line-number --no-heading --fixed-strings --ignore-case --hidden --follow --glob "!.git/*" --color "always" '.shellescape(<q-args>).'| tr -d "\017"', 1, <bang>0)
  endif
  
  cnoremap <C-P> <C-R>=expand("%:p:h") . "/" <CR>
  nnoremap <silent> <leader>b :Buffers<CR>
  nnoremap <silent> <leader>e :FZF -m<CR>
  "Recovery commands from history through FZF
  nmap <leader>y :History:<CR>
  
  " snippets
  let g:UltiSnipsExpandTrigger="<tab>"
  let g:UltiSnipsJumpForwardTrigger="<tab>"
  let g:UltiSnipsJumpBackwardTrigger="<c-b>"
  let g:UltiSnipsEditSplit="vertical"
  
  " ale
  let g:ale_linters = {}
  
  " Tagbar
  nmap <silent> <F4> :TagbarToggle<CR>
  let g:tagbar_autofocus = 1
  
  " Disable visualbell
  set noerrorbells visualbell t_vb=
  if has('autocmd')
    autocmd GUIEnter * set visualbell t_vb=
  endif
  
  "" Copy/Paste/Cut
  if has('unnamedplus')
    set clipboard=unnamed,unnamedplus
  endif
  
  noremap YY "+y<CR>
  noremap <leader>p "+gP<CR>
  noremap XX "+x<CR>
  
  if has('macunix')
    " pbcopy for OSX copy/paste
    vmap <C-x> :!pbcopy<CR>
    vmap <C-c> :w !pbcopy<CR><CR>
  endif
  
  "" Buffer nav
  noremap <leader>z :bp<CR>
  noremap <leader>q :bp<CR>
  noremap <leader>x :bn<CR>
  noremap <leader>w :bn<CR>
  
  "" Close buffer
  noremap <leader>c :bd<CR>
  
  "" Clean search (highlight)
  nnoremap <silent> <leader><space> :noh<cr>
  
  "" Switching windows
  noremap <C-j> <C-w>j
  noremap <C-k> <C-w>k
  noremap <C-l> <C-w>l
  noremap <C-h> <C-w>h
  
  "" Vmap for maintain Visual Mode after shifting > and <
  vmap < <gv
  vmap > >gv
  
  "" Move visual block
  vnoremap J :m '>+1<CR>gv=gv
  vnoremap K :m '<-2<CR>gv=gv
  
  "" Open current line on GitHub
  nnoremap <Leader>o :.Gbrowse<CR>
  
  "*****************************************************************************
  "" Custom configs
  "*****************************************************************************
  
  " c
  autocmd FileType c setlocal tabstop=4 shiftwidth=4 expandtab
  autocmd FileType cpp setlocal tabstop=4 shiftwidth=4 expandtab
  
  
  " elixir
  
  
  " elm
  " elm-vim
  let g:elm_setup_keybindings = 0
  let g:elm_format_autosave = 1
  
  
  " erlang
  let erlang_folding = 1
  let erlang_show_errors = 1
  
  
  " go
  " vim-go
  " run :GoBuild or :GoTestCompile based on the go file
  function! s:build_go_files()
    let l:file = expand('%')
    if l:file =~# '^\f\+_test\.go$'
      call go#test#Test(0, 1)
    elseif l:file =~# '^\f\+\.go$'
      call go#cmd#Build(0)
    endif
  endfunction
  
  let g:go_list_type = "quickfix"
  let g:go_fmt_command = "goimports"
  let g:go_fmt_fail_silently = 1
  
  let g:go_highlight_types = 1
  let g:go_highlight_fields = 1
  let g:go_highlight_functions = 1
  let g:go_highlight_methods = 1
  let g:go_highlight_operators = 1
  let g:go_highlight_build_constraints = 1
  let g:go_highlight_structs = 1
  let g:go_highlight_generate_tags = 1
  let g:go_highlight_space_tab_error = 0
  let g:go_highlight_array_whitespace_error = 0
  let g:go_highlight_trailing_whitespace_error = 0
  let g:go_highlight_extra_types = 1
  
  autocmd BufNewFile,BufRead *.go setlocal noexpandtab tabstop=4 shiftwidth=4 softtabstop=4
  
  augroup completion_preview_close
    autocmd!
    if v:version > 703 || v:version == 703 && has('patch598')
      autocmd CompleteDone * if !&previewwindow && &completeopt =~ 'preview' | silent! pclose | endif
    endif
  augroup END
  
  augroup go
  
    au!
    au Filetype go command! -bang A call go#alternate#Switch(<bang>0, 'edit')
    au Filetype go command! -bang AV call go#alternate#Switch(<bang>0, 'vsplit')
    au Filetype go command! -bang AS call go#alternate#Switch(<bang>0, 'split')
    au Filetype go command! -bang AT call go#alternate#Switch(<bang>0, 'tabe')
  
    au FileType go nmap <Leader>dd <Plug>(go-def-vertical)
    au FileType go nmap <Leader>dv <Plug>(go-doc-vertical)
    au FileType go nmap <Leader>db <Plug>(go-doc-browser)
  
    au FileType go nmap <leader>r  <Plug>(go-run)
    au FileType go nmap <leader>t  <Plug>(go-test)
    au FileType go nmap <Leader>gt <Plug>(go-coverage-toggle)
    au FileType go nmap <Leader>i <Plug>(go-info)
    au FileType go nmap <silent> <Leader>l <Plug>(go-metalinter)
    au FileType go nmap <C-g> :GoDecls<cr>
    au FileType go nmap <leader>dr :GoDeclsDir<cr>
    au FileType go imap <C-g> <esc>:<C-u>GoDecls<cr>
    au FileType go imap <leader>dr <esc>:<C-u>GoDeclsDir<cr>
    au FileType go nmap <leader>rb :<C-u>call <SID>build_go_files()<CR>
  
  augroup END
  
  " ale
  :call extend(g:ale_linters, {
      \"go": ['golint', 'go vet'], })
  
  
  " haskell
  let g:haskell_conceal_wide = 1
  let g:haskell_multiline_strings = 1
  let g:necoghc_enable_detailed_browse = 1
  autocmd Filetype haskell setlocal omnifunc=necoghc#omnifunc
  
  
  " html
  " for html files, 2 spaces
  autocmd Filetype html setlocal ts=2 sw=2 expandtab
  
  
  " javascript
  let g:javascript_enable_domhtmlcss = 1
  
  " vim-javascript
  augroup vimrc-javascript
    autocmd!
    autocmd FileType javascript setl tabstop=4|setl shiftwidth=4|setl expandtab softtabstop=4
  augroup END
  
  
  " lisp
  
  
  " lua
  
  
  " ocaml
  " Add Merlin to rtp
  let g:opamshare = substitute(system('opam config var share'),'\n$','','''')
  execute "set rtp+=" . g:opamshare . "/merlin/vim"
  
  " ale
  :call extend(g:ale_linters, {
      \'ocaml': ['merlin'], })
  
  
  " perl
  
  
  " php
  " Phpactor plugin
  " Include use statement
  nmap <Leader>u :call phpactor#UseAdd()<CR>
  " Invoke the context menu
  nmap <Leader>mm :call phpactor#ContextMenu()<CR>
  " Invoke the navigation menu
  nmap <Leader>nn :call phpactor#Navigate()<CR>
  " Goto definition of class or class member under the cursor
  nmap <Leader>oo :call phpactor#GotoDefinition()<CR>
  nmap <Leader>oh :call phpactor#GotoDefinitionHsplit()<CR>
  nmap <Leader>ov :call phpactor#GotoDefinitionVsplit()<CR>
  nmap <Leader>ot :call phpactor#GotoDefinitionTab()<CR>
  " Show brief information about the symbol under the cursor
  nmap <Leader>K :call phpactor#Hover()<CR>
  " Transform the classes in the current file
  nmap <Leader>tt :call phpactor#Transform()<CR>
  " Generate a new class (replacing the current file)
  nmap <Leader>cc :call phpactor#ClassNew()<CR>
  " Extract expression (normal mode)
  nmap <silent><Leader>ee :call phpactor#ExtractExpression(v:false)<CR>
  " Extract expression from selection
  vmap <silent><Leader>ee :<C-U>call phpactor#ExtractExpression(v:true)<CR>
  " Extract method from selection
  vmap <silent><Leader>em :<C-U>call phpactor#ExtractMethod()<CR>
  
  
  " python
  " vim-python
  augroup vimrc-python
    autocmd!
    autocmd FileType python setlocal expandtab shiftwidth=4 tabstop=8 colorcolumn=79
        \ formatoptions+=croq softtabstop=4
        \ cinwords=if,elif,else,for,while,try,except,finally,def,class,with
  augroup END
  
  " jedi-vim
  let g:jedi#popup_on_dot = 0
  let g:jedi#goto_assignments_command = "<leader>g"
  let g:jedi#goto_definitions_command = "<leader>d"
  let g:jedi#documentation_command = "K"
  let g:jedi#usages_command = "<leader>n"
  let g:jedi#rename_command = "<leader>r"
  let g:jedi#show_call_signatures = "0"
  let g:jedi#completions_command = "<C-Space>"
  let g:jedi#smart_auto_mappings = 0
  
  " ale
  :call extend(g:ale_linters, {
      \'python': ['flake8'], })
  
  " vim-airline
  let g:airline#extensions#virtualenv#enabled = 1
  
  " Syntax highlight
  let python_highlight_all = 1
  
  
  " ruby
  let g:rubycomplete_buffer_loading = 1
  let g:rubycomplete_classes_in_global = 1
  let g:rubycomplete_rails = 1
  
  augroup vimrc-ruby
    autocmd!
    autocmd BufNewFile,BufRead *.rb,*.rbw,*.gemspec setlocal filetype=ruby
    autocmd FileType ruby set tabstop=2|set shiftwidth=2|set expandtab softtabstop=2
  augroup END
  
  let g:tagbar_type_ruby = {
      \ 'kinds' : [
          \ 'm:modules',
          \ 'c:classes',
          \ 'd:describes',
          \ 'C:contexts',
          \ 'f:methods',
          \ 'F:singleton methods'
      \ ]
  \ }
  
  " RSpec.vim mappings
  map <Leader>t :call RunCurrentSpecFile()<CR>
  map <Leader>s :call RunNearestSpec()<CR>
  map <Leader>l :call RunLastSpec()<CR>
  map <Leader>a :call RunAllSpecs()<CR>
  
  " For ruby refactory
  if has('nvim')
    runtime! macros/matchit.vim
  else
    packadd! matchit
  endif
  
  " Ruby refactory
  nnoremap <leader>rap  :RAddParameter<cr>
  nnoremap <leader>rcpc :RConvertPostConditional<cr>
  nnoremap <leader>rel  :RExtractLet<cr>
  vnoremap <leader>rec  :RExtractConstant<cr>
  vnoremap <leader>relv :RExtractLocalVariable<cr>
  nnoremap <leader>rit  :RInlineTemp<cr>
  vnoremap <leader>rrlv :RRenameLocalVariable<cr>
  vnoremap <leader>rriv :RRenameInstanceVariable<cr>
  vnoremap <leader>rem  :RExtractMethod<cr>
  
  
  " rust
  " Vim racer
  au FileType rust nmap gd <Plug>(rust-def)
  au FileType rust nmap gs <Plug>(rust-def-split)
  au FileType rust nmap gx <Plug>(rust-def-vertical)
  au FileType rust nmap <leader>gd <Plug>(rust-doc)
  
  
  " scala
  
  
  " typescript
  let g:yats_host_keyword = 1
  
  
  
  " vuejs
  " vim vue
  let g:vue_disable_pre_processors=1
  " vim vue plugin
  let g:vim_vue_plugin_load_full_syntax = 1
  
  
  "*****************************************************************************
  "*****************************************************************************
  
  "" Include user's local vim config
  if filereadable(expand("~/.vimrc.local"))
    source ~/.vimrc.local
  endif
  
  "*****************************************************************************
  "" Convenience variables
  "*****************************************************************************
  
  " vim-airline
  if !exists('g:airline_symbols')
    let g:airline_symbols = {}
  endif
  
  if !exists('g:airline_powerline_fonts')
    let g:airline#extensions#tabline#left_sep = ' '
    let g:airline#extensions#tabline#left_alt_sep = '|'
    let g:airline_left_sep          = '▶'
    let g:airline_left_alt_sep      = '»'
    let g:airline_right_sep         = '◀'
    let g:airline_right_alt_sep     = '«'
    let g:airline#extensions#branch#prefix     = '⤴' "➔, ➥, ⎇
    let g:airline#extensions#readonly#symbol   = '⊘'
    let g:airline#extensions#linecolumn#prefix = '¶'
    let g:airline#extensions#paste#symbol      = 'ρ'
    let g:airline_symbols.linenr    = '␊'
    let g:airline_symbols.branch    = '⎇'
    let g:airline_symbols.paste     = 'ρ'
    let g:airline_symbols.paste     = 'Þ'
    let g:airline_symbols.paste     = '∥'
    let g:airline_symbols.whitespace = 'Ξ'
  else
    let g:airline#extensions#tabline#left_sep = ''
    let g:airline#extensions#tabline#left_alt_sep = ''
  
    " powerline symbols
    let g:airline_left_sep = ''
    let g:airline_left_alt_sep = ''
    let g:airline_right_sep = ''
    let g:airline_right_alt_sep = ''
    let g:airline_symbols.branch = ''
    let g:airline_symbols.readonly = ''
    let g:airline_symbols.linenr = ''
  endif
  ```

## 参考

- [Cygwin - Wikipedia](https://zh.wikipedia.org/wiki/Cygwin)

- [Cygwin - 百度百科](https://baike.baidu.com/item/Cygwin)
- [Cygwin 系列（一）：Cygwin 是什么 - silaoA](https://zhuanlan.zhihu.com/p/56692626)
- [Cygwin 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/cygwin/)
- [Cygwin 镜像列表](https://cygwin.com/mirrors.html)

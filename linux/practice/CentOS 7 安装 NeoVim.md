# CentOS 7 安装 NeoVim



## 源码安装

需求：

- Clang or GCC (4.4+)
- CMake (2.8.12+)

```bash
sudo su - 
yum -y install ninja-build libtool autoconf automake cmake gcc gcc-c++ make pkgconfig unzip patch
cd /usr/src/
# git clone https://hub.fastgit.org/neovim/neovim.git
# git remote set-url origin https://github.com/neovim/neovim.git
git clone https://github.com/neovim/neovim.git
cd neovim && git checkout stable
make CMAKE_BUILD_TYPE=Release
make install
```

查看程序位置：

```bash
$ which nvim
/usr/local/bin/nvim
```

卸载：

```bash
$ sudo rm /usr/local/bin/nvim
$ sudo rm -r /usr/local/share/nvim/
```

## yum 安装

```shell
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install neovim
brew install neovim
```


---
title: Linux 系统服务器设置 SSH 密钥登录
abstract: Linux 系统服务器的 SSH 登录方式最常见的有两种：通过用户密码登录或者采用密钥免密登录。安全起见，建议在 SSH 登录时采用密钥对方式进行登录服务器。
url: linux-ssh-key-login
permalink: linux-ssh-key-login
date: 2020-11-12 18:52:36
category:
  - Linux
tags:
  - Linux
---

![linux-ssh-key-login](https://img.zxj.guru/2020/11/linux-ssh-key-login.png)

Linux 系统服务器的 SSH 登录方式最常见的有两种：通过用户密码登录或者采用密钥对登录。其中使用用户密码方式登录，容易有密码被暴力破解的问题。为了安全，可以使用 [1Password 密码生成器](https://1password.com/zh-cn/password-generator/) 生成长度 30 位，包含大小写字母、数字和符号的用户密码，并且定期更换密码，这样就导致密码总是记不住，每次登录服务器都需要找一下密码。所以我们在远程 SSH 登录时采用第二章方式：使用密钥对登录服务器。

密钥形式登录的原理是：利用密钥生成器制作一对密钥(公钥+私钥)。将公钥添加到服务器的某个账户上，然后在客户端利用私钥即可完成认证并登录。这样一来，没有私钥，任何人都无法通过 SSH 暴力破解你的密码来远程登录到系统。此外，如果将公钥复制到其他账户甚至主机，利用私钥也可以登录。

密钥形式登录的过程：

1. 生成密钥对。
2. 将生成的公钥追加到 `~/.ssh/authorized_keys` 文件中。
3. 服务器打开密钥登录功能。
4. 客户端选中生成的私钥，进行密钥登录。

## 生成密钥对

### Windows

Windows 下需要安装 Git 后才能生成，不想安装 Git 的可以直接使用 Xshell 工具生成。

1. 点击 Xshell 菜单栏中的 <kbd>工具</kbd> - <kbd>新建用户密钥生成向导</kbd> 开始生成密钥对。

   ![xshell-create-ssh-key-0](https://img.zxj.guru/2020/11/xshell-create-ssh-key-0.jpg)

2. 点击 <kbd>下一步</kbd>。

   ![xshell-create-ssh-key-1](https://img.zxj.guru/2020/11/xshell-create-ssh-key-1.jpg)

3. 点击 <kbd>下一步</kbd>。

   ![xshell-create-ssh-key-2](https://img.zxj.guru/2020/11/xshell-create-ssh-key-2.jpg)

4. 补充信息，然后点击 <kbd>完成</kbd>。

   ![xshell-create-ssh-key-3](https://img.zxj.guru/2020/11/xshell-create-ssh-key-3.jpg)

5. 查看并复制公钥内容。

   ![xshell-create-ssh-key-4](https://img.zxj.guru/2020/11/xshell-create-ssh-key-4.jpg)

### Linux

1. 打开终端。

2. 输入以下命令（替换为您的电子邮件地址）。

   ```bash
   $ ssh-keygen -t ed25519 -C "your_email@example.com"
   #如果您使用的是不支持 Ed25519 算法的旧系统，请使用以下命令：
   $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

3. 这将创建以所提供的电子邮件地址为标签的新 SSH 密钥。

   ```bash
   > Generating public/private ed25519 key pair.
   ```

4. 提示您 "`Enter a file in which to save the key`（输入要保存密钥的文件）"时，按 <kbd>Enter</kbd> 键。 这将接受默认文件位置。

   ```bash
   > Enter a file in which to save the key (/home/you/.ssh/id_ed25519): [Press enter]
   ```

5. 在提示时输入安全密码。

   ```bash
   > Enter passphrase (empty for no passphrase): [Type a passphrase]
   > Enter same passphrase again: [Type passphrase again]
   ```

6. 查看并复制公钥内容。

   ```bash
   $ cat ~/.ssh/id_rsa.pub
   ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAklOUpkDHrfHY17SbrmTIpNLTGK9Tjom/BWDSU
   GPl+nafzlHDTYW7hdI4yZ5ew18JH4JW9jbhUFrviQzM7xlELEVf4h9lFX5QVkbPppSwg0cda3
   Pbv7kOdJ/MTyBlWXFCR+HAo3FXRitBqxiX1nKhXpHAZsMciLq8V6RjsNAQwdsdMFvSlVK/7XA
   t3FaoJoAsncM1Q9x5+3V0Ww68/eIFmb1zuUFljQJKprrX88XypNDvjYNby6vw/Pb0rwert/En
   mZ+AW4OZPnTPI89ZPmVMLuayrD2cE86Z/il8b+gw3r3+1nKatmIkjn2so1d01QraTlMqVSsbx
   NrRFi9wrf+M7Q== schacon@mylaptop.local
   ```

> 如果您的私钥没有存储在默认位置之一（如 `~/.ssh/id_rsa`），您需要告知 SSH 身份验证代理其所在位置。 要将密钥添加到 ssh-agent，请输入 `ssh-add ~/path/to/my_key`。

## 在服务器上安装公钥

`authorized_keys` 是 linux 操作系统下，专门用来存放公钥的地方，只要公钥放到了服务器的正确位置，并且拥有正确的权限，你才可以通过你的私钥，免密登录 linux 服务器。

1. 登录服务器。

   ```bash
   ssh ryanpd5i@13.229.188.59
   ```

2. 将公钥内容追加到 `~/.ssh/authorized_keys` 文件中。

   ```bash
   echo "公钥内容" >> ~/.ssh/authorized_keys
   ```

3. 更改文件权限。

   ```bash
   sudo chmod 600 ~/.ssh/authorized_keys
   sudo chmod 700 ~/.ssh
   ```

## 服务器打开密钥登录功能

1. 编辑 `/etc/ssh/sshd_config` 文件，进行如下设置：

   ```bash
   RSAAuthentication yes
   PubkeyAuthentication yes
   #bash
   sudo sed -i '/#PubkeyAuthentication yes/iRSAAuthentication yes' /etc/ssh/sshd_config
   sudo sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config
   ```

2. 阻止 root 用户通过 SSH 登录：

   ```bash
   PermitRootLogin yes
   #bash
   sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config
   ```

## 以密钥方式登录

Linux 下：

```bash
ssh ryanpd5i@13.229.188.59
```

Windows Xshell 下：

![xshell-ssh-key-login](https://img.zxj.guru/2020/11/xshell-ssh-key-login.jpg)

当你完成全部设置，并以密钥方式登录成功后，再禁用密码登录：

```bash
PasswordAuthentication no
#bash
sudo sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
```

最后，重启 SSH 服务：

```bash
service sshd restart
```

## 参考

- [Generating a new SSH key and adding it to the ssh-agent - GitHub Docs](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [设置 SSH 通过密钥登录](https://www.runoob.com/w3cnote/set-ssh-login-key.html)

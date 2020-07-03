---
title: Linux 系统服务器禁止 root 用户登录
abstract: Linux 账户下 root 账户属于超级用户，具有全权管理权，可以做任何事。如果误操作会产生很大的破坏性。如果被黑，对方得到 root 的权限就能够读取写入系统上的所有文件。为了避免这一现象，我们需要添加新的用户并赋予管理员权限。
url: linux-permit-root-login
permalink: linux-permit-root-login
date: 2020-11-12 18:06:33
category:
  - Linux
tags:
  - Linux
---

![linux-permit-root-login](https://img.zxj.guru/2020/11/linux-permit-root-login.png)

Linux 账户下 root 账户属于超级用户，具有全权管理权，可以做任何事。如果误操作会产生很大的破坏性。如果被黑，对方得到 root 的权限就能够读取写入系统上的所有文件。为了避免这一现象，我们需要添加新的用户并赋予管理员权限。该用户想要获取 root 权限可以使用 sudo 方式，sudo 只限制该用户有限的命令下有 root 权限， 而不是将所有 root 的命令权限给该用户，这样可以避免该用户使用 root 账户密码。

## 添加新用户赋管理员权限

1. 添加新用户。

   ```bash
   # useradd ryanpd5i
   ```

2. 给新用户设置密码，会让你输入两次密码。

   ```bash
   # passwd ryanpd5i
   Changing password for user ryanpd5i.
   New password: r4hRBzGTN#FQt#iyxvGPFP^zB#q4Wu
   Retype new password: r4hRBzGTN#FQt#iyxvGPFP^zB#q4Wu
   passwd: all authentication tokens updated successfully.
   ```

3. 将新用户加入 wheel 组。

   > 在 Linux 中 wheel 组就类似于一个管理员的组。
   >
   > 通常在 Linux 下，即使我们有系统管理员 root 的权限，也不推荐用 root 用户登录。一般情况下用普通用户登录就可以了，在需要 root 权限执行一些操作时，再 su 登录成为 root 用户。但是，任何人只要知道了 root 的密码，就都可以通过 su 命令来登录为 root 用户，这无疑为系统带来了安全隐患。所以，将普通用户加入到 wheel 组，被加入的这个普通用户就成了管理员组内的用户，但如果不对一些相关的配置文件进行配置，这个管理员组内的用户与普通用户也没什么区别，就像警察下班后，没有带枪、穿这便衣和普通人（用户）一样，虽然他的确是警察。根据应用的实例不同应用 wheel 组的方法也不同。这里对于服务器来说，我们希望的是剥夺被加入到 wheel 组用户以外的普通用户通过 su 命令来登录为 root 的机会（只有属于 wheel 组的用户才可以用 su 登录为 root）。这样就进一步增强了系统的安全性。

   ```bash
   usermod -a -G wheel ryanpd5i
   ```

4. 修改 `sudo` 的配置文件 `sudoers`。在 `/etc/sudoers` 文件中的 `root ALL=(ALL) ALL` 行后添加 `ryanpd5i ALL=(ALL) ALL` 。

   ```bash
   # 文件添加写权限
   chmod 640 /etc/sudoers

   # 在 root    ALL=(ALL)     ALL 行后添加 ryanpd5i    ALL=(ALL)     ALL

   # 执行 root 权限操作时不输入密码，不建议这样做
   # 将`# %wheel    ALL=(ALL)    NOPASSWD: ALL` 一行中行首的 '#' 删除

   # 撤销文件写权限
   chmod 440 /etc/sudoers
   ```

   > 生产环境建议指定具体目录或命令。例如：
   >
   > - `ryanpd5i ALL=(root) /mnt/sudodir` 目录 **/mnt/sudodir** 里面的程序 `ryanpd5i` 用户可以使用 root 权限（但是需要输入账户密码）来执行；
   > - `ryanpd5i ALL=(root) NOPASSWD: /etc/ssh` 目录 **/etc/ssh** 里面的文件 `ryanpd5i` 用户可以使用 root 权限（不用输入账户密码）来读写；

现在就可以使用 `sudo su -` 然后输入用户密码来使用 root 权限。

## SSH 禁止 root 用户登录

### 阻止 root 用户通过 SSH 登录

阻止 root 用户使用 SSH 远程登录服务器。

```bash
PermitRootLogin yes
#bash
sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config
```

### 设定仅允许指定用户登录

设置只允许指定用户登录服务器。注意：一旦开启这个参数，root 用户就不能使用 SSH 远程登录服务器，在 SSH 登录时会收到"Access denied"的提示。

方法：在 `PasswordAuthentication yes` 行后添加 `AllowUsers ryanpd5i`。

```bash
sed -i '/^PasswordAuthentication yes/aAllowUsers ryanpd5i' /etc/ssh/sshd_config
```

最后，重启 SSH 服务：

```bash
service sshd restart
```

## 参考

- [命令前加 sudo 执行和用真正的 root 用户执行有什么区别](https://www.zhihu.com/question/51746286/answer/127360329)

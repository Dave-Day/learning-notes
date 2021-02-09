---
title: 文本处理命令 sed
url: linux-shell-sed
---

# 文本处理 sed

本章主要讲解 Shell 中最核心的文本处理三剑客之 sed 的用法。

## sed 的工作模式

### 基础介绍

- sed(Stream Editor)：流编辑器。对标准输出或文件逐行进行处理。

### 语法格式

|        | 格式                                      |
| ------ | ----------------------------------------- |
| 第一种 | `stdout | sed [option] "pattern command"` |
| 第二种 | `sed [option] "pattern command" file`     |

## sed 的选项

### 选项

| 选项 | 含义                                |
| ---- | ----------------------------------- |
| `-n` | 只打印模式匹配行                    |
| `-e` | 直接在命令行进行 sed 编辑，默认选项 |
| `-f` | 编辑动作保存在文件中，指定文件执行  |
| `-r` | 支持扩展正则表达式                  |
| `-i` | 直接修改文件内容                    |

### 测试

#### 测试代码

```shell
#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# sed 中的 option 练习

filepath=$(
    cd "$(dirname "$0")"
    pwd
)
testpath="${filepath}/test_dir"
filename="${testpath}/passwd"
Green_font_prefix="\033[32m" && Red_font_prefix="\033[31m" && Green_background_prefix="\033[42;37m" && Red_background_prefix="\033[41;37m" && Font_color_suffix="\033[0m"

function test_sed_option() {
    # 生成测试文件
    mkdir -p ${testpath} && cd ${testpath}
    cp /etc/passwd ./

    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中以 root 开始的行 ------${Font_color_suffix}\n" && sed -n '/^root/p' ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 zsh 或者 bash 的行 ------${Font_color_suffix}\n" && sed -n -e '/bash/p' -e '/zsh/p' ${filename}
    # 使用 -r 扩展正则表达式处理
    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 zsh 或者 bash 的行(使用扩展正则表达式) ------${Font_color_suffix}\n" && sed -n -r '/bash|zsh/p' ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 root 的行 ------${Font_color_suffix}\n" && sed -n '/root/p' ${filename}

    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 /var/spool/mail 的行 ------${Font_color_suffix}\n" && sed -n '/\/var\/spool\/mail/p' ${filename}
    # 使用 -f 指定文件处理
    echo "/\/var\/spool\/mail/p" >>edit.sed
    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 /var/spool/mail 的行(使用指定文件处理) ------${Font_color_suffix}\n" && sed -n -f edit.sed ${filename}

    # 使用 -i 直接修改文件内容
    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 root 的行(sed) ------${Font_color_suffix}\n" && sed -n '/root/p' ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 root 的行(grep) ------${Font_color_suffix}\n" && grep -n 'root' ${filename}
    echo -e "\n${Green_font_prefix}------ 将 passwd 文件中的 root 替换为 jaime 并打印 ------${Font_color_suffix}\n" && sed -n 's/root/jaime/g;p' ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 jaime 的行(sed) ------${Font_color_suffix}\n" && sed -n '/jaime/p' ${filename}
    echo -e "\n${Green_font_prefix}------ 直接将 passwd 文件中的 root 替换为 jaime ------${Font_color_suffix}\n" && sed -i 's/root/jaime/g' ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 passwd 文件中包含 jaime 的行(grep) ------${Font_color_suffix}\n" && grep -n 'jaime' ${filename}

    # 删除测试目录
    cd ${filepath} && rm -rf test_dir/
    # rm -r passwd edit.sed
}

test_sed_option
```

#### 运行结果

```bash
------ 打印 passwd 文件中以 root 开始的行 ------

root:x:0:0:root:/root:/bin/zsh

------ 打印 passwd 文件中包含 zsh 或者 bash 的行 ------

root:x:0:0:root:/root:/bin/zsh
ryan:x:1000:1000:ryan:/home/ryan:/bin/zsh

------ 打印 passwd 文件中包含 zsh 或者 bash 的行(使用扩展正则表达式) ------

root:x:0:0:root:/root:/bin/zsh
ryan:x:1000:1000:ryan:/home/ryan:/bin/zsh

------ 打印 passwd 文件中包含 root 的行 ------

root:x:0:0:root:/root:/bin/zsh
operator:x:11:0:operator:/root:/sbin/nologin

------ 打印 passwd 文件中包含 /var/spool/mail 的行 ------

mail:x:8:12:mail:/var/spool/mail:/sbin/nologin

------ 打印 passwd 文件中包含 /var/spool/mail 的行(使用指定文件处理) ------

mail:x:8:12:mail:/var/spool/mail:/sbin/nologin

------ 打印 passwd 文件中包含 root 的行(sed) ------

root:x:0:0:root:/root:/bin/zsh
operator:x:11:0:operator:/root:/sbin/nologin

------ 打印 passwd 文件中包含 root 的行(grep) ------

1:root:x:0:0:root:/root:/bin/zsh
10:operator:x:11:0:operator:/root:/sbin/nologin

------ 将 passwd 文件中的 root 替换为 jaime 并打印 ------

jaime:x:0:0:jaime:/jaime:/bin/zsh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/jaime:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
ryan:x:1000:1000:ryan:/home/ryan:/bin/zsh
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
gluster:x:997:993:GlusterFS daemons:/run/gluster:/sbin/nologin
libstoragemgmt:x:996:992:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
qemu:x:107:107:qemu user:/:/sbin/nologin
unbound:x:995:991:Unbound DNS resolver:/etc/unbound:/sbin/nologin
saslauth:x:994:76:Saslauthd user:/run/saslauthd:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
usbmuxd:x:113:113:usbmuxd user:/:/sbin/nologin
saned:x:993:990:SANE scanner daemon user:/usr/share/sane:/sbin/nologin
colord:x:992:988:User for colord:/var/lib/colord:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
geoclue:x:991:987:User for geoclue:/var/lib/geoclue:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
setroubleshoot:x:990:986::/var/lib/setroubleshoot:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
rtkit:x:172:172:RealtimeKit:/proc:/sbin/nologin
pulse:x:171:171:PulseAudio System Daemon:/var/run/pulse:/sbin/nologin
sssd:x:989:983:User for sssd:/:/sbin/nologin
radvd:x:75:75:radvd user:/:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
avahi:x:70:70:Avahi mDNS/DNS-SD Stack:/var/run/avahi-daemon:/sbin/nologin
nginx:x:987:981:Nginx web server:/var/lib/nginx:/sbin/nologin

------ 打印 passwd 文件中包含 jaime 的行(sed) ------


------ 直接将 passwd 文件中的 root 替换为 jaime ------


------ 打印 passwd 文件中包含 jaime 的行(grep) ------

1:jaime:x:0:0:jaime:/jaime:/bin/zsh
10:operator:x:11:0:operator:/jaime:/sbin/nologin

```

## sed 中的 pattern 详解

### 匹配模式

| 匹配模式                       | 含义                                           |
| ------------------------------ | ---------------------------------------------- |
| `10commmand`                   | 匹配到第 10 行                                 |
| `10,20command`                 | 匹配从第 10 行开始，到第 20 行结束             |
| `10,+5command`                 | 匹配从第 10 行开始，到第 16 行结束             |
| `/pattern1/command`            | 匹配到 pattern1 的行                           |
| `/patttern1,/pattern2/command` | 匹配从 pattern 的行开始，到 pattern2 的行结束  |
| `10,/pattern1/command`         | 匹配从第 10 行开始，到匹配到 pattern1 的行结束 |
| `/pattern1/,10command`         | 匹配到 pattern1 的行开始，到第 10 行结束       |

注意： 

- 匹配模式中存在变量时，建议使用双引号。`sed -i "/${var1}/${var2}/g"`
- 需要引入自定义变量时，如果外面使用单引号，则自定义变量也必须使用单引号。`sed -i '/'${var1}'/'${var2}'/g'`

```bash
1. LineNumber: 指定行号

    sed -n "17p" file   # 打印 file 的第 17 行
    
2. StartLine, EndLine: 指定起始和结束行号

    sed -n "10, 20p" file   # 打印 file 的 第 10 - 20 行
    
3. StartLine,+N:指定起始行号，然后后面 N 行

    sed -n "10, +5p" file   # 打印 file 的 第 10 - 16 行
    
4. /pattern1/: 正则表达式匹配的行

    sed -n "/^root/p" file  # 打印 file 文件中以 root 开始的行
    
5. /pattern1/,/pattern2/: 从匹配到 pattern1 的行，到匹配到 pattern2 的行

    sed -n /^mail/,/^ftp/p" file    # 打印 file 文件中从 mail 开始的行到 ftp 开始的行
    
6. LineNumber,/pattern1/: 从指定行开始匹配，匹配到 pattern1 的行结束

    sed -n "4,/shutdown$/p" file    # 打印 file 文件中从第 4 行到以 shutdown 
    结束的行
    
7. /pattern1/,LineNumber: 从匹配到 pattern1 的行开始到指定行结束

    sed -n "/^bin/,6p" file     # 打印 file 文件中从以 bin 开始的行到 第 6 行
```

### 测试

#### 测试代码

```shell
#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#  sed 中的 pattern 练习

filename='/etc/passwd'
Green_font_prefix="\033[32m" && Red_font_prefix="\033[31m" && Green_background_prefix="\033[42;37m" && Red_background_prefix="\033[41;37m" && Font_color_suffix="\033[0m"

function test_sed_pattern() {
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 的第 3 行 ------${Font_color_suffix}\n" && sed -n "3p" ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 的第 1 - 5 行 ------${Font_color_suffix}\n" && sed -n "1, 5p" ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 的第 1 ,+5 行 ------${Font_color_suffix}\n" && sed -n "1, +5p" ${filename}

    # 正则表达式
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 中以 root 开始的行 ------${Font_color_suffix}\n" && sed -n "/^root/p" ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 中从 mail 开始的行到 ftp 开始的行 ------${Font_color_suffix}\n" && sed -n "/^mail/,/^ftp/p" ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 中从第 4 行到以 shutdown 结束的行 ------${Font_color_suffix}\n" && sed -n "4,/shutdown$/p" ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 中从以 bin 开始的行到第 6 行 ------${Font_color_suffix}\n" && sed -n "/^bin/,6p" ${filename}
    # 正则表达式转义
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 中包含 /var/spool/mail 的行 ------${Font_color_suffix}\n" && sed -n "/\/var\/spool\/mail/p" ${filename}
    # 扩展正则表达式
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 中包含 bash 或者 zsh 的行 ------${Font_color_suffix}\n" && sed -n -r "/bash|zsh/p" ${filename}

    # 如果起始行号 > 终止行号，只会显示起始行号的那一行
    echo -e "\n${Green_font_prefix}------ 在 /etc/passwd 中从包含 sshd 的行并显示行号 ------${Font_color_suffix}\n" && grep -n "sshd" ${filename}
    echo -e "\n${Green_font_prefix}------ 打印 /etc/passwd 中从包含 sshd 的行到第 6 行 ------${Font_color_suffix}\n" && sed -n "/sshd/,6p" ${filename}

}

test_sed_pattern
```



#### 运行结果

```bash
------ 打印 /etc/passwd 的第 3 行 ------

daemon:x:2:2:daemon:/sbin:/sbin/nologin

------ 打印 /etc/passwd 的第 1 - 5 行 ------

root:x:0:0:root:/root:/bin/zsh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin

------ 打印 /etc/passwd 的第 1 ,+5 行 ------

root:x:0:0:root:/root:/bin/zsh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync

------ 打印 /etc/passwd 中以 root 开始的行 ------

root:x:0:0:root:/root:/bin/zsh

------ 打印 /etc/passwd 中从 mail 开始的行到 ftp 开始的行 ------

mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin

------ 打印 /etc/passwd 中从第 4 行到以 shutdown 结束的行 ------

adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown

------ 打印 /etc/passwd 中从以 bin 开始的行到第 6 行 ------

bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync

------ 打印 /etc/passwd 中包含 /var/spool/mail 的行 ------

mail:x:8:12:mail:/var/spool/mail:/sbin/nologin

------ 打印 /etc/passwd 中包含 bash 或者 zsh 的行 ------

root:x:0:0:root:/root:/bin/zsh
ryan:x:1000:1000:ryan:/home/ryan:/bin/zsh

------ 在 /etc/passwd 中从包含 sshd 的行并显示行号 ------

17:sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin

------ 打印 /etc/passwd 中从包含 sshd 的行到第 6 行 ------

sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
```

## sed 中的编辑命令

### 命令对照表

| 类别   | 编辑命令     | 含义                                 |
| ------ | ------------ | ------------------------------------ |
| 查询   | p            | 打印                                 |
| 增加 1 | a            | 行后追加                             |
| 增加 2 | i            | 行前增加                             |
| 增加 3 | r            | 外部文件读入，行后追加               |
| 增加 4 | w            | 匹配行写入外部文件                   |
| 删除   | d            | 删除                                 |
| 修改 1 | s/old/new    | 将第一个 old 替换为 new              |
| 修改 2 | s/old/new/g  | 将全部的 old 替换为 new              |
| 修改 3 | s/old/new/2g | 将第两个开始的所有的 old 替换为 new  |
| 修改 4 | s/old/new/ig | 将全部的 old 替换为 new ，忽略大小写 |

### 测试 1

#### 测试代码

```shell
#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# sed 中的 command 练习

filepath=$(
    cd "$(dirname "$0")"
    pwd
)
testpath="${filepath}/test_dir"
filename="${testpath}/passwd"
Green_font_prefix="\033[32m" && Red_font_prefix="\033[31m" && Green_background_prefix="\033[42;37m" && Red_background_prefix="\033[41;37m" && Font_color_suffix="\033[0m"

function test_sed_command() {
    mkdir -p ${testpath} && cd ${testpath}

    # 删除一行 delete
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 删除 passwd 文件中一行 ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 删除 passwd 文件中的第 1 行 ...${Font_color_suffix}" && sed -n '1d' ${filename}
    echo -e "${Green_font_prefix} 直接删除前打印 passwd 的第 1 行 ...${Font_color_suffix}" && sed -n "1p" ${filename}
    echo -e "${Green_font_prefix} 直接删除 passwd 文件中的第 1 行 ... ${Font_color_suffix}" && sed -i '1d' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 的第 1 行 ...${Font_color_suffix}" && sed -n "1p" ${filename}

    # 删除多行 1
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 删除 passwd 文件中多行 ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 直接删除前打印 passwd 的第 1 - 3 行 ...${Font_color_suffix}" && sed -n "1,3p" ${filename}
    echo -e "${Green_font_prefix} 直接删除 passwd 文件中的第 1 - 3 行 ... ${Font_color_suffix}" && sed -i '1,3d' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 的第 1 - 3 行 ...${Font_color_suffix}" && sed -n "1,3p" ${filename}

    # 删除多行 2
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 删除 passwd 文件中多行 2 ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 直接删除前打印 passwd 中包含 /sbin/nologin 的行 ...${Font_color_suffix}" && sed -n '/\/sbin\/nologin/p' ${filename}
    echo -e "${Green_font_prefix} 直接删除 passwd 中包含 /sbin/nologin 的行 ... ${Font_color_suffix}" && sed -i '/\/sbin\/nologin/d' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 中包含 /sbin/nologin 的行 ...${Font_color_suffix}" && sed -n '/\/sbin\/nologin/p' ${filename}

    # 删除多行 3
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 删除 passwd 文件中多行 3 ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 直接删除前打印 passwd 中从 mail 开始的行到 ftp 开始的行 ...${Font_color_suffix}" && sed -n '/^mail/,/^ftp/p' ${filename}
    echo -e "${Green_font_prefix} 直接删除 passwd 中从 mail 开始的行到 ftp 开始的行 ... ${Font_color_suffix}" && sed -i '/^mail/,/^ftp/d' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 中从 mail 开始的行到 ftp 开始的行 ...${Font_color_suffix}" && sed -n '/^mail/,/^ftp/p' ${filename}

    # 行后追加内容 append
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ passwd 文件行后追加内容 ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 直接追加前打印 passwd 中包含 root:/root 的行 ...${Font_color_suffix}" && sed -n '/root:\/root/p' ${filename}
    echo -e "${Green_font_prefix} 直接在 passwd 中包含 root:/root 的行后追加 This is user which can login system ...${Font_color_suffix}" && sed -i '/root:\/root/a This is user which can login system' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 中 1 - 3 行 ...${Font_color_suffix}" && sed -n "1,3p" ${filename}

    # 行前插入内容 insert
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ passwd 文件行前插入内容 ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 打印 passwd 中从 mail 开始的行到 ftp 开始的行 ...${Font_color_suffix}" && sed -n '/^mail/,/^ftp/p' ${filename}
    echo -e "${Green_font_prefix} 直接在 passwd 中从 mail 开始的行到 ftp 开始的行前添加 This is nologin user  ...${Font_color_suffix}" && sed -i '/^mail/,/^ftp/i This is nologin user' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 中从 mail 开始的行到 ftp 开始的行 ...${Font_color_suffix}" && sed -n '/^mail/,/^ftp/p' ${filename}

    # 将指定文件内容追加到匹配行后 rewrite
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ passwd 文件中添加指定文件的内容 ------${Font_color_suffix}\n"
    echo "This is user which can login system" >>rewrite
    echo -e "${Green_font_prefix} 直接追加前打印 passwd 中包含 root:/root 的行 ...${Font_color_suffix}" && sed -n '/root:\/root/p' ${filename}
    echo -e "${Green_font_prefix} 直接在 passwd 中包含 root:/root 的行后追加 rewrite 文件内容 ...${Font_color_suffix}" && sed -i '/root:\/root/r rewrite' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 中 1 - 3 行 ...${Font_color_suffix}" && sed -n "1,3p" ${filename}

    # 将匹配到的行内容保存到其它文件 write
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ passwd 文件中的内容追加到指定文件中 ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 直接追加前打印 passwd 中包含 root:/root 的行 ...${Font_color_suffix}" && sed -n '/root:\/root/p' ${filename}
    echo -e "${Green_font_prefix} 直接将 passwd 中包含 root:/root 的行内容保存到 write 文件中 ...${Font_color_suffix}" && sed -i '/root:\/root/w write' ${filename}
    echo -e "${Green_font_prefix} 打印 write 文件 ...${Font_color_suffix}" && cat -n write

    # 替换第一个
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 替换 passwd 中第一个 root 为 jaime ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 root 的行(grep) ...${Font_color_suffix}" && grep -n 'root' ${filename}
    echo -e "${Green_font_prefix} 直接将 passwd 文件中的第一个 root 替换为 jaime ...${Font_color_suffix}" && sed -i 's/root/jaime/g' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 jaime 的行(grep) ...${Font_color_suffix}" && grep -n 'jaime' ${filename}

    # 替换第二个开始的所有的 root
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 替换 passwd 中从第二个开始的所有的 root 为 jaime ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 root 的行(grep) ...${Font_color_suffix}" && grep -n 'root' ${filename}
    echo -e "${Green_font_prefix} 直接将 passwd 文件中从第二个开始的所有的 root 为 jaime ...${Font_color_suffix}" && sed -i 's/root/jaime/g' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 jaime 的行(grep) ...${Font_color_suffix}" && grep -n 'jaime' ${filename}

    # 替换所有的 root
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 替换 passwd 中所有的 root 为 jaime ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 root 的行(grep) ...${Font_color_suffix}" && grep -n 'root' ${filename}
    echo -e "${Green_font_prefix} 直接将 passwd 文件中的所有的 root 替换为 jaime ...${Font_color_suffix}" && sed -i 's/root/jaime/g' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 jaime 的行(grep) ...${Font_color_suffix}" && grep -n 'jaime' ${filename}

    # 替换所有的 ssh
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 替换 passwd 中所有的 ssh|SSH 为 http ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 ssh|SSH 的行(grep) ...${Font_color_suffix}" && grep -n -E 'ssh|SSH' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 ssh|SSH 的行(sed) ...${Font_color_suffix}" && sed -n -r '/ssh|SSH/p' ${filename}
    echo -e "${Green_font_prefix} 直接将 passwd 文件中的所有的 ssh|SSH 替换为 jaime(不区分大小写) ...${Font_color_suffix}" && sed -i 's/ssh/http/ig' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 http 的行(grep) ...${Font_color_suffix}" && grep -n 'http' ${filename}

    # 显示行号
    rm -f passwd && cp -f /etc/passwd ./
    echo -e "\n${Red_font_prefix}------ 查找 passwd 文件中包含 zsh 或者 bash 的行并显示行号 ------${Font_color_suffix}\n"
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 zsh 或者 bash 的行并显示行号(使用 sed 扩展正则表达式) ...${Font_color_suffix}\n" && sed -n -r '/bash|zsh/=;p' ${filename}
    echo -e "${Green_font_prefix} 打印 passwd 文件中包含 zsh 或者 bash 的行并显示行号(grep) ...${Font_color_suffix}" && grep -n -E 'bash|zsh' ${filename}

    # 删除测试文件
    cd ${filepath} && rm -rf test_dir/

}
test_sed_command
```



#### 运行结果

```bash
------ 删除 passwd 文件中一行 ------

 删除 passwd 文件中的第 1 行 ...
 直接删除前打印 passwd 的第 1 行 ...
root:x:0:0:root:/root:/bin/zsh
 直接删除 passwd 文件中的第 1 行 ... 
 打印 passwd 的第 1 行 ...
bin:x:1:1:bin:/bin:/sbin/nologin

------ 删除 passwd 文件中多行 ------

 直接删除前打印 passwd 的第 1 - 3 行 ...
root:x:0:0:root:/root:/bin/zsh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
 直接删除 passwd 文件中的第 1 - 3 行 ... 
 打印 passwd 的第 1 - 3 行 ...
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync

------ 删除 passwd 文件中多行 2 ------

 直接删除前打印 passwd 中包含 /sbin/nologin 的行 ...
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
gluster:x:997:993:GlusterFS daemons:/run/gluster:/sbin/nologin
libstoragemgmt:x:996:992:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
qemu:x:107:107:qemu user:/:/sbin/nologin
unbound:x:995:991:Unbound DNS resolver:/etc/unbound:/sbin/nologin
saslauth:x:994:76:Saslauthd user:/run/saslauthd:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
usbmuxd:x:113:113:usbmuxd user:/:/sbin/nologin
saned:x:993:990:SANE scanner daemon user:/usr/share/sane:/sbin/nologin
colord:x:992:988:User for colord:/var/lib/colord:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
geoclue:x:991:987:User for geoclue:/var/lib/geoclue:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
setroubleshoot:x:990:986::/var/lib/setroubleshoot:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
rtkit:x:172:172:RealtimeKit:/proc:/sbin/nologin
pulse:x:171:171:PulseAudio System Daemon:/var/run/pulse:/sbin/nologin
sssd:x:989:983:User for sssd:/:/sbin/nologin
radvd:x:75:75:radvd user:/:/sbin/nologin
gdm:x:42:42::/var/lib/gdm:/sbin/nologin
gnome-initial-setup:x:988:982::/run/gnome-initial-setup/:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
avahi:x:70:70:Avahi mDNS/DNS-SD Stack:/var/run/avahi-daemon:/sbin/nologin
nginx:x:987:981:Nginx web server:/var/lib/nginx:/sbin/nologin
 直接删除 passwd 中包含 /sbin/nologin 的行 ... 
 打印 passwd 中包含 /sbin/nologin 的行 ...

------ 删除 passwd 文件中多行 3 ------

 直接删除前打印 passwd 中从 mail 开始的行到 ftp 开始的行 ...
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
 直接删除 passwd 中从 mail 开始的行到 ftp 开始的行 ... 
 打印 passwd 中从 mail 开始的行到 ftp 开始的行 ...

------ passwd 文件行后追加内容 ------

 直接追加前打印 passwd 中包含 root:/root 的行 ...
root:x:0:0:root:/root:/bin/zsh
 直接在 passwd 中包含 root:/root 的行后追加 This is user which can login system ...
 打印 passwd 中 1 - 3 行 ...
root:x:0:0:root:/root:/bin/zsh
This is user which can login system
bin:x:1:1:bin:/bin:/sbin/nologin

------ passwd 文件行前插入内容 ------

 打印 passwd 中从 mail 开始的行到 ftp 开始的行 ...
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
 直接在 passwd 中从 mail 开始的行到 ftp 开始的行前添加 This is nologin user  ...
 打印 passwd 中从 mail 开始的行到 ftp 开始的行 ...
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
This is nologin user
operator:x:11:0:operator:/root:/sbin/nologin
This is nologin user
games:x:12:100:games:/usr/games:/sbin/nologin
This is nologin user
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin

------ passwd 文件中添加指定文件的内容 ------

 直接追加前打印 passwd 中包含 root:/root 的行 ...
root:x:0:0:root:/root:/bin/zsh
 直接在 passwd 中包含 root:/root 的行后追加 rewrite 文件内容 ...
 打印 passwd 中 1 - 3 行 ...
root:x:0:0:root:/root:/bin/zsh
This is user which can login system
bin:x:1:1:bin:/bin:/sbin/nologin

------ passwd 文件中的内容追加到指定文件中 ------

 直接追加前打印 passwd 中包含 root:/root 的行 ...
root:x:0:0:root:/root:/bin/zsh
 直接将 passwd 中包含 root:/root 的行内容保存到 write 文件中 ...
 打印 write 文件 ...
     1	root:x:0:0:root:/root:/bin/zsh

------ 替换 passwd 中第一个 root 为 jaime ------

 打印 passwd 文件中包含 root 的行(grep) ...
1:root:x:0:0:root:/root:/bin/zsh
10:operator:x:11:0:operator:/root:/sbin/nologin
 直接将 passwd 文件中的第一个 root 替换为 jaime ...
 打印 passwd 文件中包含 jaime 的行(grep) ...
1:jaime:x:0:0:root:/root:/bin/zsh
10:operator:x:11:0:operator:/jaime:/sbin/nologin

------ 替换 passwd 中从第二个开始的所有的 root 为 jaime ------

 打印 passwd 文件中包含 root 的行(grep) ...
1:root:x:0:0:root:/root:/bin/zsh
10:operator:x:11:0:operator:/root:/sbin/nologin
 直接将 passwd 文件中从第二个开始的所有的 root 为 jaime ...
 打印 passwd 文件中包含 jaime 的行(grep) ...
1:root:x:0:0:jaime:/jaime:/bin/zsh

------ 替换 passwd 中所有的 root 为 jaime ------

 打印 passwd 文件中包含 root 的行(grep) ...
1:root:x:0:0:root:/root:/bin/zsh
10:operator:x:11:0:operator:/root:/sbin/nologin
 直接将 passwd 文件中的所有的 root 替换为 jaime ...
 打印 passwd 文件中包含 jaime 的行(grep) ...
1:jaime:x:0:0:jaime:/jaime:/bin/zsh
10:operator:x:11:0:operator:/jaime:/sbin/nologin

------ 替换 passwd 中所有的 ssh|SSH 为 http ------

 打印 passwd 文件中包含 ssh|SSH 的行(grep) ...
17:sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
 打印 passwd 文件中包含 ssh|SSH 的行(sed) ...
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
 直接将 passwd 文件中的所有的 ssh|SSH 替换为 jaime(不区分大小写) ...
 打印 passwd 文件中包含 http 的行(grep) ...
17:httpd:x:74:74:Privilege-separated http:/var/empty/httpd:/sbin/nologin

------ 查找 passwd 文件中包含 zsh 或者 bash 的行并显示行号 ------

 打印 passwd 文件中包含 zsh 或者 bash 的行并显示行号(使用 sed 扩展正则表达式) ...

1
root:x:0:0:root:/root:/bin/zsh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
20
ryan:x:1000:1000:ryan:/home/ryan:/bin/zsh
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
gluster:x:997:993:GlusterFS daemons:/run/gluster:/sbin/nologin
libstoragemgmt:x:996:992:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
qemu:x:107:107:qemu user:/:/sbin/nologin
unbound:x:995:991:Unbound DNS resolver:/etc/unbound:/sbin/nologin
saslauth:x:994:76:Saslauthd user:/run/saslauthd:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
usbmuxd:x:113:113:usbmuxd user:/:/sbin/nologin
saned:x:993:990:SANE scanner daemon user:/usr/share/sane:/sbin/nologin
colord:x:992:988:User for colord:/var/lib/colord:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
geoclue:x:991:987:User for geoclue:/var/lib/geoclue:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
setroubleshoot:x:990:986::/var/lib/setroubleshoot:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
rtkit:x:172:172:RealtimeKit:/proc:/sbin/nologin
pulse:x:171:171:PulseAudio System Daemon:/var/run/pulse:/sbin/nologin
sssd:x:989:983:User for sssd:/:/sbin/nologin
radvd:x:75:75:radvd user:/:/sbin/nologin
gdm:x:42:42::/var/lib/gdm:/sbin/nologin
gnome-initial-setup:x:988:982::/run/gnome-initial-setup/:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
avahi:x:70:70:Avahi mDNS/DNS-SD Stack:/var/run/avahi-daemon:/sbin/nologin
nginx:x:987:981:Nginx web server:/var/lib/nginx:/sbin/nologin
 打印 passwd 文件中包含 zsh 或者 bash 的行并显示行号(grep) ...
1:root:x:0:0:root:/root:/bin/zsh
20:ryan:x:1000:1000:ryan:/home/ryan:/bin/zsh
```

### 反向引用

`&` 和 `\1` 引用模式匹配到的整个串。区别：

- `&` 只能表示匹配到的完整字符串，只能引用整个字符串。
-  `\1` 可以使用 `()` 将匹配到的不需要改变的部分括起来，小括号需要转义。（例如：如果只需要替换匹配到的字符串的一部分，这是只能使用 `\1` ，然后将不需要改变的部分用括号括起来，替换时只替换括号外的）

### 测试 2

#### 需求描述

例如：有一个文件 `str`，内容如下。

```markdown
hadAAp is a bigdata frame.
Spark hadBBp Kaffa.
Paper on hadCCp.
Google hadEEp.
```

1. 将文件中的 hadAAp, hadBBp, ... hadEEp后面加后缀 s。（hadAAp -> hadAAps,  hadEEp -> hadEEps）
2. 将上一步改变后的文件中的 hadAAps, hadBBps, ... hadEEps 后面加后缀 O 。（hadAAps -> hadAApsO,  hadEEps -> hadEEpsO）
3. 将上一步改变后的文件中的 hadAApsO, hadBBpsO, ... hadEEpsO 全部替换为 hadoop。
4. 将上一步改变后的文件中的 hadoop 全部替换为 HADOOP。

#### 思路分析

1. 替换两种操作：

    ```bash
    $ sed -i 's/had..p/&s/g' str # had..p 表示匹配 hadAAp, hadBBp, ... hadEEp 字符串，& 引用 had..p 串
    $ sed -i 's/\(had..p\)/\1s/g' str # had..p 表示匹配 hadAAp, hadBBp, ... hadEEp 字符串，\1 引用 had..p 串
    ```
    
2. 匹配模式中存在变量时，建议使用双引号。

#### 代码编写

```shell
#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# sed 中的 command 练习 2

filepath=$(
    cd "$(dirname "$0")"
    pwd
)
testpath="${filepath}/test_dir"
filename="${testpath}/str"
Green_font_prefix="\033[32m" && Red_font_prefix="\033[31m" && Green_background_prefix="\033[42;37m" && Red_background_prefix="\033[41;37m" && Font_color_suffix="\033[0m"

function sed_str() {
    # 生成测试文件
    mkdir -p ${testpath} && cd ${testpath}
    cat >>${filename} <<EOF
hadAAp is a bigdata frame.
Spark hadBBp Kaffa.
Paper on hadCCp.
Google hadEEp.
EOF
    echo -e "${Green_font_prefix} 打印 str 文件内容 ...${Font_color_suffix}" && cat -n ${filename}

    echo -e "${Red_font_prefix} 将 str 文件中的 hadAAp, hadBBp, ... hadEEp 后面加后缀 s ...${Font_color_suffix}" && sed -i 's/had..p/&s/g' ${filename}
    echo -e "${Green_font_prefix} 打印 str 文件内容 ...${Font_color_suffix}" && cat -n ${filename}

    echo -e "${Red_font_prefix} 将 str 文件中的 hadAAps, hadBBps, ... hadEEps 后面加后缀 O ...${Font_color_suffix}" && sed -i 's/\(had..ps\)/\1O/g' ${filename}
    echo -e "${Green_font_prefix} 打印 str 文件内容 ...${Font_color_suffix}" && cat -n ${filename}

    echo -e "${Red_font_prefix} 将 str 文件中的 hadAApsO, hadBBpsO, ... hadEEpsO 全部替换为 hadoop ...${Font_color_suffix}" && sed -i 's/\(had\)...../\1oop/g' ${filename}
    echo -e "${Green_font_prefix} 打印 str 文件内容 ...${Font_color_suffix}" && cat -n ${filename}

    old_str="hadoop"
    new_str="HADOOP"
    echo -e "${Red_font_prefix} 将 str 文件中的 hadoop 全部替换为 HADOOP(使用单引号操作,变量不加单引号) ...${Font_color_suffix}" && sed -i 's/${old_str}/${new_str}/g' ${filename}
    echo -e "${Green_font_prefix} 打印 str 文件内容 ...${Font_color_suffix}" && cat -n ${filename}

    sed -i "s/HADOOP/hadoop/g" ${filename}
    echo -e "${Red_font_prefix} 将 str 文件中的 hadoop 全部替换为 HADOOP(使用双引号操作) ...${Font_color_suffix}" && sed -i "s/${old_str}/${new_str}/g" ${filename}
    echo -e "${Green_font_prefix} 打印 str 文件内容 ...${Font_color_suffix}" && cat -n ${filename}

    sed -i "s/HADOOP/hadoop/g" ${filename}
    echo -e "${Red_font_prefix} 将 str 文件中的 hadoop 全部替换为 HADOOP(使用单引号操作,变量加单引号) ...${Font_color_suffix}" && sed -i 's/'${old_str}'/'${new_str}'/g' ${filename}
    echo -e "${Green_font_prefix} 打印 str 文件内容 ...${Font_color_suffix}" && cat -n ${filename}

    # 删除测试文件夹
    cd ${filepath} && rm -rf test_dir/
}

sed_str
```

#### 脚本执行

```bash
 打印 str 文件内容 ...
     1	hadAAp is a bigdata frame.
     2	Spark hadBBp Kaffa.
     3	Paper on hadCCp.
     4	Google hadEEp.
 将 str 文件中的 hadAAp, hadBBp, ... hadEEp 后面加后缀 s ...
 打印 str 文件内容 ...
     1	hadAAps is a bigdata frame.
     2	Spark hadBBps Kaffa.
     3	Paper on hadCCps.
     4	Google hadEEps.
 将 str 文件中的 hadAAps, hadBBps, ... hadEEps 后面加后缀 O ...
 打印 str 文件内容 ...
     1	hadAApsO is a bigdata frame.
     2	Spark hadBBpsO Kaffa.
     3	Paper on hadCCpsO.
     4	Google hadEEpsO.
 将 str 文件中的 hadAApsO, hadBBpsO, ... hadEEpsO 全部替换为 hadoop ...
 打印 str 文件内容 ...
     1	hadoop is a bigdata frame.
     2	Spark hadoop Kaffa.
     3	Paper on hadoop.
     4	Google hadoop.
 将 str 文件中的 hadoop 全部替换为 HADOOP(使用单引号操作,变量不加单引号) ...
 打印 str 文件内容 ...
     1	hadoop is a bigdata frame.
     2	Spark hadoop Kaffa.
     3	Paper on hadoop.
     4	Google hadoop.
 将 str 文件中的 hadoop 全部替换为 HADOOP(使用双引号操作) ...
 打印 str 文件内容 ...
     1	HADOOP is a bigdata frame.
     2	Spark HADOOP Kaffa.
     3	Paper on HADOOP.
     4	Google HADOOP.
 将 str 文件中的 hadoop 全部替换为 HADOOP(使用单引号操作,变量加单引号) ...
 打印 str 文件内容 ...
     1	HADOOP is a bigdata frame.
     2	Spark HADOOP Kaffa.
     3	Paper on HADOOP.
     4	Google HADOOP.
```



## 利用 sed 查找文件内容

### 测试

#### 测试代码

```shell

```



#### 运行结果

```bash

```



## 利用 sed 删除文件内容



## 利用 sed 修改文件内容



## 利用 sed 追加文件内容


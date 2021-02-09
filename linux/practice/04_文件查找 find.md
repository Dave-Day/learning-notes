---
title: 文件查找命令 find
url: linux-shell-find
---

# 文件查找命令 find

该小节讲解 Shell 中常用的命令，包括文件查找 find 和 locate 的使用，尤其是 find 的各种高级用法，并结合 xargs 对大量文件进行处理；之后讲解数据备份、文件压缩、目录备份以及下载工具的使用方法；所有的用法都会在真实环境给大家做演示...

## find

### 语法

| 语法格式                    |
| --------------------------- |
| `find [路径] [选项] [操作]` |

#### 选项参数对照表

| 选项                   | 含义                                       |
| ---------------------- | ------------------------------------------ |
| `-name`                | 根据**文件名**查找                         |
| `-perm`                | 根据**文件权限**查找                       |
| `-prune`               | 排除某些查找目录                           |
| `-user`                | 根据**文件属主**查找                       |
| `-group`               | 根据**文件属组**查找                       |
| `-mtime -n \| +n`      | 根据**文件更改时间**查找                   |
| `-nogroup`             | 查找无有效属组的文件                       |
| `-nouser`              | 查找无有效属主的文件                       |
| `-newer file1 ! file2` | 查找更新时间比 file1 新但比 file2 旧的文件 |
| `-type`                | 根据文件类型查找                           |
| `-size -n +n`          | 根据文件大小查找                           |
| `-mindepth n`          | 从 n 级子目录开始查找                      |
| `-maxdepth n`          | 最多搜索到 n 级子目录                      |

#### 常用选项

- -name。例如查找 /etc/ 目录下以 conf 结尾的文件： `find /etc/ -name '*conf'`；
- -iname。例如查找当前目录下文件名为 aa 的文件，不区分大小写：`find . -iname 'aa'`；
- -user。例如查找当前路径下文件属主为 ryan 的所有文件：`find . -user ryan`；
- -group。例如查找当前路径下文件属组为 yarn 的所有文件：`find . -group yarn`；
- -type。
  - f。例如查找当前目录下的文件：`find . -type f`；
  - d。例如查找当前目录下的目录：`find . -type d`；
  - c。例如查找当前目录下的字符设备文件：`find . -type c`；
  - b。例如查找当前目录下的块设备文件：`find . -type b`；
  - l。例如查找当前目录下的链接文件：`find . -type l`；
  - p。例如查找当前目录下的管道文件：`find . -type p`。
- -size，单位默认字节(c)。
  - -n。例如查找当前目录下文件大小大于 1M 的文件：`find . -size +1M`；
  - +n。例如查找当前目录下文件大小小于 100k 的文件：`find . -size -100k`；
- mtime。
  - -n。例如查找 /etc/ 目录下 5 天之内修改且以 conf 结尾的文件： `find /etc/ -mtime -5 -name '*conf'`；
  - +n。例如查找 /etc/ 目录下 10 天之前修改且属主为 root 的文件： `find /etc/ -mtime +10 -user root`；
- -mmin。
  - -n。例如查找 /etc/目录下 30 分钟之内修改的文件：`find /etc/ -mmin -30 -type f`；
  - +n。例如查找 /etc/目录下 30 分钟之前修改的目录：`find /etc/ -mmin +30 -type d`；
- -mindepth n。例如在 /etc/ 目录下的 3 级子目录开始搜索：`find /etc/ -mindepth 3`；
- -maxdepth n。例如查找 /etc/ 目录下以 conf 结尾且文件大小大于 10k 的文件，但最多搜索到 2 级子目录：`find /etc/ -maxdepth 2 -name '*conf'`；
- -nouser。例如查找当前目录下的没有属主的文件：`find . -type f -nouser`；
- -nogroup。例如查找当前目录下的没有属组的文件：`find . -type f -nogroup`；
- -perm。例如查找当前目录下的权限为 644 的文件：`find . -type f -perm 644`；
- -prune。排除目录。
  - 例如查找当前目录下的属主为 hdfs 且文件大小大于 500 字节的文件，但排除 etc 和 opt 目录：`find . -path ./etc -prune -o -path ./opt -prune -o -type f -a -user hdfe -a -size +500c`；
  - 例如在当前目录下的 1 级子目录开始查找文件属主为 ryanjie、文件属组为 jaime、文件大小大于 10M 且文件名为 abcd 或 efgh 的文件，最多查找到 3 级子目录，但排除 ./test_1/hijk 和 ./test_1/opq 目录：`find . -path ./test_1/hijk -prune -o -path ./test_1/opq -prune -o -type f -mindepth 1 -maxdepth 3 -user ryanjie -group jaime -size +10M -perm 777 -a \(-name "abcd" -o -name "efgh"\) -exec ls -la {} \;`
- -newer file1。例如查找 /etc/ 目录下更新时间比 aa 新但是比 ./bb 旧的文件：`find /etc/ -newer aa ! -newer ./bb`

#### 操作

- print。打印输出。（find 命令默认输出时就会打印，所以加与不加没区别）
- -exec。对搜索到的文件执行特定的操作，格式为 `-exec 'command' {} \;`
  - 例如查找当前目录下的文件（非目录）、文件名以 conf 结尾、文件大小大于 10k ，然后将其删除。`find . -type f -name '*conf' -size +10k -exec rm -f {} \;`
  - 例如查找 /var/log/ 目录下以 log 结尾且文件更新时间在 7 天之前的文件，然后将其删除。`find /var/log/ -name '*log' -mtime +7 -exec rm -f {} \;`
  - 例如查找当前目录下的文件（非目录）、文件名以 conf 结尾、文件大小大于 10k ，然后将其复制到 /root/conf/ 目录下。`find . -type f -name '*conf' -size +10k -exec cp {} /root/conf/ \;`
- -ok。和 exec 功能一样，区别在于 ok 在每次操作时都会给用户提示。
- 逻辑运算符。`-a` 与； `-o` 或； `-not` | `!` 非。
  - 例如查找当前目录下文件属主为 hdfs 且文件大小大于 300 字节的文件。`find . -type f -a -user hdfs -a -size +300c`
  - 例如查找当前目录下文件属主不是 hdfs 的所有文件。`find . -type f -not -user hdfs` 或者 `find . -type f ! -user hdfs`
  - 例如查找当前目录下文件属主为 hdfs 或者文件以 xml 结尾的普通文件。`find -type f -a \( -user hdfs -o -name '*xml' \)`

### 练习

#### 脚本编写

```shell
#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# find 练习

filepath=$(
    cd $(dirname $0)
    pwd
)
testpath="${filepath}/test_dir"

Green_font_prefix="\033[32m" && Red_font_prefix="\033[31m" && Green_background_prefix="\033[42;37m" && Red_background_prefix="\033[41;37m" && Font_color_suffix="\033[0m"

check_root() {
    if [ ${UID} -ne 0 ]; then
        echo -e "当前非 ROOT 账号(或没有 ROOT 权限)，无法继续操作，请更换 ROOT 账号或使用 su命令获取临时 ROOT 权限" && exit 1
    fi
}

check_sys() {
    IS_MACOS=$(uname | grep 'Darwin' | wc -l)
    if [[ -f /etc/redhat-release ]]; then
        release="centos"
    elif [ ${IS_MACOS} -eq 1 ]; then
        release="macos"
    elif cat /etc/issue | grep -q -E -i "debian"; then
        release="debian"
    elif cat /etc/issue | grep -q -E -i "ubuntu"; then
        release="ubuntu"
    elif cat /etc/issue | grep -q -E -i "centos|red hat|redhat"; then
        release="centos"
    elif cat /proc/version | grep -q -E -i "debian"; then
        release="debian"
    elif cat /proc/version | grep -q -E -i "ubuntu"; then
        release="ubuntu"
    elif cat /proc/version | grep -q -E -i "centos|red hat|redhat"; then
        release="centos"
    fi
}

check_tree_installed_status() {
    if [ -z $(command -v tree) ]; then
        echo -e "tree 依赖没有安装，开始安装..."
        check_sys
        if [[ ${release} == "centos" ]]; then
            yum update && yum install tree -y
        elif [[ ${release} == "macos" ]]; then
            brew install tree
        else
            apt-get update && apt-get install tree -y
        fi
        if [ -z $(command -v tree) ]; then
            echo -e "tree 安装失败，请检查！" && exit 1
        else
            echo -e "tree 安装成功！"
        fi
    fi
}

test_find() {
    # check_tree_installed_status
    mkdir -p ${testpath} && cd ${testpath}

    # conf、xml、ini
    touch grub.conf loadbalance.conf photo.xml excel.xml php.ini virtuoso.ini
    echo -e "\n${Green_font_prefix}------ 查找当前目录下以 conf 结尾的文件 ------${Font_color_suffix}\n" && find ${testpath} -name "*conf" -exec ls -la {} \;

    # aabb 文件
    mkdir aabb AABB
    echo -e "\n${Green_font_prefix}------ 查找当前目录下文件名为 aabb 的文件(不区分大小写) ------${Font_color_suffix}\n" && find ${testpath} -iname 'aabb'

    # jaime 属主、jaimegroup 属组文件
    groupadd jaimegroup && useradd -g jaimegroup jaime
    chown jaime:jaimegroup grub.conf loadbalance.conf photo.xml
    echo -e "\n${Green_font_prefix}------ 查找当前路径下文件属主为 jaime 的文件 ------${Font_color_suffix}\n" && find ${testpath} -user jaime -exec ls -la {} \; | awk 'BEGIN{printf "%12s %12s %18s\n", "User", "Group", "FileName";printf "--------------------------------------\n"} {printf "%12s %12s %18s\n", $3, $4, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前路径下文件属组为 jaimegroup 的文件 ------${Font_color_suffix}\n" && find ${testpath} -group jaimegroup -exec ls -la {} \; | awk 'BEGIN{printf "%12s %12s %18s\n", "User", "Group", "FileName";printf "--------------------------------------\n"} {printf "%12s %12s %18s\n", $3, $4, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前目录下的文件 ------${Font_color_suffix}\n" && find ${testpath} -type f -exec ls -la {} \;
    # echo -e "\n${Green_font_prefix}------ 查找当前路径下的目录 ------${Font_color_suffix}\n" && find ${testpath} -type d -exec ls -la {} \;

    # 链接文件
    echo "1122" >>model && ln -s model model-soft
    echo -e "\n${Green_font_prefix}------ 查找当前路径下的链接文件 ------${Font_color_suffix}\n" && find ${testpath} -type l -exec ls -la {} \;

    # 管道文件
    mkfifo aabb.pipe AAbb.pipe
    echo -e "\n${Green_font_prefix}------ 查找当前路径下的管道文件 ------${Font_color_suffix}\n" && find ${testpath} -type p -exec ls -la {} \;

    # 50mb, 50kb, 25mb, 25kb, 521 大小的文件
    head -c 50M /dev/zero >50mb.test
    head -c 50K /dev/zero >50kb.test
    head -c 25K /dev/zero >25kb.test
    head -c 512 /dev/zero >512c.test
    head -c 25M /dev/zero >25mb.test
    # dd if=/dev/zero of=25mb.test bs=25MB count=1
    # dd if=/dev/zero of=25kb.test bs=25KB count=1
    # dd if=/dev/zero of=512c.test bs=512 count=1
    echo -e "\n${Green_font_prefix}------ 查找当前目录下文件大小大于 1M 的文件 ------${Font_color_suffix}\n" && find ${testpath} -size +1M -name '*.test' -exec ls -la {} \; | awk 'BEGIN{printf "%6s %9s\n", "size", "FileName";printf "------------------\n"} {printf "%4dmb %9s\n", $5/1024/1024, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前目录下文件大小等于 25M 的文件 ------${Font_color_suffix}\n" && find ${testpath} -size +1M -name '*.test' -exec ls -la {} \; | awk 'BEGIN{printf "%6s %9s\n", "size", "FileName";printf "------------------\n"} {printf "%4dmb %9s\n", $5/1024/1024, $9}'

    # 特定时间的文件
    echo -e "\n${Green_font_prefix}------ 修改系统时间为 2020-10-02 18:25:15 ------${Font_color_suffix}\n" && date -s "20201002 18:25:15"
    touch -d "2020-10-02 18:25:15" now.file
    touch -d "2020-10-02 18:00:15" 25_min_ago.file
    touch -d "2020-10-02 18:05:15" 20_min_ago.file
    touch -d "2020-10-02 17:35:15" 50_min_ago.file
    touch -d "2020-10-02 17:25:15" 1_hour_ago.file
    touch -d "2020-09-25 18:25:15" 7_days_ago.file
    touch -d "2020-09-18 18:25:15" 14_days_ago.file
    echo -e "\n${Green_font_prefix}------ 查找当前目录下 5 天之内修改且以 file 结尾的文件 ------${Font_color_suffix}\n" && find ${testpath} -mtime -5 -name "*file" -exec ls -la {} \; | awk 'BEGIN{printf "%6s %3s %6s %18s\n", "Month", "Day", "Time", "FileName";printf "--------------------------------------\n"} {printf "%6s %3d %6s %22s\n", $6, $7, $8, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前目录下 5 天之前修改且以 file 结尾的文件 ------${Font_color_suffix}\n" && find ${testpath} -mtime +5 -name "*file" -exec ls -la {} \; | awk 'BEGIN{printf "%6s %3s %6s %18s\n", "Month", "Day", "Time", "FileName";printf "--------------------------------------\n"} {printf "%6s %3d %6s %22s\n", $6, $7, $8, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前目录下 30 分钟内修改且以 file 结尾的文件 ------${Font_color_suffix}\n" && find ${testpath} -mmin -30 -name "*file" -exec ls -la {} \; | awk 'BEGIN{printf "%6s %3s %6s %18s\n", "Month", "Day", "Time", "FileName";printf "--------------------------------------\n"} {printf "%6s %3d %6s %22s\n", $6, $7, $8, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前目录下 30 分钟前修改且以 file 结尾的文件 ------${Font_color_suffix}\n" && find ${testpath} -mmin +30 -name "*file" -exec ls -la {} \; | awk 'BEGIN{printf "%6s %3s %6s %18s\n", "Month", "Day", "Time", "FileName";printf "--------------------------------------\n"} {printf "%6s %3d %6s %22s\n", $6, $7, $8, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前目录下更新时间比 14_days_ago.file 新但是比 25_min_ago.file 旧的文件 ------${Font_color_suffix}\n" && find ${testpath} -type f -name "*file" -newer ./14_days_ago.file -exec ls -la {} \; ! -newer 25_min_ago.file | awk 'BEGIN{printf "%6s %3s %6s %18s\n", "Month", "Day", "Time", "FileName";printf "--------------------------------------\n"} {printf "%6s %3d %6s %22s\n", $6, $7, $8, $9}'

    # 无属主、无属组文件
    chown 10086:10086 now.file 7_days_ago.file 50kb.test
    echo -e "\n${Green_font_prefix}------ 查找当前目录下的没有属主的文件 ------${Font_color_suffix}\n" && find ${testpath} -type f -nouser -exec ls -la {} \; | awk 'BEGIN{printf "%12s %18s\n", "User", "FileName";printf "--------------------------------------\n"} {printf "%12s %18s\n", $3, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前目录下的没有属组的文件 ------${Font_color_suffix}\n" && find ${testpath} -type f -nouser -exec ls -la {} \; | awk 'BEGIN{printf "%12s %18s\n", "Group", "FileName";printf "--------------------------------------\n"} {printf "%12s %18s\n", $4, $9}'

    # 权限文件
    chmod 644 grub.conf php.ini
    chmod 777 photo.xml
    echo -e "\n${Green_font_prefix}------ 查找当前目录下权限为 644 的文件 ------${Font_color_suffix}\n" && find ${testpath} -type f -perm 644 -exec ls -la {} \; | awk 'BEGIN{printf "%12s %18s\n", "Permissions", "FileName";printf "--------------------------------------\n"} {printf "%12s %18s\n", $1, $9}'
    echo -e "\n${Green_font_prefix}------ 查找当前目录下权限为 777 的文件 ------${Font_color_suffix}\n" && find ${testpath} -type f -perm 777 -exec ls -la {} \; | awk 'BEGIN{printf "%12s %18s\n", "Permissions", "FileName";printf "--------------------------------------\n"} {printf "%12s  %18s\n", $1, $9}'

    # 三级文件夹
    mkdir -p ${testpath}/test/dir1 && cd ${testpath}/test/dir1 && touch grub.conf loadbalance.conf php1.ini default_my.cnf my1.cnf mysql-clients1.cnf server1.cnf
    mkdir -p ${testpath}/test/dir2 && cd ${testpath}/test/dir2 && touch grub.conf loadbalance.conf php2.ini default_my.cnf my2.cnf mysql-clients2.cnf server2.cnf
    mkdir -p ${testpath}/test_1/abcd/efgh && cd ${testpath}/test_1/abcd/efgh && head -c 6M /dev/zero >abcd && head -c 12M /dev/zero >efgh && chown jaime:jaimegroup efgh && chmod 777 efgh
    mkdir -p ${testpath}/test_1/hijk/lmn && cd ${testpath}/test_1/hijk/lmn && head -c 6M /dev/zero >abcd && head -c 12M /dev/zero >efgh && chown jaime:jaimegroup efgh && chmod 777 efgh
    mkdir -p ${testpath}/test_1/opq/rst/uvw/xyz && cd ${testpath}/test_1/opq/rst/uvw/xyz && head -c 6M /dev/zero >abcd && head -c 12M /dev/zero >efgh && chown jaime:jaimegroup efgh && chmod 777 efgh
    mkdir -p ${testpath}/test_1/rst/uvw/xyz && cd ${testpath}/test_1/rst/uvw/xyz && head -c 6M /dev/zero >abcd && head -c 12M /dev/zero >efgh && chown jaime:jaimegroup efgh && chmod 777 efgh
    cd ${testpath}

    # 查看目录结构
    # tree

    echo -e "\n${Green_font_prefix}------ 在当前目录下查找以 conf 结尾或文件名以 a 开头的文件 ------${Font_color_suffix}\n" && find ${testpath} -type f -a \( -name "*conf" -o -name "^a" \)
    # 限制查找当前目录下的 grub.conf loadbalance.conf 文件，只会查找子目录下的
    echo -e "\n${Green_font_prefix}------ 在当前目录下的 2 级子目录开始查找以 conf 结尾或文件名以 a 开头的文件 ------${Font_color_suffix}\n" && find ${testpath} -mindepth 2 -type f -a \( -name "*conf" -o -name "^a" \)

    echo -e "\n${Green_font_prefix}------ 在当前目录下的 1 级子目录开始查找文件名为 abcd 或 efgh 的文件 ------${Font_color_suffix}\n" && find ${testpath} -mindepth 1 -type f -a \( -name "abcd" -o -name "efgh" \)
    # 限制查找 ./test_1/opq 以及 ./test_1/rst 下的 abcd efgh 文件
    echo -e "\n${Green_font_prefix}------ 在当前目录下的 1 级子目录开始查找文件名为 abcd 或 efgh 的文件，最多查找到 4 级子目录 ------${Font_color_suffix}\n" && find ${testpath} -mindepth 1 -maxdepth 4 -type f -a \( -name "abcd" -o -name "efgh" \)
    echo -e "\n${Green_font_prefix}------ 在当前目录下的 1 级子目录开始查找文件属主为 jaime、文件属组为 jaimegroup、文件大小大于 10M 且文件名为 abcd 或 efgh 的文件，最多查找到 5 级子目录，但排除 ./test_1/hijk 和 ./test_1/opq 目录 ------${Font_color_suffix}\n" && find ${testpath} -mindepth 1 -maxdepth 5 -path ./test_1/hijk -prune -o -path ./test_1/opq -prune -o -type f -user jaime -group jaimegroup -size +10M -perm 777 -a \( -name "abcd" -o -name "efgh" \) -exec ls -la {} \;

    # 恢复系统时间
    ntpdate ntp.aliyun.com
    ntpdate time1.cloud.tencent.com

    # 删除文件
    cd ${filepath} && rm -rf test_dir
    # grub.conf loadbalance.conf photo.xml excel.xml php.ini virtuoso.ini AAbb.pipe aabb.pipe model model-soft *.test *.file test/ test_1/

    # 删除 jaime 用户、 jaimegroup 组
    userdel -r jaime && groupdel jaimegroup
}

check_root
test_find
```

#### 脚本执行

```bash
------ 查找当前目录下以 conf 结尾的文件 ------

-rw-r--r--. 1 root root 0 Oct 2 18:25 /root/shell/test_dir/grub.conf
-rw-r--r--. 1 root root 0 Oct 2 18:25 /root/shell/test_dir/loadbalance.conf

------ 查找当前目录下文件名为 aabb 的文件(不区分大小写) ------

/root/shell/test_dir/aabb
/root/shell/test_dir/AABB

------ 查找当前路径下文件属主为 jaime 的文件 ------

        User        Group           FileName
--------------------------------------
       jaime   jaimegroup /root/shell/test_dir/grub.conf
       jaime   jaimegroup /root/shell/test_dir/loadbalance.conf
       jaime   jaimegroup /root/shell/test_dir/photo.xml

------ 查找当前路径下文件属组为 jaimegroup 的文件 ------

        User        Group           FileName
--------------------------------------
       jaime   jaimegroup /root/shell/test_dir/grub.conf
       jaime   jaimegroup /root/shell/test_dir/loadbalance.conf
       jaime   jaimegroup /root/shell/test_dir/photo.xml

------ 查找当前目录下的文件 ------

-rw-r--r--. 1 jaime jaimegroup 0 Oct 2 18:25 /root/shell/test_dir/grub.conf
-rw-r--r--. 1 jaime jaimegroup 0 Oct 2 18:25 /root/shell/test_dir/loadbalance.conf
-rw-r--r--. 1 jaime jaimegroup 0 Oct 2 18:25 /root/shell/test_dir/photo.xml
-rw-r--r--. 1 root root 0 Oct 2 18:25 /root/shell/test_dir/excel.xml
-rw-r--r--. 1 root root 0 Oct 2 18:25 /root/shell/test_dir/php.ini
-rw-r--r--. 1 root root 0 Oct 2 18:25 /root/shell/test_dir/virtuoso.ini

------ 查找当前路径下的链接文件 ------

lrwxrwxrwx. 1 root root 5 Oct 2 18:25 /root/shell/test_dir/model-soft -> model

------ 查找当前路径下的管道文件 ------

prw-r--r--. 1 root root 0 Oct 2 18:25 /root/shell/test_dir/aabb.pipe
prw-r--r--. 1 root root 0 Oct 2 18:25 /root/shell/test_dir/AAbb.pipe

------ 查找当前目录下文件大小大于 1M 的文件 ------

  size  FileName
------------------
  50mb /root/shell/test_dir/50mb.test
  25mb /root/shell/test_dir/25mb.test

------ 查找当前目录下文件大小等于 25M 的文件 ------

  size  FileName
------------------
  50mb /root/shell/test_dir/50mb.test
  25mb /root/shell/test_dir/25mb.test

------ 修改系统时间为 2020-10-02 18:25:15 ------

Fri Oct  2 18:25:15 EDT 2020

------ 查找当前目录下 5 天之内修改且以 file 结尾的文件 ------

 Month Day   Time           FileName
--------------------------------------
   Oct   2  18:25 /root/shell/test_dir/now.file
   Oct   2  18:00 /root/shell/test_dir/25_min_ago.file
   Oct   2  18:05 /root/shell/test_dir/20_min_ago.file
   Oct   2  17:35 /root/shell/test_dir/50_min_ago.file
   Oct   2  17:25 /root/shell/test_dir/1_hour_ago.file

------ 查找当前目录下 5 天之前修改且以 file 结尾的文件 ------

 Month Day   Time           FileName
--------------------------------------
   Sep  25  18:25 /root/shell/test_dir/7_days_ago.file
   Sep  18  18:25 /root/shell/test_dir/14_days_ago.file

------ 查找当前目录下 30 分钟内修改且以 file 结尾的文件 ------

 Month Day   Time           FileName
--------------------------------------
   Oct   2  18:25 /root/shell/test_dir/now.file
   Oct   2  18:00 /root/shell/test_dir/25_min_ago.file
   Oct   2  18:05 /root/shell/test_dir/20_min_ago.file

------ 查找当前目录下 30 分钟前修改且以 file 结尾的文件 ------

 Month Day   Time           FileName
--------------------------------------
   Oct   2  17:35 /root/shell/test_dir/50_min_ago.file
   Oct   2  17:25 /root/shell/test_dir/1_hour_ago.file
   Sep  25  18:25 /root/shell/test_dir/7_days_ago.file
   Sep  18  18:25 /root/shell/test_dir/14_days_ago.file

------ 查找当前目录下更新时间比 14_days_ago.file 新但是比 25_min_ago.file 旧的文件 ------

 Month Day   Time           FileName
--------------------------------------
   Oct   2  18:25 /root/shell/test_dir/now.file
   Oct   2  18:00 /root/shell/test_dir/25_min_ago.file
   Oct   2  18:05 /root/shell/test_dir/20_min_ago.file
   Oct   2  17:35 /root/shell/test_dir/50_min_ago.file
   Oct   2  17:25 /root/shell/test_dir/1_hour_ago.file
   Sep  25  18:25 /root/shell/test_dir/7_days_ago.file

------ 查找当前目录下的没有属主的文件 ------

        User           FileName
--------------------------------------
       10086 /root/shell/test_dir/50kb.test
       10086 /root/shell/test_dir/now.file
       10086 /root/shell/test_dir/7_days_ago.file

------ 查找当前目录下的没有属组的文件 ------

       Group           FileName
--------------------------------------
       10086 /root/shell/test_dir/50kb.test
       10086 /root/shell/test_dir/now.file
       10086 /root/shell/test_dir/7_days_ago.file

------ 查找当前目录下权限为 644 的文件 ------

 Permissions           FileName
--------------------------------------
 -rw-r--r--. /root/shell/test_dir/grub.conf
 -rw-r--r--. /root/shell/test_dir/loadbalance.conf
 -rw-r--r--. /root/shell/test_dir/excel.xml
 -rw-r--r--. /root/shell/test_dir/php.ini
 -rw-r--r--. /root/shell/test_dir/virtuoso.ini
 -rw-r--r--. /root/shell/test_dir/model
 -rw-r--r--. /root/shell/test_dir/50mb.test
 -rw-r--r--. /root/shell/test_dir/50kb.test
 -rw-r--r--. /root/shell/test_dir/25kb.test
 -rw-r--r--. /root/shell/test_dir/512c.test
 -rw-r--r--. /root/shell/test_dir/25mb.test
 -rw-r--r--. /root/shell/test_dir/now.file
 -rw-r--r--. /root/shell/test_dir/25_min_ago.file
 -rw-r--r--. /root/shell/test_dir/20_min_ago.file
 -rw-r--r--. /root/shell/test_dir/50_min_ago.file
 -rw-r--r--. /root/shell/test_dir/1_hour_ago.file
 -rw-r--r--. /root/shell/test_dir/7_days_ago.file
 -rw-r--r--. /root/shell/test_dir/14_days_ago.file

------ 查找当前目录下权限为 777 的文件 ------

 Permissions           FileName
--------------------------------------
 -rwxrwxrwx.  /root/shell/test_dir/photo.xml

------ 在当前目录下查找以 conf 结尾或文件名以 a 开头的文件 ------

/root/shell/test_dir/grub.conf
/root/shell/test_dir/loadbalance.conf
/root/shell/test_dir/test/dir1/grub.conf
/root/shell/test_dir/test/dir1/loadbalance.conf
/root/shell/test_dir/test/dir2/grub.conf
/root/shell/test_dir/test/dir2/loadbalance.conf

------ 在当前目录下的 2 级子目录开始查找以 conf 结尾或文件名以 a 开头的文件 ------

/root/shell/test_dir/test/dir1/grub.conf
/root/shell/test_dir/test/dir1/loadbalance.conf
/root/shell/test_dir/test/dir2/grub.conf
/root/shell/test_dir/test/dir2/loadbalance.conf

------ 在当前目录下的 1 级子目录开始查找文件名为 abcd 或 efgh 的文件 ------

/root/shell/test_dir/test_1/abcd/efgh/abcd
/root/shell/test_dir/test_1/abcd/efgh/efgh
/root/shell/test_dir/test_1/hijk/lmn/abcd
/root/shell/test_dir/test_1/hijk/lmn/efgh
/root/shell/test_dir/test_1/opq/rst/uvw/xyz/abcd
/root/shell/test_dir/test_1/opq/rst/uvw/xyz/efgh
/root/shell/test_dir/test_1/rst/uvw/xyz/abcd
/root/shell/test_dir/test_1/rst/uvw/xyz/efgh

------ 在当前目录下的 1 级子目录开始查找文件名为 abcd 或 efgh 的文件，最多查找到 4 级子目录 ------

/root/shell/test_dir/test_1/abcd/efgh/abcd
/root/shell/test_dir/test_1/abcd/efgh/efgh
/root/shell/test_dir/test_1/hijk/lmn/abcd
/root/shell/test_dir/test_1/hijk/lmn/efgh

------ 在当前目录下的 1 级子目录开始查找文件属主为 jaime、文件属组为 jaimegroup、文件大小大于 10M 且文件名为 abcd 或 efgh 的文件，最多查找到 5 级子目录，但排除 ./test_1/hijk 和 ./test_1/opq 目录 ------

-rwxrwxrwx. 1 jaime jaimegroup 12582912 Oct  2 18:25 /root/shell/test_dir/test_1/abcd/efgh/efgh
-rwxrwxrwx. 1 jaime jaimegroup 12582912 Oct  2 18:25 /root/shell/test_dir/test_1/hijk/lmn/efgh
-rwxrwxrwx. 1 jaime jaimegroup 12582912 Oct  2 18:25 /root/shell/test_dir/test_1/rst/uvw/xyz/efgh
```

## 总结及适用场景分析

find、locate、whereis 和 which 总结及适用场景分析。

### locate 命令

- 文件查找命令，所属软件包 mlocate。
- 不同于 find 命令是在整块磁盘中搜索，locate 命令是在数据库文件中查找。新创建的文件使用 locate 命令可能会查找不到，使用 updatedb 命令更新数据库文件后便可查找到。
- find 是默认全部匹配，locate 是默认部分匹配。

### updatedb 命令

- 用户更新 `/var/lib/mlocate.db`。
- 所使用配置文件 `/etc/updatedb.conf`。
- 该命令在后台 cron 计划任务中定期执行。

### whereis 命令

| 选项 | 含义               |
| ---- | ------------------ |
| -b   | 只返回二进制文件   |
| -m   | 只返回帮助文档文件 |
| -s   | 只返回源代码文件   |

### which 命令

- 仅查找二进制程序文件。

| 选项 | 含义             |
| ---- | ---------------- |
| -b   | 只返回二进制文件 |

### 各命令使用场景推荐

| 命令    | 适用场景                           | 优缺点                   |
| ------- | ---------------------------------- | ------------------------ |
| find    | 查找某一类文件，比如文件名部分一致 | 功能强大，速度慢         |
| locate  | 只能查找单个文件                   | 功能单一，速度快         |
| whereis | 查找程序的可执行文件、帮助文档等   | 不常用                   |
| which   | 只查找程序的可执行文件             | 常用于查找程序的绝对路径 |

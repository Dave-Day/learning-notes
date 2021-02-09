---
title: 文本处理命令 grep
url: linux-shell-grep
---

# 文本处理命令 grep

本章主要讲解 grep 和 egrep。

## grep

grep 是"`Global Regular Expressions Print`"的首字母缩写词，意为全局正则表达式打印。grep 是一个逐行扫描指定文件或文件的程序，返回包含模式的行。模式是一种表达式，它通过将字符解释为元字符来指定一组字符串。例如，星号元字符（\*）被解释为"前面元素的零个或多个"。这使用户能够在 grep 命令中键入一系列短字符和元字符，以使计算机向我们显示哪些文件匹配的行。

### 语法格式

|        | 语法                                    |
| ------ | --------------------------------------- | ------------------------ |
| 第一种 | `grep [option] [pattern] [file1,file2]` |
| 第二种 | `command                                | grep [option] [pattren]` |

### 参数

| 选项 | 含义                                       |
| ---- | ------------------------------------------ |
| `-v` | 不显示匹配行信息                           |
| `-i` | 搜索时忽略大小写                           |
| `-n` | 显示行号                                   |
| `-r` | 递归搜素                                   |
| `-E` | 支持扩展正则表达式                         |
| `-F` | 不按正则表达式匹配，按照字符串字面意思匹配 |
| `-c` | 只显示匹配行总数，不显示具体内容           |
| `-w` | 匹配整词                                   |
| `-x` | 匹配整行                                   |
| `-l` | 只显示文件名，不显示匹配行内容             |
| `-s` | 不显示错误信息                             |

### 练习

#### 测试脚本

```shell
#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# grep 练习

filepath=$(
    cd "$(dirname "$0")"
    pwd
)
testpath="${filepath}/test_dir"
Green_font_prefix="\033[32m" && Red_font_prefix="\033[31m" && Green_background_prefix="\033[42;37m" && Red_background_prefix="\033[41;37m" && Font_color_suffix="\033[0m"

function test_grep() {
    mkdir -p ${testpath} && cd ${testpath}
    # 将 man 文档分割成数个文件，每个文件 20 行
    split /etc/man_db.conf -d -a 2 -l 20 man_db_

    echo -e "\n${Green_font_prefix}------ 查找当前目录下的所有文件 ------${Font_color_suffix}\n" && find ${filepath} -type f -exec ls -la {} \;
    echo -e "\n${Green_font_prefix}------ 在 man_db_00 文件中查找包含 man 字段的行 ------${Font_color_suffix}\n" && grep man man_db_00
    echo -e "\n${Green_font_prefix}------ 在 man_db_00 文件中查找包含 man 字段的行(不区分大小写) ------${Font_color_suffix}\n" && grep -i man man_db_00
    echo -e "\n${Green_font_prefix}------ 在 man_db_00 文件中查找不包含 man 字段的行(反向查找) ------${Font_color_suffix}\n" && grep -v man man_db_00
    echo -e "\n${Green_font_prefix}------ 在 man_db_00 文件中查找包含 man 字段的行并显示行号 ------${Font_color_suffix}\n" && grep -n man man_db_00
    echo -e "\n${Green_font_prefix}------ 在 man_db_01 文件中查找符合正则表达式 *PATH* 的行并显示行号 ------${Font_color_suffix}\n" && grep -n "*PATH*" man_db_01
    echo -e "\n${Green_font_prefix}------ 在 man_db_01 文件中查找符合 *PATH* 的行并显示行号(不按照正则表达式匹配) ------${Font_color_suffix}\n" && grep -n -F "*PATH*" man_db_01
    echo -e "\n${Green_font_prefix}------ 在 man_db_01 文件中查找符合扩展正则表达式 man|MAN 的行并显示行号 ------${Font_color_suffix}\n" && grep -n -E "man|MAN" man_db_01
    echo -e "\n${Green_font_prefix}------ 在 man_db_01 文件中查找符合扩展正则表达式 man|MAN 的行总数 ------${Font_color_suffix}\n" && grep -c -E "man|MAN" man_db_01
    echo -e "\n${Green_font_prefix}------ 在 man_db_01 文件中查找包含 /bin 的行并显示行号 ------${Font_color_suffix}\n" && grep "/bin" man_db_01
    echo -e "\n${Green_font_prefix}------ 在 man_db_01 文件中查找符合 /bin 全字符的行并显示行号 ------${Font_color_suffix}\n" && grep -w "/bin" man_db_01
    echo -e "\n${Green_font_prefix}------ 查找当前目录下的所有文件中查找包含 man 字段的行并显示行号(递归搜索) ------${Font_color_suffix}\n" && grep -r -n man

    # 删除测试目录
    cd ${filepath} && rm -rf test_dir/
}

test_grep
```

#### 运行结果

```bash
------ 查找当前目录下的所有文件 ------

-rw-r--r--. 1 ryan ryan 2715 Jan 31  2021 /home/ryan/Documents/1.sh
-rw-r--r--. 1 ryan ryan 801 Oct  2 19:10 /home/ryan/Documents/test_dir/man_db_00
-rw-r--r--. 1 ryan ryan 749 Oct  2 19:10 /home/ryan/Documents/test_dir/man_db_01
-rw-r--r--. 1 ryan ryan 1045 Oct  2 19:10 /home/ryan/Documents/test_dir/man_db_02
-rw-r--r--. 1 ryan ryan 722 Oct  2 19:10 /home/ryan/Documents/test_dir/man_db_03
-rw-r--r--. 1 ryan ryan 541 Oct  2 19:10 /home/ryan/Documents/test_dir/man_db_04
-rw-r--r--. 1 ryan ryan 917 Oct  2 19:10 /home/ryan/Documents/test_dir/man_db_05
-rw-r--r--. 1 ryan ryan 396 Oct  2 19:10 /home/ryan/Documents/test_dir/man_db_06

------ 在 man_db_00 文件中查找包含 man 字段的行 ------

# This file is used by the man-db package to configure the man and cat paths.
# It is also used to provide a manpath for those without one by examining
# their PATH environment variable. For details see the manpath(5) man page.
# MANDATORY_MANPATH            manpath_element
# MANPATH_MAP        path_element    manpath_element
# MANDB_MAP        global_manpath    [relative_catpath]
#MANDATORY_MANPATH             /usr/src/pvm3/man
MANDATORY_MANPATH            /usr/man

------ 在 man_db_00 文件中查找包含 man 字段的行(不区分大小写) ------

# This file is used by the man-db package to configure the man and cat paths.
# It is also used to provide a manpath for those without one by examining
# their PATH environment variable. For details see the manpath(5) man page.
# MANDATORY_MANPATH            manpath_element
# MANPATH_MAP        path_element    manpath_element
# MANDB_MAP        global_manpath    [relative_catpath]
# every automatically generated MANPATH includes these fields
#MANDATORY_MANPATH             /usr/src/pvm3/man
MANDATORY_MANPATH            /usr/man

------ 在 man_db_00 文件中查找不包含 man 字段的行(反向查找) ------

#
#
#
# Lines beginning with `#' are comments and are ignored. Any combination of
# tabs or spaces may be used as `whitespace' separators.
#
# There are three mappings allowed in this file:
# --------------------------------------------------------
#---------------------------------------------------------
# every automatically generated MANPATH includes these fields
#
#

------ 在 man_db_00 文件中查找包含 man 字段的行并显示行号 ------

3:# This file is used by the man-db package to configure the man and cat paths.
4:# It is also used to provide a manpath for those without one by examining
5:# their PATH environment variable. For details see the manpath(5) man page.
12:# MANDATORY_MANPATH            manpath_element
13:# MANPATH_MAP        path_element    manpath_element
14:# MANDB_MAP        global_manpath    [relative_catpath]
18:#MANDATORY_MANPATH             /usr/src/pvm3/man
20:MANDATORY_MANPATH            /usr/man

------ 在 man_db_01 文件中查找符合正则表达式 *PATH* 的行并显示行号 ------

7:#        *PATH*        ->    *MANPATH*

------ 在 man_db_01 文件中查找符合 *PATH* 的行并显示行号(不按照正则表达式匹配) ------

7:#        *PATH*        ->    *MANPATH*

------ 在 man_db_01 文件中查找符合扩展正则表达式 man|MAN 的行并显示行号 ------

1:MANDATORY_MANPATH            /usr/share/man
2:MANDATORY_MANPATH            /usr/local/share/man
4:# set up PATH to MANPATH mapping
5:# ie. what man tree holds man pages for what binary directory.
7:#        *PATH*        ->    *MANPATH*
9:MANPATH_MAP    /bin            /usr/share/man
10:MANPATH_MAP    /usr/bin        /usr/share/man
11:MANPATH_MAP    /sbin            /usr/share/man
12:MANPATH_MAP    /usr/sbin        /usr/share/man
13:MANPATH_MAP    /usr/local/bin        /usr/local/man
14:MANPATH_MAP    /usr/local/bin        /usr/local/share/man
15:MANPATH_MAP    /usr/local/sbin        /usr/local/man
16:MANPATH_MAP    /usr/local/sbin        /usr/local/share/man
17:MANPATH_MAP    /usr/X11R6/bin        /usr/X11R6/man
18:MANPATH_MAP    /usr/bin/X11        /usr/X11R6/man
19:MANPATH_MAP    /usr/games        /usr/share/man
20:MANPATH_MAP    /opt/bin        /opt/man

------ 在 man_db_01 文件中查找符合扩展正则表达式 man|MAN 的行总数 ------

17

------ 在 man_db_01 文件中查找包含 /bin 的行并显示行号 ------

MANPATH_MAP    /bin            /usr/share/man
MANPATH_MAP    /usr/bin        /usr/share/man
MANPATH_MAP    /usr/local/bin        /usr/local/man
MANPATH_MAP    /usr/local/bin        /usr/local/share/man
MANPATH_MAP    /usr/X11R6/bin        /usr/X11R6/man
MANPATH_MAP    /usr/bin/X11        /usr/X11R6/man
MANPATH_MAP    /opt/bin        /opt/man

------ 在 man_db_01 文件中查找符合 /bin 全字符的行并显示行号 ------

MANPATH_MAP    /bin            /usr/share/man

------ 查找当前目录下的所有文件中查找包含 man 字段的行并显示行号(递归搜索) ------

man_db_00:3:# This file is used by the man-db package to configure the man and cat paths.
man_db_00:4:# It is also used to provide a manpath for those without one by examining
man_db_00:5:# their PATH environment variable. For details see the manpath(5) man page.
man_db_00:12:# MANDATORY_MANPATH            manpath_element
man_db_00:13:# MANPATH_MAP        path_element    manpath_element
man_db_00:14:# MANDB_MAP        global_manpath    [relative_catpath]
man_db_00:18:#MANDATORY_MANPATH             /usr/src/pvm3/man
man_db_00:20:MANDATORY_MANPATH            /usr/man
man_db_01:1:MANDATORY_MANPATH            /usr/share/man
man_db_01:2:MANDATORY_MANPATH            /usr/local/share/man
man_db_01:5:# ie. what man tree holds man pages for what binary directory.
man_db_01:9:MANPATH_MAP    /bin            /usr/share/man
man_db_01:10:MANPATH_MAP    /usr/bin        /usr/share/man
man_db_01:11:MANPATH_MAP    /sbin            /usr/share/man
man_db_01:12:MANPATH_MAP    /usr/sbin        /usr/share/man
man_db_01:13:MANPATH_MAP    /usr/local/bin        /usr/local/man
man_db_01:14:MANPATH_MAP    /usr/local/bin        /usr/local/share/man
man_db_01:15:MANPATH_MAP    /usr/local/sbin        /usr/local/man
man_db_01:16:MANPATH_MAP    /usr/local/sbin        /usr/local/share/man
man_db_01:17:MANPATH_MAP    /usr/X11R6/bin        /usr/X11R6/man
man_db_01:18:MANPATH_MAP    /usr/bin/X11        /usr/X11R6/man
man_db_01:19:MANPATH_MAP    /usr/games        /usr/share/man
man_db_01:20:MANPATH_MAP    /opt/bin        /opt/man
man_db_02:1:MANPATH_MAP    /opt/sbin        /opt/man
man_db_02:3:# For a manpath element to be treated as a system manpath (as most of those
man_db_02:6:# manpath. If no catpath string is used, the catpath will default to the
man_db_02:7:# given manpath.
man_db_02:9:# You *must* provide all system manpaths, including manpaths for alternate
man_db_02:10:# operating systems, locale specific manpaths, and combinations of both, if
man_db_02:11:# they exist, otherwise the permissions of the user running man/mandb will
man_db_02:12:# be used to manipulate the manual pages. Also, mandb will not initialise
man_db_02:13:# the database cache for any manpaths not mentioned below unless explicitly
man_db_02:20:# Any manpaths that are subdirectories of other manpaths must be mentioned
man_db_03:1:# *before* the containing manpath. E.g. /usr/man/preformat must be listed
man_db_03:2:# before /usr/man.
man_db_03:6:MANDB_MAP    /usr/man        /var/cache/man/fsstnd
man_db_03:7:MANDB_MAP    /usr/share/man        /var/cache/man
man_db_03:8:MANDB_MAP    /usr/local/man        /var/cache/man/oldlocal
man_db_03:9:MANDB_MAP    /usr/local/share/man    /var/cache/man/local
man_db_03:10:MANDB_MAP    /usr/X11R6/man        /var/cache/man/X11R6
man_db_03:11:MANDB_MAP    /opt/man        /var/cache/man/opt
man_db_04:2:#DEFINE     troff     groff -mandoc
man_db_04:3:#DEFINE     nroff     nroff -mandoc -c
man_db_06:10:# NOCACHE keeps man from creating cat pages.
```

## 类似命令

### egrep

egrep 是"`Extended Global Regular Expressions Print`"的首字母缩写词。grep 默认不支持扩展正则表达式，只支持基础正则表达式，想要支持扩展正则表达式可以：

- 使用 `grep -E` 命令
- 使用 `wgrep` 命令

### fgrep

fgrep 是 "`Fixed-string Global Regular Expressions Print`" 的首字母缩写词，意为固定字符串全局正则表达式打印。

`fgrep` 命令用于查找文件里符合条件的字符串，等价于 `grep -F` 命令。

### pgrep

pgrep 是"`Process-ID Global Regular Expressions Print`"的首字母缩写词。pgrep 命令以名称为依据从运行进程队列中查找进程，并显示查找到的进程 id。每一个进程 ID 以一个十进制数表示，通过一个分割字符串和下一个 ID 分开，默认的分割字符串是一个新行。对于每个属性选项，用户可以在命令行上指定一个以逗号分割的可能值的集合。

#### 选项

| 选项 | 描述                             |
| ---- | -------------------------------- |
| `-o` | 仅显示找到的最小（起始）进程号； |
| `-n` | 仅显示找到的最大（结束）进程号； |
| `-l` | 显示进程名称；                   |
| `-P` | 指定父进程号；                   |
| `-g` | 指定进程组；                     |
| `-t` | 指定开启进程的终端；             |
| `-u` | 指定进程的有效用户 ID。          |

#### 文档

```bash
Usage:
 pgrep [options] <pattern>

Options:
 -d, --delimiter <string>  specify output delimiter
 -l, --list-name           list PID and process name
 -a, --list-full           list PID and full command line
 -v, --inverse             negates the matching
 -w, --lightweight         list all TID
 -c, --count               count of matching processes
 -f, --full                use full process name to match
 -g, --pgroup <PGID,...>   match listed process group IDs
 -G, --group <GID,...>     match real group IDs
 -n, --newest              select most recently started
 -o, --oldest              select least recently started
 -P, --parent <PPID,...>   match only child processes of the given parent
 -s, --session <SID,...>   match session IDs
 -t, --terminal <tty,...>  match by controlling terminal
 -u, --euid <ID,...>       match by effective IDs
 -U, --uid <ID,...>        match by real IDs
 -x, --exact               match exactly with the command name
 -F, --pidfile <file>      read PIDs from file
 -L, --logpidfile          fail if PID file is not locked
 --ns <PID>                match the processes that belong to the same
                           namespace as <pid>
 --nslist <ns,...>         list which namespaces will be considered for
                           the --ns option.
                           Available namespaces: ipc, mnt, net, pid, user, uts

 -h, --help     display this help and exit
 -V, --version  output version information and exit
```

#### 测试

```bash
[ryan@ryan-tencentcloud-2]~ pgrep -lo nginx # nginx 最小进程号
4399 nginx
[ryan@ryan-tencentcloud-2]~ pgrep -ln nginx # nginx 最大进程号
4400 nginx
[ryan@ryan-tencentcloud-2]~ pgrep -l nginx # nginx 进程号和进程名
4399 nginx
4400 nginx
[ryan@ryan-tencentcloud-2]~ pgrep -la nginx # nginx 进程号和命令
4399 nginx: master process /usr/sbin/nginx
4400 nginx: worker process
```

### rgrep

` rgrep` 命令用于递归查找文件里符合条件的字符串，类似于 `grep -r` 命令。

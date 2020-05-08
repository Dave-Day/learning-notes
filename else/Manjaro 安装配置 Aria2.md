## Manjaro 安装配置 Aria2

> GNU/Linux 平台下 Aria2 图形界面工具：
>
> - persepolis：Qt front-end for aria2 download manager.
>   - 安装： `yay persepolis `
> - motrix：A full-featured download manager.
>   - 安装：`yay motrix `
>   - Motrix 在 Linux 中首次启动可能需要使用 `sudo` 运行，因为可能没有创建下载会话文件的权限 (`/var/cache/aria2.session`)。

## 安装 Aria2

### 官方版本

> 官方版本缺点：
>
> - 线程限制
> - 线程掉线
>
> 推荐使用下面重新编译的增强版。

```bash
sudo pacman -S aria2
```

### 优化增强版

> [Aria2 static builds for GNU/Linux with custom patches | Aria2 静态编译 ( GNU/Linux 多平台 ) 破解线程 防掉线程 优化增强版](https://github.com/P3TERX/aria2-builder)

```bash
cd ~/Downloads

# amd64
wget https://download.fastgit.org/P3TERX/aria2-builder/releases/download/1.35.0_2020.06.13/aria2-1.35.0-static-linux-amd64.tar.gz
# i386
wget https://download.fastgit.org/P3TERX/aria2-builder/releases/download/1.35.0_2020.06.13/aria2-1.35.0-static-linux-i386.tar.gz
# arm64
wget https://download.fastgit.org/P3TERX/aria2-builder/releases/download/1.35.0_2020.06.13/aria2-1.35.0-static-linux-arm64.tar.gz
# armhf
wget https://download.fastgit.org/P3TERX/aria2-builder/releases/download/1.35.0_2020.06.13/aria2-1.35.0-static-linux-armhf.tar.gz

# 解压
tar zxvf aria2-1.35.0-static-*.tar.gz

# 给予权限
sudo chmod +x aria2c && sudo mv aria2c /usr/local/bin
```

## 配置 Aria2

### 下载配置文件

```bash
# 创建下载 Aria2 路径
mkdir -p ~/Downloads/Aria2/

# 创建 Aria2 配置文件路径
mkdir ~/.aria2 && cd $_

# 下载配置文件
## Github
wget https://raw.githubusercontent.com/Ryanjiena/Blog/master/aria2/aria2.zip
## jsdelivr
https://cdn.jsdelivr.net/gh/Ryanjiena/Blog@master/aria2/aria2.zip

# 解压后删除文件
zip aria2.zip && rm -f aria2.zip 

# 给予权限
sudo chmod +x aria2 clean.sh delete.sh 

# 创建软链接
sudo ln -s ~/.aria2/aria2 /usr/local/bin/aria2
```

### 修改 aria2.conf

> 增强版: [myfreeer/aria2-build-msys2](https://github.com/myfreeer/aria2-build-msys2/releases) (Windows) 和 [P3TERX/aria2-builder](https://github.com/P3TERX/aria2-builder/releases) (GNU/Linux) 项目所构建的增强版本。

#### 基本设置

```properties
# 下载路径. 可使用绝对路径或相对路径, 默认: 当前启动位置
dir=/home/ryanjie/Downloads/Aria2/

# 从会话文件中读取下载任务
input-file=/home/ryanjie/.aria2/aria2.session

# 日志文件, 默认:  不保存
# 日志文件的路径. 如果设置为 "-", 日志则写入到 stdout. 如果设置为空字符串(""), 日志将不会记录到磁盘上.
log=/home/ryanjie/.aria2/aria2.log

# 最大同时下载数, 默认: 5
max-concurrent-downloads=8

# 检查完整性, 默认: false
# 通过对文件的每个分块或整个文件进行哈希验证来检查文件的完整性. 此选项仅对BT、Metalink及设置了 --checksum 选项的 HTTP(S)/FTP 链接生效.
check-integrity=false

# 断点续传
# 继续下载部分完成的文件. 启用此选项可以继续下载从浏览器或其他程序按顺序下载的文件. 此选项目前只支持 HTTP(S)/FTP 下载的文件.
continue=true
```

#### HTTP/FTP/SFTP 设置

```properties
# 代理服务器
# 设置所有协议的代理服务器地址. 如果覆盖之前设置的代理服务器, 使用 "" 即可. 您还可以针对特定的协议覆盖此选项, 即使用 --http-proxy, --https-proxy 和 --ftp-proxy 选项. 此设置将会影响所有下载. 代理服务器地址的格式为 [http: //][USER: PASSWORD@]HOST[: PORT].
# all-proxy=

# 代理服务器用户名
# all-proxy-user=

# 代理服务器密码
# all-proxy-passwd=

# 连接超时时间（秒）. 默认: 60
# 设置建立 HTTP/FTP/代理服务器 连接的超时时间(秒). 当连接建立后, 此选项不再生效, 请使用 --timeout 选项.
connect-timeout=10

# 模拟运行
# 如果设置为"是", aria2 将仅检查远程文件是否存在而不会下载文件内容. 此选项仅对 HTTP/FTP 下载生效. 如果设置为 true, BT 下载将会直接取消.
# dry=

# 最小速度限制（字节）. 默认: 0 (无限制)
# 当下载速度低于此选项设置的值(B/s) 时将会关闭连接. 0 表示不设置最小速度限制. 您可以增加数值的单位 K 或 M (1K = 1024, 1M = 1024K). 此选项不会影响 BT 下载.
lowest-speed-limit=0

# 单服务器最大连接数, 默认: 1
# 最大值为 16 (使用增强版无此限制).  最大值受限于单任务最大连接线程数(split)所设定的值. 
max-connection-per-server=32

# 文件未找到重试次数, 默认: 0 (禁用)
# 如果 aria2 从远程 HTTP/FTP 服务器收到 "文件未找到" 的状态超过此选项设置的次数后下载将会失败. 设置为 0 将会禁用此选项. 此选项仅影响 HTTP/FTP 服务器. 重试时同时会记录重试次数, 所以也需要设置 --max-tries 这个选项.
max-file-not-found=10

# 最大尝试次数, 默认: 5
# 设置最大尝试次数. 0 表示不限制.
max-tries=0

# 最小文件分片大小, 默认: 20M
# aria2 不会分割小于 2*SIZE 字节的文件. 
# 例如, 文件大小为 20MB, 如果 SIZE 为 10M, aria2 会把文件分成 2 段 [0-10MB) 和 [10MB-20MB), 并且使用 2 个源进行下载 (如果 --split >= 2). 如果 SIZE 为 15M, 由于 2*15M > 20MB, 因此 aria2 不会分割文件并使用 1 个源进行下载. 
# 您可以增加数值的单位 K 或 M (1K = 1024, 1M = 1024K). 可以设置的值为: 1M-1024M. (使用增强版最小值可设置为1K )
# 理论上值越小使用下载分段就越多, 所能获得的实际线程数就越大, 下载速度就越快, 但受限于所下载文件服务器的策略. 
min-split-size=4M

# .netrc 文件路径, 默认: /home/ryanjie/.netrc
# netrc-path=/home/ryanjie/.netrc

# 禁用 netrc, 默认: false
no-netrc=true

# 不使用代理服务器列表
# 设置不使用代理服务器的主机名, 域名, 包含或不包含子网掩码的网络地址, 多个使用逗号分隔.
# no-proxy=

# 代理服务器请求方法, 默认: get
# 设置用来请求代理服务器的方法. 方法可设置为 get 或 tunnel. HTTPS 下载将忽略此选项并总是使用 tunnel.
proxy-method=get

# 获取服务器文件时间, 默认: false
# 从 HTTP/FTP 服务获取远程文件的时间戳, 如果可用将设置到本地文件
remote-time=true

# URI 复用, 默认: true
# 当所有给定的 URI 地址都已使用, 继续使用已经使用过的 URI 地址.
reuse-uri=false

# 重试等待时间（秒）, 默认: 0 (禁用)
# 设置重试间隔时间(秒). 当此选项的值大于 0 时, aria2 在 HTTP 服务器返回 503 响应时将会重试.
retry-wait=10

## 增强扩展设置(非官方) ##
# 在服务器返回 HTTP 400 Bad Request 时重试, 仅当 retry-wait > 0 时有效, 默认 false
retry-on-400=true
# 在服务器返回 HTTP 403 Forbidden 时重试, 仅当 retry-wait > 0 时有效, 默认 false
retry-on-403=true
# 在服务器返回 HTTP 406 Not Acceptable 时重试, 仅当 retry-wait > 0 时有效, 默认 false
retry-on-406=true
# 在服务器返回未知状态码时重试, 仅当 retry-wait > 0 时有效, 默认 false
retry-on-unknown=true

# 服务器状态保存文件
# 指定用来保存服务器状态的文件名. 您可以使用 --server-stat-if 参数读取保存的数据.
# server-stat-of=

# 服务器状态超时（秒）, 默认: 86400(24h)
# 指定服务器状态的过期时间 (单位为秒).
server-stat-timeout=86400

# 单任务连接数, 默认: 5
# 下载时使用 N 个连接. 如果提供超过 N 个 URI 地址, 则使用前 N 个地址, 剩余的地址将作为备用. 如果提供的 URI 地址不足 N 个, 这些地址多次使用以保证同时建立 N 个连接. 同一服务器的连接数会被 --max-connection-per-server 选项限制.
split=64

# 分片选择算法, 默认: default
# 可选值: 'default' 'inorder' 'random' 'geom'
# 指定 HTTP/FTP 下载使用的分片选择算法. 分片表示的是并行下载时固定长度的分隔段. 
# 如果设置为"默认", aria2 将会按减少建立连接数选择分片. 由于建立连接操作的成本较高, 因此这是合理的默认行为. 
# 如果设置为"顺序", aria2 将选择索引最小的分片. 索引为 0 时表示为文件的第一个分片. 这将有助于视频的边下边播. --enable-http-pipelining 选项有助于减少重连接的开销. 请注意, aria2 依赖于 --min-split-size 选项, 所以有必要对 --min-split-size 选项设置一个合理的值. 
# 如果设置为"随机", aria2 将随机选择一个分片. 就像"顺序"一样, 依赖于 --min-split-size 选项. 
# 如果设置为"几何", aria2 会先选择索引最小的分片, 然后会为之前选择的分片保留指数增长的空间. 这将减少建立连接的次数, 同时文件开始部分将会先行下载. 这也有助于视频的边下边播.
stream-piece-selector=default

# 超时时间（秒）, 默认:  60
timeout=10

# URI 选择算法, 默认:  feedback(反馈)
# 可选值: 'inorder' 'feedback' 'adaptive'
# 指定 URI 选择的算法. 可选的值包括 "按顺序", "反馈" 和 "自适应". 
# 如果设置为"按顺序", URI 将按列表中出现的顺序使用. 
# 如果设置为"反馈", aria2 将根据之前的下载速度选择 URI 列表中下载速度最快的服务器. 同时也将有效跳过无效镜像. 之前统计的下载速度将作为服务器状态文件的一部分, 参见 --server-stat-of 和 --server-stat-if 选项. 
# 如果设置为"自适应", 将从最好的镜像和保留的连接里选择一项. 补充说明, 其返回的镜像没有被测试过, 同时如果每个镜像都已经被测试过时, 返回的镜像还会被重新测试. 否则, 其将不会选择其他镜像. 
# 例如"反馈", 其使用服务器状态文件.
uri-selector=feedback
```

#### HTTP 设置

```properties
# 检查证书, 默认: true
check-certificate=true

# GZip 支持, 默认: false
# 如果远程服务器的响应头中包含 Content-Encoding: gzip 或 Content-Encoding: deflate , 将发送包含 Accept: deflate, gzip 的请求头并解压缩响应.
http-accept-gzip=true

# 认证质询, 默认: false
# 仅当服务器需要时才发送 HTTP 认证请求头. 如果设置为"否", 每次都会发送认证请求头. 例外: 如果用户名和密码包含在 URI 中, 将忽略此选项并且每次都会发送认证请求头.
http-auth-challenge=false

# 禁用缓存, 默认: false
# 发送的请求头中将包含 Cache-Control: no-cache 和 Pragma: no-cache header 以避免内容被缓存. 如果设置为"否", 上述请求头将不会发送, 同时您也可以使用 --header 选项将 Cache-Control 请求头添加进去.
http-no-cache=false

# HTTP 默认用户名
# http-user=

# HTTP 默认密码
# http-passwd=

# HTTP 代理服务器
# http-proxy=http://127.0.0.1:8889

# HTTP 代理服务器用户名
# http-proxy-user=

# HTTP 代理服务器密码
# http-proxy-passwd=

# HTTPS 代理服务器
# https-proxy=http://127.0.0.1:8889

# HTTPS 代理服务器用户名
# https-proxy-user=

# HTTPS 代理服务器密码
# https-proxy-passwd=

# 请求来源
# 设置 HTTP 请求来源 (Referer). 此选项将影响所有 HTTP/HTTPS 下载. 如果设置为 *, 请求来源将设置为下载链接. 此选项可以配合 --parameterized-uri 选项使用.
# referer=

# 启用持久连接, 默认: true
# 启用 HTTP/1.1 持久连接.
enable-http-keep-alive=true

# 启用 HTTP 管线化, 默认: false
# 启用 HTTP/1.1 管线化.
enable-http-pipelining=false

# 自定义请求头
# 增加 HTTP 请求头内容. 每行放置一项, 每项包含 "请求头名: 请求头值".
# header=

# Cookies 保存路径
# 以 Mozilla/Firefox(1.x/2.x)/Netscape 格式将 Cookies 保存到文件中. 如果文件已经存在, 将被覆盖. 会话过期的 Cookies 也将会保存, 其过期时间将会设置为 0.
# save-cookies= 

# 启用 HEAD 方法, 默认: false
# 第一次请求 HTTP 服务器时使用 HEAD 方法.
use-head=false

# 自定义 User Agent
# user-agent=netdisk;P2SP;2.2.60.26
# user-agent=qBittorrent/4.2.5
user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4160.0 Safari/537.36 Edg/85.0.537.0
```

#### FTP/SFTP 设置

```properties
# FTP 默认用户名, 默认: anonymous
# ftp-user=

# FTP 默认密码, 默认: ARIA2USER@
# 如果 URI 中包含用户名单不包含密码, aria2 首先会从 .netrc 文件中获取密码. 
# 如果在 .netrc 文件中找到密码, 则使用该密码. 否则, 使用此选项设置的密码.
# ftp-passwd=

# 被动模式, 默认: 是
# 在 FTP 中使用被动模式. 如果设置为"否", 则使用主动模式. 此选项不适用于 SFTP 传输.
# ftp-pasv=

# FTP 代理服务器
# ftp-proxy=

# FTP 代理服务器用户名
# ftp-proxy-user=

# FTP 代理服务器密码
# ftp-proxy-passwd=

# 传输类型
# 可选值:  二进制、ASCII
# ftp-type=

# 连接复用, 默认: 是
# ftp-reuse-connection=

# SSH 公钥校验和
# 设置 SSH 主机公钥的校验和. TYPE 为哈希类型. 支持的哈希类型为 sha-1 和 md5. DIGEST 是十六进制摘要. 
# 例如: sha-1=b030503d4de4539dc7885e6f0f5e256704edf4c3. 此选项可以在使用 SFTP 时用来验证服务器的公钥. 
# 如果此选项不设置, 即保留默认, 不会进行任何验证. 
# ssh-host-key-md=
```

#### BitTorrent 设置

```properties
# 分离仅做种任务, 默认: false
# 统计当前活动下载任务(参见 -j 选项) 时排除仅做种的任务. 
# 这意味着, 如果参数设置为 -j3, 此选项打开并且当前有 3 个正在活动的任务, 并且其中有 1 个进入做种模式, 那么其会从正在下载的数量中排除(即数量会变为 2), 在队列中等待的下一个任务将会开始执行. 
# 但要知道, 在 RPC 方法中, 做种的任务仍然被认为是活动的下载任务.
# 从正在下载的任务中排除已经下载完成且正在做种的任务, 并开始等待列表中的下一个任务. 
bt-detach-seed-only=true

# 启用哈希检查完成事件, 默认: true
# 允许 BT 下载哈希检查(参见 -V 选项) 完成后调用命令. 默认情况下, 当哈希检查成功后, 通过 --on-bt-download-complete 设置的命令将会被执行. 如果要禁用此行为, 请设置为"否".
# 需要 aria2 v1.19.3 或更高版本
bt-enable-hook-after-hash-check=true

# 启用本地节点发现 (LPD) , 默认: false
# PT 下载(私有种子)会自动禁用 
bt-enable-lpd=true

# BT 排除服务器地址
# 逗号分隔的 BT 排除服务器地址. 您可以使用 * 匹配所有地址, 因此将排除所有服务器地址. 当在 shell 命令行使用 * 时, 需要使用转义符或引号.
# bt-exclude-tracker=

# 外部 IP 地址
# 指定用在 BitTorrent 下载和 DHT 中的外部 IP 地址. 它可能被发送到 BitTorrent 服务器. 
# 对于 DHT, 此选项将会报告本地节点正在下载特定的种子. 这对于在私有网络中使用 DHT 非常关键. 
# 虽然这个方法叫外部, 但其可以接受各种类型的 IP 地址.
# bt-external-ip=

# 强制加密, 默认: false
# BT 消息中的内容需要使用 arc4 加密. 
# 此选项不会修改上述两个选项的内容. 如果设置为"是", 将拒绝以前的 BT 握手, 并仅使用模糊握手及加密消息.
# 启用后将拒绝旧的 BT 握手协议并仅使用混淆握手及加密. 可以解决部分运营商对 BT 下载的封锁, 且有一定的防版权投诉与迅雷吸血效果. 
# 此选项相当于后面两个选项(bt-require-crypto=true, bt-min-crypto-level=arc4)的快捷开启方式, 但不会修改这两个选项的值. 
bt-force-encryption=true

# 做种前检查文件哈希, 默认: true
# 如果设置为"是", 当使用 --check-integrity 选项完成哈希检查及文件完成后才继续做种. 
# 如果您希望仅当文件损坏或未完成时检查文件, 请设置为"否". 此选项仅对 BT 下载有效
bt-hash-check-seed=true

# 加载已保存的元数据文件(.torrent), 默认: false
# 当使用磁链下载时, 在从 DHT 获取种子元数据之前, 首先尝试加载使用 --bt-save-metadata 选项保存的文件. 
# 如果文件加载成功, 则不会从 DHT 下载元数据.
bt-load-saved-metadata=true

# 最多打开文件数, 默认: 100
# 设置 BT/Metalink 下载全局打开的最大文件数.
bt-max-open-files=100

# 最大连接节点数, 默认: 55
# 设置每个 BT 下载的最大连接节点数. 0 表示不限制.
bt-max-peers=0

# 仅下载种子文件, 默认: false
# 仅下载种子文件. 种子文件中描述的文件将不会下载. 此选项仅对磁链生效.
bt-metadata-only=false

# 最低加密级别, 默认: plain（明文）
# 可选: plain（明文）, arc4（加密）
# 设置加密方法的最小级别. 如果节点提供多种加密方法, aria2 将选择满足给定级别的最低级别.
bt-min-crypto-level=arc4

# 优先下载
# 尝试先下载每个文件开头或结尾的分片. 此选项有助于预览文件. 参数可以包括两个关键词: head 和 tail. 
# 如果包含两个关键词, 需要使用逗号分隔. 每个关键词可以包含一个参数, SIZE. 
# 例如, 如果指定 head=SIZE, 每个文件的最前 SIZE 数据将会获得更高的优先级. tail=SIZE 表示每个文件的最后 SIZE 数据. SIZE 可以包含 K 或 M (1K = 1024, 1M = 1024K).
bt-prioritize-piece=head=88M,tail=88M

# 删除未选择的文件, 默认: false
# 当 BT 任务完成后删除未选择的文件. 要选择需要下载的文件, 请使用 --select-file 选项. 
# 如果没有选择, 则所有文件都默认为需要下载. 此选项会从磁盘上直接删除文件, 请谨慎使用此选项.
bt-remove-unselected-file=true

# 需要加密, 默认: false
# 如果设置为"是", aria 将不会接受以前的 BitTorrent 握手协议(\19BitTorrent 协议)并建立连接. 因此 aria2 总是模糊混淆握手.
bt-require-crypto=true

# 期望下载速度, 默认: 50K
# 如果一个 BT 下载的整体下载速度低于此选项设置的值, aria2 会临时提高连接数以提高下载速度. 
# 在某些情况下, 设置期望下载速度可以提高您的下载速度. 您可以增加数值的单位 K 或 M (1K = 1024, 1M = 1024K).
bt-request-peer-speed-limit=10M

# 保存种子文件(.torrent), 默认: false
# 保存种子文件为 ".torrent" 文件. 此选项仅对磁链生效. 文件名为十六进制编码后的哈希值及 ".torrent"后缀. 保存的目录与下载文件的目录相同. 如果相同的文件已存在, 种子文件将不会保存.
bt-save-metadata=true

# 不检查已经下载的文件, 默认: false
# 继续之前的BT任务时, 无需再次校验.
bt-seed-unverified=false

# 无速度时自动停止时间（秒）, 默认: 0 (禁用)
# 当 BT 任务下载速度持续为 0, 达到此选项设置的时间后停止下载. 如果设置为 0, 此功能将禁用.
bt-stop-timeout=0

# BT 服务器连接超时时间（秒）, 默认: 60
# 设置 BT 服务器的连接超时时间 (秒). 当连接建立后, 此选项不再生效, 请使用 --bt-tracker-timeout 选项.
bt-tracker-connect-timeout=10

# BT 服务器连接间隔时间（秒）, 默认: 0 (自动)
# 设置请求 BT 服务器的间隔时间 (秒). 此选项将完全覆盖服务器返回的最小间隔时间和间隔时间, aria2 仅使用此选项的值.
# 如果设置为 0, aria2 将根据服务器的响应情况和下载进程决定时间间隔.
bt-tracker-interval=0

# BT 服务器超时时间（秒）, 默认: 60
bt-tracker-timeout=10

# DHT (IPv4) 文件, 默认: /home/ryanjie/.aria2/dht.dat
# 修改 IPv4 DHT 路由表文件路径.
dht-file-path=/home/ryanjie/.aria2/dht.dat

# DHT (IPv6) 文件, 默认: 
# 修改 IPv6 DHT 路由表文件路径.
dht-file-path6=/home/ryanjie/.aria2/dht6.dat

# # IPv4 DHT 网络引导节点
# dht-entry-point=dht.transmissionbt.com: 6881

# # IPv6 DHT 网络引导节点
# dht-entry-point6=dht.transmissionbt.com: 6881

# DHT 监听端口(UDP), 默认: 6881-6999
# 设置 DHT (IPv4, IPv6) 和 UDP 服务器使用的 UCP 端口. 
# 多个端口可以使用逗号 "," 分隔, 例如: 6881,6885. 您还可以使用短横线 "-" 表示范围: 6881-6999, 或可以一起使用: 6881-6889, 6999.
dht-listen-port=51413

# DHT 消息超时时间（秒）, 默认: 10
dht-message-timeout=10

# 启用 DHT (IPv4), PT 下载(私有种子)会自动禁用. 默认: true
# 启用 IPv4 DHT 功能. 此选项同时会启用 UDP 服务器支持. 如果种子设置为私有, 即使此选项设置为"是", aria2 也不会启用 DHT.
# PT 下载(私有种子)会自动禁用. 
enable-dht=true

# 启用 DHT (IPv6), 默认: false
# 启用 IPv6 DHT 功能. 如果种子设置为私有, 即使此选项设置为"是", aria2 也不会启用 DHT. 使用 --dht-listen-port 选项设置监听的端口.
# 在没有 IPv6 支持的环境开启可能会导致 DHT 功能异常
# PT 下载(私有种子)会自动禁用. 
enable-dht6=false

# 启用节点交换, 默认: true
# 启用节点交换扩展. 如果种子设置为私有, 即使此选项设置为"是", aria2 也不会启用此功能.
# PT 下载(私有种子)会自动禁用.
enable-peer-exchange=true

# 下载种子中的文件(.torrent), 默认: true
# 可选值:  true、false 和 mem.
# 如果设置为"是"或"仅内存", 当后缀为 .torrent 或内容类型为 application/x-bittorrent 的文件下载完成时, aria2 将按种子文件读取并下载该文件中提到的文件. 
# 如果设置为"仅内存", 该种子文件将不会写入到磁盘中, 而仅会存储在内存中. 
# 如果设置为"否", 则 .torrent 文件会下载到磁盘中, 但不会按种子文件读取并且其中的文件不会进行下载.
follow-torrent=true

# 监听端口(TCP), 默认: 6881-6999
# 设置 BT 下载的 TCP 端口. 多个端口可以使用逗号 "," 分隔, 例如: 6881,6885. 您还可以使用短横线 "-" 表示范围: 6881-6999, 或可以一起使用: 6881-6889, 6999.
listen-port=51413

# 全局最大上传速度（字节）, 默认: 0 (无限制)
# 设置全局最大上传速度 (字节/秒). 0 表示不限制. 您可以增加数值的单位 K 或 M (1K = 1024, 1M = 1024K).
max-overall-upload-limit=1M

# 最大上传速度（字节）, 默认: 0 (无限制)
# 设置每个任务的最大上传速度 (字节/秒). 0 表示不限制. 您可以增加数值的单位 K 或 M (1K = 1024, 1M = 1024K).
max-upload-limit=0

# 节点 ID 前缀
# 指定节点 ID 的前缀. BT 中节点 ID 长度为 20 字节. 
# 如果超过 20 字节, 将仅使用前 20 字节. 如果少于 20 字节, 将在其后不足随机的数据保证为 20 字节.
peer-id-prefix=-qB4250-

# Peer Agent
# 指定 BT 扩展握手期间用于节点客户端版本的字符串.
# 需要 aria2 v1.33.0 或更高版本
# PT 下载需要保持 user-agent 和 peer-agent 两个参数一致
# 部分 PT 站对 Aria2 有特殊封禁机制, 客户端伪装不一定有效, 且有封禁账号的风险. 
peer-agent=qBittorrent/4.2.5

# 最小分享率, 默认: 1.0
# 指定分享率. 当分享率达到此选项设置的值时会完成做种. 强烈建议您将此选项设置为大于等于 1.0. 
# 如果您想不限制分享比率, 可以设置为 0.0. 
# 如果同时设置了 --seed-time 选项, 当任意一个条件满足时将停止做种.
seed-ratio=1.0

# 最小做种时间
# 以 (小数形式的) 分钟指定做种时间. 此选项设置为 0 时, 将在 BT 任务下载完成后不进行做种.
seed-time=0

# 下载停止后执行的命令
# 从 正在下载 到 删除、错误、完成 时触发. 暂停被标记为未开始下载, 故与此项无关. 
on-download-stop=/home/ryanjie/.aria2/delete.sh

# 下载完成后执行的命令
# 此项未定义则执行 下载停止后执行的命令 (on-download-stop)
on-download-complete=/home/ryanjie/.aria2/clean.sh

# 下载错误后执行的命令
# 此项未定义则执行 下载停止后执行的命令 (on-download-stop)
# on-download-error=

# 下载暂停后执行的命令
# on-download-pause=

# 下载开始后执行的命令
# on-download-start=

# BT 下载完成后执行的命令
# on-bt-download-complete=
```

#### Metalink 设置

```properties
# 下载 Metalink 中的文件, 默认: true
# 可选值:  true、false 和 mem.
# 如果设置为"是"或"仅内存", 当后缀为 .meta4 或 .metalink 或内容类型为 application/metalink4+xml 或 application/metalink+xml 的文件下载完成时, aria2 将按 Metalink 文件读取并下载该文件中提到的文件. 
# 如果设置为"仅内存", 该 Metalink 文件将不会写入到磁盘中, 而仅会存储在内存中. 
# 如果设置为"否", 则 .metalink 文件会下载到磁盘中, 但不会按 Metalink 文件读取并且其中的文件不会进行下载.
follow-metalink=true

# 基础 URI
# 指定基础 URI 以便解析本地磁盘中存储的 Metalink 文件里 metalink:url 和 metalink:metaurl 中的相对 URI 地址. 
# 如果 URI 表示的为目录, 最后需要以 / 结尾.
# metalink-base-uri=


# 语言
# metalink-language=

# 首选服务器位置
# 首选服务器所在的位置. 可以使用逗号分隔的列表, 例如: jp,us.
# metalink-location=

# 操作系统
# 下载文件的操作系统.
# metalink-os=

# 版本号
# 下载文件的版本号.
# metalink-version=

# 首选使用协议, 默认: none
# 可选值: 'http' 'https' 'ftp' 'none'
# 指定首选使用的协议. 可以设置为 http, https, ftp 或"无". 设置为"无"时禁用此选项.
metalink-preferred-protocol=none

# 仅使用唯一协议, 默认: true
# 如果一个 Metalink 文件可用多种协议, 并且此选项设置为"是", aria2 将只会使用其中一种. 使用 --metalink-preferred-protocol 参数指定首选的协议.
metalink-enable-unique-protocol=true
```

#### RPC 设置

```properties
# 启用 JSON-RPC/XML-RPC 服务器, 默认: false
enable-rpc=true

# 种子文件下载完后暂停, 默认: false
# 当种子文件下载完成后暂停后续的下载. 在 aria2 中有 3 种种子文件的下载类型: 
#     (1) 下载 .torrent 文件. 
#     (2) 通过磁链下载的种子文件. 
#     (3) 下载 Metalink 文件. 这些种子文件下载完后会根据文件内容继续进行下载. 
# 此选项会暂停这些后续的下载. 此选项仅当 --enable-rpc 选项启用时生效.
pause-metadata=false

# 接受所有远程请求, 默认: false
# 在 RPC 响应头增加 Access-Control-Allow-Origin 字段, 值为 * .
rpc-allow-origin-all=true

# 在所有网卡上监听, 默认: false
# 在所有网络适配器上监听 JSON-RPC/XML-RPC 的请求, 如果设置为"否", 仅监听本地网络的请求.
rpc-listen-all=true

# RPC 监听端口, 默认: 6800
rpc-listen-port=6800

# RPC 密钥
rpc-secret=666666

# RPC 最大请求大小（字节）, 默认: 2M
# 设置 JSON-RPC/XML-RPC 最大的请求大小. 
# 如果 aria2 检测到请求超过设定的字节数, 会直接取消连接.
rpc-max-request-size=10M

# 保存通过 WebUI(RPC) 上传的种子文件(.torrent), 默认: true
# 在 dir 选项设置的目录中保存上传的种子文件或 Metalink 文件. 文件名包括 SHA-1 哈希后的元数据和扩展名两部分. 
# 对于种子文件, 扩展名为 '.torrent'. 对于 Metalink 为 '.meta4'. 
# 如果此选项设置为"否", 通过 aria2.addTorrent() 或 aria2.addMetalink() 方法添加的下载将无法通过 --save-session 选项保存.
# 所有涉及种子文件保存的选项都建议开启, 不保存种子文件有任务丢失的风险. 
# 通过 RPC 自定义临时下载目录可能不会保存种子文件. 
rpc-save-upload-metadata=true

# RPC 服务中 SSL/TLS 加密, 默认: false
# RPC 将通过 SSL/TLS 加密传输. RPC 客户端需要使用 https 协议连接服务器. 
# 对于 WebSocket 客户端, 使用 wss 协议. 使用 --rpc-certificate 和 --rpc-private-key 选项设置服务器的证书和私钥.
# 启用加密后必须使用 https 或者 wss 协议连接
# 不推荐开启, 建议使用 web server 反向代理, 比如 Nginx、Caddy , 灵活性更强. 
rpc-secure=false

# 在 RPC 服务中启用 SSL/TLS 加密时的证书文件(.pem/.crt)
# rpc-certificate=/home/ryanjie/.aria2/xxx.pem

# 在 RPC 服务中启用 SSL/TLS 加密时的私钥文件(.key)
# rpc-private-key=/home/ryanjie/.aria2/xxx.key
```

#### 高级设置

```properties
# 允许覆盖, 默认: false
# 如果相应的控制文件(.aria2)不存在时从头重新下载文件. 参见 --auto-file-renaming 选项.
allow-overwrite=false

# 允许分片大小变化, 默认: false
# 如果设置为"否", 当分片长度与控制文件中的不同时, aria2 将会中止下载. 
# 如果设置为"是", 您可以继续, 但部分下载进度将会丢失.
allow-piece-length-change=true

# 始终断点续传, 默认: true
# 始终断点续传. 如果设置为"是", aria2 始终尝试断点续传, 如果无法恢复, 则中止下载. 
# 如果设置为"否", 对于不支持断点续传的 URI 或 aria2 遇到 N 个不支持断点续传的 URI (N 为 --max-resume-failure-tries 选项设置的值), aria2 会从头下载文件. 参见 --max-resume-failure-tries 参数.
always-resume=false

# 异步 DNS, 默认:  是
async-dns=true

# 文件自动重命名, 默认:  true
# 重新命名已经存在的文件. 此选项仅对 HTTP(S)/FTP 下载有效. 新的文件名后会在文件名后、扩展名 (如果有) 前追加句点和数字(1..9999).
auto-file-renaming=true

# 自动保存间隔（秒）, 默认:  60
# 每隔设置的秒数自动保存控制文件(*.aria2). 
# 如果设置为 0, 下载期间控制文件不会自动保存. 不论设置的值为多少, aria2 会在任务结束时保存控制文件. 
# 可以设置的值为 0 到 600.
auto-save-interval=30

# 条件下载, 默认:  false
# 仅当本地文件比远程文件旧时才进行下载. 此功能仅适用于 HTTP(S) 下载. 
# 如果在 Metalink 中文件大小已经被指定则功能无法生效. 同时此功能还将忽略 Content-Disposition 响应头.
# 如果存在控制文件, 此选项将被忽略. 此功能通过 If-Modified-Since 请求头获取较新的文件. 当获取到本地文件的修改时间时, 此功能将使用用户提供的文件名 (参见 --out 选项), 
# 如果没有指定 --out 选项则使用 URI 中的文件名. 为了覆盖已经存在的文件, 需要使用 --allow-overwrite 参数.
conditional-get=false

# 配置文件路径
conf-path=/home/ryanjie/.aria2/aria2.conf

# 控制台日志级别, 默认:  一般 (Notice)
# 可选: 调试 (Debug), 普通 (Info), 一般 (Notice), 警告 (Warn), 错误 (Error) 
# 可选值: 'debug' 'info' 'notice' 'warn' 'error'
console-log-level=debug

# 使用 UTF-8 处理 Content-Disposition, 默认: false
# 处理 "Content-Disposition" 头中的字符串时使用 UTF-8 字符集来代替 ISO-8859-1, 例如, 文件名参数, 但不是扩展版本的文件名.
# 需要 aria2 v1.31.0 或更高版本
content-disposition-default-utf8=true

# 启用后台进程, 默认: false
daemon=true

# 延迟加载, 默认: false
# 如果设置为"是", aria2 在启动时不会读取 --input-file 选项设置的文件中的所有 URI 地址, 而是会在之后需要时按需读取. 
# 如果输入文件中包含大量要下载的 URI, 此选项可以减少内存的使用. 
# 如果设置为"否", aria2 会在启动时读取所有的 URI. 当 -save-session 使用时将会禁用 --deferred-input 选项.
deferred-input=false

# 禁用 IPv6, 默认: false
disable-ipv6=true

# 磁盘缓存（字节）, 默认: 16M
# 启用磁盘缓存. 如果设置为 0, 将禁用磁盘缓存. 此功能将下载的数据缓存在内存中, 最多占用此选项设置的字节数. 
# 缓存存储由 aria2 实例创建并对所有下载共享. 由于数据以较大的单位写入并按文件的偏移重新排序, 所以磁盘缓存的一个优点是减少磁盘的 I/O. 
# 如果调用哈希检查时并且数据缓存在内存中时, 将不需要从磁盘中读取. 大小可以包含 K 或 M (1K = 1024, 1M = 1024K).
disk-cache=16M

# 下载结果
# 此选项将修改下载结果的格式. 可选: 'default' 'full' 'hide'
# 如果设置为"默认", 将打印 GID, 状态, 平均下载速度和路径/URI. 如果涉及多个文件, 仅打印第一个请求文件的路径/URI, 其余的将被忽略. 
# 如果设置为"完整", 将打印 GID, 状态, 平均下载速度, 下载进度和路径/URI. 其中, 下载进度和路径/URI 将会每个文件打印一行. 
# 如果设置为"隐藏", 下载结果将会隐藏.
download-result=default

# DSCP
# 为 QoS 设置 BT 上行 IP 包的 DSCP 值. 此参数仅设置 IP 包中 TOS 字段的 DSCP 位, 而不是整个字段. 
# 如果您从 /usr/include/netinet/ip.h 得到的值, 需要除以 4 (否则值将不正确, 例如您的 CS1 类将会转为 CS4). 
# 如果您从 RFC, 网络供应商的文档, 维基百科或其他来源采取常用的值, 可以直接使用.
dscp=0

# 最多打开的文件描述符, 默认: 1024
# 设置打开的文件描述符的软限制 (soft limit). 
# 此选项仅当满足如下条件时开放: 
#     a. 系统支持它 (posix). 
#     b. 限制没有超过硬限制 (hard limit). 
#     c. 指定的限制比当前的软限制高. 这相当于设置 ulimit, 除了其不能降低限制. 
# 此选项仅当系统支持 rlimit API 时有效.
rlimit-nofile=1024

# 终端输出使用颜色, 默认: true
enable-color=true

# 启用 MMap, 默认: false
# 内存中存放映射文件. 当文件空间没有预先分配至, 此选项无效. 参见 --file-allocation.
enable-mmap=false

# 事件轮询方法
# 设置事件轮询的方法. 可选的值包括 epoll, kqueue, port, poll 和 select. 
# 对于 epoll, kqueue, port 和 poll, 只有系统支持时才可用. 最新的 Linux 支持 epoll. 各种 *BSD 系统包括 Mac OS X 支持 kqueue. Open Solaris 支持 port. 
# 默认值根据您使用的操作系统不同而不同.
# event-poll=select

# 文件分配方法, 默认: prealloc
# 可选的值包括 无、prealloc、trunc 和 falloc.
# 指定文件分配方法. "无" 不会预先分配文件空间. "prealloc"会在下载开始前预先分配空间. 这将会根据文件的大小需要一定的时间. 
# 如果您使用的是较新的文件系统, 
#     例如 ext4 (带扩展支持), btrfs, xfs 或 NTFS (仅 MinGW 构建), "falloc" 是最好的选择. 其几乎可以瞬间分配大(数 GiB)文件. 不要在旧的文件系统, 
#     例如 ext3 和 FAT32 上使用 falloc, 因为与 prealloc 花费的时间相同, 并且其会阻塞 aria2 知道分配完成. 当您的系统不支持 posix_fallocate(3) 函数时, falloc 可能无法使用. 
#     "trunc" 使用 ftruncate(2) 系统调用或平台特定的实现将文件截取到特定的长度. 
# 在多文件的 BitTorrent 下载中, 若某文件与其相邻的文件共享相同的分片时, 则相邻的文件也会被分配.
# 
# 预分配对于机械硬盘可有效降低磁盘碎片、提升磁盘读写性能、延长磁盘寿命. 
# 机械硬盘使用 ext4（具有扩展支持）, btrfs, xfs 或 NTFS（仅 MinGW 编译版本）等文件系统建议设置为 falloc
# 若无法下载, 提示 fallocate failed.cause: Operation not supported 则说明不支持, 请设置为 none
# prealloc 分配速度慢, trunc 无实际作用, 不推荐使用. 
# 固态硬盘不需要预分配, 只建议设置为 none , 否则可能会导致双倍文件大小的数据写入, 从而影响寿命. 
file-allocation=none

# 强制保存, 默认: false
# 即使任务完成或删除时使用 --save-session 选项时也保存该任务. 
# 此选项在这种情况下还会保存控制文件(.aria2文件). 此选项可以保存被认为已经完成但正在做种的 BT 任务, 文件被移除且任务存在的情况下重启后会重新下载. 
# 关闭后已完成的任务列表会在重启后清空. 
force-save=false

# 保存未找到的文件, 默认: true
# 当使用 --save-session 选项时, 即使当任务中的文件不存在时也保存该下载任务. 此选项同时会将这种情况保存到控制文件中.
# 需要 aria2 v1.27.0 或更高版本
save-not-found=true

# 仅哈希检查, 默认: false
# 如果设置为"是", 哈希检查完使用 --check-integrity 选项, 根据是否下载完成决定是否终止下载.
hash-check-only=false

# 控制台可读输出, 默认: true
# 在控制台输出可读格式的大小和速度 (例如, 1.2Ki, 3.4Mi).
human-readable=true

# 保留未完成的任务, 默认: true
# 保留所有未完成的下载结果, 即使超过了 --max-download-result 选项设置的数量. 这将有助于在会话文件中保存所有的未完成的下载 (参考 --save-session 选项). 
# 需要注意的是, 未完成任务的数量没有上限. 
# 如果不希望这样, 请关闭此选项.
keep-unfinished-download-result=true

# 最多下载结果, 默认: 1000
# 设置内存中存储最多的下载结果数量. 下载结果包括已完成/错误/已删除的下载. 下载结果存储在一个先进先出的队列中, 因此其可以存储最多指定的下载结果的数量. 当队列已满且有新的下载结果创建时, 最老的下载结果将从队列的最前部移除, 新的将放在最后. 
# 此选项设置较大的值后如果经过几千次的下载将导致较高的内存消耗. 设置为 0 表示不存储下载结果. 
# 注意, 未完成的下载将始终保存在内存中, 不考虑该选项的设置. 参考 --keep-unfinished-download-result 选项.
max-download-result=1000

# MMap 最大限制（字节）, 默认: 9223372036854775807Bytes (2^63-1字节, 8388608TB, 8192PB, 64位的运算极限)
# 设置启用 MMap (参见 --enable-mmap 选项) 最大的文件大小. 文件大小由一个下载任务中所有文件大小的和决定. 
# 例如, 如果一个下载包含 5 个文件, 那么文件大小就是这些文件的总大小. 如果文件大小超过此选项设置的大小时, MMap 将会禁用.
# 需要 aria2 v1.20.0 或更高版本
max-mmap-limit=9223372036854775807

# 最大断点续传尝试次数
# 当 --always-resume 选项设置为"否"时, 如果 aria2 检测到有 N 个 URI 不支持断点续传时, 将从头开始下载文件. 
# 如果 N 设置为 0, 当所有 URI 都不支持断点续传时才会从头下载文件. 参见 --always-resume 选项.
max-resume-failure-tries=0

# 最低 TLS 版本, 默认: TLSv1.1
# 可选值: 'TLSv1.1' 'TLSv1.2' 'TLSv1.3'
# 指定启用的最低 SSL/TLS 版本.
min-tls-version=TLSv1.1

# 日志级别, 默认: 调试 (debug)
# 可选: 调试 (Debug), 普通 (Info), 一般 (Notice), 警告 (Warn), 错误 (Error) 
# 可选值: 'debug' 'info' 'notice' 'warn' 'error'
log-level=debug

# 优化并发下载, 默认: false
# 根据可用带宽优化并发下载的数量. aria2 使用之前统计的下载速度通过规则 N = A + B Log10 (速度单位为 Mbps) 得到并发下载的数量. 
# 其中系数 A 和 B 可以在参数中以冒号分隔自定义. 默认值 (A=5, B=25) 可以在 1Mbps 网络上使用通常 5 个并发下载, 在 100Mbps 网络上为 50 个. 
# 并发下载的数量保持在 --max-concurrent-downloads 参数定义的最大之下.
# optimize-concurrent-downloads=

# 文件分片大小（字节）, 默认: 1M
# 设置 HTTP/FTP 下载的分配大小. aria2 根据这个边界分割文件. 所有的分割都是这个长度的倍数. 此选项不适用于 BitTorrent 下载. 
# 如果 Metalink 文件中包含分片哈希的结果此选项也不适用.
# 最小值为 1M (增强版为 1K), 默认: 1M
piece-length=1M

# 显示控制台输出, 默认: true
show-console-readout=true

# 下载摘要输出间隔（秒）, 默认: 60
summary-interval=60

# 全局最大下载速度, 默认:  0 (无限制)
# 设置全局最大下载速度 (字节/秒). 
# 0 表示不限制. 您可以增加数值的单位 K 或 M (1K = 1024, 1M = 1024K).
max-overall-download-limit=0

# 最大下载速度, 默认:  0 (无限制)
# 设置每个任务的最大下载速度 (字节/秒). 
# 0 表示不限制. 您可以增加数值的单位 K 或 M (1K = 1024, 1M = 1024K).
max-download-limit=0

# 禁用配置文件, 默认:  false
no-conf=false

# 文件分配限制, 默认: 5M
# 不对比此参数设置大小小的分配文件. 您可以增加数值的单位 K 或 M (1K = 1024, 1M = 1024K).
no-file-allocation-limit=20M

# 启用参数化 URI 支持, 默认:  false
# 启用参数化 URI 支持. 您可以指定部分的集合: http: //{sv1,sv2,sv3}/foo.iso. 同时您也可以使用步进计数器指定数字化的序列: http: //host/image[000-100: 2].img. 步进计数器可以省略. 
# 如果所有 URI 地址不指向同样的文件, 例如上述第二个示例, 需要使用 -Z 选项.
parameterized-uri=false

# 禁用控制台输出, 默认:  false
quiet=false

# 实时数据块验证, 默认:  true
# 如果提供了数据块的校验和, 将在下载过程中通过校验和验证数据块.
realtime-chunk-checksum=true

# 删除控制文件
# 在下载前删除控制文件. 使用 --allow-overwrite=true 选项时, 总是从头开始下载文件. 此选项将有助于使用不支持断点续传代理服务器的用户.
# remove-control-file=

# 状态保存文件
# 当退出时保存错误及未完成的任务到指定的文件中. 您可以在重启 aria2 时使用 --input-file 选项重新加载. 
# 如果您希望输出的内容使用 GZip 压缩, 您可以在文件名后增加 .gz 扩展名. 
# 请注意, 通过 aria2.addTorrent() 和 aria2.addMetalink() RPC 方法添加的下载, 其元数据没有保存到文件的将不会保存. 
#        通过 aria2.remove() 和 aria2.forceRemove() 删除的下载将不会保存.
save-session=/home/ryanjie/.aria2/aria2.session

# 保存状态间隔（秒）, 默认: 0(进程正常退出时保存)
# 每隔此选项设置的时间(秒)后会保存错误或未完成的任务到 --save-session 选项指定的文件中. 如果设置为 0, 仅当 aria2 退出时才会保存.
save-session-interval=30

# Socket 接收缓冲区大小（字节）, 默认: 0 (禁用)
# 设置 Socket 接收缓冲区最大的字节数. 指定为 0 时将禁用此选项. 当使用 SO_RCVBUF 选项调用 setsockopt() 时此选项的值将设置到 Socket 的文件描述符中.
# 需要 aria2 v1.19.3 或更高版本
socket-recv-buffer-size=0

# 自动关闭时间（秒）, 默认: 0 (禁用)
# 在此选项设置的时间(秒)后关闭应用. 如果设置为 0, 此功能将禁用.
stop=0

# 缩短控制台输出内容, 默认: true
# 缩短控制台输出的内容在一行中.
truncate-console-readout=true
```

## 使用 Aria2

### 启动 Aria2



### 查看 Aria2 状态



### 停止 Aria2



### 重启 Aria2



### 查看配置信息



### BT-Tracker服务器





### 查看日志信息











## 浏览器配置

### Aria2-for-chrome

> A aria2 download task management extension for chromium based browser.
>
> Aria2 for chrome 是一款为Chrome定制的下载任务管理扩展，能够自动拦截或手动添加下载任务到Aria2来完成网络资源下载。同时，引入了AriaNG作为前端方便用户对Aria2进行操作和管理。

#### Features

1. 自动拦截浏览器下载任务

   - 拦截通知

   - 支持磁力链接

   - 快捷键开关自动拦截 (默认：Alt+A)

   - 下载前手动设置各种详细参数

   - 通过域名、扩展名或文件大小过滤下载任务

     > 过滤优先级：网站 > 扩展名 > 文件大小，优先处理白名单

2. 设置URL规则以根据下载地址自动选择不同的Aria2 RPC

3. 内置Aria2前端：AriaNG，多种呈现方式：弹窗，新标签，新窗口

4. 所有配置云端同步

5. 中英双语支持

6. Aria2下载状态监测

7. 上下文菜单导出下载任务

8. 接受来自其他扩展的下载请求

9. 选项配置页面快捷键（保存：Alt+S 重置：Alt+R 下载：Alt+J 上传：Alt+U）

10. 只需一次配置，自动导出默认RPC设置到AriaNG

#### 安装

- [Website](https://alexhua.github.io/Aria2-for-chrome/)
- [Github](https://github.com/alexhua/Aria2-for-chrome)
- [Chrome Web Store](https://chrome.google.com/webstore/detail/aria2-for-chrome/mpkodccbngfoacfalldjimigbofkhgjn)
- [Microsoft Edge](https://microsoftedge.microsoft.com/addons/detail/jjfgljkjddpcpfapejfkelkbjbehagbh) 





## 相关链接

- [aria2 homepage](https://aria2.github.io/)
- [aria2 documentation](https://aria2.github.io/manual/en/html/)
- [aria2 source code (Github)](https://github.com/aria2/aria2)
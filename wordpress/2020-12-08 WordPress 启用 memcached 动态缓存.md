---
title: WordPress 启用 memcached 动态缓存
abstract: WordPress 使用 memcached 缓存动态内容，将数据库的数据缓存在内存中，下次需要的时候直接从内存中取数据，减少 MySQL 的访问次数，也加速了 WordPress 对网页的处理。
url: wordpress-memcached
permalink: wordpress-memcached
date: 2020-12-08 20:55:06
category:
  - WordPress
tags:
  - WordPress
---

![wordpress-memcached](https://img.zxj.guru/2020/12/wordpress-memcached.png)

WordPress 动态缓存加速方案：一种是基于 memcached 缓存动态内容，将数据库的数据缓存在内存中，下次需要的时候直接从内存中取数据，减少 MySQL 的访问次数，也加速了 WordPress 对网页的处理。这种方式直接从内存中存取数据，理论上比静态缓存的 IO 开销更小，但是由于 memcached 需要占用一定 php 资源，因此会对 CPU 带来一些额外的压力。

另一种是基于 nginx 的 fastcgi 纯静态缓存，这是将所有的动态 HTML 页面都缓存到硬盘文件，nginx 针对 http 请求只处理静态内容，因此对服务器的开销很小，速度快。对于动态内容不多的站点，用这个方法能极大缓解 cpu 的负担，由 nginx 来高效地处理并发。

## 安装 memcached 服务

`Memcached` 是一个高性能的分布式内存对象缓存系统，用于动态 Web 应用以减轻数据库负载。它通过在内存中缓存数据和对象来减少读取数据库的次数，从而提供动态、数据库驱动网站的速度。

### memcache or memcached

> - php memcache 拓展：<http://cn2.php.net/manual/zh/book.memcache.php>
> - php memcached 拓展：<http://cn2.php.net/manual/zh/book.memcached.php>
>
> 对于 php 而言就是两个不同的客户端库，memcache 是基于 pecl 扩展库写的，memcache 是基于 libmemcached 扩展库写的，两个库其实都是一堆写好的 c 代码编译成的动态链接库， memcached 里面多了一些方法，里面还多支持了几个协议。目前通常建议直接使用后者。
>
> PS：如果想更深入了解，可以搜索下 `memcache vs memcached`

### 安装 memcached

> 这里的 `memcached`是 `Mencached` 的服务端 [memcached](http://danga.com/memcached)，用来处理缓存数据。

#### LNMP 环境

进入 lnmp 解压后的目录，执行：`./addons.sh install memcached`

![lnmp_install_memcached](https://img.zxj.guru/2020/12/lnmp_install_memcached.png)

输入对应的序号 `2`，回车，再次确认回车开始安装。

> 卸载 `memcached` 执行：`./addons.sh uninstall memcached`

#### 宝塔面板

在<kbd>面板</kbd> - <kbd>软件商店</kbd> 中搜索 `mencached`，选择软件名称为 `Memcached` 的安装即可。为了安全起见建议选择编译安装。

![bt_mencached](https://img.zxj.guru/2020/12/bt_mencached.png)

安装完成后修改相关配置文件：

```bash
#改为监听127.0.0.1，并关闭UDP连接方式，若为远程服务调用或不需要的话请跳过此行
sed -i 's/OPTIONS=""/OPTIONS="-l 127.0.0.1 -U 0"/g' /etc/init.d/memcached

#启动并设置开机服务
chmod +x /etc/init.d/memcached
service memcached start
chkconfig --add memcached
chkconfig memcached on
```

然后在 PHP 管理中安装 `memcached` 扩展。

![bt_php_memcached](https://img.zxj.guru/2020/12/bt_php_memcached.png)

### 校验安装

检查一下 `memcached` 服务是否运行：

```bash
$ systemctl status memcached
● memcached.service - LSB: memcached - Memory caching daemon
   Loaded: loaded (/etc/rc.d/init.d/memcached; bad; vendor preset: disabled)
   Active: active (exited) since Sun 2020-12-08 21:02:18 CST; 5min ago
```

检查 `php-memcached` 扩展是否加载，如果输出 memcached 则表示成功。

```bash
$ php -m | grep memcached
memcached
```

### 测试缓存

如果能输出 `100 `表示 `memcached` 安装成功且正常运行。

```bash
cat > test.php <<-EOF
<?php
\$m = new Memcached();
\$m->addServer( '127.0.0.1', 11211 );
\$m->set( 'foo', 100 );
echo \$m->get( 'foo' ) . "\n";
EOF
php -f test.php && rm -f test.php
```

## 安装 WordPress Memcached 插件

### 安装插件

1. 访问 [memcached-redux/trunk](http://svn.wp-plugins.org/memcached-redux/trunk/) 页面下载 `object-cache.php` 上传到 `wp-content` 目录。

2. 在网站根目录下的 `wp-config.php` 页面找到下面代码：

   ```java
   #英文站点
   /* That's all, stop editing! Happy blogging. */
   #中文站点
   /* 好了！请不要再继续编辑。请保存本文件。使用愉快！ */
   ```

   在该段代码上方添加 `WP_CACHE_KEY_SALT` 变量。

   ```php
   define( 'WP_CACHE_KEY_SALT', '...long random string...' );
   #例如: 设置为域名
   define( 'WP_CACHE_KEY_SALT', 'www.zxj.guru' );
   ```

   当一台服务器安装多个 WordPress 站点使用 Memcached 时，这有助于防止缓存数据冲突。 对于每个 WordPress 站点，该值必须唯一。

> 如果发现页面可以打开，但是里面没有 Hits 数据，说明 WordPress 并没有成功连接到 memcached，我们需要手动指定 memcached 服务器：
>
> 在网站根目录下的 `wp-config.php` 页面找到下面代码：
>
> ```java
> #英文站点
> /* That's all, stop editing! Happy blogging. */
> #中文站点
> /* 好了！请不要再继续编辑。请保存本文件。使用愉快！ */
> ```
>
> 在该段代码上方添加
>
> ```php
> $memcached_servers = array(
>     'default' => array(
>      // 这里定义的是memcached服务器，一般我们是单机部署，所以注释掉一行，并将memcached监听IP和端口根据实际修改，比如本文是127.0.0.1
>         // '<memcached监听IP>:<端口>',
>         '127.0.0.1:11211'
>     )
> );
> ```
>
> 实际的 memcached 监听 IP 和端口，你可以通过如下命令查看：
>
> ```bash
> $ netstat -nutlp | grep memcache
> tcp        0      0 127.0.0.1:11211         0.0.0.0:*               LISTEN      3070/memcached
> ```

### 查看效果

查看 Memcached 状态：在 <kbd>WordPress 的仪表盘</kbd> → <kbd>工具</kbd> → <kbd>Memcached</kbd> 界面通过计算 cmd_get 和 get_hits 来计算命中率。

图形化展示：

1. 下载 [PECL memcache extension](http://pecl.php.net/package/memcache)。（国内蓝奏云下载地址：[https://jiea.lanzous.com/b01tttrja#ryan](https://jiea.lanzous.com/b01tttrja#ryan)）

   | Version                                                 | State  | Release Date | Downloads                                                                                                                                                                                          |
   | ------------------------------------------------------- | ------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | [8.0](http://pecl.php.net/package/memcache/8.0)         | stable | 2020-12-06   | [memcache-8.0.tgz](http://pecl.php.net/get/memcache-8.0.tgz) (76.6kB)                                                                                                                              |
   | [4.0.5.2](http://pecl.php.net/package/memcache/4.0.5.2) | stable | 2019-12-20   | [memcache-4.0.5.2.tgz](http://pecl.php.net/get/memcache-4.0.5.2.tgz) (73.3kB) [![windows](https://img.zxj.guru/2020/12/windows-icon.png)DLL](http://pecl.php.net/package/memcache/4.0.5.2/windows) |
   | [4.0.5.1](http://pecl.php.net/package/memcache/4.0.5.1) | stable | 2019-12-19   | [memcache-4.0.5.1.tgz](http://pecl.php.net/get/memcache-4.0.5.1.tgz) (73.3kB) [![windows](https://img.zxj.guru/2020/12/windows-icon.png)DLL](http://pecl.php.net/package/memcache/4.0.5.1/windows) |
   | [3.0.8](http://pecl.php.net/package/memcache/3.0.8)     | beta   | 2013-04-07   | [memcache-3.0.8.tgz](http://pecl.php.net/get/memcache-3.0.8.tgz) (68.9kB) [![windows](https://img.zxj.guru/2020/12/windows-icon.png)DLL](http://pecl.php.net/package/memcache/3.0.8/windows)       |

2. 解压 `memcache-8.0.tgz`，找到 `memcache.php` 文件。

3. 找到下面代码编辑，在文件 22-29 行左右。

   ```php
   define('ADMIN_USERNAME','memcache');     // Admin Username
   define('ADMIN_PASSWORD','password');      // Admin Password
   define('DATE_FORMAT','Y/m/d H:i:s');
   define('GRAPH_SIZE',200);
   define('MAX_ITEM_DUMP',50);

   $MEMCACHE_SERVERS[] = 'mymemcache-server1:11211'; // add more as an array
   $MEMCACHE_SERVERS[] = 'mymemcache-server2:11211'; // add more as an array
   ```

   修改为

   ```php
   define('ADMIN_USERNAME','LzB9j5rZgB');     // 登录名自行修改
   define('ADMIN_PASSWORD','6bUn@YgiG4xre$f9pNQMNkpQSFf$DS');      // 密码自行修改
   define('DATE_FORMAT','Y/m/d H:i:s');
   define('GRAPH_SIZE',200);
   define('MAX_ITEM_DUMP',50);

   // 这里定义的是 memcached 服务器，一般我们是单机部署，所以注释掉一行，并将 memcached 监听 IP 和端口根据实际修改
   $MEMCACHE_SERVERS[] = '127.0.0.1:11211'; // add more as an array
   //$MEMCACHE_SERVERS[] = 'mymemcache-server2:11211'; // add more as an array
   ```

   > 实际的 memcached 监听 IP 和端口，你可以通过如下命令查看：
   >
   > ```bash
   > $ netstat -nutlp | grep memcache
   > tcp        0      0 127.0.0.1:11211         0.0.0.0:*               LISTEN      3070/memcached
   > ```

4. 上传到网站私密目录（临时测试可以放到根目录），然后通过前台访问 `memcache.php` 文件，输入上面的用户名和密码即可看到 memcached 状态：

## 纯静态缓存

目前已经完成了数据库查询的动态缓存，如果想要进一步提高性能将网站的页面静态化，存储在 memcached 分配的内存中，可以使用 WordPress 插件 [Batcache](https://wordpress.org/plugins/batcache)。

### 安装 Batcache 插件

1. 在 WordPress 插件市场下载 [Batcache](https://wordpress.org/plugins/batcache)。
2. 解压下载的 `batcache.1.5.zip` 。（或者直接从 [batcache/trunk](http://svn.wp-plugins.org/batcache/trunk/) 页面下载）
3. 将 `advanced-cache.php` 文件上传到 `/wp-content/` 目录。
4. 在 `wp-config.php` 文件中添加 `define('WP_CACHE', true);` 激活 Batcache 插件；
5. 在浏览器中将网站的某个页面刷新几次，在开发者工具源码页，在 `</head>` 结束标签上方可以看到 Batcache 的状态。
6. 在 `advanced-cache.php`文件中调整相关参数，大概在文件 43-49 行左右。

   ```php
   var $max_age =  300; // Expire batcache items aged this many seconds (zero to disable batcache)
   var $remote  =    0; // Zero disables sending buffers to remote datacenters (req/sec is never sent)
   var $times   =    2; // Only batcache a page after it is accessed this many times... (two or more)
   var $seconds =  120; // ...in this many seconds (zero to ignore this and use batcache immediately)
   ```

   `max_age` 代表缓存过期时间（以秒为单位），`times` 表示访问多少次才创建缓存（2 是最小值），`seconds` 表示在多少秒之后才创建缓存（0 表示立即）。

   修改为：

   ```php
   var $max_age =  3600;
   var $remote  =    0;
   var $times   =    2;
   var $seconds =  120;
   ```

   将缓存有效期设为 `3600` 秒，也就是过 1 小时后缓存将重新生成。在 120 秒内，连续访问该页面 2 次将生成缓存。具体数字可以根据实际情况修改。

7. （可选）将 `batcache.php` 上传到 `/wp-content/plugins/` 网站插件目录。

## 参考

- [WordPress 启用 memcached 动态缓存以及报错解决](https://zhang.ge/5097.html)
- [Memcached Object Cache – installation](https://wordpress.org/plugins/memcached/#installation)
- [Batcache – installation](https://wordpress.org/plugins/batcache/#installation)

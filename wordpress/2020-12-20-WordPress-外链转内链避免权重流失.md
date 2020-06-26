---
title: WordPress 外链转内链避免权重流失
abstract: WordPress 外链转为内链，这样可以减少权重的流失或者隐藏某些推荐链接。实现方法有两种：安装插件实现或者直接使用代码实现。
url: wordpress-redirection-link.html
permalink: wordpress-redirection-link.html
date: 2020-12-20 02:08:26
category:
  - WordPress
tags:
  - WordPress
---

WordPress 外链转为内链，这样可以减少权重的流失或者隐藏某些推荐链接。实现方法有两种：安装插件实现或者直接使用代码实现。

![wordpress-redirection-link](https://img.zxj.guru/2020/12/wordpress-redirection-link.png)

## 重写外链

### 安装插件

在后台插件安装界面搜索 `Anylink` 即可在线安装。插件配置时需注意：

- 跳转目录名称：`go` 。应该与网站根目录下跳转页面文件夹名相同。

![imgbed.cn图床](https://vkceyugu.cdn.bspapp.com/VKCEYUGU-imgbed/f49dad2b-31fa-41b9-b646-227518732604.png)

### 代码实现

#### 替换文章内容中的外链

在主题目录下的 `functions.php` 新增如下函数，即可将文章中的外链替换为 `go` 跳转的形式：

```php
//给外部链接加上跳转 https://zhang.ge/4683.html
add_filter('the_content','the_content_nofollow',999);
function the_content_nofollow($content)
{
    preg_match_all('/<a(.*?)href="(.*?)"(.*?)>/',$content,$matches);
    if($matches){
        foreach($matches[2] as $val){
            if(strpos($val,'://')!==false && strpos($val,home_url())===false && !preg_match('/\.(jpg|jepg|png|ico|bmp|gif|tiff)/i',$val)){
                $content=str_replace("href=\"$val\"", "href=\"".home_url()."/go/?url=$val\" ",$content);
            }
        }
    }
    return $content;
}
```

#### 替换评论者的链接

在主题目录下的 `functions.php` 查找是否存在修改评论链接为新窗口 `commentauthor` 函数，如果存在则如下修改第 8 行，将 `$url` 修改为 `/go/?url=$url`，其实就是在前面新增一个 `go` 跳转。

```php
//评论链接新窗口
function commentauthor($comment_ID = 0) {
    $url    = get_comment_author_url( $comment_ID );
    $author = get_comment_author( $comment_ID );
    if ( empty( $url ) || 'http://' == $url )
        echo $author;
    else
        echo "<a href='".home_url()."/go/?url=$url' rel='external nofollow' target='_blank' class='url'>$author</a>";
}
```

## 新增跳转页面

在网站根目录新增一个文件夹，命名为 `go`，并在 `go` 文件夹下新增一个 `index.php`，内容如下：(一共[ 6 个模板](https://jiea.lanzous.com/b01ttqr7a)，可以在 <https://files.ryanjie.vercel.app/go> 页面预览)

### 模板 1

预览页面：[预览](https://files.ryanjie.vercel.app/go/go-1.html)

```php
<!-- https://zhang.ge/5086.html -->
<?php
if (
    strlen($_SERVER['REQUEST_URI']) > 384 ||
    strpos($_SERVER['REQUEST_URI'], "eval(") ||
    strpos($_SERVER['REQUEST_URI'], "base64")
) {
    @header("HTTP/1.1 414 Request-URI Too Long");
    @header("Status: 414 Request-URI Too Long");
    @header("Connection: Close");
    @exit;
}
//通过QUERY_STRING取得完整的传入数据，然后取得url=之后的所有值，兼容性更好
$t_url = preg_replace('/^url=(.*)$/i', '$1', $_SERVER["QUERY_STRING"]);

//数据处理
if (!empty($t_url)) {
    //判断取值是否加密
    if ($t_url == base64_encode(base64_decode($t_url))) {
        $t_url =  base64_decode($t_url);
    }
    //对取值进行网址校验和判断
    preg_match('/^(http|https|thunder|qqdl|ed2k|Flashget|qbrowser):\/\//i', $t_url, $matches);
    if ($matches) {
        $url = $t_url;
        $title = '页面加载中,请稍候...';
    } else {
        preg_match('/\./i', $t_url, $matche);
        if ($matche) {
            $url = 'http://' . $t_url;
            $title = '页面加载中,请稍候...';
        } else {
            $url = 'http://' . $_SERVER['HTTP_HOST'];
            $title = '参数错误，正在返回首页...';
        }
    }
} else {
    $title = '参数缺失，正在返回首页...';
    $url = 'http://' . $_SERVER['HTTP_HOST'];
}
?>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="robots" content="noindex, nofollow" />
    <meta charset="UTF-8">
    <link rel="shortcut icon" href="https://www.baidu.com/favicon.ico">
    <noscript>
        <meta http-equiv="refresh" content="1;url='<?php echo $url; ?>';"></noscript>
    <script>
        function link_jump() {
            //禁止其他网站使用我们的跳转页面
            var MyHOST = new RegExp("<?php echo $_SERVER['HTTP_HOST']; ?>");
            if (!MyHOST.test(document.referrer)) {
                location.href = "http://" + MyHOST;
            }
            location.href = "<?php echo $url; ?>";
        }
        //延时0.5S跳转，可自行修改延时时间
        setTimeout(link_jump, 500);
        //延时50S关闭跳转页面，用于文件下载后不会关闭跳转页的问题
        setTimeout(function() {
            window.opener = null;
            window.close();
        }, 50000);
    </script>
    <title><?php echo $title; ?></title>
    <style type="text/css">a, abbr, acronym, address, applet, article, aside, audio, b, big, blockquote, body, canvas, caption, center, cite, code, dd, del, details, dfn, div, dl, dt, em, embed, fieldset, figcaption, figure, footer, form, h1, h2, h3, h4, h5, h6, header, hgroup, html, i, iframe, img, ins, kbd, label, legend, li, mark, menu, nav, object, ol, output, p, pre, q, ruby, s, samp, section, small, span, strike, strong, sub, summary, sup, table, tbody, td, tfoot, th, thead, time, tr, tt, u, ul, var, video { margin: 0; padding: 0; border: 0; font-size: 100%; font: inherit; vertical-align: baseline } body { background: #3498db } #loader-container { width: 188px; height: 188px; color: #fff; margin: 0 auto; position: absolute; top: 50%; left: 50%; margin-right: -50%; transform: translate(-50%, -50%); border: 5px solid #3498db; border-radius: 50%; -webkit-animation: borderScale 1s infinite ease-in-out; animation: borderScale 1s infinite ease-in-out } #loadingText { font-family: "Microsoft YaHei", Helvetica, Arial, Lucida Grande, Tahoma, sans-serif, Raleway, sans-serif; font-size: 1.4em; position: absolute; top: 50%; left: 50%; margin-right: -50%; transform: translate(-50%, -50%) } @-webkit-keyframes borderScale { 0% { border: 5px solid #fff } 50% { border: 25px solid #3498db } 100% { border: 5px solid #fff } } @keyframes borderScale { 0% { border: 5px solid #fff } 50% { border: 25px solid #3498db } 100% { border: 5px solid #fff } }
    </style>
  </head>

  <body>
    <div id="loader-container">
      <p id="loadingText">页面加载中...</p></div>
  </body>
</html>
```

### 模板 2

预览页面：[预览](https://files.ryanjie.vercel.app/go/go-2.html)

```php
<?php
if (
    strlen($_SERVER['REQUEST_URI']) > 384 ||
    strpos($_SERVER['REQUEST_URI'], "eval(") ||
    strpos($_SERVER['REQUEST_URI'], "base64")
) {
    @header("HTTP/1.1 414 Request-URI Too Long");
    @header("Status: 414 Request-URI Too Long");
    @header("Connection: Close");
    @exit;
}
//通过QUERY_STRING取得完整的传入数据，然后取得url=之后的所有值，兼容性更好
$t_url = preg_replace('/^url=(.*)$/i', '$1', $_SERVER["QUERY_STRING"]);

//数据处理
if (!empty($t_url)) {
    //判断取值是否加密
    if ($t_url == base64_encode(base64_decode($t_url))) {
        $t_url =  base64_decode($t_url);
    }
    //对取值进行网址校验和判断
    preg_match('/^(http|https|thunder|qqdl|ed2k|Flashget|qbrowser):\/\//i', $t_url, $matches);
    if ($matches) {
        $url = $t_url;
        $title = '页面加载中,请稍候...';
    } else {
        preg_match('/\./i', $t_url, $matche);
        if ($matche) {
            $url = 'http://' . $t_url;
            $title = '页面加载中,请稍候...';
        } else {
            $url = 'http://' . $_SERVER['HTTP_HOST'];
            $title = '参数错误，正在返回首页...';
        }
    }
} else {
    $title = '参数缺失，正在返回首页...';
    $url = 'http://' . $_SERVER['HTTP_HOST'];
}
?>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="robots" content="noindex, nofollow" />
    <meta charset="UTF-8">
    <link rel="shortcut icon" href="https://www.baidu.com/favicon.ico">
    <noscript>
        <meta http-equiv="refresh" content="1;url='<?php echo $url; ?>';"></noscript>
    <script>
        function link_jump() {
            //禁止其他网站使用我们的跳转页面
            var MyHOST = new RegExp("<?php echo $_SERVER['HTTP_HOST']; ?>");
            if (!MyHOST.test(document.referrer)) {
                location.href = "http://" + MyHOST;
            }
            location.href = "<?php echo $url; ?>";
        }
        //延时0.5S跳转，可自行修改延时时间
        setTimeout(link_jump, 500);
        //延时50S关闭跳转页面，用于文件下载后不会关闭跳转页的问题
        setTimeout(function() {
            window.opener = null;
            window.close();
        }, 50000);
    </script>
    <title><?php echo $title; ?></title>
    <style type="text/css">body { background: #555 } .loading { -webkit-animation: fadein 2s; -moz-animation: fadein 2s; -o-animation: fadein 2s; animation: fadein 2s } @-moz-keyframes fadein { from { opacity: 0 } to { opacity: 1 } } @-webkit-keyframes fadein { from { opacity: 0 } to { opacity: 1 } } @-o-keyframes fadein { from { opacity: 0 } to { opacity: 1 } } @keyframes fadein { from { opacity: 0 } to { opacity: 1 } } .spinner-wrapper { position: absolute; top: 0; left: 0; z-index: 300; height: 100%; min-width: 100%; min-height: 100%; background: rgba(255, 255, 255, 0.93) } .spinner-text { position: absolute; top: 45%; left: 50%; margin-left: -100px; margin-top: 2px; color: #000; letter-spacing: 1px; font-size: 20px; font-family: Arial } .spinner { position: absolute; top: 45%; left: 50%; display: block; margin-left: -160px; width: 1px; height: 1px; border: 20px solid rgba(255, 0, 0, 1); -webkit-border-radius: 50px; -moz-border-radius: 50px; border-radius: 50px; border-left-color: transparent; border-right-color: transparent; -webkit-animation: spin 1.5s infinite; -moz-animation: spin 1.5s infinite; animation: spin 1.5s infinite } @-webkit-keyframes spin { 0%, 100% { -webkit-transform: rotate(0deg) scale(1) } 50% { -webkit-transform: rotate(720deg) scale(0.6) } } @-moz-keyframes spin { 0%, 100% { -moz-transform: rotate(0deg) scale(1) } 50% { -moz-transform: rotate(720deg) scale(0.6) } } @-o-keyframes spin { 0%, 100% { -o-transform: rotate(0deg) scale(1) } 50% { -o-transform: rotate(720deg) scale(0.6) } } @keyframes spin { 0%, 100% { transform: rotate(0deg) scale(1) } 50% { transform: rotate(720deg) scale(0.6) } }
    </style>
  </head>

  <body>
    <div class="loading">
      <div class="spinner-wrapper">
        <span class="spinner-text">页面加载中，请稍候...</span>
        <span class="spinner"></span>
      </div>
    </div>
  </body>
</html>
```

### 模板 3

预览页面：[预览](https://files.ryanjie.vercel.app/go/go-3.html)

```php
    <?php
    if (
        strlen($_SERVER['REQUEST_URI']) > 384 ||
        strpos($_SERVER['REQUEST_URI'], "eval(") ||
        strpos($_SERVER['REQUEST_URI'], "base64")
    ) {
        @header("HTTP/1.1 414 Request-URI Too Long");
        @header("Status: 414 Request-URI Too Long");
        @header("Connection: Close");
        @exit;
    }
    //通过QUERY_STRING取得完整的传入数据，然后取得url=之后的所有值，兼容性更好
    $t_url = preg_replace('/^url=(.*)$/i', '$1', $_SERVER["QUERY_STRING"]);

    //数据处理
    if (!empty($t_url)) {
        //判断取值是否加密
        if ($t_url == base64_encode(base64_decode($t_url))) {
            $t_url =  base64_decode($t_url);
        }
        //对取值进行网址校验和判断
        preg_match('/^(http|https|thunder|qqdl|ed2k|Flashget|qbrowser):\/\//i', $t_url, $matches);
        if ($matches) {
            $url = $t_url;
            $title = '页面加载中,请稍候...';
        } else {
            preg_match('/\./i', $t_url, $matche);
            if ($matche) {
                $url = 'http://' . $t_url;
                $title = '页面加载中,请稍候...';
            } else {
                $url = 'http://' . $_SERVER['HTTP_HOST'];
                $title = '参数错误，正在返回首页...';
            }
        }
    } else {
        $title = '参数缺失，正在返回首页...';
        $url = 'http://' . $_SERVER['HTTP_HOST'];
    }
    ?>
    <html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="robots" content="noindex, nofollow" />
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="https://www.baidu.com/favicon.ico">
        <noscript>
            <meta http-equiv="refresh" content="1;url='<?php echo $url; ?>';"></noscript>
        <script>
            function link_jump() {
                //禁止其他网站使用我们的跳转页面
                var MyHOST = new RegExp("<?php echo $_SERVER['HTTP_HOST']; ?>");
                if (!MyHOST.test(document.referrer)) {
                    location.href = "http://" + MyHOST;
                }
                location.href = "<?php echo $url; ?>";
            }
            //延时0.5S跳转，可自行修改延时时间
            setTimeout(link_jump, 500);
            //延时50S关闭跳转页面，用于文件下载后不会关闭跳转页的问题
            setTimeout(function() {
                window.opener = null;
                window.close();
            }, 50000);
        </script>
        <title><?php echo $title; ?></title>
        <style type="text/css">a { background: #13a3a5; padding: 5px; margin: 10px; display: block; cursor: pointer; font-size: 1.5em; float: left; text-decoration: none; font-size: 18px; color: #fff } a, body { font-weight: 100 } body { -webkit-tap-highlight-color: transparent; background-color: #222428; font-size: 100%; font-family: Open Sans; height: 100% } .loader { top: 50%; left: 50%; -webkit-transform: translate(-50%, -50%); -mos-transform: translate(-50%, -50%); transform: translate(-50%, -50%); text-align: center; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; cursor: default; width: 80%; overflow: visible } .loader, .loader div { position: absolute; height: 36px } .loader div { width: 30px; margin: 0 10px; opacity: 0; animation: move 2s linear infinite; -o-animation: move 2s linear infinite; -moz-animation: move 2s linear infinite; -webkit-animation: move 2s linear infinite; transform: rotate(180deg); -o-transform: rotate(180deg); -moz-transform: rotate(180deg); -webkit-transform: rotate(180deg); color: #fff; font-size: 3em } .loader div:nth-child(8):before { background: #db2f00 } .loader div:nth-child(8):before, .loader div:nth-child(9):before { content: ''; position: absolute; bottom: -15px; left: 0; width: 30px; height: 30px; border-radius: 100% } .loader div:nth-child(9):before { background: #f2f2f2 } .loader div:nth-child(10):before { bottom: -15px; height: 30px; background: #13a3a5 } .loader div:after, .loader div:nth-child(10):before { content: ''; position: absolute; left: 0; width: 30px; border-radius: 100% } .loader div:after { bottom: -40px; height: 5px; background: #39312d } .loader div:nth-child(2) { animation-delay: .2s; -o-animation-delay: .2s; -moz-animation-delay: .2s; -webkit-animation-delay: .2s } .loader div:nth-child(3) { animation-delay: .4s; -o-animation-delay: .4s; -webkit-animation-delay: .4s } .loader div:nth-child(4) { animation-delay: .6s; -o-animation-delay: .6s; -moz-animation-delay: .6s; -webkit-animation-delay: .6s } .loader div:nth-child(5) { animation-delay: .8s; -o-animation-delay: .8s; -moz-animation-delay: .8s; -webkit-animation-delay: .8s } .loader div:nth-child(6) { animation-delay: 1s; -o-animation-delay: 1s; -moz-animation-delay: 1s; -webkit-animation-delay: 1s } .loader div:nth-child(7) { animation-delay: 1.2s; -o-animation-delay: 1.2s; -moz-animation-delay: 1.2s; -webkit-animation-delay: 1.2s } .loader div:nth-child(8) { animation-delay: 1.4s; -o-animation-delay: 1.4s; -moz-animation-delay: 1.4s; -webkit-animation-delay: 1.4s } .loader div:nth-child(9) { animation-delay: 1.6s; -o-animation-delay: 1.6s; -moz-animation-delay: 1.6s; -webkit-animation-delay: 1.6s } .loader div:nth-child(10) { animation-delay: 1.8s; -o-animation-delay: 1.8s; -moz-animation-delay: 1.8s; -webkit-animation-delay: 1.8s } @keyframes move { 0% { right: 0; opacity: 0 } 35% { right: 41% } 35%, 65% { -webkit-transform: rotate(0); transform: rotate(0); opacity: 1 } 65% { right: 59% } to { right: 100%; -webkit-transform: rotate(-180deg); transform: rotate(-180deg) } } @-webkit-keyframes move { 0%, to { opacity: 0 } 0% { right: 0 } 35% { right: 41% } 35%, 75% { -webkit-transform: rotate(0); transform: rotate(0); opacity: 1 } 75% { right: 59% } to { right: 100%; -webkit-transform: rotate(-180deg); transform: rotate(-180deg); opacity: 0 } }
    </style>
  </head>

  <body class="ie8" style="">
    <div class="loader">
      <div>L</div>
      <div>O</div>
      <div>A</div>
      <div>D</div>
      <div>I</div>
      <div>N</div>
      <div>G</div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </body>
</html>
```

### 模板 4

预览页面：[预览](https://files.ryanjie.vercel.app/go/go-4.html)

```php
    <?php
    if (
        strlen($_SERVER['REQUEST_URI']) > 384 ||
        strpos($_SERVER['REQUEST_URI'], "eval(") ||
        strpos($_SERVER['REQUEST_URI'], "base64")
    ) {
        @header("HTTP/1.1 414 Request-URI Too Long");
        @header("Status: 414 Request-URI Too Long");
        @header("Connection: Close");
        @exit;
    }
    //通过QUERY_STRING取得完整的传入数据，然后取得url=之后的所有值，兼容性更好
    $t_url = preg_replace('/^url=(.*)$/i', '$1', $_SERVER["QUERY_STRING"]);

    //数据处理
    if (!empty($t_url)) {
        //判断取值是否加密
        if ($t_url == base64_encode(base64_decode($t_url))) {
            $t_url =  base64_decode($t_url);
        }
        //对取值进行网址校验和判断
        preg_match('/^(http|https|thunder|qqdl|ed2k|Flashget|qbrowser):\/\//i', $t_url, $matches);
        if ($matches) {
            $url = $t_url;
            $title = '页面加载中,请稍候...';
        } else {
            preg_match('/\./i', $t_url, $matche);
            if ($matche) {
                $url = 'http://' . $t_url;
                $title = '页面加载中,请稍候...';
            } else {
                $url = 'http://' . $_SERVER['HTTP_HOST'];
                $title = '参数错误，正在返回首页...';
            }
        }
    } else {
        $title = '参数缺失，正在返回首页...';
        $url = 'http://' . $_SERVER['HTTP_HOST'];
    }
    ?>
    <html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="robots" content="noindex, nofollow" />
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="https://www.baidu.com/favicon.ico">
        <noscript>
            <meta http-equiv="refresh" content="1;url='<?php echo $url; ?>';"></noscript>
        <script>
            function link_jump() {
                //禁止其他网站使用我们的跳转页面
                var MyHOST = new RegExp("<?php echo $_SERVER['HTTP_HOST']; ?>");
                if (!MyHOST.test(document.referrer)) {
                    location.href = "http://" + MyHOST;
                }
                location.href = "<?php echo $url; ?>";
            }
            //延时0.5S跳转，可自行修改延时时间
            setTimeout(link_jump, 500);
            //延时50S关闭跳转页面，用于文件下载后不会关闭跳转页的问题
            setTimeout(function() {
                window.opener = null;
                window.close();
            }, 50000);
        </script>
        <title><?php echo $title; ?></title>
        <style type="text/css">* { margin: 0; padding: 0; border: 0 } body, html { min-height: 100% } body { background: radial-gradient(#eee, #444) } .loader { position: absolute; top: 0; bottom: 0; left: 0; right: 0; margin: auto; width: 175px; height: 100px } .loader span { display: block; background: #ccc; width: 7px; height: 10%; border-radius: 14px; margin-right: 5px; float: left; margin-top: 25% } .loader span:last-child { margin-right: 0 } .loader span:nth-child(1) { animation: load 2.5s 1.4s infinite linear } .loader span:nth-child(2) { animation: load 2.5s 1.2s infinite linear } .loader span:nth-child(3) { animation: load 2.5s 1s infinite linear } .loader span:nth-child(4) { animation: load 2.5s .8s infinite linear } .loader span:nth-child(5) { animation: load 2.5s .6s infinite linear } .loader span:nth-child(6) { animation: load 2.5s .4s infinite linear } .loader span:nth-child(7) { animation: load 2.5s .2s infinite linear } .loader span:nth-child(8) { animation: load 2.5s 0s infinite linear } .loader span:nth-child(9) { animation: load 2.5s .2s infinite linear } .loader span:nth-child(10) { animation: load 2.5s .4s infinite linear } .loader span:nth-child(11) { animation: load 2.5s .6s infinite linear } .loader span:nth-child(12) { animation: load 2.5s .8s infinite linear } .loader span:nth-child(13) { animation: load 2.5s 1s infinite linear } .loader span:nth-child(14) { animation: load 2.5s 1.2s infinite linear } .loader span:nth-child(15) { animation: load 2.5s 1.4s infinite linear } @keyframes load { 0% { background: #ccc; margin-top: 25%; height: 10% } 50% { background: #444; height: 100%; margin-top: 0 } 100% { background: #ccc; height: 10%; margin-top: 25% } }
    </style>
  </head>

  <body>
    <div class="loader">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>
  </body>
</html>
```

### 模板 5

预览页面：[预览](https://files.ryanjie.vercel.app/go/go-5.html)

```php
<?php
if (
    strlen($_SERVER['REQUEST_URI']) > 384 ||
    strpos($_SERVER['REQUEST_URI'], "eval(") ||
    strpos($_SERVER['REQUEST_URI'], "base64")
) {
    @header("HTTP/1.1 414 Request-URI Too Long");
    @header("Status: 414 Request-URI Too Long");
    @header("Connection: Close");
    @exit;
}
//通过QUERY_STRING取得完整的传入数据，然后取得url=之后的所有值，兼容性更好
$t_url = preg_replace('/^url=(.*)$/i', '$1', $_SERVER["QUERY_STRING"]);

//数据处理
if (!empty($t_url)) {
    //判断取值是否加密
    if ($t_url == base64_encode(base64_decode($t_url))) {
        $t_url =  base64_decode($t_url);
    }
    //对取值进行网址校验和判断
    preg_match('/^(http|https|thunder|qqdl|ed2k|Flashget|qbrowser):\/\//i', $t_url, $matches);
    if ($matches) {
        $url = $t_url;
        $title = '页面加载中,请稍候...';
    } else {
        preg_match('/\./i', $t_url, $matche);
        if ($matche) {
            $url = 'http://' . $t_url;
            $title = '页面加载中,请稍候...';
        } else {
            $url = 'http://' . $_SERVER['HTTP_HOST'];
            $title = '参数错误，正在返回首页...';
        }
    }
} else {
    $title = '参数缺失，正在返回首页...';
    $url = 'http://' . $_SERVER['HTTP_HOST'];
}
?>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="robots" content="noindex, nofollow" />
    <meta charset="UTF-8">
    <link rel="shortcut icon" href="https://www.baidu.com/favicon.ico">
    <noscript>
        <meta http-equiv="refresh" content="1;url='<?php echo $url; ?>';"></noscript>
    <script>
        function link_jump() {
            //禁止其他网站使用我们的跳转页面
            var MyHOST = new RegExp("<?php echo $_SERVER['HTTP_HOST']; ?>");
            if (!MyHOST.test(document.referrer)) {
                location.href = "http://" + MyHOST;
            }
            location.href = "<?php echo $url; ?>";
        }
        //延时0.5S跳转，可自行修改延时时间
        setTimeout(link_jump, 500);
        //延时50S关闭跳转页面，用于文件下载后不会关闭跳转页的问题
        setTimeout(function() {
            window.opener = null;
            window.close();
        }, 50000);
    </script>
    <title><?php echo $title; ?></title>
    <style type="text/css">html { overflow: hidden } html, html body { height: 100%; min-height: 100% } html body { background: #222428; background-size: 163px; font: 14px/21px Monaco, sans-serif; color: #999; font-smoothing: antialiased; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; text-size-adjust: 100% } html body a, html body a:visited { text-decoration: none; color: #ff805f } html body h4 { margin: 0; color: #666 } .scene { width: 100%; height: 100%; -webkit-perspective: 600; perspective: 600; display: flex; align-items: center; justify-content: center } .scene svg { width: 15pc; height: 15pc } .dc-logo { position: fixed; right: 10px; bottom: 10px } .dc-logo:hover svg { -webkit-transform-origin: 50% 50%; transform-origin: 50% 50%; -webkit-animation: arrow-spin 2.5s 0s cubic-bezier(0.165, 0.84, 0.44, 1) infinite; animation: arrow-spin 2.5s 0s cubic-bezier(0.165, 0.84, 0.44, 1) infinite } .dc-logo:hover:hover:before { content: '\2764'; color: #00fffe; left: -70px } .dc-logo:hover:hover:after, .dc-logo:hover:hover:before { padding: 6px; font: 10px/1 Monaco, sans-serif; font-size: 10px; text-transform: uppercase; position: absolute; top: -30px; white-space: nowrap; z-index: 20px; box-shadow: 0 0 4px #222; background: rgba(0, 0, 0, .4) } .dc-logo:hover:hover:after { content: 'Digital Craft'; color: #6e6f71; right: 0; background-image: none } @keyframes arrow-spin { 50% { -webkit-transform: rotateY(360deg); transform: rotateY(360deg) } }
    </style>
  </head>

  <body>
    <div class="scene">
      <svg version="1.1" id="dc-spinner" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width: "38" height: "38" viewbox="0 0 38 38" preserveaspectratio="xMinYMin meet">
        <text x="14" y="21" font-family="Monaco" font-size="2px" style="letter-spacing:0.6" fill="grey">LOADING
          <animate attributename="opacity" values="0;1;0" dur="1.8s" repeatcount="indefinite" /></text>
        <path fill="#373a42" d="M20,35c-8.271,0-15-6.729-15-15S11.729,5,20,5s15,6.729,15,15S28.271,35,20,35z M20,5.203 C11.841,5.203,5.203,11.841,5.203,20c0,8.159,6.638,14.797,14.797,14.797S34.797,28.159,34.797,20 C34.797,11.841,28.159,5.203,20,5.203z"></path>
        <path fill="#373a42" d="M20,33.125c-7.237,0-13.125-5.888-13.125-13.125S12.763,6.875,20,6.875S33.125,12.763,33.125,20 S27.237,33.125,20,33.125z M20,7.078C12.875,7.078,7.078,12.875,7.078,20c0,7.125,5.797,12.922,12.922,12.922 S32.922,27.125,32.922,20C32.922,12.875,27.125,7.078,20,7.078z"></path>
        <path fill="#2AA198" stroke="#2AA198" stroke-width="0.6027" stroke-miterlimit="10" d="M5.203,20 c0-8.159,6.638-14.797,14.797-14.797V5C11.729,5,5,11.729,5,20s6.729,15,15,15v-0.203C11.841,34.797,5.203,28.159,5.203,20z">
          <animatetransform attributename="transform" type="rotate" from="0 20 20" to="360 20 20" calcmode="spline" keysplines="0.4, 0, 0.2, 1" keytimes="0;1" dur="2s" repeatcount="indefinite" /></path>
        <path fill="#859900" stroke="#859900" stroke-width="0.2027" stroke-miterlimit="10" d="M7.078,20 c0-7.125,5.797-12.922,12.922-12.922V6.875C12.763,6.875,6.875,12.763,6.875,20S12.763,33.125,20,33.125v-0.203 C12.875,32.922,7.078,27.125,7.078,20z">
          <animatetransform attributename="transform" type="rotate" from="0 20 20" to="360 20 20" dur="1.8s" repeatcount="indefinite" /></path>
      </svg>
    </div>
  </body>
</html>
```

### 模板 6

预览页面：[预览](https://files.ryanjie.vercel.app/go/go-6.html)

```php
<?php
if (
    strlen($_SERVER['REQUEST_URI']) > 384 ||
    strpos($_SERVER['REQUEST_URI'], "eval(") ||
    strpos($_SERVER['REQUEST_URI'], "base64")
) {
    @header("HTTP/1.1 414 Request-URI Too Long");
    @header("Status: 414 Request-URI Too Long");
    @header("Connection: Close");
    @exit;
}
//通过QUERY_STRING取得完整的传入数据，然后取得url=之后的所有值，兼容性更好
$t_url = preg_replace('/^url=(.*)$/i', '$1', $_SERVER["QUERY_STRING"]);

//数据处理
if (!empty($t_url)) {
    //判断取值是否加密
    if ($t_url == base64_encode(base64_decode($t_url))) {
        $t_url =  base64_decode($t_url);
    }
    //对取值进行网址校验和判断
    preg_match('/^(http|https|thunder|qqdl|ed2k|Flashget|qbrowser):\/\//i', $t_url, $matches);
    if ($matches) {
        $url = $t_url;
        $title = '页面加载中,请稍候...';
    } else {
        preg_match('/\./i', $t_url, $matche);
        if ($matche) {
            $url = 'http://' . $t_url;
            $title = '页面加载中,请稍候...';
        } else {
            $url = 'http://' . $_SERVER['HTTP_HOST'];
            $title = '参数错误，正在返回首页...';
        }
    }
} else {
    $title = '参数缺失，正在返回首页...';
    $url = 'http://' . $_SERVER['HTTP_HOST'];
}
?>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="robots" content="noindex, nofollow" />
    <meta charset="UTF-8">
    <link rel="shortcut icon" href="https://www.baidu.com/favicon.ico">
    <noscript>
        <meta http-equiv="refresh" content="1;url='<?php echo $url; ?>';"></noscript>
    <script>
        function link_jump() {
            //禁止其他网站使用我们的跳转页面
            var MyHOST = new RegExp("<?php echo $_SERVER['HTTP_HOST']; ?>");
            if (!MyHOST.test(document.referrer)) {
                location.href = "http://" + MyHOST;
            }
            location.href = "<?php echo $url; ?>";
        }
        //延时0.5S跳转，可自行修改延时时间
        setTimeout(link_jump, 500);
        //延时50S关闭跳转页面，用于文件下载后不会关闭跳转页的问题
        setTimeout(function() {
            window.opener = null;
            window.close();
        }, 50000);
    </script>
    <title><?php echo $title; ?></title>
    <style type="text/css">body { margin: 0; height: 100vh; display: flex; align-items: center; justify-content: center; background: #222428 } .container { width: 8em; height: 1em; font-size: 35px; display: flex; justify-content: space-between } .container span { width: 1em; height: 1em; --duration: 1.5s } .girl { animation: slide var(--duration) ease-in-out infinite alternate } @keyframes slide { 0% { transform: translateX(0); filter: brightness(1) } to { transform: translatex(6.75em); filter: brightness(1.45) } } .boys { width: 6em; display: flex; justify-content: space-between } .boys span { animation: var(--duration) ease-in-out infinite alternate } .boys span:nth-child(1) { animation-name: jump-off-1 } .boys span:nth-child(2) { animation-name: jump-off-2 } .boys span:nth-child(3) { animation-name: jump-off-3 } .boys span:nth-child(4) { animation-name: jump-off-4 } @keyframes jump-off-1 { 0%, 15% { transform: rotate(0deg) } 35%, to { transform-origin: -50% center; transform: rotate(-180deg) } } @keyframes jump-off-2 { 0%, 30% { transform: rotate(0deg) } 50%, to { transform-origin: -50% center; transform: rotate(-180deg) } } @keyframes jump-off-3 { 0%, 45% { transform: rotate(0deg) } 65%, to { transform-origin: -50% center; transform: rotate(-180deg) } } @keyframes jump-off-4 { 0%, 60% { transform: rotate(0deg) } 80%, to { transform-origin: -50% center; transform: rotate(-180deg) } } .container span:before { content: ''; position: absolute; width: inherit; height: inherit; border-radius: 15%; box-shadow: 0 0 .1em rgba(0, 0, 0, .3) } .girl:before { background-color: hotpink } .boys span:before { background-color: #1e90ff; animation: var(--duration) ease-in-out infinite alternate } .boys span:nth-child(1):before { filter: brightness(1); animation-name: jump-down-1 } .boys span:nth-child(2):before { filter: brightness(1.15); animation-name: jump-down-2 } .boys span:nth-child(3):before { filter: brightness(1.3); animation-name: jump-down-3 } .boys span:nth-child(4):before { filter: brightness(1.45); animation-name: jump-down-4 } @keyframes jump-down-1 { 5% { transform: scale(1, 1) } 15% { transform-origin: center bottom; transform: scale(1.3, 0.7) } 20%, 25% { transform-origin: center bottom; transform: scale(0.8, 1.4) } 40% { transform-origin: center top; transform: scale(1.3, 0.7) } 55%, to { transform: scale(1, 1) } } @keyframes jump-down-2 { 20% { transform: scale(1, 1) } 30% { transform-origin: center bottom; transform: scale(1.3, 0.7) } 35%, 40% { transform-origin: center bottom; transform: scale(0.8, 1.4) } 55% { transform-origin: center top; transform: scale(1.3, 0.7) } 70%, to { transform: scale(1, 1) } } @keyframes jump-down-3 { 35% { transform: scale(1, 1) } 45% { transform-origin: center bottom; transform: scale(1.3, 0.7) } 50%, 55% { transform-origin: center bottom; transform: scale(0.8, 1.4) } 70% { transform-origin: center top; transform: scale(1.3, 0.7) } 85%, to { transform: scale(1, 1) } } @keyframes jump-down-4 { 50% { transform: scale(1, 1) } 60% { transform-origin: center bottom; transform: scale(1.3, 0.7) } 65%, 70% { transform-origin: center bottom; transform: scale(0.8, 1.4) } 85% { transform-origin: center top; transform: scale(1.3, 0.7) } to { transform: scale(1, 1) } }
    </style>
  </head>

  <body>
    <div class="container">
      <span class="girl"></span>
      <div class="boys">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </body>
</html>
```

## 新增 robots 规则

为了防止搜索引擎抓取这种跳转链接，我们可以在 `robots.txt` 里面新增禁止抓取 `/go` 的规则：

```markdown
User-agent: \*
Disallow:
Disallow: /wp-admin/
Disallow: /go/
Sitemap: https://www.baidu.com/sitemap.xml
```

## 设置伪静态

`Nginx`伪静态规则：

```properties
# 外链跳转伪静态 php版本
rewrite ^/go/(.*)$ /go.php?url=$1 last; #注意go.php的实际路径，默认为网站根目录
```

## 参考文章

- [分享两种外链跳转方法，可避免权重流失](https://zhang.ge/2703.html)
- [分享一个 WordPress 外链跳转教程，兼容知更鸟暗箱下载和文章索引](https://zhang.ge/4683.html)

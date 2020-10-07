---
title: 使用 WebP 图片加速您的网站
date: 2020-05-02 10:58:34
categories: Website
---

<!-- more -->

## 使用 WebP 图片加速您的网站

WebP 是一种同时提供了有损压缩与无损压缩（可逆压缩）的图片文件格式，派生自影像编码格式 VP8，被认为是 WebM 多媒体格式的姊妹项目，是由 Google 在购买 On2 Technologies 后发展出来，以 BSD 授权条款发布。

WebP 最初在 2010 年发布，目标是减少文件大小，但达到和 JPEG 格式相同的图片质量，希望能够减少图片档在网络上的发送时间。2011 年 11 月 8 日，Google 开始让 WebP 支持无损压缩和透明色（alpha 通道）的功能，而在 2012 年 8 月 16 日的参考实做 libwebp 0.2.0 中正式支持。根据 Google 较早的测试，WebP 的无损压缩比网络上找到的 PNG 档少了 45％的文件大小，即使这些 PNG 档在使用 pngcrush 和 PNGOUT 处理过，WebP 还是可以减少 28％的文件大小。

> [WebP 压缩技术详细介绍](https://developers.google.com/speed/webp/docs/compression)

## WebP 的工作原理

有损的 WebP 压缩使用预测编码对图像进行编码，与 VP8 视频编解码器用于压缩视频中关键帧的方法相同。预测编码使用相邻像素块中的值来预测块中的值，然后仅对差异进行编码。

无损 WebP 压缩使用已经看到的图像片段来准确重建新像素。如果未找到有趣的匹配项，它也可以使用本地调色板。

## WebP 技术

WebP 的有损压缩算法是基于 VP8 视频格式的帧内编码（英语：Intra-frame coding），并以 RIFF 作为容器格式。 因此，它是一个具有八位色彩深度和以 1:2 的比例进行色度子采样的亮度-色度模型（YCbCr 4:2:0）的基于块的转换方案。 不含内容的情况下，RIFF 容器要求只需 20 字节的开销，依然能保存额外的 元数据(metadata)。 WebP 图像的边长限制为 16383 像素。

WebP 是基于块预测的。每个块都是根据它上面三个块的值和其左边一个块的值进行预测的（块解码以光栅扫描顺序完成：从左到右，从上到下）。块预测有四种基本模式：水平、垂直、DC（单色）和 TrueMotion。利用离散余弦变换或沃尔什-阿达玛转换将预测错误的数据和未预测块压缩在 4×4 像素子块中。这两种转换都是使用定点算术（英语：fixed-point arithmetic）完成的，以避免舍入误差。输出使用熵编码进行压缩。 WebP 也明确支持并行解码。

参考实现包含一个 Linux 命令行程序的转换器，以及以及用于解码的库，与 WebM 相同。开源社区很快设法将转换器移植到其他平台，例如 Windows。

WebP 的无损压缩采用先进的技术，例如用于不同颜色通道的专用熵代码，利用反向参考距离的 2D 位置和最近使用的颜色的颜色缓存。这补充了字典编码、霍夫曼编码和颜色索引变换等基本技术。

## WebP 支持

目前网页浏览器当中，Google Chrome 和 Opera 原生支持静态与动态的 WebP 格式，而 Google Chrome 自 12 版开始支持 WebP 的渐进式解码功能。此外所有可以原生播放 WebM 影像的浏览器，也可以透过 javascript 来显示 WebP 影像。又 Pale Moon 26+浏览器仅支持静态的 WebP 图像。Firefox 浏览器亦在 65.0 版本支持 WebP 图像。

网页浏览器 GNOME Web 和 KDE 图片浏览器 Gwenview 也支持 WebP。

图像软件当中，Picasa（从 3.9 版本起）、PhotoLine（英语：PhotoLine）、Pixelmator、ImageMagick、XnView、IrfanView、GDAL（英语：GDAL）、Aseprite 和 GIMP（2.10 起）皆原生支持 WebP 格式。

苹果在 macOS Sierra 及 iOS 10 的早期 beta 版本中加入了 WebP 支持。而在 2016 年 9 月 7 日发布的 iOS 10 和 macOS Sierra GM 种子版本中却移除了 WebP 的支持。

## 使用 WebP 的好处

仅仅说 WebP 比 JPG 和 PNG“更好”还不够。重要的是要了解 WebP 的工作机制，以及为什么在其他文件格式上使用 WebP 这么多好处。

对于传统的图像格式，压缩总是在质量和大小间拿捏。

JPG 有损压缩会导致图像的清晰度和精细度下降。一旦应用，就不能撤消。

WebP 有损压缩则使用所谓的预测编码来更准确地调整图像中的像素。正如 Google 所说，[还有其他一些因素在起作用](https://developers.google.com/speed/webp/docs/compression)：块自适应量化也有很大的不同。过滤有助于中等/低比特率。与霍夫曼编码相比，布尔算术编码提供了 5％-10％的压缩增益。”

**平均而言，Google 估计 WebP 有损压缩会导致文件质量比相同质量的 JPG 小 25％至 34％。**

至于 PNG 无损压缩，它在保持图像质量方面效果很好，但是对图像大小的影响不如 JPG 对等。与 WebP 相比，当然不是。

WebP 更有效地处理这种类型的压缩。这是由于使用了多种压缩技术以及应用于图像的熵编码。再次，谷歌解释了它是如何工作的：“应用于图像的变换包括像素的空间预测，色彩空间变换，使用局部出现的调色板，将多个像素打包为一个像素和 alpha 替换。”

**平均而言，Google 估计 WebP 无损压缩所产生的文件比相同质量的 PNG 大约小 26％。**

不仅如此，WebP 能够执行其他文件格式无法执行的操作。设计人员可以在 RGB 颜色上使用 WebP 有损编码，并在具有透明背景（alpha 通道）的图像上使用无损编码。

动画图像以 GIF 格式提供，也将从 WebP 压缩系统中受益。原因如下：

![webp](https://pic.ryanjie.cn/2020/05/webp.webp)

由于这种强大的无损和有损压缩组合，动画视频的尺寸可以比 GIF 压缩的视频小得多。

**Google 估计，使用有损压缩时，平均压缩量约为 GIF 原始大小的 64％，而使用无损压缩时，平均压缩量为 19％。**

做过一个测试，对比 PNG 原图、PNG 无损压缩、PNG 转 WebP（无损）、PNG 转 WebP（有损）的压缩效果：

![webp-test](https://pic.ryanjie.cn/2020/05/webp-test.webp)

## Wordpress 支持 WebP

默认情况下，WordPress 不支持上传 WebP 格式的图片，在主题的`functions.php`里添加以下代码即可。

### webp 上传

```php
//** *Enable upload for webp image files.*/
function webp_upload_mimes($existing_mimes) {
    $existing_mimes['webp'] = 'image/webp';
    return $existing_mimes;
}
add_filter('mime_types', 'webp_upload_mimes');
```

### webp 预览

虽然现在已经可以上传 WebP 格式的图片了，但在媒体列表中看不到缩略图，这是因为 WordPress 在用`wp_generate_attachment_metadata()`函数生成图片数据时，使用了`file_is_displayable_image()`函数判断文件是否为图片，判断 WebP 图片的结果为否，因此中断了保存图片数据的操作。

解决办法是在主题的`functions.php`里添加以下代码：

```php
//** * Enable preview / thumbnail for webp image files.*/
function webp_is_displayable($result, $path) {
    if ($result === false) {
        $displayable_image_types = array( IMAGETYPE_WEBP );
        $info = @getimagesize( $path );

        if (empty($info)) {
            $result = false;
        } elseif (!in_array($info[2], $displayable_image_types)) {
            $result = false;
        } else {
            $result = true;
        }
    }

    return $result;
}
add_filter('file_is_displayable_image', 'webp_is_displayable', 10, 2);
```

参考上述代码，修改主题 `functions.php` ，部署后重新进入后台就会发现支持 webp 上传和 webp 预览。

不想每次主题更新后都要到主题 `functions.php` 修改的用户，可以自己建一个插件，在 `/wp-content/plugins` 下新建一个文件 `WordPress-WebP.php`，然后开头加注释声明插件信息，最后启用插件就好。

### 懒人插件

```php
<?php
/*
Plugin Name: WordPress 支持 webp 上传和 webp 预览
Plugin URI: https://www.ryanjie.cn/xx.html
Description: 使 WordPress 支持 webp 上传和 webp 预览。
Version: 1.0
Author: Ryanjie
Author URI: https://www.ryanjie.cn
*/

//** *Enable upload for webp image files.*/
function webp_upload_mimes($existing_mimes) {
    $existing_mimes['webp'] = 'image/webp';
    return $existing_mimes;
}
add_filter('mime_types', 'webp_upload_mimes');

//** * Enable preview / thumbnail for webp image files.*/
function webp_is_displayable($result, $path) {
    if ($result === false) {
        $displayable_image_types = array( IMAGETYPE_WEBP );
        $info = @getimagesize( $path );

        if (empty($info)) {
            $result = false;
        } elseif (!in_array($info[2], $displayable_image_types)) {
            $result = false;
        } else {
            $result = true;
        }
    }

    return $result;
}
add_filter('file_is_displayable_image', 'webp_is_displayable', 10, 2);
```

将以上代码保存为 `WordPress-WebP.php` 放在 `/wp-content/plugins` 目录下，然后在 WordPress 后台启用插件。

```bash
wget -c -O /home/ryanjie/www.ryanjie.cn/wp-content/plugins/WordPress-WebP.php https://pic.ryanjie.cn/2020/05/WordPress-WebP.php
# chmod 755 /home/ryanjie/www.ryanjie.cn/wp-content/plugins/WordPress-WebP.php
```

## WebP 转换工具

### 解码库

WebP 解码库[`libwebp`](https://developers.google.com/speed/webp/docs/api)。

### 命令行工具

- [Downloads repository](https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html)
- [本站下载](https://file.ryanjie.cn/Program/webp)

> - libwebp-1.1.0-0-windows-x64.zip： Windows-x64 平台的 64 位可执行文件及库。
> - libwebp-1.1.0-linux-x86-64.tar.gz：GNU/Linux-x86_64 平台的 64 位可执行文件 x86_64 库。
> - libwebp-1.1.0-mac-10.15.tar.gz： Mac OS X 10.15 平台的 64 位可执行文件及库。

#### 使用教程

- [cwebp](https://developers.google.com/speed/webp/docs/cwebp)
- [dwebp](https://developers.google.com/speed/webp/docs/dwebp)
- [gif2webp](https://developers.google.com/speed/webp/docs/gif2webp)
- [img2webp](https://developers.google.com/speed/webp/docs/img2webp)

```bash
# convert the input file to a WebP file using a quality factor of 80
on a 0->100 scale (0 being the lowest quality, 100 being the best. Default
value is 75).
$ cwebp input.png -q 80 -o output.webp
$ cwebp -longhelp

# convert WebP file to bmp file
$ dwebp test.webp -bmp -o test.bmp
$ dwebp -h
```

## 在线工具

- [Google - Squoosh](https://squoosh.app/)
- [腾讯智图](https://zhitu.isux.us)

## 参考

- [WebP - Wikipedia](https://zh.wikipedia.org/wiki/WebP)
- [WebP - Google Developers](https://developers.google.com/speed/webp/)
- [使用 WebP 图片加速您的网站](https://www.wpdaxue.com/use-webp-pictures-to-speed-up-your-website.html)
- [WordPress 支持 WebP 格式图片上传方法](https://blog.mimvp.com/article/34702.html)

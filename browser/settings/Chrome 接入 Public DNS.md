---
title: Chrome 接入 Public DNS
url: chrome-setting-public-dns
---

# Chrome 接入 Public DNS

在使用公共 DNS 之前，我们可以先简单了解下什么是公共 DNS。

公共 DNS，是面向所有互联网用户的全球公共递归域名解析服务。DNS 能帮助用户在互联网上寻找路径，把域名转换成为网络可以识别的 IP 地址，使能够正常上网。

一般来说，未配置公共 DNS 之前，通常使用的是自动获取 DNS 方式， 也就是使用本地运营商提供的 DNS，而本地 DNS 通常缓慢且不安全，甚至部分 DNS 提供商还会出售您的隐私信息，或向您推送广告。

这时候，就需要更换一个解析速度更快，隐私保护更安全的公共 DNS（公共域名解析服务）。

## Chrome 浏览器中接入 Public DNS

步骤如下：

1. 在 chrome 浏览器地址栏中，输入 `chrome://flags/#dns-over-https` , 并回车。

2. 在打开的 Experiments 设置页中，将 **【Support for HTTPSSVC records in DNS.】** 的 `Default` 修改为 `Enabled`，然后点击 <kbd>Relaunch</kbd> 重启浏览器。

   ![chrome-dns-over-https](https://img.zxj.guru/browser/chrome-dns-over-https.jpg)

3. 在 chrome 浏览器地址栏中，输入 `chrome://settings/security` , 并回车，进入 **安全** 设置页面。

4. 在 **安全** 设置页面，开启 **【使用安全 DNS】** 并选择 **【使用自定义】**，然后填入填入 **`https://doh.pub/dns-query`**。

   ![chrome-setting-public-dns](https://img.zxj.guru/browser/chrome-setting-public-dns.jpg)

5. 退出设置页面，即可完成 Chrome 浏览器中接入 Public DNS 操作。

## 参考

- [Chrome 接入 Public DNS - DNSPod 服务与支持](https://docs.dnspod.cn/public-dns/5fb5e06362110a2b153a7837/)

---
title: 将腾讯域名的 DNS 服务器修改为华为云 DNS
date: 2020-05-05 12:18:19
categories: Website
---

<!-- more -->

<!-- TOC -->

- [将腾讯域名的 DNS 服务器修改为华为云 DNS](#将腾讯域名的-dns-服务器修改为华为云-dns)
  - [DNS 地址修改步骤](#dns-地址修改步骤)
  - [DNS 地址设置建议](#dns-地址设置建议)
  - [参考文章](#参考文章)

<!-- /TOC -->

<a id="markdown-将腾讯域名的-dns-服务器修改为华为云-dns" name="将腾讯域名的-dns-服务器修改为华为云-dns"></a>

# 将腾讯域名的 DNS 服务器修改为华为云 DNS

<a id="markdown-dns-地址修改步骤" name="dns-地址修改步骤"></a>

## DNS 地址修改步骤

1. 登录 [腾讯云域名管理控制台](https://console.cloud.tencent.com/domain/)，进入 “我的域名” 页面。

2. 选择待修改 DNS 的域名，单击【管理】。如下图所示：

   ![img](https://pic.ryanjie.cn/2020/05/huaweicloud_dns_1.png)

3. 在 “基本信息” 栏中，单击 “DNS 服务器” 的【修改】。如下图所示：

   ![img](https://pic.ryanjie.cn/2020/05/huaweicloud_dns_2.png)

4. 在弹出的 “修改 DNS 服务器” 窗口中，填写您套餐对应的 DNS 服务器地址，单击【提交】，完成修改。如下图所示：

   ![img](https://pic.ryanjie.cn/2020/05/huaweicloud_dns_3.png)

5. 设置“域名服务器”为华为云 DNS 提供的 DNS 地址。

   当前(202005)，华为云 DNS 对用户提供解析服务的新的 DNS 地址为：

   - `ns1.huaweicloud-dns.com`：中国大陆各区域 DNS 地址
   - `ns1.huaweicloud-dns.cn`：中国大陆各区域 DNS 地址
   - `ns1.huaweicloud-dns.net`：除中国大陆之外国家或地区 DNS 地址
   - `ns1.huaweicloud-dns.org`：除中国大陆之外国家或地区 DNS 地址

   华为云之前的 DNS 的地址

   - `ns1.hwcloud-dns.com`
   - `ns1.hwcloud-dns.net`

<a id="markdown-dns-地址设置建议" name="dns-地址设置建议"></a>

## DNS 地址设置建议

由于中国大陆的国际出口带宽限制，用户在中国大陆和中国大陆之外国家或地区之间跨地区访问时，会出现网络时延增大的现象。

因此，对于公网域名的 NS 记录集设置，建议您，

- 如果您的网站用户主要集中在中国大陆，设置 DNS 地址为：`ns1.huaweicloud-dns.com`、`ns1.huaweicloud-dns.cn`。
- 如果您的网站用户主要集中在中国大陆之外国家或地区，设置 DNS 地址为：`ns1.huaweicloud-dns.net`、`ns1.huaweicloud-dns.org`。
- 如果您的网站用户遍布全球，同时设置上述四个 DNS 地址。

<a id="markdown-参考文章" name="参考文章"></a>

## 参考文章

- [华为云 DNS 对用户提供域名服务的 DNS 是什么？](https://support.huaweicloud.com/dns_faq/dns_faq_012.html)
- [怎样把域名从其他服务商迁移到华为云 DNS？](http://support.huaweicloud.com/dns_faq/dns_faq_001.html)
- [修改域名 DNS 服务器](https://cloud.tencent.com/document/product/302/5518)

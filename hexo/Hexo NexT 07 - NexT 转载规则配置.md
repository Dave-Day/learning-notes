---
title: Hexo NexT 07 - NexT 转载规则配置
date: 2018-11-16 19:27:10
categories: Hexo
---

<!-- more -->

## Hexo NexT 07 - NexT 转载规则配置

> 创作共用 4.0 国际许可。
>
> 具体查看链接：<https://creativecommons.org/share-your-work/licensing-types-examples>。
>
> 许可证类型： by | by-nc | by-nc-nd | by-nc-sa | by-nd | by-sa | zero。
>
> 如果您喜欢 CC license 的翻译版本，可以设置语言值，例如 deed.zh。
>
> CC 许可证有 39 种语言，您可以在 <https://creativecommons.org> 上找到所需的语言以及它的正确缩写。

- license：许可证类型
- sidebar：侧边栏是否显示
- post：文章最后是否显示
- language：语言（中文简体：`deed.zh` 英文`deed.en` 日本語 `deed.ja` 中文繁体 `deed.zh_TW`）

```yaml
# Creative Commons 4.0 International License.
# See: https://creativecommons.org/share-your-work/licensing-types-examples
# Available values of license: by | by-nc | by-nc-nd | by-nc-sa | by-nd | by-sa | zero
# You can set a language value if you prefer a translated version of CC license, e.g. deed.zh
# CC licenses are available in 39 languages, you can find the specific and correct abbreviation you need on https://creativecommons.org
creative_commons:
  license: by-nc-sa
  sidebar: false
  post: true
  language: deed.zh
```

## 许可条件

当采用知识共享许可协议，创作者选择了一套他们希望应用到他们的工作条件。

![署名](https://pic.ryanjie.cn/images/CC_licenses/attrib.gif) **署名（通过）**

所有 CC 许可要求其他人谁使用您的作品以任何方式必须给您贷款，您请求的方式，但不是在暗示您赞同他们或他们的使用方式。如果他们想使用您的工作没有给您的信用卡或签注的目的，他们必须先得到您的许可。

![相同方式共享](https://pic.ryanjie.cn/images/CC_licenses/standard.gif) **相同方式共享（SA）**

您让其他人复制，分发，展示，执行和修改您的工作，只要他们分布在同一条款的任何修改工作。如果他们想在其他方面分发修改的作品，他们必须先得到您的许可。

![非商业性使用](https://pic.ryanjie.cn/images/CC_licenses/noncomm.gif) **非商业性使用（NC）**

您让其他人复制，分发，展示，演出，（除非您已选择 NoDerivatives）修改和使用您的工作比市场上其他任何目的，除非他们首先获得您的许可。

![禁止演绎NoDerivatives](https://pic.ryanjie.cn/images/CC_licenses/nomod.gif) **禁止演绎（ND）**

您让其他人复制，分发，展示和执行工作的唯一原件。如果他们想修改您的工作，他们必须先得到您的许可。

## 许可证类型

- [署名（CC BY）](https://creativecommons.org/share-your-work/licensing-types-examples#by)
- [署名相同方式共享（CC BY-SA）](https://creativecommons.org/share-your-work/licensing-types-examples#by-sa)
- [署名 - 禁止演绎（CC BY-ND）](https://creativecommons.org/share-your-work/licensing-types-examples#by-nd)
- [署名 - 非商业性使用（CC BY-NC）](https://creativecommons.org/share-your-work/licensing-types-examples#by-nc)
- [署名 - 非商业性使用 - 相同方式共享（CC BY-NC-SA）](https://creativecommons.org/share-your-work/licensing-types-examples#by-nc-sa)
- [署名 - 非商业性使用 - 禁止演绎（CC BY-NC-ND）](https://creativecommons.org/share-your-work/licensing-types-examples#by-nc-nd)

### ![cc](https://pic.ryanjie.cn/images/CC_licenses/cc.gif)![Attribution](https://pic.ryanjie.cn/images/CC_licenses/Attribution.gif)[署名 4.0 国际 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.zh)

这是一份普通人可以理解的[许可协议](https://creativecommons.org/licenses/by/4.0/legalcode.zh-Hans)概要 (但不是替代) 。 [免责声明](https://creativecommons.org/licenses/by/4.0/deed.zh#).

#### 您可以自由地

- **共享** — 在任何媒介以任何形式复制、发行本作品
- **演绎** — 修改、转换或以本作品为基础进行创作在任何用途下，甚至商业目的。

**只要您遵守许可协议条款，许可人就无法收回您的这些权利。**

#### 惟须遵守下列条件

- **署名** — 您必须给出[适当的署名](https://creativecommons.org/licenses/by/4.0/deed.zh#)，提供指向本许可协议的链接，同时[标明是否（对原始作品）作了修改](https://creativecommons.org/licenses/by/4.0/deed.zh#)。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。

- **没有附加限制** — 您不得适用法律术语或者 [技术措施](https://creativecommons.org/licenses/by/4.0/deed.zh#) 从而限制其他人做许可协议允许的事情。

#### 声明

- 您不必因为公共领域的作品要素而遵守许可协议，或者您的使用被可适用的 [例外或限制](https://creativecommons.org/licenses/by/4.0/deed.zh#)所允许。
- 不提供担保。许可协议可能不会给与您意图使用的所必须的所有许可。例如，其他权利比如[形象权、隐私权或人格权](https://creativecommons.org/licenses/by/4.0/deed.zh#)可能限制您如何使用作品。

### ![cc](https://pic.ryanjie.cn/images/CC_licenses/cc.gif)![Attribution](https://pic.ryanjie.cn/images/CC_licenses/Attribution.gif)![ShareAlike](https://pic.ryanjie.cn/images/CC_licenses/ShareAlike.gif)[署名-相同方式共享 4.0 国际 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.zh)

这是一份普通人可以理解的[许可协议](https://creativecommons.org/licenses/by-sa/4.0/legalcode.zh-Hans)概要 (但不是替代) 。 [免责声明](https://creativecommons.org/licenses/by-sa/4.0/deed.zh#).

#### 您可以自由地

- **共享** — 在任何媒介以任何形式复制、发行本作品
- **演绎** — 修改、转换或以本作品为基础进行创作在任何用途下，甚至商业目的。

**只要您遵守许可协议条款，许可人就无法收回您的这些权利。**

#### 惟须遵守下列条件

- **署名** — 您必须给出[适当的署名](https://creativecommons.org/licenses/by-sa/4.0/deed.zh#)，提供指向本许可协议的链接，同时[标明是否（对原始作品）作了修改](https://creativecommons.org/licenses/by-sa/4.0/deed.zh#)。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。
- **相同方式共享** — 如果您再混合、转换或者基于本作品进行创作，您必须基于[与原先许可协议相同的许可协议](https://creativecommons.org/licenses/by-sa/4.0/deed.zh#) 分发您贡献的作品。

- **没有附加限制** — 您不得适用法律术语或者 [技术措施](https://creativecommons.org/licenses/by-sa/4.0/deed.zh#) 从而限制其他人做许可协议允许的事情。

#### 声明

- 您不必因为公共领域的作品要素而遵守许可协议，或者您的使用被可适用的 [例外或限制](https://creativecommons.org/licenses/by-sa/4.0/deed.zh#)所允许。
- 不提供担保。许可协议可能不会给与您意图使用的所必须的所有许可。例如，其他权利比如[形象权、隐私权或人格权](https://creativecommons.org/licenses/by-sa/4.0/deed.zh#)可能限制您如何使用作品。

### ![cc](https://pic.ryanjie.cn/images/CC_licenses/cc.gif)![Attribution](https://pic.ryanjie.cn/images/CC_licenses/Attribution.gif)![NoDerivatives](https://pic.ryanjie.cn/images/CC_licenses/NoDerivatives.gif)[署名-禁止演绎 4.0 国际 (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/deed.zh)

这是一份普通人可以理解的[许可协议](https://creativecommons.org/licenses/by-nd/4.0/legalcode.zh-Hans)概要 (但不是替代) 。 [免责声明](https://creativecommons.org/licenses/by-nd/4.0/deed.zh#).

#### 您可以自由地

- **共享** — 在任何媒介以任何形式复制、发行本作品在任何用途下，甚至商业目的。

**只要您遵守许可协议条款，许可人就无法收回您的这些权利。**

#### 惟须遵守下列条件

- **署名** — 您必须给出[适当的署名](https://creativecommons.org/licenses/by-nd/4.0/deed.zh#)，提供指向本许可协议的链接，同时[标明是否（对原始作品）作了修改](https://creativecommons.org/licenses/by-nd/4.0/deed.zh#)。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。
- **禁止演绎** — 如果您 [再混合、转换、或者基于该作品创作](https://creativecommons.org/licenses/by-nd/4.0/deed.zh#)，您不可以分发修改作品。

- **没有附加限制** — 您不得适用法律术语或者 [技术措施](https://creativecommons.org/licenses/by-nd/4.0/deed.zh#) 从而限制其他人做许可协议允许的事情。

#### 声明

- 您不必因为公共领域的作品要素而遵守许可协议，或者您的使用被可适用的 [例外或限制](https://creativecommons.org/licenses/by-nd/4.0/deed.zh#)所允许。
- 不提供担保。许可协议可能不会给与您意图使用的所必须的所有许可。例如，其他权利比如[形象权、隐私权或人格权](https://creativecommons.org/licenses/by-nd/4.0/deed.zh#)可能限制您如何使用作品。

### ![cc](https://pic.ryanjie.cn/images/CC_licenses/cc.gif)![Attribution](https://pic.ryanjie.cn/images/CC_licenses/Attribution.gif)![NonCommercial](https://pic.ryanjie.cn/images/CC_licenses/NonCommercial.gif)[署名-非商业性使用 4.0 国际 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.zh)

这是一份普通人可以理解的[许可协议](https://creativecommons.org/licenses/by-nc/4.0/legalcode.zh-Hans)概要 (但不是替代) 。 [免责声明](https://creativecommons.org/licenses/by-nc/4.0/deed.zh#).

#### 您可以自由地

- **共享** — 在任何媒介以任何形式复制、发行本作品
- **演绎** — 修改、转换或以本作品为基础进行创作

**只要您遵守许可协议条款，许可人就无法收回您的这些权利。**

#### 惟须遵守下列条件

- **署名** — 您必须给出[适当的署名](https://creativecommons.org/licenses/by-nc/4.0/deed.zh#)，提供指向本许可协议的链接，同时[标明是否（对原始作品）作了修改](https://creativecommons.org/licenses/by-nc/4.0/deed.zh#)。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。
- **非商业性使用** — 您不得将本作品用于[商业目的](https://creativecommons.org/licenses/by-nc/4.0/deed.zh#)。

- **没有附加限制** — 您不得适用法律术语或者 [技术措施](https://creativecommons.org/licenses/by-nc/4.0/deed.zh#) 从而限制其他人做许可协议允许的事情。

#### 声明

- 您不必因为公共领域的作品要素而遵守许可协议，或者您的使用被可适用的 [例外或限制](https://creativecommons.org/licenses/by-nc/4.0/deed.zh#)所允许。
- 不提供担保。许可协议可能不会给与您意图使用的所必须的所有许可。例如，其他权利比如[形象权、隐私权或人格权](https://creativecommons.org/licenses/by-nc/4.0/deed.zh#)可能限制您如何使用作品。

### ![cc](https://pic.ryanjie.cn/images/CC_licenses/cc.gif)![Attribution](https://pic.ryanjie.cn/images/CC_licenses/Attribution.gif)![NonCommercial](https://pic.ryanjie.cn/images/CC_licenses/NonCommercial.gif)![ShareAlike](https://pic.ryanjie.cn/images/CC_licenses/ShareAlike.gif)[署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)

这是一份普通人可以理解的[许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.zh-Hans)概要 (但不是替代) 。 [免责声明](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh#).

#### 您可以自由地

- **共享** — 在任何媒介以任何形式复制、发行本作品
- **演绎** — 修改、转换或以本作品为基础进行创作

**只要您遵守许可协议条款，许可人就无法收回您的这些权利。**

#### 惟须遵守下列条件

- **署名** — 您必须给出[适当的署名](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh#)，提供指向本许可协议的链接，同时[标明是否（对原始作品）作了修改](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh#)。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。
- **非商业性使用** — 您不得将本作品用于[商业目的](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh#)。
- **相同方式共享** — 如果您再混合、转换或者基于本作品进行创作，您必须基于[与原先许可协议相同的许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh#) 分发您贡献的作品。

- **没有附加限制** — 您不得适用法律术语或者 [技术措施](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh#) 从而限制其他人做许可协议允许的事情。

#### 声明

- 您不必因为公共领域的作品要素而遵守许可协议，或者您的使用被可适用的 [例外或限制](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh#)所允许。
- 不提供担保。许可协议可能不会给与您意图使用的所必须的所有许可。例如，其他权利比如[形象权、隐私权或人格权](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh#)可能限制您如何使用作品。

### ![cc](https://pic.ryanjie.cn/images/CC_licenses/cc.gif)![Attribution](https://pic.ryanjie.cn/images/CC_licenses/Attribution.gif)![NonCommercial](https://pic.ryanjie.cn/images/CC_licenses/NonCommercial.gif)![NoDerivatives](https://pic.ryanjie.cn/images/CC_licenses/NoDerivatives.gif)[署名-非商业性使用-禁止演绎 4.0 国际 (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh)

这是一份普通人可以理解的[许可协议](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.zh-Hans)概要 (但不是替代) 。 [免责声明](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh#).

#### 您可以自由地

- **共享** — 在任何媒介以任何形式复制、发行本作品

**只要您遵守许可协议条款，许可人就无法收回您的这些权利。**

#### 惟须遵守下列条件

- **署名** — 您必须给出[适当的署名](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh#)，提供指向本许可协议的链接，同时[标明是否（对原始作品）作了修改](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh#)。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。
- **非商业性使用** — 您不得将本作品用于[商业目的](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh#)。
- **禁止演绎** — 如果您 [再混合、转换、或者基于该作品创作](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh#)，您不可以分发修改作品。

- **没有附加限制** — 您不得适用法律术语或者 [技术措施](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh#) 从而限制其他人做许可协议允许的事情。

#### 声明

- 您不必因为公共领域的作品要素而遵守许可协议，或者您的使用被可适用的 [例外或限制](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh#)所允许。
- 不提供担保。许可协议可能不会给与您意图使用的所必须的所有许可。例如，其他权利比如[形象权、隐私权或人格权](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh#)可能限制您如何使用作品。

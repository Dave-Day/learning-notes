---
title: Hexo NexT 03 - NexT 部署
date: 2018-11-12 04:38:52
categories: Hexo
---

<!-- more -->

## Hexo NexT 03 - NexT 部署

> **原文地址：<https://theme-next.org/docs/getting-started/deployment>**

## 本地部署

- 在本地修改文件。
- 本地测试： `hexo clean && hexo g && hexo s`。
- 部署： `hexo g -d`。

如果您是 macOS 用户，并且使用 `hexo-deployer-git`插件，确保`lib/`目录下没有被 Git 忽略（例如检查 `~/.gitignore_global` ）。否则可能会在部署后会丢失一些重要文件。

## 持续集成

- 直接在线编辑文件，立即生效
- 自动部署，同时部署到多个位置

### Travis CI

Travis CI 使您的团队能够自信地测试和发布您的应用程序。它为每个人、各种规模的项目和团队构建，支持超过 20 种不同的语言，包括 Javascript 和 Node.js、Ruby、PHP、Python、Mac/iOS，以及 Docker，同时让您完全控制构建环境，根据自己的需要进行定制。

#### 获取权限

有两种方法可以为 Travis CI 获取必要的权限。部署密钥具有高安全性的优点，而访问令牌具有更灵活的优点。

**访问令牌**

此方法适用于具有私有子模块的仓库

- 在博客所在的存储库中创建一个 `source` 的空分支。
- 获取访问令牌:设置—>开发人员设置—>个人访问令牌—>生成新令牌。根据实际情况设置访问权限。需要注意的是，访问令牌在这个页面上只显示一次，应该复制它，否则只能重新生成它。
- 使用 github 账号登录[Travis CI 网站](https://travis-ci.com/)。您可以在当前 github 帐户中找到仓库，选择要部署的仓库，然后单击设置。填写 github 生成的个人访问令牌，选择 Travis 需要监控仓库的分支。

**部署密钥**

Deploy key 是在 repo 中设置的 SSH 密钥，用于授予客户端对 repo 的只读（以及 r/w，如果需要的话）访问权。此方法适用于大多数公共博客存储库，并且存储库中没有私有子模块。

- 在博客所在的存储库中创建一个 `source` 的空分支。

- Generate a ssh key

  ```bash
  $ ssh-keygen -t rsa -b 4096 -C "{email}" -f ~/.ssh/deploy_key
  ```

- 在 repo 中添加部署公钥，并将其删除

  ```bash
  $ rm -f deploy_key.pub
  ```

- 使用 Travis 命令加密私钥，并将其添加到 git 中

  ```bash
  $ gem install travis
  $ travis login
  $ travis encrypt deploy_key
  $ rm -f deploy_key
  $ git add deploy_key.enc
  ```

#### 配置 .travis.yml 文件

**hexo/.travis.yml**

```yaml
dist: trusty
sudo: required

addons:
  ssh_known_hosts:
    - github.com
    - git.coding.net
  apt:
    packages:
      - nasm

env:
  global:
    - TZ=Asia/Tokyo

language: node_js
node_js: node

branches:
  only:
    - source

git:
  depth: false
  submodules: false

cache:
  apt: true
  directories:
    - node_modules

before_install:
  # Git Config
  - sed -i 's/git@github.com:/https:\/\/github.com\//' .gitmodules
  - git config --global user.name "YOUR-GITHUB-NAME"
  - git config --global user.email "YOUR-EMAIL"

  # Restore last modified time
  - 'git ls-files -z | while read -d '''' path; do touch -d "$(git log -1 --format="@%ct" "$path")" "$path"; done'

  # Submodules
  - git submodule update --recursive --remote --init

  # Deploy history
  - git clone --branch=master --single-branch YOUR-BLOG-REPO .deploy_git

  # SSH Setup
  - openssl aes-256-cbc -K $encrypted_693585a97b8c_key -iv $encrypted_693585a97b8c_iv -in deploy_key.enc -out deploy_key -d
  - eval "$(ssh-agent -s)"
  - chmod 600 ./deploy_key
  - ssh-add ./deploy_key

install: npm install

before_script:

script:
  - hexo clean
  - hexo g -d
```

### GitLab CI

GitLab 提供持续集成服务和页面服务。如果将 `.gitlab-ci.yml` 文件添加到存储库的根目录中，并将 gitlab 项目配置为使用运行器，则每次提交或推送都会触发 ci 管道。 `.gitlab-ci.yml` 文件告诉 gitlab runner 要做什么。默认情况下，它运行一个包含三个阶段的管道：构建、测试和部署。您不需要使用所有三个阶段；没有作业的阶段将被忽略。最后，您的网站将自动发布在 GitLab 主机上。

1. 将 `.gitlab-ci.yml` 添加到存储库的根目录中，并对其进行配置
   **hexo/.gitlab-ci.yml**

   ```yaml
   image: node:8.11.2

   before_script:
     # Set TimeZone, eg: Asia/Shanghai
     # - export TZ='Asia/Shanghai'
     # Restore last modified time
     - 'git ls-files -z | while read -d '''' path; do touch -d "$(git log -1 --format="@%ct" "$path")" "$path"; done'

   pages:
     stage: build
     cache:
       paths:
         - node_modules/
     script:
       - npm install hexo-cli -g
       - npm install
       # NEXT NPM installation start
       - npm install hexo-symbols-count-time
       # NEXT NPM installation end
       # NEXT External Libraries installation start
       - git clone https://github.com/theme-next/theme-next-pace themes/next/source/lib/pace
       # NEXT External Libraries installation end
       - hexo deploy
     artifacts:
       paths:
         - public
     only:
       - master
   ```

2. 将 `scaffolds`, `source`, `themes`, `.gitignor`, `.gitlab-ci.yml`, `_config.yml`, and `package.json` 上传到[Gitlab 存储库](https://gitlab.com/)。

   ```bash
   $ git init
   $ ssh -T git@gitlab.com
   $ git remote add origin YOUR-GITLAB-REPO-SSH-LINK
   $ git add .
   $ git commit -m "COMMIT MESSAGE"
   $ git push -u origin master
   ```

现在，您的静态网站可以访问 `https://yourname.gitlab.io/project` ，它类似于 GitHub。[GitLab 页面配置教程](https://gitlab.com/help/user/project/pages/index.md)。

当然，您也可以在 GitHub 页面或其他页面服务上发布静态网站。配置 `.gitlab-ci.yml`有两种方法：

#### HTTPS

- `获取访问令牌：设置 → 开发人员设置 → 个人访问令牌 → 生成新令牌`。根据实际情况设置访问权限。需要注意的是，访问令牌在此页上只显示一次，应该复制，否则只能重新生成。

- 单击 `Gitlab` 中的 `SETTINGS-CI/CD→Variables`，并将访问令牌定义为自定义变量 `GITHUB_access_token`。或者设置用于 `repo` 的用户名密码。

- 配置 `.gitlab-ci.yml`**只在文件末尾添加 deploy 阶段**
  **hexo/.gitlab-ci.yml**

  ```yaml
  github:
    stage: deploy
    script:
      - cd ./public
      - git init
      - git config --global user.name "YOUR-USER-NAME"
      - git config --global user.email "YOUR-EMAIL"
      - git add .
      - git commit -m "gitlab-auto-deploy"
      - git push --force --quiet --set-upstream https://$GITHUB_ACCESS_TOKEN@github.com/username/username.github.io.git master # replace github_access_token
    # - git config http.postBuffer 524288000
    # - git push --force --quiet --set-upstream https://$USERNAME:$PASSWORD@git.coding.net/username/reponame.git master # replace username & password, please escape the password
    only:
      - master
  ```

#### SSH

Deploy key 是在 repo 中设置的 SSH 密钥，用于授予客户端对 repo 的只读（以及 r/w，如果需要的话）访问权。此方法适用于大多数公共博客存储库，并且存储库中没有私有子模块。

- 生成部署密钥

  ```bash
  $ ssh-keygen -t rsa -b 4096 -C "{email}" -f ~/.ssh/deploy_key
  ```

- 单击 Gitlab 中的 `SETTINGS-CI/CD → Variables` ，复制私钥的内容并将其定义为自定义变量`DEPLOY_private_key`。

- 配置 `.gitlab-ci.yml` 只更新脚本 `before_script`
  **hexo/.gitlab-ci.yml**

  ```yaml
  before_script:
    # Set TimeZone, eg: Asia/Shanghai
    # - export TZ='Asia/Shanghai'

    - git config --global user.name "YOUR-USER-NAME"
    - git config --global user.email "YOUR-EMAIL"

    # Restore last modified time
    - 'git ls-files -z | while read -d '''' path; do touch -d "$(git log -1 --format="@%ct" "$path")" "$path"; done'
    # Install ssh-agent if not already installed, it is required by Docker.
    # (change apt-get to yum if you use a CentOS-based image)
    - "which ssh-agent || ( apt-get update -y && apt-get install openssh-client -y )"
    # Run ssh-agent (inside the build environment)
    - eval $(ssh-agent -s)
    # Add the SSH key stored in SSH_PRIVATE_KEY variable to the agent store
    - ssh-add <(echo "$DEPLOY_PRIVATE_KEY")
    # For Docker builds disable host key checking. Be aware that by adding that
    # you are suspectible to man-in-the-middle attacks.
    # WARNING: Use this only with the Docker executor, if you use it with shell
    # you will overwrite your user's SSH config.
    - mkdir -p ~/.ssh
    - '[[ -f /.dockerenv ]] && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config'
    # In order to properly check the server's host key, assuming you created the
    # SSH_SERVER_HOSTKEYS variable previously, uncomment the following two lines
    # instead.
    # - mkdir -p ~/.ssh
    # - '[[ -f /.dockerenv ]] && echo "$SSH_SERVER_HOSTKEYS" > ~/.ssh/known_hosts'
    # Install pandoc, eg: v1.19.2.1
    # - wget https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-1-amd64.deb
    # - dpkg -i ./pandoc-1.19.2.1-1-amd64.deb

  image: node:8.11.2

  pages:
    cache:
      paths:
        - node_modules/
    script:
      - npm install -g hexo-cli
      - npm install
      # NEXT NPM installation start
      - npm install hexo-symbols-count-time
      # NEXT NPM installation end
      # NEXT External Libraries installation start
      - git clone https://github.com/theme-next/theme-next-pace themes/next/source/lib/pace
      # NEXT External Libraries installation end
      - hexo deploy

    artifacts:
      paths:
        - public
    only:
      - master
  ```

  > 变量不会被屏蔽，如果明确要求，它们的值可以显示在作业日志中。因此，请确保 Gitlab 管道只能由您自己查看。

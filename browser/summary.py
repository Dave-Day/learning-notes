#!python
# -*- coding:utf-8 -*-

import os
import sys
import frontmatter

# file_dir = "E:\\Github\\Github\\learning-notes\\browser"
# for root, dirs, files in os.walk(file_dir):
#     print(root)  # 当前目录路径
#     print(dirs)  # 当前路径下所有子目录
#     print(files)  # 当前路径下所有非目录子文件

dir_md = sys.argv[1]
post = frontmatter.load(dir_md)
post_title = post.metadata['title']
post_url = post.metadata['url']

result = "- [" + post_title + "](" + str(post_url) + ")"

file = r'E:\Github\Github\learning-notes\browser\summary.md'
with open(file, 'a+', encoding='utf-8') as f:
    f.write(result+'\n')

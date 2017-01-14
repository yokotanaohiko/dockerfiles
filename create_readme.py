#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re


H1_match = re.compile(r'^#\ (.*)')
def create_ref(dirname):
    readme_path = dirname + '/README.md'
    if not os.path.exists(readme_path):
        return ''

    with open(readme_path) as f:
        h1_list = H1_match.findall(f.read())

    return_string = '''
##### [{header}](./{dirname})

    '''.format(
        header=h1_list[0],
        dirname=dirname
    )
    return return_string

readme_string = '''
# dockerfiles
DockerFileをまとめたもの

### 前提条件

+ dockerがインストールされている
  + [この辺り](https://docs.docker.com/engine/installation/linux/ubuntulinux/#/install-the-latest-version)を参考にインストールする

  ```
  sudo apt-get update
  sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
  sudo apt-get install docker-engine
  sudo service docker start
  ```

### 作れるもの

'''

for dirname in os.listdir('.'):
    if os.path.isdir(dirname):
        readme_string += create_ref(dirname)

with open('README.md', 'w') as f:
    f.write(readme_string)

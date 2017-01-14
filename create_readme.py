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

### 使い方

+ Ubuntu環境を作る

  ```
  make ubuntu
  ```

+ Python環境を作る

  ```
  make python
  ```

### 作れるもの

'''

for dirname in os.listdir('.'):
    if os.path.isdir(dirname):
        readme_string += create_ref(dirname)

with open('README.md', 'w') as f:
    f.write(readme_string)

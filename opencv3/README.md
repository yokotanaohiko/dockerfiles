# OpenCVの環境を構築するスクリプト

## 概要

+ ubuntuの上にOpenCV3の環境を構築する
+ [Miniconda3の環境](../miniconda3)に依存している

## 事前準備

+ OpenCVのプログラムをダウンロードし、`opencv3`以下に置く
  + [こちらから](https://github.com/opencv/opencv/releases)

  ```
  cd dockerfiles/opencv3
  wget https://github.com/opencv/opencv/archive/3.2.0.tar.gz
  ```
+ Dockerfileを書き換える
  
  ダウンロードするOpenCVのバージョンを指定する

  ```
  ENV OPENCV_VERSION 3.2.0
  ```

+ Makefileを実行する

  ```
  cd dockerfiles
  make opencv3
  ```

## 使い方

```
docker run --user pythonbase -it opencv /bin/bash --login
```

+ pythonbaseというユーザーでログインすると、opencvが使える状態になっている
+ docker imageの名前は、`opencv`となる
+ ログイン後下記のコマンドでOpenCVが使えることを確認できる

  ```
  python -c 'import cv2'
  ```

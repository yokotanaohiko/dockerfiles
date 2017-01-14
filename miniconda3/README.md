# Pythonの環境を構築する

## 概要

+ pyenvを使ってminiconda3の環境を構築する
+ [ubuntu](../ubuntu)に依存している

## 作り方

```
cd dockerfiles/miniconda3
docker build -t pythonbase .
```

## 動作確認

```
docker run --user pythonbase -it pythonbase /bin/bash --login
```

+ ログイン後下記のコマンドでpythonがインストールされていることを確認する

```
python --version
```

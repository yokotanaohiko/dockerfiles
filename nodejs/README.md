# Node.jsの環境を構築する

## 概要

+ ubuntu 16.04の上にnpmコマンドを打てる環境を構築する

## 作り方

```
cd nodejs
docker build -t nodejs .
```

## 動作確認

```
docker run --user ubuntubase -it opencv /bin/bash --login
```

+ ログイン後下記のコマンドを実行し、npmコマンドが打てるかを確認する

```
npm --version
```

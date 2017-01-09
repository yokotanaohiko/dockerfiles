# 必要最小限のコマンドが入った Ubuntu16.04を作る

FROM ubuntu:16.04

USER root
RUN apt-get update 
RUN apt-get -y install \
    bzip2 \
    git  \
    curl \
    wget  \
    tmux  \
    vim  \
    net-tools \
    make \
    cmake \
    libtool \
    autoconf \
    automake \
    unzip \
    g++ \
    sudo

RUN useradd -m ubuntubase && echo "ubuntubase:ubuntubase" | chpasswd && adduser ubuntubase sudo

USER ubuntubase
CMD /bin/bash

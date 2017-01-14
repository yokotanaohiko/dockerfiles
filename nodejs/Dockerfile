# Node.jsの環境構築

FROM ubuntubase

USER root
RUN apt-get update 
RUN apt-get -y install \
    sudo  \
    git  \
    wget  \
    tmux  \
    vim  \
    bzip2  \
    net-tools \
    npm
ENV USERNAME nodejsbase
RUN useradd -m $USERNAME && echo "$USERNAME:$USERNAME" | chpasswd && adduser $USERNAME sudo
USER $USERNAME

WORKDIR /home/$USERNAME

CMD /bin/bash

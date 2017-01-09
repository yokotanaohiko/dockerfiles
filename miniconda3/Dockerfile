# Miniconda3を使ったPythonの最低限の環境

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
    net-tools
ENV USERNAME pythonbase
RUN useradd -m $USERNAME && echo "$USERNAME:$USERNAME" | chpasswd && adduser $USERNAME sudo
USER $USERNAME

WORKDIR /home/$USERNAME
RUN git clone https://github.com/yyuu/pyenv.git /home/$USERNAME/.pyenv
COPY bash_profile /home/$USERNAME/.bash_profile

ENV PYENV_ROOT /home/$USERNAME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN eval "$(pyenv init -)"
RUN pyenv install miniconda3-latest
RUN pyenv global miniconda3-latest
RUN pyenv rehash

CMD /bin/bash

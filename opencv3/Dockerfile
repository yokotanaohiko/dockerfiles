FROM pythonbase

ENV USERNAME pythonbase

RUN /home/$USERNAME/.pyenv/shims/pip install numpy

USER root
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /tmp/
ENV OPENCV_VERSION 3.2.0
COPY $OPENCV_VERSION.tar.gz ./
RUN tar zxf $OPENCV_VERSION.tar.gz

WORKDIR /tmp/opencv-$OPENCV_VERSION/build
COPY run_make.sh ./
RUN sh run_make.sh pythonbase
RUN make
RUN make install
RUN cp /usr/local/lib/python3.5/site-packages/cv2.*.so /home/pythonbase/.pyenv/versions/miniconda3-latest/lib/python3.5/site-packages/

CMD /bin/bash

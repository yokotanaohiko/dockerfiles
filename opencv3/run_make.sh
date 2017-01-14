USER=$1

cmake \
-D CMAKE_BUILD_TYPE=RELEASE \
-DBUILD_opencv_python3=ON \
-DWITH_V4L=OFF \
-DWITH_FFMPEG=OFF \
-DWITH_VTK=OFF \
-DPYTHON3_EXECUTABLE=/home/$USER/.pyenv/shims/python \
-DPYTHON3_LIBRARIES=/home/$USER/.pyenv/versions/miniconda3-latest/lib/python3.5/site-packages \
-DPYTHON3_INCLUDE_PATH=/home/$USER/.pyenv/versions/miniconda3-latest/include/python3.5m \
-DPYTHON3_NUMPY_INCLUDE_DIRS=/home/$USER/.pyenv/versions/miniconda3-latest/lib/python3.5/site-packages/numpy/core/include \
..

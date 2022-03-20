# docker build .
# docker run --rm -ti <image no> 

FROM tensorflow/tensorflow 
# COPY requirements.txt ./
COPY ../pyImageSort ./

# RUN apt update && apt upgrade -y && apt nasm -y && apt gdb -y
RUN apt update && apt upgrade -y 
RUN python -m pip install --upgrade pip
RUN pip install scikit-learn
RUN pip install pytesseract 

# RUN useradd tf -g docker && echo tf | passwd tf --stdin 
RUN useradd -rm -d /home/tf -s /bin/bash -g docker -G sudo -u 1001 -p tf tf
USER tf
WORKDIR /home/tf

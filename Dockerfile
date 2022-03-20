FROM alpine
COPY . /usr/src
RUN apk add nano gcc nasm gdb
RUN apk add python3 py3-pip
# RUN pip install scikit-learn
# RUN pip install pytesseract

RUN useradd -rm -d /home/alp -s /bin/bash -G sudo -u 1001 alp 
USER alp
WORKDIR /home/alp

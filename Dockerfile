FROM alpine
COPY . /usr/src
RUN apk update && apk add nano gcc nasm gdb

FROM ubuntu:18.04

# lib32z1
RUN apt update 
RUN apt install -y apt-utils xinetd

RUN useradd -m mazerunner
WORKDIR /home/mazerunner
RUN cp -R /lib* /home/mazerunner && \
    cp -R /usr/lib* /home/mazerunner
RUN mkdir /home/mazerunner/dev && \
    mknod /home/mazerunner/dev/null c 1 3 && \
    mknod /home/mazerunner/dev/zero c 1 5 && \
    mknod /home/mazerunner/dev/random c 1 8 && \
    mknod /home/mazerunner/dev/urandom c 1 9 && \
    chmod 666 /home/mazerunner/dev/*
RUN mkdir /home/mazerunner/bin && \
    cp /bin/sh /home/mazerunner/bin && \
    cp /bin/ls /home/mazerunner/bin && \
    cp /bin/cat /home/mazerunner/bin

COPY ./mazerunner.xinetd /etc/xinetd.d/mazerunner
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

COPY ./grabnpwn /home/mazerunner/
COPY ./flag.txt /home/mazerunner
RUN chown -R root:mazerunner /home/mazerunner && \
    chmod -R 750 /home/mazerunner && \
    chmod 740 /home/mazerunner/flag.txt
COPY ./banner.txt /etc/banner.txt
CMD ["/start.sh"]
EXPOSE 2000

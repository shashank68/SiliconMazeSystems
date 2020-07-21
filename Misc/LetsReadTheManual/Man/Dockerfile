FROM ubuntu:18.04

RUN apt update 
RUN apt install -y openssh-server less
RUN mkdir /var/run/sshd
WORKDIR /home/ctfroot
RUN cp -R /lib* /home/ctfroot && \
    cp -R /usr/lib* /home/ctfroot
RUN mkdir /home/ctfroot/dev && \
    mknod /home/ctfroot/dev/null c 1 3 && \
    mknod /home/ctfroot/dev/zero c 1 5 && \
    mknod /home/ctfroot/dev/random c 1 8 && \
    mknod /home/ctfroot/dev/urandom c 1 9 && \
    chmod 666 /home/ctfroot/dev/*
RUN mkdir /home/ctfroot/etc && \
    cp -vf /etc/passwd /home/ctfroot/etc/ && \
    cp -vf /etc/group /home/ctfroot/etc/
RUN mkdir /home/ctfroot/bin && mkdir -p /home/ctfroot/usr/bin && \
    cp /bin/sh /home/ctfroot/bin && \
    cp /bin/ls /home/ctfroot/bin && \
    cp /bin/echo /home/ctfroot/bin && \
    cp /usr/bin/less /home/ctfroot/usr/bin
RUN mkdir -p /home/ctfroot/home/mazerunner
RUN useradd -d /home/mazerunner mazerunner

RUN echo "mazerunner:please" | chpasswd
RUN echo "alias sh='echo We dont do that here'" > /home/ctfroot/home/mazerunner/.profile
RUN echo "less manner; exit" >> /home/ctfroot/home/mazerunner/.profile
COPY ./sshd_config /etc/ssh/sshd_config

COPY ./manner /home/ctfroot/home/mazerunner
COPY ./flag.txt /home/ctfroot/home/mazerunner

RUN chown -R root:mazerunner /home/ctfroot && \
    chmod -R 750 /home/ctfroot && \
    chmod 740 /home/ctfroot/home/mazerunner/flag.txt

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D", "-e"]

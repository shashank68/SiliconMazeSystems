FROM sickp/alpine-sshd:latest
RUN apk add less
RUN passwd -d root
RUN adduser -D -s /bin/sh maz3
RUN printf "pleasereadtheManual12\npleasereadtheManual12" | passwd maz3
RUN echo "HELLO READER" > /etc/motd
RUN echo "less manner && exit" > /home/maz3/.profile
# RUN chown -R maz3:maz3 /home/maz3
RUN chown -R root:root /home/maz3
RUN chmod 744 /home/maz3/.profile
COPY rootfs/flag.txt /home/maz3/
COPY rootfs/manner /home/maz3/
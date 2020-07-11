FROM python:2-slim

RUN useradd -p abc12 -s /bin/sh ctfuser
RUN echo "ctfuser:abc12" | chpasswd

RUN apt update && apt install ucspi-tcp

RUN chmod 500 /
WORKDIR /app
COPY files/flag.txt .
COPY files/Snaky.py /bin/
RUN chmod 705 . && chmod 444 flag.txt

ENTRYPOINT tcpserver -t 0 0.0.0.0 3000 python /bin/Snaky.py
USER ctfuser
# ENTRYPOINT sh

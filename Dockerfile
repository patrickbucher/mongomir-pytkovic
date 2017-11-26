FROM debian:jessie-slim
MAINTAINER Patrick Bucher "patrick.bucher@stud.hslu.ch"

ENV BINDIR /home/developer/bin
ENV DATADIR /home/developer/data
ENV APPDIR /home/developer/webapp
ENV LOGDIR /home/developer/log

COPY config/apt.conf /etc/apt/apt.conf

RUN apt-get update && apt-get install -y wget curl mongodb sqlite3 python3 python3-pip 
RUN pip3 install falcon gunicorn pymongo sqlite3client
RUN useradd -m developer

RUN mkdir -p $APPDIR && mkdir -p $DATADIR && mkdir -p $LOGDIR && mkdir -p $BINDIR
COPY data/database.sqlite.gz $DATADIR/
RUN gunzip $DATADIR/database.sqlite.gz
COPY python/*.py $APPDIR/
COPY bin/*.sh $BINDIR/
RUN chown -R developer:developer $APPDIR $DATADIR $LOGDIR $BINDIR
RUN chmod +x $BINDIR/*.sh

USER developer

EXPOSE 8000
CMD ["/home/developer/bin/server-start.sh"]

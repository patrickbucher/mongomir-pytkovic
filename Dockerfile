FROM debian:jessie-slim
MAINTAINER Patrick Bucher "patrick.bucher@stud.hslu.ch"

ENV BINDIR /home/developer/bin
ENV DATADIR /home/developer/data
ENV APPDIR /home/developer/webapp
ENV LOGDIR /home/developer/log

COPY config/apt.conf /etc/apt/apt.conf

RUN apt-get update && apt-get install -y wget curl mongodb sqlite3 python3 python3-pip 
RUN pip3 install falcon gunicorn
RUN useradd -m developer

RUN mkdir -p $APPDIR && mkdir -p $DATADIR && mkdir -p $LOGDIR && mkdir -p $BINDIR
COPY python/*.py $APPDIR/
COPY config/server-start.sh $BINDIR/
RUN chown -R developer:developer $APPDIR $DATADIR $LOGDIR $BINDIR
RUN chmod +x $BINDIR/server-start.sh
COPY data/database.sqlite.gz $DATADIR/

USER developer

EXPOSE 8000
CMD ["/home/developer/bin/server-start.sh"]

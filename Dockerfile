FROM debian:jessie-slim
MAINTAINER Patrick Bucher "patrick.bucher@stud.hslu.ch"

ENV BINDIR /home/developer/bin
ENV DATDIR /home/developer/data
ENV APPDIR /home/developer/webapp
ENV LOGDIR /home/developer/log
ENV MIGDIR /home/developer/migration

COPY config/apt.conf /etc/apt/apt.conf
COPY config/.vimrc /home/developer/

RUN apt-get update && apt-get install -y wget curl mongodb sqlite3 python3 python3-pip webfs vim
RUN pip3 install falcon gunicorn pymongo sqlite3client
RUN useradd -m developer

RUN mkdir -p $APPDIR && mkdir -p $DATDIR && mkdir -p $LOGDIR && mkdir -p $BINDIR
COPY data/database.sqlite.gz $DATDIR/
RUN gunzip $DATDIR/database.sqlite
COPY bin/*.sh $BINDIR/
COPY migration/migration.py $MIGDIR/migration.py
RUN chmod +x $MIGDIR/migration.py
RUN chown -R developer:developer /home/developer
RUN chmod +x $BINDIR/*.sh
COPY webapp $APPDIR

USER developer

EXPOSE 8000 8001
CMD ["/home/developer/bin/server-start.sh"]

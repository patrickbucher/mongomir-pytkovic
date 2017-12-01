#!/bin/sh

SERVER_LOG="$LOGDIR/webfsd.out"

$BINDIR/mongo-start.sh &
$BINDIR/gunicorn-start.sh &
webfsd -p 8001 -r $APPDIR -l "$SERVER_LOG" -j -f index.html

while [ ! -f "$SERVER_LOG" ] ;
do
    sleep 1
done

tail -f "$SERVER_LOG"

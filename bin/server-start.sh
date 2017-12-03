#!/bin/sh

SERVER_LOG="$LOGDIR/nginx-error.log"

$BINDIR/mongo-start.sh &
$BINDIR/gunicorn-start.sh &
nginx

while [ ! -f "$SERVER_LOG" ] ;
do
    sleep 1
done

tail -f "$SERVER_LOG"

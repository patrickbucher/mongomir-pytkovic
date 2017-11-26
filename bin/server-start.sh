#!/bin/sh

$BINDIR/mongo-start.sh &
$BINDIR/gunicorn-start.sh &

SERVER_LOG="$LOGDIR/falcon.out"

while [ ! -f "$SERVER_LOG" ] ;
do
    sleep 1
done

tail -f "$SERVER_LOG"

#!/bin/sh

$BINDIR/mongo-start.sh &
$BINDIR/gunicorn-start.sh &

LOGFILE="$LOGDIR/falcon.log"

while [ ! -f "$LOGFILE" ] ;
do
    sleep 1
done

tail -f "$LOGFILE"

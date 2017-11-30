#!/bin/sh

$BINDIR/mongo-start.sh &
$BINDIR/migration.sh
$BINDIR/gunicorn-start.sh &

LOGFILE="$LOGDIR/gunicorn.out"

while [ ! -f "$LOGFILE" ]
do
    sleep 1
done

tail -f "$LOGFILE"

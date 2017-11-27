#!/bin/sh

$BINDIR/mongo-start.sh &
$BINDIR/migration.sh
$BINDIR/gunicorn-start.sh &

tail -f $LOGDIR/gunicorn.out

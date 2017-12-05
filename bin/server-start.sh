#!/bin/sh

$BINDIR/mongo-start.sh &
$BINDIR/gunicorn-start.sh &
nginx

touch "$LOGDIR/gunicorn.out"
touch "$LOGDIR/gunicorn.err"
touch "$LOGDIR/falcon.out"
touch "$LOGDIR/mongo.out"
touch "$LOGDIR/mongo.err"
touch "$LOGDIR/nginx-error.log"
touch "$LOGDIR/nginx-access.log"

eval "$BINDIR/tailall.sh $LOGDIR/*"

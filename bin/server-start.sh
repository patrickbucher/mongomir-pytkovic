#!/bin/sh

$BINDIR/mongo-start.sh &
$BINDIR/gunicorn-start.sh &
nginx

touch "$LOGDIR/gunicorn.out" "$LOGDIR/gunicorn.err" "$LOGDIR/falcon.out" "$LOGDIR/mongo.out" "$LOGDIR/mongo.err" "$LOGDIR/nginx-error.log" "$LOGDIR/nginx-access.log"

tail -f "$LOGDIR/gunicorn.out" -f "$LOGDIR/gunicorn.err" -f "$LOGDIR/falcon.out" -f "$LOGDIR/mongo.out" -f "$LOGDIR/mongo.err" -f "$LOGDIR/nginx-error.log" -f "$LOGDIR/nginx-access.log"

#!/bin/sh

cd $APPDIR
gunicorn -b 0.0.0.0:8000 sample:api >$LOGDIR/out.log 2>$LOGDIR/err.log

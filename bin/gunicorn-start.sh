#!/bin/sh

cd $APPDIR
gunicorn -b 0.0.0.0:8000 sample:api >$LOGDIR/gunicorn.out 2>$LOGDIR/gunicorn.err

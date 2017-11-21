#/usr/bin/sh

cd $APPDIR
gunicorn sample:api >$LOGDIR/out.log 2>$LOGDIR/err.log

#!/bin/sh

/usr/bin/mongod --dbapth $DATADIR >$LOGDIR/mongo.out 2>$LOGDIR/mongo.err

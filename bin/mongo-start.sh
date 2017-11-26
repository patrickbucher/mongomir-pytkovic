#!/bin/sh

/usr/bin/mongod --dbapth $DATDIR >$LOGDIR/mongo.out 2>$LOGDIR/mongo.err

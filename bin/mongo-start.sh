#!/bin/sh

mkdir -p $DATDIR/.mongo
/usr/bin/mongod --port 27017 --dbpath $DATDIR/.mongo >$LOGDIR/mongo.out 2>$LOGDIR/mongo.err

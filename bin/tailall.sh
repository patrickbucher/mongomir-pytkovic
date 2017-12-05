#!/bin/sh

ARGS=''
shift # ignore first argument
while [ "$#" -gt 0 ]; do
    if [ -f "$1" ]; then
        ARGS="$ARGS -f $1"
        shift
    fi
done
if [ -z "$ARGS" ]; then
    exit
fi
eval "tail$ARGS"

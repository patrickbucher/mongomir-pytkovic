#!/bin/sh

$BINDIR/mongo-start.sh &
$MIGDIR/migration.py

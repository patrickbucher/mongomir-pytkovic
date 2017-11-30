# Mongomir Pytkovic

DBS project using MongoDB, Python and the [European Soccer Database](https://www.kaggle.com/hugomathien/soccer) from Kaggle.

Just run `make server` and visit [http://localhost:8000/match](http://localhost:8000/match). (Mac users need to set up port forwarding to their docker machine.)

## Docker

Build the image:

    make build

Run the image (interactive bash session):

    make run

Perform the migration:

    make migration

Run the image (as a web server, this will build the image and perform the
migration, if necessary):

    make server

Remove _all_ Docker containers:

    make clean

Remove _all_ Docker images:

    make purge

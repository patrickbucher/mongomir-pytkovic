# Mongomir Pytkovic

**Mac users are required to switch to the `mac` branch!**

DBS project using MongoDB, Python and the [European Soccer Database](https://www.kaggle.com/hugomathien/soccer) from Kaggle.

Just run `make server` and visit [http://192.168.99.100:8000/match](http://192.168.99.100:8000/match) (the IP address might be different, run `docker-machine ip` to find it out).

## Docker

Build the image:

    make build

Run the image (interactive bash session):

    make run

Run the image (as a web server, this will build the image and perform the
migration, if necessary):

    make server

Remove _all_ Docker containers:

    make clean

Remove _all_ Docker images:

    make purge

# Mongomir Pytkovic

DBS project using MongoDB, Python and the [European Soccer Database](https://www.kaggle.com/hugomathien/soccer) from Kaggle.

Just run `make server` and visit [http://localhost:8001/](http://localhost:8001/match). (Mac users need to set up port forwarding to their docker machine.)

**Important:** Because the usage of two different ports (8000 for the REST API and 8001 for the static web content), it violates the [Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy).  For Testing, a plugin needs to be run and activated ([CORS Everywhere (Firefox)](https://addons.mozilla.org/de/firefox/addon/cors-everywhere/) or [CORS Toggle (Chrome)](https://chrome.google.com/webstore/detail/cors-toggle/jioikioepegflmdnbocfhgmpmopmjkim), for example).

## Docker

Build the image:

    make build

Run the image (interactive bash session):

    make run

Run the image (as root):

    make rootrun

Perform the migration:

    make migration

Run the image (as a web server, this will build the image and perform the
migration, if necessary):

    make server

Remove _all_ Docker containers:

    make clean

Remove _all_ Docker images:

    make purge

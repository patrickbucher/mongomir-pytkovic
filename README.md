# Mongomir Pytkovic

DBS project using MongoDB, Python and the [European Soccer Database](https://www.kaggle.com/hugomathien/soccer) from Kaggle.

## Docker

Build the image:

    docker build -t mongomir .

Run the image (interactive session):

    docker run -it mongomir bash

Run the image (as a web server):

    docker run -d -p 8000:8000 mongomir

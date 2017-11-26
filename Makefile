build:
	docker build -t mongomir .

run:
	docker run -it --name mongomir -v "`pwd`"/migration:/home/developer/migration --rm mongomir bash

server:
	docker run -it --name mongomir -p 8000:8000 --rm mongomir

clean:
	docker rm -f `docker ps -qa --filter name=mongomir`

purge:
	docker rmi -f `docker images -qa`

.built build:
	docker build -t mongomir .
	gunzip -f -k data/database.sqlite.gz
	touch .built
	rm -f .ran

.ran run: .built
	docker run -it --name mongomir --rm mongomir bash
	touch .ran

server: .built
	docker run -it --name mongomir -p 8000:8000 --rm mongomir

clean:
	rm -f .ran 
	docker rm -f `docker ps -qa`

purge:
	rm -f data/database.sqlite
	rm -f .built .ran
	docker rmi -f `docker images -qa`

.built build:
	docker build -t mongomir .
	gunzip -f -k data/database.sqlite.gz
	touch .built
	rm -f .ran .migrated

.ran run: .built
	docker run -it --name mongomir --rm mongomir bash
	touch .ran

.ran rootrun: .built
	docker run -it --name mongomir -u root --rm mongomir bash
	touch .ran

.migrated migration: .built
	docker run -td --name mongomir -p 8000:8000 --rm mongomir
	docker exec mongomir /home/developer/bin/migration.sh
	docker commit mongomir mongomir
	docker stop mongomir
	touch .migrated

server: .built .migrated
	docker run -it --name mongomir -p 8000:8000 --rm mongomir

clean:
	rm -f .ran .migrated
	docker rm -f `docker ps -qa`

purge:
	rm -f data/database.sqlite
	rm -f .built .ran .migrated
	docker rmi -f `docker images -qa`

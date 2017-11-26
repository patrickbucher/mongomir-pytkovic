.built build:
	docker build -t mongomir .
	gunzip -f -k data/database.sqlite.gz
	touch .built
	rm -rf .migrated .ran

.ran run: .built
	docker run -it --name mongomir -v "`pwd`"/data:/home/developer/data --rm mongomir bash
	touch .ran

.migrated migration: .built
	docker run -it --name mongomir -v "`pwd`"/data:/home/developer/data --rm mongomir /home/developer/bin/migration.sh
	touch .migrated

server: .built .migrated
	docker run -it --name mongomir -v "`pwd`"/data:/home/developer/data -p 8000:8000 --rm mongomir

clean:
	docker rm -f `docker ps -qa`
	rm -f .ran .migrated

purge: .built
	docker rmi -f `docker images -qa`
	rm -f data/sqlite.database
	rm -f .built .migrated .ran
	rm -rf data/.mongo

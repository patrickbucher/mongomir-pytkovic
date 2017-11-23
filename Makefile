build:
	docker build -t mongomir .

run:
	docker run -it mongomir bash

server:
	docker run -d -p 8000:8000 mongomir


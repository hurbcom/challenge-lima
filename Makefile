run:
	sudo docker build --no-cache -t challenge-echo .
	clear
	sudo docker run -it challenge-echo bash

run-test:
	docker run challenge-echo npm test
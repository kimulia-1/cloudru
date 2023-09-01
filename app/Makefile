D = docker
all: init

init:
	$(D) build -t app:v1.0 .
	$(D) run -d -p 8000:8000 --name my_cont app:v1.0

delete:
	$(D) stop my_cont
	$(D) rm my_cont
	$(D) rmi app:v1.0
	$(D) ps -a
	$(D) images

refresh: delete init
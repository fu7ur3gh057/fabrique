.PHONY: help start clean logs

include .env
export 
DOCKER_PROJECT = ${PROJECT_NAME}

help:
	@echo "Available targets:"
	@echo "help	-	show this help message"
	@echo "start	-	Build  Docker Compose Services"
	@echo "clean	-	Stop and remove all Docker Compose resources"
	@echo "logs	-	Get last 100 logs"

start:
	docker compose -f docker-compose.yml up -d --build


#clean:
#	docker compose -f docker-compose.yml down --volumes  --rmi all

clean:
	docker compose -f docker-compose.yml down --volumes

logs:
	docker compose -f docker-compose.yml logs --tail=100
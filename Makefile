
deploy:
	eval $(docker-machine env recipevm) && \
	docker-compose -f docker-compose-prod.yml up --build

deploy-local:
	eval $(docker-machine env -u) && \
	docker-compose -f docker-compose-prod.yml up --build

build-dev:
	docker-compose up --build

dev:
	docker-compose up


deploy:
	eval $(docker-machine env recipevm) && \
	docker-compose -f docker-compose-prod.yml up --build

deploy-local:
	eval $(docker-machine env -u) && \
	docker-compose -f docker-compose-prod.yml up --build

build-dev:
	docker-compose up --build

test:
	docker-compose up --build -d && docker-compose run web make test && docker-compose down

dev:
	docker-compose up

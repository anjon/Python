install:
	# Install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	# Format Code
	black *.py mylib/*.py oop/*.py
lint:
	# flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py oop/*.py
test:
	# test
	python -m pytest -vv --cov=mylib --cov=main test_*.py 
build:
	# build containers
	docker build -t deploy-fastapi .
run:
	# Run docker
	#docker run -p 127.0.0.1:8080:8080 deploy-fastapi
deploy:
	# deploy 
all: install lint test deploy 
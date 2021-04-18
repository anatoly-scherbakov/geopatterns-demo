TF_VERSION := 0.14.9

PLATFORM := $(shell uname -s | tr A-Z a-z)
ARCH := $(shell uname -m | sed 's/x86_64/amd64/' | sed -e 's/i[3,6]86/386/')

DIR := geopatterns_demo

# Name of Terraform executable file
TF := terraform-$(TF_VERSION)

ifeq ($(TF_AUTO_APPROVE), true)
tf_flags := -auto-approve
endif


.ONESHELL:
.SHELLFLAGS = -ce
infrastructure/$(TF):
	# Download Terraform executable file for the specified version.
	curl -f https://releases.hashicorp.com/terraform/$(TF_VERSION)/terraform_$(TF_VERSION)_$(PLATFORM)_$(ARCH).zip -o /tmp/terraform.zip
	unzip -p /tmp/terraform.zip terraform > ./infrastructure/$(TF)
	rm -f /tmp/terraform.zip
	chmod +x ./infrastructure/$(TF)


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: infrastructure
infrastructure: ./infrastructure/$(TF) layer/${DIR}_lambda_layer.zip
	# Deploy infrastructure to the cloud.
	# Terraform will ask to confirm changes and you will have to answer `yes` to deploy. You can look in Terraform docs how to suppress questions.
	echo TF_AUTO_APPROVE = $(TF_AUTO_APPROVE)
	cd infrastructure/
	./$(TF) init
	./$(TF) apply $(tf_flags)


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: plan
plan: ./infrastructure/$(TF)
	cd infrastructure/
	./$(TF) init
	./$(TF) plan


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: build
build:
	# To run Lambda, we have to build a ZIP archive with our code plus all dependencies in it.
	# Unfortunately, Poetry cannot do that out of the box yet. The workaround was adapted from:
	#     https://github.com/python-poetry/poetry/issues/1937
	mkdir -p build
	rm -rf build/*
	poetry export -f requirements.txt --without-hashes | pip install -r /dev/stdin -t build/
	cp -rf ${DIR} build/


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: deploy
deploy: build infrastructure
	@echo "Deployment complete."


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: lint
lint:
	mypy --ignore-missing-imports ${DIR}
	flakehell lint ${DIR}


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: format
format:
	isort ${DIR}
	cd infrastructure
	./$(TF) fmt


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: serve_api
serve_api:
	python -m uvicorn --port 8080 ${DIR}.api:api


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: serve_api
serve:
	mkdocs serve -a localhost:8081


.ONESHELL:
.SHELLFLAGS = -ce
layer/${DIR}_lambda_layer.zip: layer/Dockerfile
	cd layer
	docker build -t ${DIR} .

	# Create an instance of the image (without actually running it)
	# this is just so we can copy the zip file out
	docker create --name ${DIR} ${DIR} echo
	docker cp ${DIR}:/opt/${DIR}_lambda_layer.zip .
	docker rm ${DIR}


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: test
test: lint
	echo "Testing complete."

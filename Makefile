TF_VERSION := 0.14.9

PLATFORM := $(shell uname -s | tr A-Z a-z)
ARCH := $(shell uname -m | sed 's/x86_64/amd64/' | sed -e 's/i[3,6]86/386/')

# Name of Terraform executable file
TF := terraform-$(TF_VERSION)


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
infrastructure: ./infrastructure/$(TF)
	# Deploy infrastructure to the cloud.
	# Terraform will ask to confirm changes and you will have to answer `yes` to deploy. You can look in Terraform docs how to suppress questions.
	cd infrastructure/
	./$(TF) init
	./$(TF) apply


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


.ONESHELL:
.SHELLFLAGS = -ce
.PHONY: deploy
deploy: build infrastructure
	@echo "Deployment complete."

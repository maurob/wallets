image := wallets
linting_image := ghcr.io/karpatkey/pylint310
path := src
linting_paths := src # or more space-separated paths
repo_dir := $(shell git rev-parse --show-toplevel)
docker_base_run := docker run --rm -i -v $(PWD):/repo
docker_root_run := $(docker_base_run) -e USER=root
docker_run := $(docker_base_run) -e USER=$(USER) --user $$(id -u):$$(id -g)


# Git tools

.PHONY: install-pre-commit
install-pre-commit:
	@cp $(repo_dir)/.pre-commit $(repo_dir)/.git/hooks/pre-commit
	@echo "The pre-commit hook has been installed."


# Personal docker environment (Dockerfile required)

.PHONY: build
build:
	@docker build -t $(image) .


.PHONY: build-if-no-image
build-if-no-image:
	@docker inspect --type=image $(image) > /dev/null || docker build -t $(image) .


.PHONY: rootshell
rootshell: build-if-no-image
	@$(docker_root_run) -t $(image) bash


.PHONY: shell
shell: build-if-no-image
	@$(docker_run) -t $(image) bash


.PHONY: test
test: build-if-no-image
	@$(docker_run) $(image) pytest -v $(path)


# External docker image for linting

.PHONY: lint
lint:
	@$(docker_run) $(linting_image) $(linting_paths)
	@echo "Linter rules [OK]"


.PHONY: lint-shell
lint-shell:
	@$(docker_run) -t --entrypoint bash $(linting_image)


.PHONY: pretty
pretty:
	@$(docker_run) --entrypoint /pretty.sh $(linting_image) $(linting_paths)

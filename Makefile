linting_image := ghcr.io/karpatkey/pylint310
linting_paths := src # or more space-separated paths
repo_dir := $(shell git rev-parse --show-toplevel)
docker_base_run := docker run --rm -i -v $(PWD):/repo
docker_run := $(docker_base_run) -e USER=$(USER) --user $$(id -u):$$(id -g)


# Git tools

.PHONY: install-pre-commit
install-pre-commit:
	@cp $(repo_dir)/.pre-commit $(repo_dir)/.git/hooks/pre-commit
	@echo "The pre-commit hook has been installed."


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

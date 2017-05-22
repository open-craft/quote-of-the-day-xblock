.DEFAULT_GOAL := dev.run

.PHONY: dev.clean dev.build dev.run

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  help                       display this help message"
	@echo "  dev.clean                  clean up docker development container and image"
	@echo "  dev.build                  rebuild docker image"
	@echo "  dev.run                    run the XBlock in the XBlock workbench"
	@echo "  dev.update                 compile dependency files"
	@echo "  dev.requirements           setup dependencies"
	@echo ""

dev.clean:
	-docker rm xblock-quote-of-the-day-dev
	-docker rmi xblock-quote-of-the-day-dev

dev.build:
	docker build -t xblock-quote-of-the-day-dev $(CURDIR)

dev.run: dev.clean dev.build
	docker run -p 8000:8000 -v $(CURDIR):/usr/local/src/xblock-quote-of-the-day --name xblock-quote-of-the-day-dev xblock-quote-of-the-day-dev

dev.update:
	pip install -q pip-tools
	pip-compile --upgrade -o requirements/base.txt requirements/base.in
	pip-compile --upgrade -o requirements/dev.txt requirements/dev.in
	pip-compile --upgrade -o requirements/test.txt requirements/test.in

dev.requirements:
	pip-sync requirements/base.txt requirements/dev.txt requirements/private.* requirements/test.txt

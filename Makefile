# JSONdb
# Create databases using JSON files
# Github: https://www.github.com/0x4248/JSONdb
# Licence: GNU General Public License v3.0
# By: 0x4248

# Commands
MVN = mvn
PYTHON = python3

# Paths
SCRIPTS = scripts
CLEANUP = build/ target/ src/python/JSONdb.egg-info demo.json demo.csv

all: build

build: build-jar build-python

clean:
	@echo "Cleaning up..."
	@rm -rf $(CLEANUP)
	@echo "Done."

test-csv:
	@bash scripts/test_csv.sh

build-jar:
	@echo "Building JAR..."
	@mvn clean package
	@echo "Done."

build-python:
	@echo "Building Python package..."
	@$(PYTHON) -m build
	@echo "Done."
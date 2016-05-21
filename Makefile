PYTHON ?= python
.PHONY: run test clean
run:
	$(PYTHON) -m core.run

clean:
	find . -name "*.pyc" -delete

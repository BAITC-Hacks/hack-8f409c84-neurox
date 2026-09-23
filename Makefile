PYTHON ?= python
.PHONY: install run test demo eval inspect embeddings
install:
	$(PYTHON) -m pip install -r requirements.txt
run:
	$(PYTHON) -m uvicorn app.api:app --reload
test:
	$(PYTHON) -m pytest -q
demo:
	$(PYTHON) -m scripts.demo
eval:
	$(PYTHON) -m scripts.eval_explanations
inspect:
	$(PYTHON) -m scripts.inspect_data
embeddings:
	$(PYTHON) -m scripts.build_embeddings

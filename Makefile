.PHONY: install test run docker

install:
	pip install -r requirements.txt

test:
	pytest --maxfail=1 --disable-warnings -q

run:
	python src/backend/app.py

        
        
        
        
        
        

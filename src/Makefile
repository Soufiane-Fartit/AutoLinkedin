.PHONY: all test clean
PYTHON_INTERPRETER = python3

cleaning :
	pwd
	rm -f ../data/CVs/CV_*.docx
	rm -f ../data/jobsFound.json
	rm -f ../data/jobsFoundParsed.json

scraping :
	cd scrap && $(PYTHON_INTERPRETER) scraper.py

parsing :
	cd process && $(PYTHON_INTERPRETER) parse.py

generating :
	cd autoCV && $(PYTHON_INTERPRETER) generate_cv.py

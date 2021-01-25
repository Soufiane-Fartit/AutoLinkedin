.PHONY: all test clean
PYTHON_INTERPRETER = python3

clean :
	pwd
	rm -f ../data/Resumes/CV_*.docx
	rm -f ../data/ScrapedJobsData/jobsFound.json
	rm -f ../data/ScrapedJobsData/jobsFoundParsed.json

scrap :
	cd scraping && $(PYTHON_INTERPRETER) scraper.py

parse :
	cd processing && $(PYTHON_INTERPRETER) parse.py

generate :
	cd autoCV && $(PYTHON_INTERPRETER) generate_cv.py

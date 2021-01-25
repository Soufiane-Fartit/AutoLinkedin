> :warning: **Use at your own risks**: This project is just for fun. I advise against actually using it in real life.
> :warning: **This is not a complete solution**: Rather a demo and there's still work to be done

## What does it do ?
Scrap Linkedin for jobs, search for skills, and create a custom resume that contains the needed keywords to avoid being stopped by ATS systems.

## How does it do it ?
> * Use Selenium and BeautifulSoup to connect to linkedin and find jobs
> * Use Regex Patterns and list of skills to match in jobs descriptions
> * use python-docx to create a word file (the resume)

## What does it need ?
> * Chromedriver (can be downloaded online)
> * Linkedin links to scrap
> * Linkedin credentials
> * Education, Work History, Skills ... in a json format

## Requirements :
> * re
> * selenium
> * bs4
> * flashtext
> * python-docx


## How to use ?

Fill the autoCV/data.py with personal infos, then run the commands :

> deletes all created files :
```
make cleaning
````

> scrap linkedin for jobs :
```
make scraping
```

> extract skills from jobs :
```
make parsing
```

> generate custom resumes for each job :
```
make generating
```


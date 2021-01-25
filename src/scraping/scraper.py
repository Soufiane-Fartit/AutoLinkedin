import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup
from utils import *
from getpass import getpass

class Scraper:
    """CONNETS TO LINKEDIN AND SEARCH FOR JOBS. JOBS FOUND WILL BE STORED IN /DATA/ScrapedJobsData/JOBSFOUND.JSON
    """
    def __init__(self, search_links, driver_path="./chromedriver"):
        self.username = input("Your Email Please : ")
        self.password = getpass("Your Password Please : ")
        
        self.browser = webdriver.Chrome(driver_path)
        self.browser.set_window_size(1910, 1085)
        self.search_links = search_links
        self.job_dicts = []
        

    def login(self):
        """CONNECTS TO LINKEDIN
        """
        self.browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        time.sleep(3)

        #Enter login info:
        elementID = self.browser.find_element_by_id('username')
        elementID.send_keys(self.username)
        time.sleep(2)

        elementID = self.browser.find_element_by_id('password')
        elementID.send_keys(self.password)
        time.sleep(1)

        elementID.submit()
    
    def dumpJobsFound(self):
        """SAVE JOBS INTO A JSON FILE
        """
        import json
        with open('../../data/ScrapedJobsData/jobsFound.json', 'w') as fout:
            json.dump(self.job_dicts, fout, ensure_ascii=False, indent = 4)

    def scrapAllLinks(self):
        """ITERATE OVER LINKS PROVIDED AND SCRAP JOBS FROM THEM
        """
        for search_link in self.search_links:
            self.scrapLink(search_link)

    def scrapLink(self, search_link):
        """GIVEN A LINK IT ITERATES OVER JOBS ONE BY ONE AND SCRAP INFORMATION
        """
        self.browser.get(search_link)

        # Iterate over jobs
        jobIDs = self.browser.find_elements_by_class_name('jobs-search-results__list-item')

        for i, jobID in enumerate(jobIDs):
            try :
                print(f"job N : {i}")
                job_dict = {}

                jobID.click()

                src = self.browser.page_source
                soup = BeautifulSoup(src, 'lxml')
                """
                #   GET LINK TO APPLY
                #   
                #   todo : Error when it encounters an EASY APPLY 

                try :
                    jj = self.browser.find_elements_by_class_name('jobs-apply-button--top-card')[0]
                    jj.click()
                    #time.sleep(1)
                    self.browser.switch_to.window(self.browser.window_handles[-1])
                    url = self.browser.current_url
                    #time.sleep(1)
                    self.browser.close()
                    #time.sleep(1)
                    self.browser.switch_to.window(self.browser.window_handles[-1])
                except :
                    pass
                else :
                    job_dict['url'] = url
                """
                job_dict['title'] = classifyJob(soup.find("h2", {"class":"jobs-details-top-card__job-title"}).text.replace(".e","").replace("(H/F)","").replace("(F/H)","")).lstrip().rstrip()
                
                job_dict['city'] = ""
                
                job_description = soup.find("div", {"id": "job-details"})
                parsed_job_description = remove_html_tags(str(job_description)).replace('\n','')
                parsed_job_description = re.sub('\n        \n\n          ', ':', parsed_job_description).lower()
                job_dict['description'] = parsed_job_description.lstrip().rstrip()
                
                job_dict['emails'] = re.findall(r'[\w\.-]+@[\w\.-]+', parsed_job_description)

                job_description_elements = [re.sub("<[^>]*>","",x).lstrip(">| ") for x in re.findall(r'<*?>.*?<br/>', str(job_description))]
                job_dict['job_description_elements'] = job_description_elements

                #for title, text in zip(titles, texts):
                #    job_dict[title] = text
                
                self.job_dicts.append(job_dict)
            except :
                pass

# LINKS TO LOOK UP
search_links = ["https://www.linkedin.com/jobs/search/?f_E=2&f_TPR=r86400&keywords=data%20scientist%20-experimente%20-%22ans%20d%27exp%C3%A9rience%22%20-senior%20-stage%20-stagiaire%20-alternance%20-doctorant%20-docteur%20-freelance",
                "https://www.linkedin.com/jobs/search/?f_E=2&f_TPR=r86400&geoId=105015875&keywords=machine%20learning%20-experimente%20-%22ans%20d%27exp%C3%A9rience%22%20-senior%20-stage%20-stagiaire%20-alternance%20-doctorant%20-docteur%20-freelance&location=France",
                "https://www.linkedin.com/jobs/search/?f_E=2&f_TPR=r86400&geoId=105015875&keywords=data%20analyst%20-experimente%20-%22ans%20d%27exp%C3%A9rience%22%20-senior%20-stage%20-stagiaire%20-alternance%20-doctorant%20-docteur%20-freelance&location=France"]

scraper = Scraper(search_links, driver_path="../../chromedriver")
scraper.login()
scraper.scrapAllLinks()
scraper.dumpJobsFound()

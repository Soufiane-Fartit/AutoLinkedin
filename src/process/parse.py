import json
import re
from flashtext import KeywordProcessor
from collections import Counter
from utils import getSkillsList

all_skills_found = []
jobs_skills = []

# LOAD JOBS SCRAPED
with open('../../data/jobsFound.json', 'r') as jobs_file:
    jobs = json.load(jobs_file)

"""
skills = []
with open('../../data/all_linkedin_skills.txt', 'r') as jobs_file:
    for line in jobs_file:
        skills.append(line.rstrip("\n"))
"""

for i, job in enumerate(jobs) :
    #print(job['title'])
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(getSkillsList())
    skills_found = [keyword_processor.extract_keywords(element) for element in job['job_description_elements']]
    
    seps = [", ", "| ", " - ", "/"]
    skills_found_2 = []
    for sep in seps :
        skills_found_2 = skills_found_2+[re.findall(f"{sep}(.*?){sep}", element) for element in job['job_description_elements']]
    flat_skills_found = list(set([item for sublist in skills_found for item in sublist if len(item)<25 and len(item)>0]))
    flat_skills_found_2 = list(set([item for sublist in skills_found_2 for item in sublist if len(item)<25 and len(item)>0]))
    flat_skills_found = flat_skills_found + flat_skills_found_2
    #print(flat_skills_found)

    try :
        m = max([len(x) for x in skills_found])
        m_idx = [len(x) for x in skills_found].index(max([len(x) for x in skills_found]))
        jobs[i]['skills_found'] = flat_skills_found
    except :
        m = -1
        m_idx = -1
        jobs[i]['skills_found'] = []
    
    jobs_skills.append({'skills': skills_found, 'flat_skills_found': flat_skills_found, 'm':m, 'index':m_idx})
    #all_skills_found = all_skills_found + flat_skills_found


# SAVE DATA EXTRACTED
with open('../../data/jobsFoundParsed.json', 'w') as fout:
    jobs = [job for job in jobs if 'skills_found' in job]
    json.dump(jobs, fout, ensure_ascii=False, indent = 4)


"""
c = Counter(all_skills_found)
most_common = c.most_common(100)
most_common_ = [x for x,y in most_common]
"""
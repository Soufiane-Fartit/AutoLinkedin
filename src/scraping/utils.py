def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def classifyJob(title_):
    keyword_dict = {
        "Data Scientist": {'positive':["data", "scientist"], 'negative':[]},
        "Data Analyst": {'positive':["data", "analyst", "analyste", "données"], 'negative':[]},
        "Data Engineer": {'positive':["ingénieur", "engineer", "data", "données"], 'negative':[]},
        "Ingénieur en Machine Learning": {'positive':["machine", "learning", "engineer", "ingénieur"], 'negative':[]},
        "Python Developer" : {'positive':["python", "developer", "developpeur "], 'negative':[]},
    }
    jobs_list = keyword_dict.keys()
    pos_scores = [len([word for word in title_.split(" ") if word in keyword_dict[job_title]['positive']]) for job_title in keyword_dict.keys()]
    neg_scores = [len([word for word in title_.split(" ") if word in keyword_dict[job_title]['negative']]) for job_title in keyword_dict.keys()]
    tot_scores = [pos-neg for pos, neg in zip(pos_scores, neg_scores)]
    
    maxi = max(tot_scores)
    max_idx = [i for i, j in enumerate(tot_scores) if j == maxi]
    
    return list(jobs_list)[max_idx[0]]

def makeLinkFromKeywords(pos_keywords, neg_keywords, n_days=1):
    link = "https://www.linkedin.com/jobs/search/?"
    link_FirstJob = "f_E=2&"
    link_n_days = "f_TPR=r" + str(n_days * 86400) + "&"

    neg_keywords = ["-"+x for x in neg_keywords]
    link_keywords = "keywords=" + "%20".join(pos_keywords+neg_keywords)
    final_link = link+ link_FirstJob + link_n_days + link_keywords
    
    return final_link
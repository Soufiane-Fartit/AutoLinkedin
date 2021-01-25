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

"""
DEPRECATED - WILL BE REMOVED
def classifyJob(title_):
    title = title_.lower().replace("(","").replace(")","").replace("-","").split(" ")
    if "data" in title and "scientist" in title:
        title_ = "Data Scientist"
    elif "data" in title and "analyst" in title:
        title_ = "Data Analyst"
    elif "données" in title and "analyste" in title:
        title_ = "Data Analyst"
    elif "données" in title and "ingenieur" in title:
        title_ = "Data Engineer"
    elif "data" in title and "engineer" in title:
        title_ = "Data Engineer"
    elif "machine" in title and "learning" in title and "engineer" in title:
        title_ = "Ingénieur en Machine Learning"
    elif "machine" in title and "learning" in title and "ingenieur" in title:
        title_ = "Ingénieur en Machine Learning"
    elif "developer" in title and "python" in title:
        title_ = "Python Developer"
    elif "developpeur" in title and "python" in title:
        title_ = "Python Developer"
    elif "dev" in title and "python" in title:
        title_ = "Python Developer"
    elif "engineer" in title and "python" in title and "software" in title:
        title_ = "Python Developer"
    elif "ingenieur" in title and "python" in title and "logiciel" in title:
        title_ = "Python Developer"
    else:
        pass

    return title_
"""
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)



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
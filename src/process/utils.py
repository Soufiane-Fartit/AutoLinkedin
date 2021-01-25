def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def getSkills():
    import pandas as pd


    data = pd.read_excel('../../data/Skillset.xlsx', engine='openpyxl')
    skills_dict = {}

    skills_dict['Maths'] = [x for x in data['Maths'].values.tolist() if str(x) != 'nan']
    skills_dict['Business'] = [x for x in data['Business'].values.tolist() if str(x) != 'nan']
    skills_dict['Marketing'] = [x for x in data['Marketing'].values.tolist() if str(x) != 'nan']
    skills_dict['Prod_mgmt.'] = [x for x in data['Prod_mgmt.'].values.tolist() if str(x) != 'nan']
    skills_dict['Mgmt.'] = [x for x in data['Mgmt.'].values.tolist() if str(x) != 'nan']
    skills_dict['Soft_Skills'] = [x for x in data['Soft_Skills'].values.tolist() if str(x) != 'nan']
    skills_dict['ML/AI'] = [x for x in data['ML/AI'].values.tolist() if str(x) != 'nan']
    skills_dict['Analytics'] = [x for x in data['Analytics'].values.tolist() if str(x) != 'nan']
    skills_dict['DevOps'] = [x for x in data['DevOps'].values.tolist() if str(x) != 'nan']
    skills_dict['Coding'] = [x for x in data['Coding'].values.tolist() if str(x) != 'nan']
    skills_dict['WebD'] = [x for x in data['WebD'].values.tolist() if str(x) != 'nan']

    return skills_dict


def getSkillsList():
    import itertools

    skills = getSkills()
    merged = list(itertools.chain(*skills.values()))
    
    return list(set(merged))


def getSkillsListByType(skill_types):
    import itertools
    
    list_of_l = [getSkills()[skill_type] for skill_type in skill_types]
    merged = list(itertools.chain(*list_of_l))

    return list(set(merged))



def getSoufLists():
    souf_domain_knowledge_list = list(map(lambda x:x.lower(), ["traitement de signal", "traitement des images", "image", "détection des anomalies", "Vision par ordinateur", 
                                                                "détection d'anomalie", "deep learning", "théoriques", "statistiques", "machine learning", "algorithmie", 
                                                                "informatique", "calculs scientifiques"]))
    souf_tech_list = list(map(lambda x:x.lower(), ["python", "Matlab", "C++", "SQL", "NoSQL", "MongoDB", "Neo4j", "Redis", "Scikit-Learn", "Keras", "Tensorflow", "Pytorch", 
                                                                "Numpy", "Numpy", "Scipy", "pySpark", "XGboost", "Opencv", "Matplotlib", "Seaborn", "Tableau", "Flask", "Git", 
                                                                "DVC", "Docker", "Github Actions", "Streamlit", "Streamlit", "Heroku"]))
    souf_soft_skills = list(map(lambda x:x.lower(), ["scrum"]))

    return souf_domain_knowledge_list, souf_tech_list, souf_soft_skills


def cosineSim(a, b, debug=False):
    from collections import Counter

    b = list(set(a+b)) # if skills missing from dataset

    a = [x.lower() for x in a]
    b = [x.lower() for x in b]
    if debug==True:
        print(a)
        print(b)
    # count word occurrences
    a_vals = Counter(a)
    b_vals = Counter(b)
    if debug==True:
        print(a_vals)
        print(b_vals)
    # convert to word-vectors
    words  = list(a_vals.keys() | b_vals.keys())
    a_vect = [a_vals.get(word, 0) for word in words]        # [0, 0, 1, 1, 2, 1]
    b_vect = [b_vals.get(word, 0) for word in words]        # [1, 1, 1, 0, 1, 0]
    if debug==True:
        print('words : ', words)
        print(a_vect)
        print(b_vect)
    # find cosine
    len_a  = sum(av*av for av in a_vect) ** 0.5             # sqrt(7)
    len_b  = sum(bv*bv for bv in b_vect) ** 0.5             # sqrt(4)
    dot    = sum(av*bv for av,bv in zip(a_vect, b_vect))    # 3
    cosine = dot / (len_a * len_b)
    return cosine


def getFranceCities():
    cities = ["paris", "marseille", "lyon", "toulouse", "nice", "nantes", "montpellier", "strasbourg", "bordeaux", 
            "lille", "rennes", "reims", "saint-etienne", "le havre", "toulon", "grenoble", "dijon", "angers", "nîmes", 
            "villeurbanne"]
    return cities

def filterCities(line):
    import re
    cities = getFranceCities()
    for city in cities :
        line = line.strip(city)
    #return re.sub('[^a-zA-Z]+', '', line)
    #return line.strip("/").strip("-").strip(" \s+")
    return line


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


def findSkillType(skill, skills_dict):
    for skills_cat in skills_dict.keys():
        if skill in skills_dict[skills_cat]:
            return skills_cat
    return 'Autres'


def clusterSkills(skills_list, skills_dict):
    skills_type = {}
    for skill in skills_list:
        skills_type[skill] = findSkillType(skill, skills_dict)
    inv_map = {}
    for k, v in skills_type.items():
        inv_map[v] = inv_map.get(v, []) + [k]
    return inv_map
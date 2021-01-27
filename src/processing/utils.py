def getSkills(skills_path):
    import pandas as pd
    data = pd.read_excel(skills_path, engine='openpyxl')
    
    skills_dict = {}
    skills_keys = data.columns[['Unnamed' not in x for x in data.columns]]
    
    for key in skills_keys :
        skills_dict[key] = [x.lower() for x in data[key].values.tolist() if str(x) != 'nan']

    return skills_dict



def getSkillsList(skills_path):
    import itertools

    skills = getSkills(skills_path)
    merged = list(itertools.chain(*skills.values()))
    
    return list(set(merged))

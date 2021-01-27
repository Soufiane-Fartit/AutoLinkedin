def getSkills(skills_path):
    import pandas as pd
    data = pd.read_excel(skills_path, engine='openpyxl')
    
    skills_dict = {}
    skills_keys = data.columns[['Unnamed' not in x for x in data.columns]]
    
    for key in skills_keys :
        skills_dict[key] = [x.lower() for x in data[key].values.tolist() if str(x) != 'nan']

    return skills_dict, skills_keys

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

def merge_skills(dict1, dict2):
     dict3 = {}
     for key in set().union(dict1, dict2):
         if key in dict1: dict3.setdefault(key, []).extend(dict1[key])
         if key in dict2: dict3.setdefault(key, []).extend(dict2[key])
     return dict3
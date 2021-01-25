def getSkills():
    import pandas as pd

    data = pd.read_excel('../../data/skills/Skillset.xlsx', engine='openpyxl')
    skills_dict = {}

    skills_dict['Maths'] = [x.lower() for x in data['Maths'].values.tolist() if str(x) != 'nan']
    skills_dict['Autres'] = [x.lower() for x in data['Autres'].values.tolist() if str(x) != 'nan']
    skills_dict['Soft_Skills'] = [x.lower() for x in data['Soft_Skills'].values.tolist() if str(x) != 'nan']
    skills_dict['ML/AI'] = [x.lower() for x in data['ML/AI'].values.tolist() if str(x) != 'nan']
    skills_dict['Visualisation'] = [x.lower() for x in data['Visualisation'].values.tolist() if str(x) != 'nan']
    skills_dict['MLOps'] = [x.lower() for x in data['MLOps'].values.tolist() if str(x) != 'nan']
    skills_dict['Langages'] = [x.lower() for x in data['Langages'].values.tolist() if str(x) != 'nan']
    skills_dict['Web'] = [x.lower() for x in data['Web'].values.tolist() if str(x) != 'nan']

    return skills_dict



def getSkillsList():
    import itertools

    skills = getSkills()
    merged = list(itertools.chain(*skills.values()))
    
    return list(set(merged))

import csv
import pandas as pd
df = pd.read_csv("C:/Users/UCC-IT-Admin/OneDrive - De La Salle University-Dasmariñas/UCCreg22-23.csv")


date_filter = df[df['REGISTRATION DATE'] > '1/1/2022']

#GRADE 12

level_filter = date_filter[date_filter['LEVEL APPLIED FOR'] == 'Grade 12']

male_filter = level_filter[level_filter['GENDER'] == 'Male']
female_filter = level_filter[level_filter['GENDER'] == 'Female']

mstem_filter = male_filter[male_filter['STRAND'] == 'STEM (Science, Technology, Engineering and Mathematics)']
marts_filter = male_filter[male_filter['STRAND'] == 'Arts & Design (Performing Arts))']
mhumms_filter = male_filter[male_filter['STRAND'] == 'HUMSS (Humanities and Social Sciences)']
mabm_filter = male_filter[male_filter['STRAND'] == 'ABM (Accountancy, Business and Management)']
mtvlhe1_filter = male_filter[male_filter['STRAND'] == 'TVL - HE 1 (Bread & Pastry Production, Housekeeping, Cookery)']
mtvlhe2_filter = male_filter[male_filter['STRAND'] == 'TVL-HE 2 (Tourism Promotion Services, Events Management Services, Travel Services)']
mtvlict1_filter = male_filter[male_filter['STRAND'] == 'TVL- ICT 2 (Computer Systems Servicing)']
mtvlict2_filter = male_filter[male_filter['STRAND'] == 'TVL-ICT 1 (Animation & Programming (.Net Technology)']

fstem_filter = female_filter[female_filter['STRAND'] == 'STEM (Science, Technology, Engineering and Mathematics)']
farts_filter = female_filter[female_filter['STRAND'] == 'Arts & Design (Performing Arts))']
fhumms_filter = female_filter[female_filter['STRAND'] == 'HUMSS (Humanities and Social Sciences)']
fabm_filter = female_filter[female_filter['STRAND'] == 'ABM (Accountancy, Business and Management)']
ftvlhe1_filter = female_filter[female_filter['STRAND'] == 'TVL - HE 1 (Bread & Pastry Production, Housekeeping, Cookery)']
ftvlhe2_filter = female_filter[female_filter['STRAND'] == 'TVL-HE 2 (Tourism Promotion Services, Events Management Services, Travel Services)']
ftvlict1_filter = female_filter[female_filter['STRAND'] == 'TVL- ICT 2 (Computer Systems Servicing)']
ftvlict2_filter = female_filter[female_filter['STRAND'] == 'TVL-ICT 1 (Animation & Programming (.Net Technology)']

strands = ["STEM", "ARTS", "HUMMS", "ABM", "TVL - HE 1", "TVL - HE 2", "TVL - ICT 1", "TVL - ICT 2"]
mfilters = [mstem_filter.shape[0], marts_filter.shape[0], mhumms_filter.shape[0], mabm_filter.shape[0], mtvlhe1_filter.shape[0],
mtvlhe2_filter.shape[0], mtvlict1_filter.shape[0], mtvlict2_filter.shape[0]]
ffilters = [fstem_filter.shape[0], farts_filter.shape[0], fhumms_filter.shape[0], fabm_filter.shape[0], ftvlhe1_filter.shape[0],
ftvlhe2_filter.shape[0], ftvlict1_filter.shape[0], ftvlict2_filter.shape[0]]

df = pd.DataFrame()
df['STRAND'] = strands
df['MALE'] = mfilters
df['FEMALE'] = ffilters

df.to_csv('Grade 12_Summary.csv') 

#GRADE 11

level_filter = date_filter[date_filter['LEVEL APPLIED FOR'] == 'Grade 11']

male_filter = level_filter[level_filter['GENDER'] == 'Male']
female_filter = level_filter[level_filter['GENDER'] == 'Female']

mstem_filter = male_filter[male_filter['STRAND'] == 'STEM (Science, Technology, Engineering and Mathematics)']
marts_filter = male_filter[male_filter['STRAND'] == 'Arts & Design (Performing Arts))']
mhumms_filter = male_filter[male_filter['STRAND'] == 'HUMSS (Humanities and Social Sciences)']
mabm_filter = male_filter[male_filter['STRAND'] == 'ABM (Accountancy, Business and Management)']
mtvlhe1_filter = male_filter[male_filter['STRAND'] == 'TVL - HE 1 (Bread & Pastry Production, Housekeeping, Cookery)']
mtvlhe2_filter = male_filter[male_filter['STRAND'] == 'TVL-HE 2 (Tourism Promotion Services, Events Management Services, Travel Services)']
mtvlict1_filter = male_filter[male_filter['STRAND'] == 'TVL- ICT 2 (Computer Systems Servicing)']
mtvlict2_filter = male_filter[male_filter['STRAND'] == 'TVL-ICT 1 (Animation & Programming (.Net Technology)']

fstem_filter = female_filter[female_filter['STRAND'] == 'STEM (Science, Technology, Engineering and Mathematics)']
farts_filter = female_filter[female_filter['STRAND'] == 'Arts & Design (Performing Arts))']
fhumms_filter = female_filter[female_filter['STRAND'] == 'HUMSS (Humanities and Social Sciences)']
fabm_filter = female_filter[female_filter['STRAND'] == 'ABM (Accountancy, Business and Management)']
ftvlhe1_filter = female_filter[female_filter['STRAND'] == 'TVL - HE 1 (Bread & Pastry Production, Housekeeping, Cookery)']
ftvlhe2_filter = female_filter[female_filter['STRAND'] == 'TVL-HE 2 (Tourism Promotion Services, Events Management Services, Travel Services)']
ftvlict1_filter = female_filter[female_filter['STRAND'] == 'TVL- ICT 2 (Computer Systems Servicing)']
ftvlict2_filter = female_filter[female_filter['STRAND'] == 'TVL-ICT 1 (Animation & Programming (.Net Technology)']

strands = ["STEM", "ARTS", "HUMMS", "ABM", "TVL - HE 1", "TVL - HE 2", "TVL - ICT 1", "TVL - ICT 2"]
mfilters = [mstem_filter.shape[0], marts_filter.shape[0], mhumms_filter.shape[0], mabm_filter.shape[0], mtvlhe1_filter.shape[0],
mtvlhe2_filter.shape[0], mtvlict1_filter.shape[0], mtvlict2_filter.shape[0]]
ffilters = [fstem_filter.shape[0], farts_filter.shape[0], fhumms_filter.shape[0], fabm_filter.shape[0], ftvlhe1_filter.shape[0],
ftvlhe2_filter.shape[0], ftvlict1_filter.shape[0], ftvlict2_filter.shape[0]]

df = pd.DataFrame()
df['STRAND'] = strands
df['MALE'] = mfilters
df['FEMALE'] = ffilters

df.to_csv('Grade 11_Summary.csv') 


grades = ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10",]
df = pd.DataFrame()
for level in grades:
    list_of_sub = []

    level_filter = date_filter[date_filter['LEVEL APPLIED FOR'] == level]
    list_of_sub.append(level)
    df['LEVEL'] = list_of_sub
    male_filter = level_filter[level_filter['GENDER'] == 'Male']
    female_filter = level_filter[level_filter['GENDER'] == 'Female']
    df['MALE'] = male_filter.shape[0]
    df['FEMALE'] = female_filter.shape[0]
    df.to_csv(level + '_Summary.csv')






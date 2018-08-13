import pandas as pd
from itertools import izip
import shutil
import os

df = pd.read_csv('complete_activity_list.csv')
login = list()
onboarding = list()
settings = list()

loginlist  = ['login','register','signup','signin']
onboardinglist = ['onboard','wizard','tutorial']
settingslist = ['settings']

df = df.dropna()

for a,f in izip(df.ActivityName, df.FileName):
    if any(s in a.lower() for s in loginlist):
        login.append(f)
    elif any(s in a.lower() for s in onboardinglist):
        onboarding.append(f)
    elif any(s in a.lower() for s in settingslist):
        settings.append(f)
   
train_number = 1210
test_number = train_number + 49
dataset_dir = '/home/saumo/Desktop/jsons/'
json_dir = '/home/saumo/Downloads/GSoC 2018/json_dir'
for l in login[:train_number]:
    shutil.copy2(os.path.join(json_dir,str(l)+'.json'), os.path.join(dataset_dir,'train','login'))
for o in onboarding[:train_number]:
    shutil.copy2(os.path.join(json_dir,str(o)+'.json'), os.path.join(dataset_dir,'train','onboarding'))
for s in settings[:train_number]:
    shutil.copy2(os.path.join(json_dir,str(s)+'.json'), os.path.join(dataset_dir,'train','settings'))

for l in login[train_number:test_number]:
    shutil.copy2(os.path.join(json_dir,str(l)+'.json'), os.path.join(dataset_dir,'test','login'))
for o in onboarding[train_number:test_number]:
    shutil.copy2(os.path.join(json_dir,str(o)+'.json'), os.path.join(dataset_dir,'test','onboarding'))
for s in settings[train_number:test_number]:
    shutil.copy2(os.path.join(json_dir,str(s)+'.json'), os.path.join(dataset_dir,'test','settings'))

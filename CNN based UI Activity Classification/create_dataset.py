import pandas as pd
from itertools import izip

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
        
import shutil
import os
train_number = 1200
valid_number = train_number + 50
test_number = valid_number + 9
dataset_dir = '/home/saumo/Desktop/screenshots/'
screenshot_dir = '/home/saumo/Downloads/GSoC 2018/combined'
for l in login[:train_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(l)+'.jpg'), os.path.join(dataset_dir,'train','login'))
for o in onboarding[:train_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(o)+'.jpg'), os.path.join(dataset_dir,'train','onboarding'))
for s in settings[:train_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(s)+'.jpg'), os.path.join(dataset_dir,'train','settings'))
    
for l in login[train_number:valid_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(l)+'.jpg'), os.path.join(dataset_dir,'valid','login'))
for o in onboarding[train_number:valid_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(o)+'.jpg'), os.path.join(dataset_dir,'valid','onboarding'))
for s in settings[train_number:valid_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(s)+'.jpg'), os.path.join(dataset_dir,'valid','settings'))

for l in login[valid_number:test_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(l)+'.jpg'), os.path.join(dataset_dir,'test','login'))
for o in onboarding[valid_number:test_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(o)+'.jpg'), os.path.join(dataset_dir,'test','onboarding'))
for s in settings[valid_number:test_number]:
    shutil.copy2(os.path.join(screenshot_dir,str(s)+'.jpg'), os.path.join(dataset_dir,'test','settings'))

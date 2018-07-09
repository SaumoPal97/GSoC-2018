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
        
print ("Login %d" % len(login))
print ("Onboarding %d" % len(onboarding))
print ("Settings %d" % len(settings))

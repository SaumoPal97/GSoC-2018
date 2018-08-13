import pandas as pd
from os import listdir
from os.path import join, isfile
dataset_dir = '/home/saumo/Desktop/jsons/'
col_names = ['class','content']
train_df  = pd.DataFrame(columns = col_names)
test_df = pd.DataFrame(columns = col_names)

files_login = [f for f in listdir(join(dataset_dir,'train','login')) if isfile(join(dataset_dir,'train','login', f))]
files_onboarding = [f for f in listdir(join(dataset_dir,'train','onboarding')) if isfile(join(dataset_dir,'train','onboarding', f))]
files_settings = [f for f in listdir(join(dataset_dir,'train','settings')) if isfile(join(dataset_dir,'train','settings', f))]
for fl in files_login:
    with open(join(dataset_dir,'train','login', fl), 'r') as myfile:
        data=myfile.read().replace('\n', ' ')
    train_df.loc[len(train_df)] = [1,data]
    myfile.close()
for fl in files_onboarding:
    with open(join(dataset_dir,'train','onboarding', fl), 'r') as myfile:
        data=myfile.read().replace('\n', ' ')
    train_df.loc[len(train_df)] = [2,data]
    myfile.close()
for fl in files_settings:
    with open(join(dataset_dir,'train','settings', fl), 'r') as myfile:
        data=myfile.read().replace('\n', ' ')
    train_df.loc[len(train_df)] = [3,data]
    myfile.close()
train_df[['class']] = train_df[['class']].astype(int)
train_df.to_csv('train.csv', index=False)

files_login = [f for f in listdir(join(dataset_dir,'test','login')) if isfile(join(dataset_dir,'test','login', f))]
files_onboarding = [f for f in listdir(join(dataset_dir,'test','onboarding')) if isfile(join(dataset_dir,'test','onboarding', f))]
files_settings = [f for f in listdir(join(dataset_dir,'test','settings')) if isfile(join(dataset_dir,'test','settings', f))]
for fl in files_login:
    with open(join(dataset_dir,'test','login', fl), 'r') as myfile:
        data=myfile.read().replace('\n', ' ')
    test_df.loc[len(test_df)] = [1,data]
    myfile.close()
for fl in files_onboarding:
    with open(join(dataset_dir,'test','onboarding', fl), 'r') as myfile:
        data=myfile.read().replace('\n', ' ')
    test_df.loc[len(test_df)] = [2,data]
    myfile.close()
for fl in files_settings:
    with open(join(dataset_dir,'test','settings', fl), 'r') as myfile:
        data=myfile.read().replace('\n', ' ')
    test_df.loc[len(test_df)] = [3,data]
    myfile.close()
test_df[['class']] = test_df[['class']].astype(int)
test_df.to_csv('test.csv', index=False)

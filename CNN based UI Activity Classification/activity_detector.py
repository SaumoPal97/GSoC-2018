import re
import json
import pandas as pd
from os import listdir, getcwd
from os.path import isfile, join, splitext

def activity_name_search(haystack):
    if u'activity_name' in haystack.keys():
        words = haystack[u'activity_name'].split('.')
        if words[-1].endswith('Activity'):
            return words[-1][:-len('Activity')]
        else :
            return words[-1]

def main:
    activity_name = list()
    file_name = list()
    mypath = getcwd()
    files = [f for f in listdir(join(mypath,'json_dir_1')) if isfile(join(mypath,'json_dir_1', f))]
    for fl in files :
        with open(join(mypath,'json_dir_1',fl),'r') as f:
            fo = json.load(f)
        activity_name.append(activity_name_search(fo))
        file_name.append(splitext(fl)[0])
        f.close()

    d = {'FileName':file_name,'ActivityName':activity_name}
    df = pd.DataFrame(d)
    df.to_csv('activity_list.csv', index=False, encoding = 'utf-8')

if __name__ == "__main__":
    main()

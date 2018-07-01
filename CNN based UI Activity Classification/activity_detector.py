import re
import json
import pandas as pd
from os import listdir, getcwd
from os.path import isfile, join, splitext

def activity_name_search(haystack):
    if u'activity_name' in haystack.keys():
        words = haystack[u'activity_name'].split('.')
        activity_name = words[-1]
        activity_name = activity_name.replace('Activity','')
        activity_name = activity_name.replace('View','')
        return activity_name

def main():
    activity_name_list = list()
    file_name_list = list()
    mypath = getcwd()
    files = [f for f in listdir(join(mypath,'json_dir_1')) if isfile(join(mypath,'json_dir_1', f))]
    for fl in files :
        with open(join(mypath,'json_dir_1',fl),'r') as f:
            fo = json.load(f)
        activity_name_list.append(activity_name_search(fo))
        file_name_list.append(splitext(fl)[0])
        f.close()

    d = {'FileName':file_name_list,'ActivityName':activity_name_list}
    df = pd.DataFrame(d)
    df.to_csv('activity_list.csv', index=False, encoding = 'utf-8')

if __name__ == "__main__":
    main()

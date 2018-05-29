import re
import json
from os import listdir, getcwd
from os.path import isfile, join, splitext

def deep_search(needles, haystack, found) :
    if type(needles) != type([]) :
        needles = [needles]
    if type(haystack) == type(dict()) :
        if 'clickable' in haystack.keys() :
            if (haystack['clickable'] == True) :
                for needle in needles:
                    if needle in haystack.keys() :
                        if needle == 'bounds' :
                            found.append(haystack[needle][2]-haystack[needle][0])
                            found.append(haystack[needle][3]-haystack[needle][1])
                        elif needle == 'ancestors' :
                            for ancestor in haystack[needle] :
                                found.append(ancestor)
                        elif needle == 'resource-id' :
                            m = re.search('(?<=:id/)\w+', haystack[needle])
                            if m is not None :
                            	words = m.group(0).split('_')
                            	for word in words :
                                	found.append(word)
                        elif needle == 'long-clickable' and haystack[needle] == True :
                            found.append(needle) 
                        elif needle != 'long-clickable' and len(haystack[needle]) > 0 :
                            found.append(haystack[needle])
                found.append(' ')
        if len(haystack.keys()) > 0 :
            for key in haystack.keys() :
                if key not in needles and key != 'clickable' :
                    deep_search(needles, haystack[key], found)
    elif type(haystack) == type([]) :
        for node in haystack :
            deep_search(needles, node, found)


def main() :
    mypath = getcwd()
    files = [f for f in listdir(join(mypath,'json_dir_1')) if isfile(join(join(mypath,'json_dir_1'), f))]
    for fl in files :
    	print fl
        with open(join(join(mypath,'json_dir_1'),fl),'r') as f:
            fo = json.load(f)
        found = list()
        needles = [u'text',u'long-clickable',u'text-hint',u'bounds',u'font-family',u'ancestors',u'resource-id']
        deep_search(needles, fo, found)
        f.close()
    
        fname = splitext(fl)[0] + '.txt'
        fi = open(join(join(mypath,'corpus_dir_1'), fname), 'w+')
        for word in found :
            if word != (' ') :
            	fi.write(repr(word).encode('utf-8'))
                fi.write(' ')
            elif word == (' ') :
               	fi.write('\n')
        fi.close()

if __name__ == "__main__":
    main()
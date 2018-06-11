import re
import json
from os import listdir, getcwd
from os.path import isfile, join, splitext

def deep_search(needles, haystack, found, previous_resource_id) :
    if type(needles) != type([]) :
        needles = [needles]
    if type(haystack) == type(dict()) :
    	if 'resource-id' in haystack.keys() :
    		if len(haystack['resource-id']) > 0 :
    			previous_resource_id = haystack['resource-id']
        if 'clickable' in haystack.keys() :
            if (haystack['clickable'] == True) :
        	for needle in needles:
                    if needle in haystack.keys() :
                        if needle == 'bounds' :
                            found.append(haystack[needle][2]-haystack[needle][0])
                            found.append(haystack[needle][3]-haystack[needle][1])
                        elif needle == 'text' or needle == 'text-hint' :
                        	words = haystack[needle].split(' ')
                        	for word in words :
                        		w = ''.join(e for e in word if e.isalnum())
                        		found.append(w.lower())
                        elif needle == 'ancestors' :
                            for ancestor in haystack[needle] :
                            	if ancestor[0] == 'X' :
                            		found.append(ancestor)
                            	else :
                            		words = ancestor.split('.')
                            		for word in words :
                            			found.append(word.lower())
                        elif needle == 'class' :
                        	if len(haystack[needle]) > 0 :
                        		words = haystack[needle].split('.')
                        		for word in words :
                        			w = ''.join(e for e in word if e.isalnum())
                        			found.append(w.lower())
                        elif needle == 'resource-id' :
                        	m = re.search('(?<=:id/)\w+', previous_resource_id)
                        	if m is not None :
                        		words = m.group(0).split('_')
                        		for word in words :
                        			found.append(word.lower())
                        elif needle == 'long-clickable' and haystack[needle] == True :
                            found.append(needle)
                        elif needle != 'long-clickable' and len(haystack[needle]) > 0 :
                            found.append(haystack[needle])
                    else :
                        m = re.search('(?<=:id/)\w+', previous_resource_id)
                        if m is not None :
                            words = m.group(0).split('_')
                            for word in words :
                            	found.append(word.lower())
                found.append(' ')
        if len(haystack.keys()) > 0 :
            for key in haystack.keys() :
                if key not in needles and key != 'clickable' :
                    deep_search(needles, haystack[key], found, previous_resource_id)
    elif type(haystack) == type([]) :
        for node in haystack :
            deep_search(needles, node, found, previous_resource_id)


def main() :
    mypath = getcwd()
    files = [f for f in listdir(join(mypath,'json_dir_1')) if isfile(join(mypath,'json_dir_1', f))]
    for fl in files :
        with open(join(mypath,'json_dir_1',fl),'r') as f:
            fo = json.load(f)
        found = list()
        needles = [u'text',u'long-clickable',u'text-hint',u'bounds',u'font-family',u'ancestors',u'resource-id',u'class']
        deep_search(needles, fo, found, "")
        f.close()
    
        fname = splitext(fl)[0] + '.txt'
        fi = open(join(mypath,'corpus_dir_1', fname), 'w+')
        for word in found :
            if word != (' ') :
            	fi.write(repr(word).encode('utf-8'))
                fi.write(' ')
            elif word == (' ') :
               	fi.write('\n')
        fi.close()

if __name__ == "__main__":
    main()
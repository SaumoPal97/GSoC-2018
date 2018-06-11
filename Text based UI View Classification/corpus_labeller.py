import os, json
from collections import OrderedDict

label_dict = OrderedDict()
label_dict['email'] = [u'email']
label_dict['text'] = [u'name',u'address',u'first',u'last',u'street',u'building']
label_dict['password'] = [u'password']
label_dict['number'] = [u'phone',u'mobile',u'pincode',u'zipcode',u'pin',u'zip']
label_dict['ad'] = [u'adview', u'advert',u'advertisement']
label_dict['skip'] = [u'skip',u'close',u'stop']
label_dict['image'] = [u'thumbnail',u'image',u'clip',u'imageview']
label_dict['button'] = [u'button']

def jsonify_data(top_directory):
    json_list = list()
    for root, dirs, files in os.walk(os.path.join(top_directory,'corpus_dir_1')):
        for file in filter(lambda file: file.endswith('.txt'), files):
            with open(os.path.join(root, file)) as f:
                document = f.readlines()
                f.close()
            document = [line.strip() for line in document]
            for line in document:
                json_dict = {}
                for key, value in label_dict.iteritems():
                    if any(x in line for x in value):
                        if (key in ['email','text','number','password']):
                            if(u'edittext' in line):
                                json_dict['feature'] = line
                                json_dict['type'] = key
                                json_list.append(json_dict)
                                break
                            else :
                                json_dict['feature'] = line
                                json_dict['type'] = 'button'
                                json_list.append(json_dict)
                                break
                        else :
                            json_dict['feature'] = line
                            json_dict['type'] = key
                            json_list.append(json_dict)
                            break
                    else:
                        json_dict['feature'] = line
                        json_dict['type'] = 'test'
                        json_list.append(json_dict)
    json_list = [dict(t) for t in set([tuple(d.items()) for d in json_list])]
    thefile = open('json_corpus.txt', 'w+')
    for item in json_list:
        thefile.write("%s\n" % item)
        
top_directory = os.getcwd()
jsonify_data(top_directory)

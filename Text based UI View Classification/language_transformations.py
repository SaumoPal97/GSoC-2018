import os, gensim, ast, random

top_directory = os.getcwd()
corpus_list = list()
answer = dict()

with open(os.path.join(top_directory,'json_corpus_train.txt')) as f:
    document = f.readlines()
    f.close()

for d in document:
    dict_text = ast.literal_eval(d)
    if dict_text['feature'] in answer.keys():
        assert answer[dict_text['feature']] == dict_text['type']
    else:
        answer[dict_text['feature']] = dict_text['type']
    corpus_list.append(dict_text['feature'])

ids = list()
all_corpus = dict()
key = 0
for text in corpus_list:
    ids.append(key)
    all_corpus[key] = text.split() 
    key +=1

random.shuffle(ids)
training_ids = ids[:int(len(ids)*0.8)]
validation_ids = ids[int(len(ids)*0.8):]

texts = list()
for t_id in training_ids:
    texts.append(all_corpus[t_id])

def create_dictionary(texts):
    dictionary = gensim.corpora.Dictionary(texts)
    dictionary.filter_extremes(no_below=1)
    dictionary.save(os.path.join(top_directory, 'transformations', 'trial.dict'))
    return dictionary

def transform_bow(texts, dictionary, top_directory):
    corpus_bow = list()
    corpus_bow += [dictionary.doc2bow(c) for c in texts]
    gensim.corpora.MmCorpus.serialize(os.path.join(top_directory,'transformations','trial.mm'), corpus_bow)
    return corpus_bow

def transform_tfidf(corpus_bow, top_directory):
    tfidf = gensim.models.TfidfModel(corpus_bow)
    tfidf.save(os.path.join(top_directory,'transformations','trial.tfidf'))
    corpus_tfidf = tfidf[corpus_bow]
    return tfidf, corpus_tfidf

def transform_lsi(corpus_tfidf, dictionary, top_directory):
    lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary)
    lsi.save(os.path.join(top_directory,'transformations','trial.lsi'))
    corpus_lsi = lsi[corpus_tfidf]
    index = gensim.similarities.MatrixSimilarity(corpus_lsi)
    index.save(os.path.join(top_directory,'transformations','trial.index'))
    return lsi, index

dictionary = create_dictionary(texts)
corpus_bow = transform_bow(texts, dictionary, top_directory)
tfidf, corpus_tfidf = transform_tfidf(corpus_bow, top_directory)
lsi, index = transform_lsi(corpus_tfidf, dictionary, top_directory)

num_total = 0
num_incorrect = 0
num_multiple_types = 0

training_topic = {}
for i in xrange(len(texts)):
    feature = ' '.join(texts[i])
    training_topic[str(i)] = {
        'type': answer[feature],
        'feature': feature
    }

log_data = []
for t_id in validation_ids:
    log_data.append('corpus: %s\n' % t_id)
    print all_corpus[t_id]
    num_total += 1
    vec_bow = dictionary.doc2bow(all_corpus[t_id])
    vec_tfidf = tfidf[vec_bow]
    vec_lsi = lsi[vec_tfidf]
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print sims
    vec_type = training_topic[str(sims[0][0])]['type']
    feature = ' '.join(all_corpus[t_id])
    print feature
    if (sims[0][1] - sims[4][1]) < 0.1:
        topic_count = {}
        for s in sims[:5]:
            key = str(s[0])
            if training_topic[key]['type'] in topic_count.keys():
                topic_count[training_topic[key]['type']] += 1
            else:
                topic_count[training_topic[key]['type']] = 1
        max_times = topic_count[max(topic_count, key=topic_count.get)]
        max_types = { training_topic[str(v[0])]['type'] for v in sims[:5] if topic_count[training_topic[str(v[0])]['type']] == max_times }
        if len(max_types) > 1:
            log_data.append('More than one candidate types: %s. Ans: %s\n' % (max_types, answer[feature]))
            num_multiple_types += 1
        vec_type = random.choice(list(max_types))
    if vec_type != answer[feature]:
        log_data.append('feature: %s. inferred: %s. ans: %s\n' % (feature, vec_type, answer[feature]))
        log_data.append('sims[:5]:\n')
        for s in sims[:5]:
            log_data.append('%s, %s, %s: %s\n' % (
                s[0], s[1], training_topic[str(s[0])]['type'], training_topic[str(s[0])]['feature']))
        log_data.append('-----\n')
        num_incorrect += 1
print '# of training data:', len(training_topic)
print 'total inferred:', num_total
print '# of multiple types:', num_multiple_types
print 'correction rate: %d/%d (%f)' % (num_total-num_incorrect, num_total, ((num_total-num_incorrect)/float(num_total)))
with open(os.path.join(top_directory, 'log.txt'), 'w') as f:
    f.writelines(log_data)
    f.write('# training data: %d\n' % len(training_topic))
    f.write('total inferred: %d\n' % num_total)
    f.write('# of multiple types: %d\n' % num_multiple_types)
    f.write('correction rate: %d/%d (%f)\n' % (num_total-num_incorrect, num_total, ((num_total-num_incorrect)/float(num_total))))

correction = []
program_log_data = []
program_log_data.append('# training data: %d\n' % len(training_topic))
program_log_data.append('total inferred: %d\n' % num_total)
program_log_data.append('# of multiple types: %d\n' % num_multiple_types)
program_log_data.append('correction rate: %d/%d (%f)\n' % (num_total-num_incorrect, num_total, ((num_total-num_incorrect)/float(num_total))))

correction.append((num_total-num_incorrect)/float(num_total))
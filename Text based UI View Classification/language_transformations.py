import os, gensim, ast

def create_dictionary(top_directory):
    train_corpus_list = list()
    test_corpus_list = list()
    with open(os.path.join(top_directory,'json_corpus.txt')) as f:
        document = f.readlines()
        f.close()
    for d in document:
        dict_text = ast.literal_eval(d)
        if (dict_text['type'] != 'test'):
            train_corpus_list.append(dict_text['feature'])
        else :
            test_corpus_list.append(dict_text['feature'])
    texts = list()
    for text in train_corpus_list:
        texts.append(text.split())
    dictionary = gensim.corpora.Dictionary(texts)
    dictionary.filter_extremes(no_below=1)
    return dictionary, texts

def transform_bow(corpus_list, dictionary, top_directory):
    corpus_bow = list()
    corpus_bow += [dictionary.doc2bow(c) for c in corpus_list]
    gensim.corpora.MmCorpus.serialize(os.path.join(top_directory,'transformations','trial.mm'), corpus_bow)
    return corpus_bow

def transform_tfidf(corpus_bow, top_directory):
    tfidf = gensim.models.TfidfModel(corpus_bow)
    tfidf.save(os.path.join(top_directory,'transformations','trial.tfidf'))
    corpus_tfidf = tfidf[corpus_bow]
    return corpus_tfidf

def transform_lsi(corpus_tfidf, dictionary, top_directory):
    lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=50)
    lsi.save(os.path.join(top_directory,'transformations','trial.lsi'))
    corpus_lsi = lsi[corpus_tfidf]
    index = gensim.similarities.MatrixSimilarity(corpus_lsi)
    index.save(os.path.join(top_directory,'transformations','trial.index'))
    return index
  
top_directory = os.getcwd()
dictionary, texts = create_dictionary(top_directory)
corpus_bow = transform_bow(texts, dictionary, top_directory)
corpus_tfidf = transform_tfidf(corpus_bow, top_directory)
index_lsi = transform_lsi(corpus_tfidf, dictionary, top_directory)

import os, gensim
from pprint import pprint

def create_dictionary(top_directory):
    corpus_list = list()
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            with open(os.path.join(root, file)) as f:
                document = f.readlines()
                f.close()
            document = [x.strip() for x in document] 
            for x in document :
                corpus_list.append(x)
    texts = list()
    for text in corpus_list:
        texts.append(text.split())
    dictionary = gensim.corpora.Dictionary(texts)
    dictionary.filter_extremes(no_below=1)
    return dictionary, texts

def transform_bow(corpus_list, dictionary, top_directory):
    corpus_bow = list()
    corpus_bow += [dictionary.doc2bow(c) for c in corpus_list]
    gensim.corpora.MmCorpus.serialize(os.path.join(top_directory, 'trial.mm'), corpus_bow)
    return corpus_bow

def transform_tfidf(corpus_bow, top_directory):
    tfidf = gensim.models.TfidfModel(corpus_bow)
    tfidf.save(os.path.join(top_directory, 'trial.tfidf'))
    corpus_tfidf = tfidf[corpus_bow]
    return corpus_tfidf

def transform_lsi(corpus_tfidf, dictionary, top_directory):
    lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=50)
    lsi.save(os.path.join(top_directory, 'trial.lsi'))
    corpus_lsi = lsi[corpus_tfidf]
    index = gensim.similarities.MatrixSimilarity(corpus_lsi)
    index.save(os.path.join(top_directory, 'trial.index'))
    return index
  
top_directory = '/home/saumo/Desktop/GSoC-2018/corpus_dir_1/'
dictionary, texts = create_dictionary(top_directory)
corpus_bow = transform_bow(texts, dictionary, top_directory)
corpus_tfidf = transform_tfidf(corpus_bow, top_directory)
index_lsi = transform_lsi(corpus_tfidf, dictionary, top_directory)
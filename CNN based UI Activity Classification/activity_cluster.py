import numpy as np
import pandas as pd
import sklearn.cluster
import distance      
from random import shuffle

def lev_similarity_func(w1,w2):
    return distance.levenshtein(w1,w2)

def activity_clusters(words):
    #unvectorized code
    #lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])
    #vectorized code
    vlev_similarity = np.vectorize(lev_similarity_func)
    lev_similarity = -1*vlev_similarity(words,np.array([words]).T) 
    affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
    affprop.fit(lev_similarity)
    for cluster_id in np.unique(affprop.labels_):
        exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
        cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
        cluster_str = ", ".join(cluster)
        print(" - *%s:* %s" % (exemplar, cluster_str))

def main():
    df = pd.read_csv('complete_activity_list.csv')
    new_complete_list = list()
    for d in df['ActivityName']:
        if type(d) is str:
            new_complete_list.append(d)
    shuffle(new_complete_list)
    words = np.asarray(new_complete_list[:int(0.02*len(new_complete_list))])
    activity_clusters(words)

if __name__ == "__main__":
    main()

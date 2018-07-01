import numpy as np
import pandas as pd
import sklearn.cluster
import distance

def activity_clusters(words):
    lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])
    affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
    affprop.fit(lev_similarity)
    for cluster_id in np.unique(affprop.labels_):
        exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
        cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
        cluster_str = ", ".join(cluster)
        print(" - *%s:* %s" % (exemplar, cluster_str))

def main():
    df = pd.read_csv('complete_activity_list.csv')
    words = np.asarray(df['ActivityName'])
    activity_clusters(words)

if __name__ == "__main__":
    main()

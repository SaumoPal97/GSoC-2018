# GSoC-2018
Will be implementing AI algorithms to improve Droidbot 

This will contain the timeline of my proposed work and my progress through it to ensure that I am on track.

## Community Bonding Period
* Familiarising myself with the following papers 
  - [Using Semantic Similarity in Crawling-based Web Application Testing](http://castman.net/static/file/paper/icst17.pdf)
  - [Inductive Representation Learning on Large Graphs](https://arxiv.org/pdf/1706.02216.pdf)
  - [Webzeitgeist: Design Mining the Web](http://vis.stanford.edu/files/2013-Webzeitgeist-CHI.pdf)

## Phase 1
This phase will be dedicated for implementation of the first paper.
* Week 1
  - Analysing the [Rico](http://rico.interactionmining.org/) dataset to find the features to include in the analysis [DONE]
  - Working upon building the corpus from the json files in the above dataset (size above 20GB) [DONE]
* Week 2
  - Implementing the bag-of-words, tf-idf and LSI trasformation using the above corpus to obtain the set of vectors
* Week 3
  - Writing a script for labelling input topics using a pre-defined dictionary
  - Implementing the cosine similarity of vectors obtained 
* Week 4
  - Integrating with Rule based method
  - Analysing the accuracy and performance on a hold-out dataset
  - Integrating with the [DroidBot](https://github.com/honeynet/droidbot) 
  
## Phase 2
This phase will be dedicated for implementation of the second paper.

## Documentation
Intially you have to keep all the json files in ```json_dir_1``` directory. Then run the following from command prompt
```
python corpus_creater.py
```
You will have the corpus created in the ```corpus_dir_1``` directory. Full corpus will be uploaded soon.
Then run the following
```
python corpus_labeller.py
```
This will create ```json_corpus_train.txt``` and ```json_corpus_test.txt``` files. The first file will be used for training and validating and the second file contains really ambigious cases to solve.

Finally run the following
```
python language_transformations.py
```
This will create bow, tfidf and lsi based transformations based on the training corpus created above and store it in the transformation folder. Using this, you can obtain results of the test files as well. Currently it is trained on an 80% split of 30 json files and validated using 20% split of the same files. The log.txt gives the following
```
corpus: 77
feature: u'action' u'bar' u'long-clickable' u'action' u'bar' 140 168 u'action' u'bar' u'android' u'support' u'v7' u'widget' u'appcompatimageview' u'android' u'widget' u'imageview' u'android' u'view' u'view' u'java' u'lang' u'object' u'action' u'bar' u'android' u'support' u'v7' u'widget' u'actionmenupresenterd'. inferred: button. ans: image
sims[:5]:
55, 0.3755637, button: u'done' u'button1' 232 168 u'sans-serif-medium' u'android' u'widget' u'button' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'button1' u'android' u'support' u'v7' u'widget' u'appcompatbutton'
5, 0.33739424, image: u'prev' u'prev' 168 168 u'prev' u'android' u'widget' u'imagebutton' u'android' u'widget' u'imageview' u'android' u'view' u'view' u'java' u'lang' u'object' u'prev' u'android' u'support' u'v7' u'widget' u'appcompatimagebutton'
27, 0.3191647, text: '' u'long-clickable' u'nickname' u'optional' 1268 -71 u'default' u'android' u'widget' u'edittext' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'ej'
54, 0.3103039, password: '' u'long-clickable' u'enter' u'your' u'password' 1268 132 u'default' u'android' u'widget' u'edittext' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'ej'
23, 0.27410212, text: '' u'long-clickable' u'enter' u'username' u'or' u'card' u'number' 1268 132 u'default' u'android' u'widget' u'edittext' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'ej'
-----
corpus: 64
corpus: 60
feature: u'content' u'content' 105 105 u'content' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'android' u'widget' u'imageview'. inferred: button. ans: image
sims[:5]:
11, 0.58978647, button: u'button' u'content' 0 0 u'content' u'android' u'widget' u'button' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'f'
13, 0.5464875, image: u'content' u'content' 175 175 u'content' u'android' u'widget' u'imageview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'android' u'widget' u'imagebutton'
12, 0.4822211, button: '' u'content' 133 136 u'content' u'android' u'widget' u'button' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'f'
30, 0.4822211, button: '' u'content' 93 152 u'content' u'android' u'widget' u'button' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'f'
33, 0.34305066, image: u'newtab' u'long-clickable' u'newtab' 105 105 u'newtab' u'android' u'view' u'view' u'java' u'lang' u'object' u'newtab' u'android' u'widget' u'imageview'
-----
corpus: 14
corpus: 10
corpus: 68
corpus: 3
feature: '' u'long-clickable' u'enter' u'address' 1152 111 u'default' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'abmlocator' u'search' u'android' u'widget' u'edittext'. inferred: password. ans: text
sims[:5]:
54, 0.65560305, password: '' u'long-clickable' u'enter' u'your' u'password' 1268 132 u'default' u'android' u'widget' u'edittext' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'ej'
23, 0.5791167, text: '' u'long-clickable' u'enter' u'username' u'or' u'card' u'number' 1268 132 u'default' u'android' u'widget' u'edittext' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'ej'
0, 0.48025247, image: u'search' u'button' u'search' u'button' 0 0 u'search' u'button' u'android' u'view' u'view' u'java' u'lang' u'object' u'search' u'button' u'android' u'widget' u'imageview'
27, 0.46489322, text: '' u'long-clickable' u'nickname' u'optional' 1268 -71 u'default' u'android' u'widget' u'edittext' u'android' u'widget' u'textview' u'android' u'view' u'view' u'java' u'lang' u'object' u'content' u'com' u'konylabs' u'api' u'ui' u'ej'
10, 0.3228951, image: u'abmlocator' u'map' u'abmlocator' u'map' 0 0 u'abmlocator' u'map' u'android' u'view' u'view' u'java' u'lang' u'object' u'abmlocator' u'map' u'android' u'widget' u'imageview'
-----
corpus: 52
corpus: 20
corpus: 57
corpus: 34
corpus: 22
corpus: 41
corpus: 26
corpus: 61
corpus: 11
corpus: 33
# training data: 64
total inferred: 17
# of multiple types: 0
correction rate: 14/17 (0.823529)
```
Further increase in training files and iterations will improve the performance of this method. Future plans include integration with Droidbot, where once we obtain the xml dump of the screen using Accessibility services which fetches UI structure as a Java object, we can run ```language_transformations.py``` to get the type of UI views contained and accordingly take actions like use a pre-defined email and password once the UI view is identified to be an email or password type or to avoid clicking ad type UI view once it is classified as one using our code. 

## Documentation
Intially we have to keep all the json files in ```json_dir_1``` directory. Then run the following from command prompt
```
python corpus_creater.py
```
You will have the corpus created in the ```corpus_dir_1``` directory. Full corpus can be found [here](https://drive.google.com/open?id=1JivdzqxEiZciR7N6DxhR0rPfYKJgy2xq).
Then run the following
```
python language_transformations.py
```
This will create three files, ```trial.mm, trial.tfidf, trial.index``` which will be used for classifying test cases. Change the ```top_directory``` in ```language_transformations.py``` file to the location where the corpus is saved.

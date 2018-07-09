## Documentation
Intially you have to keep all the json files in ```json_dir_1``` directory. Then run the following from command prompt
```
python activity_detector.py
```
You will have list of activities created in the```activity_list.csv``` file. Using all the json files, the ```complete_activity_list.csv``` has been created.
Then run the following
```
python activity_cluster.py
```
This will generate clusters of activities generated using the Affinity Propagation algorithm using the Levenshtein distance and 2% of the activities from the shuffled list which can be found in the ```cluster_output.txt``` file.
From this list, we can find some prominent activity clusters which will be used to label the training data for the CNNs. The prominent activity clusters are -
 1. SignUp/SignIn/Login/Register
 2. TermsOfUse/TermsOfService/TermsAndConditions
 3. Photo/Video/Camera/Gallery
 4. Ad
 5. Settings
 6. Preferences
 7. Search
 8. Browser
 9. List/Selection/Category/Chooser
 10. OnBoarding/Wizard/Tutorial
 11. Welcome/Landing/Intro
 12. Home/Main/MainTab/HomeScreen
 13. Tab/Menu
 14. Profile/UserProfile
 15. Password/PasswordChange/Authentication
 16. History
 17. Notifications
 18. Reader
 19. Community
 20. Navigation
 21. Time
 22. Weather
 23. Favourites

Now the number of instances for each of them will be calculated using the following python script.
```
python activity_counter.py
```
From here, we mainly go forward with three significant clusters for now, which are as follows -
 1. Login 2521
 2. Onboarding 1259
 3. Settings 1588
 
After this we run the following
```
python create_dataset.py
```
It will create the following directory structure in screenshots directory
```
screenshots
+-- test
|   +-- login
|   +-- settings
|   +-- onboarding
+-- train
|   +-- login
|   +-- settings
|   +-- onboarding
+-- valid
|   +-- login
|   +-- settings
|   +-- onboarding
```
Once this is done, we run the following
```
python cnn.py
```
It has two models inside it, one being a one 2D ConvNet layer while other being a VGG16 model trained on ImageNet dataset.
Their architecture and performance is as below -
 1. Model 1
 ```
 Architecture 
 
 Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_5 (Conv2D)            (None, 222, 222, 32)      896       
_________________________________________________________________
flatten_4 (Flatten)          (None, 1577088)           0         
_________________________________________________________________
dense_6 (Dense)              (None, 3)                 4731267   
=================================================================
Total params: 4,732,163
Trainable params: 4,732,163
Non-trainable params: 0
_________________________________________________________________

Performance 

Epoch 1/5
397s - loss: 10.7262 - acc: 0.3342 - val_loss: 9.8858 - val_acc: 0.3867
Epoch 2/5
308s - loss: 10.8468 - acc: 0.3269 - val_loss: 11.3901 - val_acc: 0.2933
Epoch 3/5
273s - loss: 10.7857 - acc: 0.3308 - val_loss: 10.1007 - val_acc: 0.3733
Epoch 4/5
273s - loss: 10.8126 - acc: 0.3292 - val_loss: 11.1752 - val_acc: 0.3067
Epoch 5/5
273s - loss: 10.6021 - acc: 0.3422 - val_loss: 11.0678 - val_acc: 0.3133
```
2. Model 2
```
Architecture

Layer (type)                 Output Shape              Param #   
=================================================================
input_2 (InputLayer)         (None, 224, 224, 3)       0         
_________________________________________________________________
block1_conv1 (Conv2D)        (None, 224, 224, 64)      1792      
_________________________________________________________________
block1_conv2 (Conv2D)        (None, 224, 224, 64)      36928     
_________________________________________________________________
block1_pool (MaxPooling2D)   (None, 112, 112, 64)      0         
_________________________________________________________________
block2_conv1 (Conv2D)        (None, 112, 112, 128)     73856     
_________________________________________________________________
block2_conv2 (Conv2D)        (None, 112, 112, 128)     147584    
_________________________________________________________________
block2_pool (MaxPooling2D)   (None, 56, 56, 128)       0         
_________________________________________________________________
block3_conv1 (Conv2D)        (None, 56, 56, 256)       295168    
_________________________________________________________________
block3_conv2 (Conv2D)        (None, 56, 56, 256)       590080    
_________________________________________________________________
block3_conv3 (Conv2D)        (None, 56, 56, 256)       590080    
_________________________________________________________________
block3_pool (MaxPooling2D)   (None, 28, 28, 256)       0         
_________________________________________________________________
block4_conv1 (Conv2D)        (None, 28, 28, 512)       1180160   
_________________________________________________________________
block4_conv2 (Conv2D)        (None, 28, 28, 512)       2359808   
_________________________________________________________________
block4_conv3 (Conv2D)        (None, 28, 28, 512)       2359808   
_________________________________________________________________
block4_pool (MaxPooling2D)   (None, 14, 14, 512)       0         
_________________________________________________________________
block5_conv1 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_conv2 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_conv3 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_pool (MaxPooling2D)   (None, 7, 7, 512)         0         
_________________________________________________________________
flatten (Flatten)            (None, 25088)             0         
_________________________________________________________________
fc1 (Dense)                  (None, 4096)              102764544 
_________________________________________________________________
fc2 (Dense)                  (None, 4096)              16781312  
_________________________________________________________________
dense_5 (Dense)              (None, 3)                 3003      
=================================================================
Total params: 134,263,547
Trainable params: 3,003
Non-trainable params: 134,260,544
_________________________________________________________________

Performance

Epoch 1/5
3225s - loss: 1.0665 - acc: 0.5250 - val_loss: 1.0489 - val_acc: 0.5600
Epoch 2/5
2988s - loss: 1.0331 - acc: 0.5725 - val_loss: 1.0176 - val_acc: 0.5867
Epoch 3/5
3007s - loss: 1.0088 - acc: 0.5786 - val_loss: 0.9925 - val_acc: 0.6000
Epoch 4/5
2998s - loss: 0.9818 - acc: 0.5881 - val_loss: 0.9777 - val_acc: 0.5733
Epoch 5/5
3019s - loss: 0.9576 - acc: 0.5989 - val_loss: 0.9682 - val_acc: 0.5867
```
Model 2 clearly outperforms Model 1, however in model 2, currently none of the layers are trained at all, that is, taking the features learnt purely from ImageNet dataset, the performance is around 56% in worst case. Better performance can be achieved by freezing only the 2D ConvNet layers while training the Fully Connected layers with the new dataset. Some data augmentation is also to be done soon to expand the dataset.



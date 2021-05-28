from PIL import Image
from os import walk
import os
import random
from sklearn.model_selection import train_test_split
import shutil
import sys
datafolder=sys.argv[1]
if len(sys.argv)>=3:
    mode=sys.argv[2]
else:
    mode="UGATIT"
if not os.path.exists(datafolder):
    os.mkdirs(datafolder)
if not os.path.exists("part1.zip"):
    os.system("wget -P . http://www.cs.ucf.edu/~aroshan/index_files/Dataset_PitOrlManh/zipped\%20images/part1.zip --no-check-certificate")
if not os.path.exists("01_images.zip"):
    os.system("wget -P . https://download.visinf.tu-darmstadt.de/data/from_games/data/01_images.zip --no-check-certificate")


tempA=os.path.join(datafolder,"tempA")
if not os.path.exists(tempA):
    os.mkdirs(tempA)
os.system("unzip 01_images.zip -d %s" % tempA)
tempB=os.path.join(datafolder,"tempB")
if not os.path.exists(tempB):
    os.mkdirs(tempB)
os.system("unzip part1.zip -d %s" % tempB)
if mode=="UGATIT":
    trainA=os.path.join(datafolder,"trainA")
    trainB=os.path.join(datafolder,"trainB")
    testA=os.path.join(datafolder,"testA")
    testB=os.path.join(datafolder,"testB")
else:
    trainA=os.path.join(datafolder,"train/A")
    trainB=os.path.join(datafolder,"train/B")
    testA=os.path.join(datafolder,"test/A")
    testB=os.path.join(datafolder,"test/B")
if not os.path.exists(trainA):
    os.mkdirs(trainA)
if not os.path.exists(trainB):
    os.mkdirs(trainB)
if not os.path.exists(testA):
    os.mkdirs(testA)
if not os.path.exists(testB):
    os.mkdirs(testB)



_, _, dataset = next(walk(tempA))
train, test = train_test_split(dataset, test_size=0.2)
     
for filename in train:
    shutil.move(os.path.join(tempA,filename), trainA)
for filename in test:
    shutil.move(os.path.join(tempA,filename), testA)
     
       
_, _, train = next(walk(trainA))
_, _, test = next(walk(testA))
print(len(train), len(test))




_, _, images = next(walk(tempB))
     
for image in images:
      
    if image.endswith('_2.jpg'):
        im = Image.open(os.path.join(tempB,image))
        width, height = im.size
        
        im_crop = im.crop((5,150,width-5,height-20))
        im_crop.save(os.path.join(trainB,image))



_, _, dataset = next(walk(trainB))
train, test = train_test_split(dataset, test_size=0.2)
       
for filename in test:
    shutil.move(os.path.join(root,filename), testB)
       
_, _, train = next(walk(trainB))
_, _, test = next(walk(testB))
print(len(train), len(test))




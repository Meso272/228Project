from PIL import Image
from os import walk
import os
import random
from sklearn.model_selection import train_test_split
import shutil
import sys
datafolder=sys.argv[1]
A_zip=sys.argv[2]#01_images.zip
B_zip=sys.argv[3]#part1.zip
if len(sys.argv)>=5:
    mode=sys.argv[4]
else:
    mode="UGATIT"
if len(sys.argv)>=6:
    skipunzip=int(sys.argv[5])
else:
    skipunzip=False
if not os.path.exists(datafolder):
    os.makedirs(datafolder)

if not os.path.exists(A_zip):
    os.system("wget -P . https://download.visinf.tu-darmstadt.de/data/from_games/data/%s --no-check-certificate" % A_zip)
if not os.path.exists(B_zip):
    os.system("wget -P . http://www.cs.ucf.edu/~aroshan/index_files/Dataset_PitOrlManh/zipped\%20images/%s --no-check-certificate" % B_zip)

tempA=os.path.join(datafolder,"tempA")
if not os.path.exists(tempA):
    os.makedirs(tempA)
tempB=os.path.join(datafolder,"tempB")
if not os.path.exists(tempB):
    os.makedirs(tempB)
if not skipunzip:
    os.system("unzip %s -d %s" % (A_zip,tempA))
    os.system("unzip %s -d %s" % (B_zip,tempB))
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
    os.makedirs(trainA)
if not os.path.exists(trainB):
    os.makedirs(trainB)
if not os.path.exists(testA):
    os.makedirs(testA)
if not os.path.exists(testB):
    os.makedirs(testB)


tempA_images=os.path.join(tempA,"images")
dataset = os.listdir(tempA_images)
for image in dataset:
    im = Image.open(os.path.join(tempA_images,image))
    im.resize((320,256)).save(os.path.join(tempA_images,image))
dataset = os.listdir(tempA_images)
train, test = train_test_split(dataset, test_size=0.2)
     
for filename in train:
    try: 
        shutil.move(os.path.join(tempA_images,filename), trainA)
    except:
        pass
for filename in test:
    try: 
        shutil.move(os.path.join(tempA_images,filename), testA)
    except:
        pass
       
train = os.listdir(trainA)
test = os.listdir(testA)
print(len(train), len(test))




images =os.listdir(tempB)
     
for image in images:
      
    if image.endswith('_2.jpg'):
        im = Image.open(os.path.join(tempB,image))
        width, height = im.size
        
        im_crop = im.crop((5,150,width-5,height-20))
        im_crop=im_crop.resize((320,256))
        im_crop.save(os.path.join(tempB,image))



dataset = os.listdir(tempB)
train, test = train_test_split(dataset, test_size=0.2)
for filename in train:
    try: 
        shutil.move(os.path.join(tempB,filename), trainB)
    except:
        pass 
for filename in test:
    try: 
        shutil.move(os.path.join(tempB,filename), testB)
    except:
        pass
       
train = os.listdir(trainB)
test = os.listdir(testB)
print(len(train), len(test))

os.system("rm -rf %s" %tempA)
os.system("rm -rf %s" %tempB)




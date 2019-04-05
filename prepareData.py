import shutil
import os
from random import shuffle

# Create dictionary for our 10 classes
class_dict = {}
with open("classes.txt","r") as txt:
    classes = [line.strip() for line in txt.readlines()]
    class_dict = dict(zip(classes,range(len(classes))))

# Split into train and test sets - Creates 'train.txt' and 'test.txt' as well copying the images to their appropriate folders
def createData(imgroot,classes,ratio):
    with open("train.txt",'w') as train:
        with open("test.txt",'w') as test:
            trainList = []
            testList = []

            for c in classes:
                imgList = []
                files = os.listdir(os.path.join(imgroot,c))
                for f in files:
                    imgList.append(f + " " + str(class_dict[c]))
                shuffle(imgList)
                split = int(ratio * len(imgList))
                for trainImg in imgList[:split]:
                    trainList.append(trainImg)
                    shutil.copyfile(imgroot + "\\" + c + "\\" + trainImg.split(" ")[0],"D:\\Projects\\Advertising\\train\\" + trainImg.split(" ")[0])
                for testImg in imgList[split:]:
                    testList.append(testImg)
                    shutil.copyfile(imgroot + "\\" + c + "\\" + testImg.split(" ")[0],"D:\\Projects\\Advertising\\test\\" + testImg.split(" ")[0])

            shuffle(trainList)
            shuffle(testList)
            for trainImgName in trainList:
                train.write(trainImgName + "\n")
            for testImgName in testList:
                test.write(testImgName + "\n")

imgroot = "D:\Projects\Images-10"
createData(imgroot,classes,0.7)

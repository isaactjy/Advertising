import cv2
import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt

class_dict = {}
with open("classes.txt","r") as txt:
    classes = [line.strip() for line in txt.readlines()]
    class_dict = dict(zip(range(len(classes)),classes))

def loadImages(root,txt):
    with open(txt,"r") as f:
        all_imgs = []
        all_classes = []
        for line in f.readlines(): 
            imgname = line.split(" ")[0]
            img_arr = cv2.imread(root + imgname)
            img_arr = img_arr[:,:,::-1]
            img_arr = cv2.resize(img_arr,(128,128))
            all_imgs.append(img_arr)
            label = int(line.split(" ")[1].strip("\n"))
            all_classes.append(label)
        return np.array(all_imgs),np.array(all_classes)

train_root = "D:\\Projects\\Advertising\\train\\"
test_root = "D:\\Projects\\Advertising\\test\\"
X_train,y_train = loadImages(train_root,"D:\\Projects\Advertising\\train.txt")
X_test,y_test = loadImages(test_root,"D:\\Projects\\Advertising\\test.txt")

print(X_train.shape)

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_train[i], cmap=plt.cm.binary)
    plt.xlabel(class_dict[y_train[i]])
plt.show()

import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(128, 128, 3)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100)

test_loss, test_acc = model.evaluate(X_test, y_test)

print('Test accuracy:', test_acc)
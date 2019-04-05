import cv2
import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

class_dict = {}
with open("classes.txt","r") as txt:
    classes = [line.strip() for line in txt.readlines()]
    class_dict = dict(zip(range(len(classes)),classes))

train_csv = pd.read_csv("D:\\Projects\\Advertising\\train.txt")
print(train_csv)
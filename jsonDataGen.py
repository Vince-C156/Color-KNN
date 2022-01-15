import numpy as np
import cv2
import json
from matplotlib import pyplot as plt
import os
from collections import defaultdict

"""
this script takes the images from a user desired directory and creates a
dictionary.

The keys of the dictionary are the nested directories within selected
directory and the values are lists of user selected pixel coordinates
from every images in each respective directory

Then it dumps and writes this dictionary into a json
"""

if __name__ == '__main__':

    trainDir = "training_dataset"

    #change to true for debug print statements
    dev = False

    data = os.listdir(trainDir)

    jsonDict = defaultdict(list)

    for color in data:

        if dev:

            print("CURRENT COLOR")
            print("================")
            print(color)
            print("================")
            print("CURRENT DIR")
            print("================")
            print(os.getcwd())
            print("================")
        
        colorDir = trainDir + "\\" + color

        print("COLOR DIRECTORY")
        print("======================")
        
        print(colorDir)
        os.chdir(colorDir)
        for img_name in os.listdir():
            print(img_name)
            img = cv2.imread(img_name)
            imgLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

            imgLAB = imgLAB.tolist()

            x_coord = 30
            y_coord = 2

            jsonDict[color].append(imgLAB[y_coord][x_coord])



        os.chdir("..")
        os.chdir("..")

    print(jsonDict.items())

    with open('data.json', 'w') as data_dumped:
        json.dump(jsonDict, data_dumped)

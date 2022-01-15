import numpy as np
import cv2
import json
from matplotlib import pyplot as plt
import os
from collections import defaultdict
from matplotlib.colors import ListedColormap
from sklearn import neighbors

"""
utils for fitting radius NN classifer
"""

#function to map color string to color value from interrop
def color2class(color):

    if color == 'white':
        return 1
    elif color == 'black':
        return 2
    elif color == 'gray':
        return 3
    elif color == 'red':
        return 4
    elif color == 'blue':
        return 5
    elif color == 'green':
        return 6
    elif color == 'yellow':
        return 7
    elif color == 'purple':
        return 8
    elif color == 'brown':
        return 9
    elif color == 'orange':
        return 10
    else:
        return 0

#call this function to fit a radius NN to data in data.json
def RKNN_fit():
    #fits radius NN and returns nearest neighbor classifer object along with
    #array of class labels associated with every point in training points
    X = list([])
    Y = list([])
    color_Y = list([])


    with open('data.json') as data:
        trainingDataDict = json.load(data)

    print(trainingDataDict)
    for color, values in trainingDataDict.items():
        target = color2class(color)

        print(values)

        for labVal in values:
            X.append(labVal)
            Y.append(target)
            color_Y.append(color)

    print(X)
    print("=====================")
    print(Y)

    fig = plt.figure()
    ax = plt.axes(projection = '3d')

    for idx, val in enumerate(X):
        ax1 = val[0]
        ax2 = val[1]
        ax3 = val[2]

        c = color_Y[idx]

        ax.scatter3D(ax1, ax2, ax3, color = c)

    plt.show()

    n_neighbors = 5
    weights = 'distance'
    #clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    R_KNN = neighbors.RadiusNeighborsClassifier(radius=50)

    R_KNN.fit(X,Y)

    return Y, R_KNN 




import csv
import scipy
import numpy as np
import pandas as pd 
import threading
import generateRandomSequence as g
import threading
import math


def flushholder(holder):
    pd.DataFrame(holder).to_csv("backup.csv")


def bulkLoad(number):
    holder = g.generateRandomSequence()
    holder = mergesort(holder)
    flushholder(holder)
    mainarray = []
    smallarray = []
    count = 0
    for i in holder:
        if(count == number):
            mainarray.append(smallarray)
            smallarray = []
            count = 0
        smallarray.append(i)
        count+=1
    if(len(smallarray)>0):
        mainarray.append(smallarray)
    flushholder(mainarray)

def mergesort(array):

    ### Fill out MergeSort here
    return np.sort(array)

array = []
def backup(root, number):
    if hasattr(root, 'children'):
        for i in root.children:
            backup(i, number)
    else:
        backuphelper(root, number)
    return 
           
def backuphelper(root, number):
    if hasattr(root, 'actvalues'):
        for i in root.actvalues:
            global array
            array.append(i)
        if(root.right == None):
            mainarray = []
            smallarray = []
            count = 0
            for i in array:
                if(count == number):
                    mainarray.append(smallarray)
                    smallarray = []
                    count = 0
                smallarray.append(i)
                count+=1
            if(len(smallarray)>0):
                mainarray.append(smallarray)
            flushholder(mainarray)

    



    
    
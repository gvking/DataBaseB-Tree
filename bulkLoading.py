
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
    
    

def backup(root, count, number):
    global array
    if hasattr(root, 'children'):  
            for i in range(0, len(root.children)):
                backup(root.children[i], count+1, number) 
    if(count == 0):
        array = np.sort(array)
        mainarray = []
        smallarray = []
        countn = 0
        for i in array:
            if(countn == number):
                mainarray.append(smallarray)
                smallarray = []
                countn = 0
            smallarray.append(i)
            countn+=1
        if(len(smallarray)>0):
            mainarray.append(smallarray)
        flushholder(mainarray)
        array = []
    if hasattr(root, 'actvalues'): 
        if(root.actvalues == []):
            hi = "ji"
        else:
            temp = []
            for i in root.actvalues:
                temp.append(i)
            for i in temp:
                array.append(float(i))


    
    
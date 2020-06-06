
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
    holder = np.sort(holder)
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







    
    
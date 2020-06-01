
import csv
import scipy
import numpy as np
import pandas as pd 
import threading
import generateRandomSequence as g
import threading


def flushholder(holder):
    pd.DataFrame(holder).to_csv("backup.csv")
print("What fill factor")
fillFactor = float(input())/100
print("what is fanout factor")
fanFactor = input()
holder = g.generateRandomSequence()
holder = np.sort(holder)
flushholder(holder)
number = float(fanFactor) * float(fillFactor)
number = int(number)
print(number)
mainarray = []
smallarray = []
count = 0
for i in holder:
    if(count == number):
        mainarray.append(smallarray)
        print(smallarray)
        smallarray = []
        count = 0
    smallarray.append(i)
    count+=1
flushholder(mainarray)







    
    
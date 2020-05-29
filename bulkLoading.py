
import csv
import scipy
import numpy as np
import pandas as pd 
import threading
import generateRandomSequence as g
import threading

holder = []
def bulkLoading(sequence):
    holder = mymergesort(sequence)
    return holder
def mymergesort(sequence):
    mid = len(sequence)/2
    flushholder(holder)
    return np.sort(sequence)
def flushholder(holder):
    pd.DataFrame(holder).to_csv("backup.csv")
flushholder
holder = g.generateRandomSequence()
holder = bulkLoading(holder)
for i in holder:
    print(i)





    
    
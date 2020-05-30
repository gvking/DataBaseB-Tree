import csv
class InternalNode():
    value = 
    children = []
    def construct(inputvalue):
        value = inputvalue
    def addChild(child):
        children.append(child)
    
    
class LeafNodePages():
    values = []
    left = None
    right = None 

holder = []
count = 0

with open('backup.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if(count > 0):
            holder.append(row[1])
        else:
            count+=1



import csv
import math
import numpy as np
import statistics
class InternalNode():
    value = -1
    children = []
    
    
class LeafNodePages():
    value = -1
    actvalues = []
    left = None
    right = None 

def searchforval(root, val):
    print(val)
    if hasattr(root, 'children'):
        while root.children:
            if( val < float(root.children[0].value)):
                return searchforval(root.children[0], val)
                break          
            for i in range(1, len(root.children)):
                if(val >= float(root.children[i-1].value) and val < float(root.children[i].value)):
                    return searchforval(root.children[i-1], val)
                    return searchforval(root.children[i], val)   
    if hasattr(root, 'actvalues'):
        for i in root.actvalues:
            if (float(i) == float(val)):
                return True


def createtree():
    holder = []
    count = 0
    number = 0

    with open('backup.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if(count > 0):
                if(count == 1):
                    number = len(row) - 1
                    leafnode = LeafNodePages()
                    leafnode.actvalues = row[1:]
                    [float(i) for i in leafnode.actvalues]
                    leafnode.value = leafnode.actvalues[int(len(leafnode.actvalues)/2)]
                    holder.append(leafnode)
                    #print(leafnode.values)
        
                    count+=1
                else:
                    leafnode = LeafNodePages()
                    leafnode.actvalues = row[1:]
                    for i in leafnode.actvalues:
                        if(i != ''):
                            float(i)
                        else:
                            del i
                    leafnode.value = leafnode.actvalues[int(len(leafnode.actvalues)/2)]
                    holder[count-2].right = leafnode
                    leafnode.left = holder[count-2]
                    holder.append(leafnode)
                    #print(leafnode.left.values)
                    count+=1 
            else:
                count+=1


    count = 0
    num = len(holder)

    while(num > 1):
        num = num/number
        num = math.ceil(num)
        newholder = []
        print(num)
        for i in range(num):
            newinternal = InternalNode()
            for k in range(count, count+num):
                if(k >= len(holder)):
                    break
                else:
                    newinternal.children.append(holder[k])
            count = count+num
            newinternal.value = newinternal.children[int(len(newinternal.children)/2)].value
            newholder.append(newinternal)

        holder = newholder
    return holder[0]
root = createtree()
print(root.value)
boolean = searchforval(root, 2148724404.0)
print(boolean)


        












# root = None
# while(len(holder) > 0):
#     length = len(holder)
#     if(length == 1):
#         root = holder[0]
#     count = 0
#     newholder = []
#     for i in range(length):
#         if(count == number):
#             newholder.append(newholder)
#             count == 0
#         internal = InternalNode()
#         internal.children.append(holder[i])
#         count +=1
#     holder = newholder






        






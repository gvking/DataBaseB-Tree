import csv
import math
import numpy as np
import bulkLoading as bl
import time
import pandas as pd



class InternalNode():
    value = -1
    children = []
    parent = None
    
    
class LeafNodePages():
    value = -1
    actvalues = []
    left = None
    right = None
    parent = None

def searchforval(root, val):
    if hasattr(root, 'children'): 
            if( val < float(root.children[0].value)):
                bool1 = searchforval(root.children[0], val) 
                if( bool1 == True):
                    return True      
            for i in range(1, len(root.children)):
                if(val >= float(root.children[i-1].value) and val <= float(root.children[i].value)):
                    bool2 = searchforval(root.children[i], val) 
                    bool3 = searchforval(root.children[i-1], val) 
                    if(bool2 == True or bool3 == True):
                        return True
            if(val >= float(root.children[-1].value)):
                return searchforval(root.children[-1], val)
                
    if hasattr(root, 'actvalues'):
        for i in root.actvalues:
            if (float(i) == float(val)):
                return True


def height(root, count):
    if hasattr(root, 'children'):
        return height(root.children[0], count+1)
    else:
        return count

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
                    holderarray = []
                    for i in range(len(leafnode.actvalues)):
                        if(leafnode.actvalues[i] == ''):
                            holderarray.append(i)
                    randcount = 0
                    for i in holderarray:
                        del leafnode.actvalues[i-randcount]
                        randcount +=1
                    index = int(len(leafnode.actvalues)/2)
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
        count = 0
        num = num/number
        num = math.ceil(num)
        newholder = []
        for i in range(num):
            newinternal = InternalNode()
            newinternal.children = []
            newinternal.value = -1
            for k in range(count, count+number):
                if(k >= len(holder)):
                    break
                else:
                    newinternal.children.append(holder[k])
            
            newinternal.value = newinternal.children[int(len(newinternal.children)/2)].value
            for k in range(count, count+number):
                if(k >= len(holder)):
                    break
                else:
                    holder[k].parent = newinternal
            newholder.append(newinternal)
            count = count+number
        holder = newholder
    return holder[0], number

inp = 0
root = None
count = 0
fillFactor = 0
fanFactor  = 0
number = 0
logofuncommittedActs = []
while(inp != "E"):
    print("Insert N for new tree, R for restore, I for insert, F for find, B to backup, H for height, or E to exit")
    inp = input()
    if(count == 5):
        inp = "B"
        print("Interrupting your action")
        print("Force back up ")
        count = 0
    if(inp == "N"):
        print("You have chosen to create a new tree! We will generate and bulkload the tree.")
        print("What fill factor")
        fillFactor = float(input())/100
        print("what is fanout factor")
        fanFactor = input()
        number = float(fanFactor) * float(fillFactor)
        number = math.ceil(number)
        beginning = time.time()
        bl.bulkLoad(number)
        root, number = createtree()
        end = time.time()
        timediff = end - beginning
        print("time took (in seconds):", timediff)
        logentry = []
        logentry.append("N")
        logentry.append(-1)
        logentry.append(count)
        logofuncommittedActs.append(logentry)
        count+=1
    if(inp == "R"):
        with open('log.csv') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if(row[1] == "I"):
                    print("An insert wasn't comitted into storage.")
                    print("Inserting " + str(row[2]))
                        
 
        beginning = time.time()
        root, number = createtree()
        end = time.time()
        timediff = end - beginning
        print("time took (in seconds):", timediff)
        logentry = []
        logentry.append("R")
        logentry.append(-1)
        logentry.append(count)
        logofuncommittedActs.append(logentry)
        count +=1
    if(inp == "I"):
        print("What value do you want to insert?")
        value = float(input())
        #Insert function over here
        logentry = []
        logentry.append("I")
        logentry.append(value)
        logentry.append(count)
        logofuncommittedActs.append(logentry)
        count+=1
    if(inp == "F"):
        print("What value do you want to search for?")
        value = input()
        beginning = time.time()
        boolean = searchforval(root, float(value))
        end = time.time()
        timediff = end - beginning
        print("time took (in seconds):", timediff)
        if(boolean == True):
            print("The value was found!")
        else:
            print("Sorry, we couldn't find that value")
        logentry = []
        logentry.append("F")
        logentry.append(value)
        logentry.append(count)
        logofuncommittedActs.append(logentry)
        count +=1
    if(inp == "B"):
        print("Backing up right now!")
        beginning = time.time()
        bl.backup(root, number)
        end = time.time()
        timediff = end - beginning
        print("time took (in seconds):", timediff)
        logofuncommittedActs = []
        count = 0
    if(inp == "H"):
        print(height(root, 1))
        count +=1
    if( inp == "Test"):
        print("You've entered the hidden function!")
        print(root.children[0].children[0].parent.value)
        print(root.children[0].value)
    pd.DataFrame(logofuncommittedActs).to_csv("log.csv")

# root = createtree()
# print(root.value)
# boolean = searchforval(root, 2148724404.0)
# print(boolean)


        












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






        






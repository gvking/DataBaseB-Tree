import csv
import math
import numpy as np
import bulkLoading as bl



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
        if(val < float(root.children[0].value)):
            return searchforval(root.children[0], val)
        for i in range(1, len(root.children)):
            if(val >= float(root.children[i-1].value) and val < float(root.children[i].value)):
                return searchforval(root.children[i-1], val)
                return searchforval(root.children[i], val)
        if(val >= float(root.children[-1].value)):
            return searchforval(root.children[-1], val)

                
    if hasattr(root, 'actvalues'):
        for i in root.actvalues:
            print(i)
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
    print(num)
    while(num > 1):
        count = 0
        num = num/number
        num = math.ceil(num)
        newholder = []
        print(num)
        for i in range(num):
            newinternal = InternalNode()
            newinternal.children = []
            newinternal.value = -1
            for k in range(count, count+number):
                if(k >= len(holder)):
                    break
                else:
                    newinternal.children.append(holder[k])
            count = count+number
            newinternal.value = newinternal.children[int(len(newinternal.children)/2)].value
            print(newinternal.value)
            newholder.append(newinternal)
        holder = newholder
    return holder[0], number

print("Welcome! Insert N for new tree, R for restore, I for insert, F for find, B to backup, or E to exit")
inp = input()
root = None
count = 0
fillFactor = 0
fanFactor  = 0
number = 0
while(inp != "E"):
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
        bl.bulkLoad(number)
        root, number = createtree()
        print("Insert N for new tree, R for restore, I for insert, F for find, B to backup, or E to exit")
        inp = input()
        count+=1
    if(inp == "R"):
        root, number = createtree()
        print("Insert N for new tree, R for restore, I for insert, F for find, B to backup, or E to exit")
        inp = input()
    if(inp == "I"):
        print("What value do you want to insert?")
        value = float(input())
        #Insert function over here

        print("Insert N for new tree, R for restore, I for insert, F for find, B to backup, or E to exit")
        inp = input()
        count+=1
    if(inp == "F"):
        print("What value do you want to search for?")
        value = input()
        boolean = searchforval(root, float(value))
        if(boolean == True):
            print("The value was found!")
        else:
            print("Sorry, we couldn't find that value")
        print("Insert N for new tree, R for restore, I for insert, F for find, B to backup, or E to exit")
        inp = input()
    if(inp == "B"):
        print("Backing up right now!")
        bl.backup(root, number)
        print("Insert N for new tree, R for restore, I for insert, F for find, B to backup, or E to exit")
        inp = input()


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






        






import csv
import math
import numpy as np
import bulkLoading as bl
import time
import pandas as pd

def insert(root, val, thresh):
    #first find the leaf node
    stopit = False
    current = root
    c=0
    while stopit == False:
        if len(current.children) == 1:
            if hasattr(current.children[0].children[0], 'actvalues'):
                current = current.children[0].children[0]
                stopit = True
            else:
                current = current.children[0]
        else:
            for i in range(len(current.children)):
                if val < float(current.children[i].value) and i==0: #traverse
                    if hasattr(current.children[i].children[0], 'actvalues'): #the child is a leaf node
                        current = current.children[i].children[0]
                        stopit = True
                        break
                    else: #child is intermediate node to keep traversing via while loop
                        current = current.children[i]
                        break
                elif i+1 == len(current.children)-1 and val >= float(current.children[i].value) and val >= float(current.children[i+1].value):
                    if hasattr(current.children[i+1].children[0], 'actvalues'): #the child is a leaf node
                        current = current.children[i+1].children[0]
                        stopit = True
                        break
                    else: #child is intermediate node to keep traversing via while loop
                        current = current.children[i+1]
                        break
                elif val >= float(current.children[i].value) and val < float(current.children[i+1].value): #traverse down
                    if hasattr(current.children[i].children[0], 'actvalues'): #the child is a leaf node
                        current = current.children[i].children[0]
                        stopit = True
                        break
                    else: #child is intermediate node to keep traversing via while loop
                        current = current.children[i]
                        break
            if stopit==True:
                break
            
    #next insert into correct leaf
    ct = 0
    while ct==0:
        current2 = current.right
        for i in range(len(current.actvalues)):
            if(len(current.actvalues) == 0):
                current.actvalues.append(0)
                ct+=1
                break
            if val < float(current.actvalues[i]):
                current.actvalues.insert(0, str(val))
                ct+=1
                break
            elif len(current.actvalues) == 1:
                current.actvalues.append(str(val))
                ct+=1
                break
            elif i+1 <= len(current.actvalues)-1 and val >= float(current.actvalues[i]) and val < float(current.actvalues[i+1]):
                current.actvalues.insert(i+1, str(val))
                ct+=1
                break
            elif (i == len(current.actvalues)-1 and val >= float(current.actvalues[i]) and current.right == None):
                current.actvalues.append(str(val))
                ct+=1
                break
            elif (i == len(current.actvalues)-1 and val >= float(current.actvalues[i]) and val < float(current2.actvalues[0])):
                current.actvalues.append(str(val))
                ct+=1
                break
            elif (i == len(current.actvalues)-1 and val >= float(current.actvalues[i]) and val >= float(current2.actvalues[0])):
                current = current.right
    parentStuff = None
    tempHolder = []
    newinternalNode = None
    while( (hasattr(current, 'actvalues') and len(current.actvalues) >= thresh) or len(current.children) >= thresh):
        if(current.parent!= None):
            if(hasattr(current, 'actvalues')):
                parentStuff = current.parent
                countStuff = 0
                temp = []
                for k in current.actvalues:
                    temp.append(k)
                    countStuff +=1
                    if(countStuff == thresh ):
                        tempHolder.append(temp)
                        temp = []
                        countStuff = 0
                if(len(temp) > 0):
                    tempHolder.append(temp)
                newtemp = []
                for i in tempHolder:
                    newinternalNode = None
                    newinternalNode = LeafNodePages()
                    newinternalNode.value = i[int(len(i)/2)] 
                    newinternalNode.parent = current.parent
                    newinternalNode.actvalues = i
                    newtemp.append(newinternalNode)
                index = current.parent.children.index(current)
                del current.parent.children[index]
                for i in newtemp:
                    current.parent.children.insert(index, i)
                    index+=1
                current = current.parent
                break

    while(len(current.children) >= thresh):
        if(current.parent != None):
                bigParental = current.parent
                bigtemp = []
                for i in current.children:
                    bigtemp.append(i)
                kindabigHolder = []
                bigHolder = []
                coolcount = 0
                for i in bigtemp:
                    coolcount+=1
                    kindabigHolder.append(i)
                    if(coolcount == thresh):
                        coolcount = 0
                        bigHolder.append(kindabigHolder)
                        kindabigHolder = []
                if(len(kindabigHolder) > 0):
                    bigHolder.append(kindabigHolder)
                newerHolder = []
                for i in bigHolder:
                    newinternalNode = None
                    newinternalNode = LeafNodePages()
                    for k in i:
                        print("value:", k.value)
                    newinternalNode.value = float(i[int(len(i)/2)].value)
                    print(newinternalNode.value)
                    newinternalNode.children = i
                    newinternalNode.parent = bigParental
                    newerHolder.append(newinternalNode)
                index = current.parent.children.index(current)
                index = current.parent.children.index(current)
                del current.parent.children[index]
                for i in newerHolder:
                    current.parent.children.insert(index, i)
                    index+=1
                
                current = current.parent
                if(current == root):
                    break
    return root        


            

        #         print(current.value)
        #         countStuff = 0
        #         temp = []
        #         tempHolder = []
        #         for k in current.children:
        #             if(countStuff == thresh):
        #                 tempHolder.append(temp)
        #                 temp = []
        #                 countStuff = 0
        #             temp.append(k)
        #             countStuff +=1
        #         if(len(temp) > 0):
        #             tempHolder.append(temp)
        #         newtemp = []
        #         for i in tempHolder:
        #             newinternalNode = None
        #             newinternalNode = InternalNode()
        #             newinternalNode.value = i[int(len(i)/2)].value
        #             newinternalNode.parent = current.parent
        #             newinternalNode.children = i  
        #             for k in i:   
                         
        #                 k.parent = newinternalNode
        #             newtemp.append(newinternalNode)
                   
        #         index = current.parent.children.index(current)
        #         del current.parent.children[index]
        #         for i in newtemp:
        #             current.parent.children.append(i)
        #             # current.parent.children.append
        #         current = current.parent
                
        # else:
        #     print("reached root")
        #     print(len(current.children))
        #     if(len(current.children) == thresh):
        #         return root
        #     print(current.children)
        #     countStuff = 0
        #     temp = []
        #     tempHolder = []
        #     for k in current.children:
        #         if(countStuff == thresh):
        #             tempHolder.append(temp)
        #             temp = []
        #         countStuff = 0
        #         temp.append(k)
        #         print(k.parent.value)
        #         countStuff +=1
        #     if(len(temp) > 0):
        #         tempHolder.append(temp)
            
            
                

            

            
            
            # break
          
    
        
    return root

class InternalNode():
    value = -1
    children = []
    parent = None
    def __lt__(self, other):
        if(type(self.value) is str):
            self.value = -1
        elif(type(other.value) is str):
            other.value = -1
        else:
            return float(self.value) < float(other.value)
    
    
class LeafNodePages():
    value = -1
    actvalues = []
    left = None
    right = None
    parent = None
    def __lt__(self, other):
        return self.value < other.value


def removeallblanks(csv):
    holder = []
    ifile = open("backup.csv")
    for line in csv.reader(ifile):
        print(line)
        if not line:
            print("hello")
    pd.DataFrame(holder).to_csv("backup.csv")
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
                    if(len(leafnode.actvalues) >= 0):
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
    print("Input N for new tree, R for restore, I for insert, F for find, B to backup, H for height, or E to exit")
    inp = input()
    if(count == 5):
        inp = "B"
        print("Interrupting your action")
        print("Force back up ")
        count = 0
    if(inp == "N"):
        logentry = []
        logentry.append("N")
        logentry.append(-1)
        logentry.append(count)
        logofuncommittedActs.append(logentry)
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
        
        count+=1
    if(inp == "R"):
        logentry = []
        logentry.append("R")
        logentry.append(-1)
        logentry.append(count)
        logofuncommittedActs.append(logentry)
        beginning = time.time()
        root, number = createtree()
        end = time.time()
        timediff = end - beginning
        print("time took (in seconds):", timediff)
        with open('log.csv') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if(len(row) < 2):
                    break
                if(row[1] == "I"):
                    print("An insert wasn't comitted into storage.")
                    print("Inserting " + str(row[2]))
                    root = insert(root, float(row[2]), number)
        
        count +=1
    if(inp == "I"):
        print("What value do you want to insert?")
        value = float(input())
        logentry = []
        logentry.append("I")
        logentry.append(value)
        logentry.append(count)
        logofuncommittedActs.append(logentry)
        #Insert function over here
        beginning = time.time()
        root = insert(root, value, number)
        bl.backup(root, 0, number)
        #removeallblanks("backup.csv")
        root, number = createtree()
        end = time.time()
        timediff = end - beginning
        print("time took (in seconds):", timediff)
        print("Inserted", value)       
        count+=1
    if(inp == "F"):
        print("What value do you want to search for?")
        value = input()
        logentry = []
        logentry.append("F")
        logentry.append(value)
        logentry.append(count)
        logofuncommittedActs.append(logentry)
        beginning = time.time()
        boolean = searchforval(root, float(value))
        end = time.time()
        timediff = end - beginning
        print("time took (in seconds):", timediff)
        if(boolean == True):
            print("The value was found!")
        else:
            print("Sorry, we couldn't find that value")
       
        count +=1
    if(inp == "B"):
        nullval = []
        pd.DataFrame(nullval).to_csv("backup.csv")
        print("Backing up right now!")
        beginning = time.time()
        bl.backup(root, 0, number)
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
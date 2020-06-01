import csv
class InternalNode():
    value = -1
    children = []
    
    
class LeafNodePages():
    values = []
    left = None
    right = None 


holder = []
count = 0
number = 0

with open('backup.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if(count > 0):
            if(count == 1):
                number = len(row)
                leafnode = LeafNodePages()
                leafnode.values = row[1]
                holder.append(leafnode)
                print(leafnode.values)
        
                count+=1
            else:
                number = len(row)
                leafnode = LeafNodePages()
                leafnode.values = row[1]
                holder[count-2].right = leafnode
                leafnode.left = holder[count-2]
                holder.append(leafnode)
                print(leafnode.left.values)
                count+=1

            
        else:
            count+=1

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






        






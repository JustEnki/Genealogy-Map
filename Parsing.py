from NVP import *

def print_object(obj, cp):
    if eval(obj + '.' + cp) is not None:
        print eval(str(obj) + '.' + cp)
        print_object(eval(str(obj) + '.' + cp), cp)

file = open("c:/Users/jelder/Desktop/Git-Folder/Genealogy-Map/Data.txt","r")
fileObj = file.read()
file.close()
object = fileObj.split("\n")
del object[-1]
dict = {}


for item in object:
    item = item.replace('"','')
    item = item.replace(', ',',')
    newItem = item.split(",")
 
    dict[newItem[1]] = NVP(newItem[3], newItem[4], newItem[1])

for item in object:
    item = item.replace('"','')
    item = item.replace(', ',',')
    newItem = item.split(",")
    for i in newItem[5:]:                                                                               #find child CID
        if len(i) > 0:                                                                                       #if parent has child
            if i in dict.keys():                                                                           #if child is already created
                dict[i].parent = dict[newItem[1]]                                                   #assign parent to child
                dict[newItem[1]].child.append(dict[i])                                            #assign child to parent
            else:
                dict[newItem[1]].child.append(i)

for k in dict.keys():
    print_object(k, 'parent')
    #print object
#print dict
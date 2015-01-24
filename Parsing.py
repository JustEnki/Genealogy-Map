file = open("c:/Users/jelder/Desktop/Git-Folder/Genealogy-Map/POs.csv","r")
fileObj = file.read()
file.close()
object = fileObj.split("\n")
dict = {}
del object[-1]
for item in object:
    newItem = item.split(",")
    """for i in newItem:
        if i == '':
            del newItem[newItem.index(i)]"""
    print newItem[1]
    dict[newItem[1]] = newItem[0]
del dict['']
print dict
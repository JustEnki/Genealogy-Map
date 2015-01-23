#This class FileParser will open the file, remove the '"' and create a list of lists

class FileParser(object):
    """This class FileParser will open a file, remove the quotations and create a list of lists
    
    """
    
    def __init__(self, fileString):
        self.fileString = fileString
        self.newFileRep = []
        
    def __iter__(self):
        self.parse_file()
        for x in self.newFileRep:
            yield x
        
    def remove_char(self, character):
        self.newFileRep = []
        file = open(self.fileString, 'r')
        for line in file.readlines():
            newLine = line.replace(character,'')
            newLine = newLine.replace('\n','')
            self.newFileRep.append(newLine)
        file.close()
        
    def create_list(self):
        representation = self.newFileRep
        self.newFileRep = []
        for item in representation:
            item = item.split(",")
            self.newFileRep.append(item)
        
    def parse_file(self):
        self.remove_char('"')
        self.create_list()
        return self.newFileRep
#This class will map the NVP nodes and return a formatted list

from FileParser import *
from NVP import *

class Map(object):
    """This class will map the NVP nodes and return a formatted list
    
    """
    
    def __init__(self, filePath):
        self.parsed_file = FileParser(filePath)
        self.NVPList = []
        
    def NVPs(self):
        for item in self.parsed_file:
            self.NVPList.append(NVP(item[3], item[4], item[1], item[5:]))
        print self.NVPList
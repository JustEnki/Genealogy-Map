#This class is a node that holds the NVP's information

class NVP(object):
    """This class creates a node that holds all the NVP's information"""
    def __init__(self, firstName, lastName, CID):
        self.firstName = firstName
        self.lastName = lastName
        self.CID = CID
        self.name = self.firstName + " " + self.lastName
        self.child = []
        self.parent = None
        
    def __repr__(self):
        return self.name
        
    def add_child(self, newNVP):
        self.child = newNVP
        
    def add_parent(self, newNVP):
        self.parent = newNVP
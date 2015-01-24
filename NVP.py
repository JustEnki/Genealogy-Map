#This class is a node that holds the NVP's information

class NVP(object):
    """This class creates a node that holds all the NVP's information"""
    def __init__(self, firstName, lastName, CID, child):
        self.firstName = firstName
        self.lastName = lastName
        self.CID = CID
        self.name = self.firstName + " " + self.lastName
        self.child = child
        
    def __repr__(self):
        return str(self.child)
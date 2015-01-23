#This class is a node that holds the NVP's information

class NVP(object):
    """This class creates a node that holds all the NVP's information"""
    def __init__(self, firstName, lastName, CID):
        self.firstName = firstName
        self.lastName = lastName
        self.CID = CID
        self.name = self.firstName + " " + self.lastName
        
    def __repr__(self):
        return self.name
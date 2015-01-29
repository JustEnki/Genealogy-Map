class NVPNode(object):
    """creates a basic NVP node
    
    """
    def __init__(self, element):
        self.element = element
        self.nextEl = None
        
    def __repr__(self):
        return str(self.nextEl.element)
        
    def add(self, newNode):
        self.nextEl = newNode
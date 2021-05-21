class Ship:
    def __init__(self,size,quantity):
        self.size = size
        self.quantity = quantity*self.size

    def getSize(self):
        return self.size

    def setQuantity(self,nq):
        self.quantity = nq

    def getQuantity(self):
        return self.quantity
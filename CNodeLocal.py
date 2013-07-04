class CNodeLocal(object):
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        
    def getUpLocal(self):
        if self.row == 0:
            return -1
        return CNodeLocal(self.row - 1, self.col, self.size)
    
    def getDownLocal(self):
        if self.row == self.size - 1:
            return -1
        return CNodeLocal(self.row + 1, self.col, self.size)
    
    def getLeftLocal(self):
        if self.col == 0:
            return -1
        return CNodeLocal(self.row, self.col - 1, self.size)
    
    def getRightLocal(self):
        if self.col == self.size - 1:
            return -1
        return CNodeLocal(self.row, self.col + 1, self.size)
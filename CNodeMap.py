from CNodeLocal import *
from CNode import *
from CRoute import *

class CNodeMap(object):
    def __init__(self, size):
        self.size = size
        self.nodeList = []
        for i in range(0, size * size):
            node = CNode(i, self)
            self.nodeList.append(node)
            
    def getNodeByNodeID(self, nodeID):
        return self.nodeList[nodeID]
        
    def getLocalByNodeID(self, nodeID):
        row = nodeID / self.size
        col = nodeID % self.size
        return CNodeLocal(row, col, self.size)
    
    def getNodeIDByLocal(self, local):
        if local.size != self.size:
            return -1
        return local.row * self.size + local.col
    
    def getNeighborNodeIDListByNodeID(self, nodeID):
        local = self.getLocalByNodeID(nodeID)
        nodeIDList = []
        neighborLocal = local.getUpLocal()
        if neighborLocal != -1:
            nodeIDList.append(self.getNodeIDByLocal(neighborLocal))
        neighborLocal = local.getDownLocal()
        if neighborLocal != -1:
            nodeIDList.append(self.getNodeIDByLocal(neighborLocal))    
        neighborLocal = local.getLeftLocal()
        if neighborLocal != -1:
            nodeIDList.append(self.getNodeIDByLocal(neighborLocal))
        neighborLocal = local.getRightLocal()
        if neighborLocal != -1:
            nodeIDList.append(self.getNodeIDByLocal(neighborLocal))
        return nodeIDList
    
    def initMap(self):
        for node in self.nodeList:            
            node.neighborNodeIDList = self.getNeighborNodeIDListByNodeID(node.nodeID)
            for neighborNodeID in node.neighborNodeIDList:
                node.routeList.append(CRoute(neighborNodeID, neighborNodeID, 1))
            print "node %d 's neighbor is " % node.nodeID
            print node.neighborNodeIDList
            
            
"""            
    def printMap(self):
        
        for i in range(0, self.size):
            list = []
            for j in range(0, self.size):
                list.append(i * self.size + j)
            print list
"""
            
                
    
            
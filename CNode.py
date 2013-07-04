from SerialNum import *

class CNode(object):
    def __init__(self, nodeID, nodeMap):
        self.nodeID = nodeID
        self.neighborNodeIDList = []
        self.routeList = []
        self.nodeMap = nodeMap
        self.snHistory = []
        
    def updateRoute(self, routeList, sn):
        updated = False
        
    
    def broadcastRouteToNeighbor(self):
        routeListToUpdate = []
        for route in self.routeList:
            if route.toUpdate == True:
                routeListToUpdate.append(route)
                
        for nodeID in self.neighborNodeIDList:
            node = self.nodeMap.getNodeByNodeID(nodeID)
            sn = SerialNum.getSerialNum()
            self.snHistory.append(sn)
            node.updateRoute(routeListToUpdate, sn)
            
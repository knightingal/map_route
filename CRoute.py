class CRoute(object):
    def __init__(self, dest, nxt, distance):
        self.dest = dest
        self.next = nxt
        self.distance = distance
        self.toUpdate = True
        
    
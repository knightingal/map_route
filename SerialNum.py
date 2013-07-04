class SerialNum(object):
    serialNum = 0
    def getSerialNum(self):
        SerialNum.serialNum += 1
        return SerialNum.serialNum
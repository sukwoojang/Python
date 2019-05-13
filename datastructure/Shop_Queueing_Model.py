import numpy as np
import Queue

class Cust:
    def __init__(self, time, mean=1):
        self.arriveTime = time + np.random.exponential(mean)
        self.orderTime = 0
        self.outTime = 0

    def setTime(self, time):
        self.orderTime = time
        cook = np.random.normal(1, 0.2)
        if cook < 0:
            cook = 0
        self.outTime = self.orderTime + cook


class Shop:
    def __init__(self, n):
        self.n = n
        self.custQueue = []
        for i in range(0, n):
            self.custQueue.append(Queue.Queue())
        self.lastCust = None

    def getSize(self):
        size = []
        for i in range(self.n):
            size.append(self.custQueue[i].size())
        return size

    def entCust(self, cust):
        size = np.array(self.getSize())
        minIdx = np.argmin(size)
        lastcust = self.custQueue[minIdx].peekLast()
        if lastcust == None:
            cust.setTime(cust.arriveTime)
        else:
            cust.setTime(lastcust.outTime)
        self.custQueue[minIdx].enQueue(cust)
        self.lastCust = cust

    def outCust(self, time):
        for i in self.custQueue:
            while i.size() > 0 and i.peek().outTime <= time:
                i.deQueue()

    def getLast():
        return cust.lastCust


s = Shop(2)
curTime = 0
while curTime <= 14 * 80:
    cust = Cust(curTime)
    s.entCust(cust)
    curTime = cust.arriveTime
    s.outCust(curTime)
    print("%7.2f -> %7.2f -> %7.2f" % (cust.arriveTime, cust.orderTime, cust.outTime))
    print(s.getSize())
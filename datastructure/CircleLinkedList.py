class CircleLInkedList:
    def __init__(self):
        self.root = Node()
        self.tail = self.root
        self.current = self.root
    def append(self,item):
        NewNode = Node(item)
        if self.root.item == None:
            self.root = NewNode
            self.tail = NewNode
            NewNode.link = self.root
        else:
            _tmp = self.tail.link
            self.tail.link = NewNode
            NewNode.link = _tmp
            self.tail = NewNode
    def listSize(self):
        curNode = self.root
        count = 1
        while curNode.link != self.root:
            curNode = curNode.link
            count += 1
        return count
    def print(self):
        curNode = self.root
        print(curNode.item)
        while curNode.link != self.root:
            curNode = curNode.link
            print(curNode.item)
    def setCurrent(self,item):
        curNode = self.root
        for i in range(self.listSize()):
            if curNode.item == item:
                self.current = curNode
            else:
                curNode = curNode.link
    def moveNext(self):
        self.current = self.current.link
        print("현재 위치는 {}입니다.".format(self.current.item))
    def insert(self, item):
        NewNode = Node(item)
        _tmp = self.current.link
        self.current.link = NewNode
        NewNode.link = _tmp
        if self.current == self.tail:
            self.tail = NewNode
    def delete(self, item):
        delYN = False
        curNode = self.root
        if curNode.item == item:
            self.root = self.root.link
            self.tail.link = self.root
            delYN =True
        else:
            while curNode.link != self.root:
                preNode = curNode
                curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link
                    if curNode == self.tail:
                        self.tail = preNode
                    delYN =True
        if delYN == False:
            print("delete failed")

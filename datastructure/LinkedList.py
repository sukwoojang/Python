class Node:
    def __init__(self, item=None):
        self.item = item
        self.link = None


class LinkedList:
    def __init__(self):
        self.root = Node()

    def append(self, item):
        newNode = Node(item)
        curNode = self.root
        if curNode.item == None:
            self.root = newNode
        else:
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode

    def print(self):
        curNode = self.root
        print(curNode.item)
        while curNode.link != None:
            curNode = curNode.link
            print(curNode.item)

    def remove(self, item):
        curNode = self.root
        preNode = self.root
        if self.root.item == item:
            self.root = self.root.link
        while curNode.link != None:
            if curNode.item == item:
                preNode.link = curNode.link
            preNode = curNode
            curNode = curNode.link

    def size(self):
        size = 1
        curNode = self.root
        while curNode.link != None:
            curNode = curNode.link
            size += 1
        return size

    def insert(self, item, index):
        if index < 0 or index >= self.size():
            print("error")
        else:
            newNode = Node(item)
            curNode = self.root
            if index == 0:
                tempNode = self.root
                self.root = newNode
                newNode.link = tempNode
            else:
                for i in range(index - 1):  # index-1까지 반복
                    curNode = curNode.link
                tempNode = curNode.link
                curNode.link = newNode
                newNode.link = tempNode

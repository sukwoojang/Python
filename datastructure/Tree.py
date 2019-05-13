class Tree:
    def __init__(self):
        self.t = [None]

    def append(self, item):
        self.t.append(item)

    def size(self):
        return len(self.t) - 1

    def getChild(self, item):
        if item in self.t:
            idx = self.t.index(item)
            if self.size() >= 2 * idx + 1:
                return self.t[2 * idx], self.t[2 * idx + 1]
            elif self.size() == 2 * idx:
                return self.t[2 * idx], None
            else:
                return None, None
        else:
            print("Item not found")

    def getParent(self, item):
        if item in self.t:
            idx = self.t.index(item)
            if idx // 2 > 0:
                return self.t[idx // 2]
            else:
                return None
        else:
            print("Item not found")


t = Tree()
for i in range(1, 10):
    t.append(i)

t.size()
t.t
t.getChild(1)
t.getParent(5)
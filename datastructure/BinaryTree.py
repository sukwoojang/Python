class Bnode:
    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = None

    def setLeft(self, item):
        self.left = item

    def setRight(self, item):
        self.right = item


class BinaryTree:
    def __init__(self, item):
        self.root = item

    def preOrder(self, n):
        print(n.item, " ", end=" ")
        if n.left: self.preOrder(n.left)
        if n.right: self.preOrder(n.right)
        return

    def inOrder(self, n):
        if n.left: self.inOrder(n.left)
        print(n.item, " ", end=" ")
        if n.right: self.inOrder(n.right)
        return

    def postOrder(self, n):
        if n.left: self.postOrder(n.left)
        if n.right: self.postOrder(n.right)
        print(n.item, " ", end=" ")
        return

    def height(self, n):
        if not n:
            return 0
        else:
            lheight = self.height(n.left)
            rheight = self.height(n.right)
            print(n.item, lheight + 1, rheight + 1)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def levelOrder(self, n):
        h = self.height(n)
        for i in range(1, h + 1):
            self._levelOrder(n, i)

    def _levelOrder(self, n, lv):
        if n is None:
            return
        elif lv == 1:
            if n.left != None and n.right != None:
                print((n.item, n.left.item, n.right.item), end= " ")
            elif n.left != None and n.right == None:
                print((n.item, n.left.item, "None"), end = " ")
            elif n.left == None and n.right != None:
                print((n.item, "None", n.right.item), end =" ")
            else:
                print((n.item, "None", "None"), end= " ")
        elif lv > 1:
            self._levelOrder(n.left, lv - 1)
            self._levelOrder(n.right, lv - 1)


a = Bnode('A')
b = Bnode('B')
c = Bnode('C')
d = Bnode('D')
e = Bnode('E')

a.setLeft(b)
a.setRight(c)
b.setLeft(d)
b.setRight(e)

AA = BinaryTree(a)

AA.preOrder(a)
AA.height(a)
AA.levelOrder(a)
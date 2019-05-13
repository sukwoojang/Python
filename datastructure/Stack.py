class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(-1)
        else:
            return None

    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None
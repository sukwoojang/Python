class Queue:
    def __init__(self):
        self.q = []

    def enQueue(self, item):
        self.q.append(item)

    def isEmpty(self):
        if len(self.q) == 0:
            return True
        else:
            return False

    def deQueue(self):
        if self.isEmpty() == False:
            self.q.pop(0)

    def peek(self):
        if self.isEmpty() == False:
            return self.q[0]

    def peekLast(self):
        if self.isEmpty() == False:
            return self.q[-1]

    def delete(self, item):
        if item in self.q:
            self.q.remove(item)
        else:
            print("해당 아이템이 존재하지 않습니다.")

    def size(self):
        return len(self.q)
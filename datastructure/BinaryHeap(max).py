class BinaryHeap:
    def __init__(self):
        self.x = [None]

    def exchange(self, i, j):
        if self.x[i] < self.x[j]:
            self.x[i], self.x[j] = self.x[j], self.x[i]

    def push(self, item):
        self.x.append(item)
        cidx = len(self.x) - 1
        pidx = cidx // 2
        while pidx >= 1:
            self.exchange(pidx, cidx)
            cidx = pidx
            pidx = cidx // 2

    def pop(self):
        _tmp = self.x[1]
        self.x[1], self.x[-1] = self.x[-1], self.x[1]
        self.x = self.x[:-1]
        self.heapify()
        return _tmp

    def child(self, idx):
        lidx = 2 * idx
        ridx = 2 * idx + 1
        if len(self.x) - 1 >= ridx:
            return lidx, ridx
        elif len(self.x) - 1 == lidx:
            return lidx, None
        else:
            return None, None

    def heapify(self):
        pidx = 1
        lastidx = len(self.x) - 1
        while pidx < lastidx + 1:
            left, right = self.child(pidx)
            if left and not right:
                self.exchange(pidx, left)
            elif left and right:
                if self.x[left] < self.x[right]:
                    self.exchange(pidx, right)
                else:
                    self.exchange(pidx, left)
            pidx += 1


h = BinaryHeap()

for i in range(1, 10):
    h.push(i)

h.x

class SparseMatrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.s = [[m, n, 0]]

    def append(self, i, j, value):
        if value != 0:
            self.s.append([i, j, value])
        self.s[0][2] = len(self.s) - 1

    def shape(self):
        return (self.m, self.n)

    def getValue(self, i, j):
        for n in range(1, len(self.s)):
            if self.s[n][0] == i and self.s[n][1] == j:
                return self.s[n][2]
        return 0

    def print(self):
        import numpy as np

        zeros = np.zeros((self.m, self.n))
        for n in range(1, len(self.s)):
            zeros[self.s[n][0] - 1, self.s[n][1] - 1] = self.s[n][2]
        print(zeros)

    def multiply(a, b):
        if a.shape()[1] != b.shape()[0]:
            print("Dimension Error")
        else:
            m = a.shape()[0]
            n = b.shape()[1]
            l = a.shape()[1]
            c = SparseMatrix(m, n)
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    _sum = 0
                    for k in range(1, l + 1):
                        _sum += a.getValue(i, k) * b.getValue(k, j)
                        if _sum != 0:
                            c.append(i, j, _sum)
        return c

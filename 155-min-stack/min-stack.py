class MinStack:
    def __init__(self):
        self.s = []
        self.m = []

    def push(self, x):
        self.s.append(x)
        self.m.append(min(x, self.m[-1] if self.m else x))

    def pop(self):
        self.s.pop()
        self.m.pop()

    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.m[-1]
class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key, value):
        for p in self.map:
            if p[0] == key:
                p[1] = value
                return
        self.map.append([key, value])

    def get(self, key):
        for p in self.map:
            if p[0] == key:
                return p[1]
        return -1

    def remove(self, key):
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map.pop(i)
                return


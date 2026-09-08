class MyHashSet:
    def __init__(self):
        self.data = []
    def add(self, key):
        if key not in self.data:
            self.data.append(key)
    def contains(self, key):
        return key in self.data
    def remove(self, key):
        if key in self.data:
            self.data.remove(key)
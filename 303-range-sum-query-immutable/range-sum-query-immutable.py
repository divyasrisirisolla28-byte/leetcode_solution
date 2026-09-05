class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    def sumRange(self, l, r):
        return self.prefix[r + 1] - self.prefix[l]
    
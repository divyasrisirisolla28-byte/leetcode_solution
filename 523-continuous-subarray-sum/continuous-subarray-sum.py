class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        s = 0
        for i, x in enumerate(nums):
            s += x
            r = s % k
            if r in d and i - d[r] >= 2:
                return True
            if r not in d:
                d[r] = i
        return False
        
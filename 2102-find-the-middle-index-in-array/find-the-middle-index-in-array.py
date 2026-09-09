class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int: 
        total = sum(nums)
        l = 0
        for i in range(len(nums)):
            r = total - l - nums[i]
            if l == r:
                return i
            l += nums[i]
        return -1

        
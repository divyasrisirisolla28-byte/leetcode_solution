class Solution:
    def runningSum(self, nums):
        ans = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            ans.append(total)

        return ans

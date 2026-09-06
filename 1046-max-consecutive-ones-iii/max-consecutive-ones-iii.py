class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxl = 0
        zeros = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            maxl = max(maxl, r - l + 1)

        return maxl
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        s = [0] * n
        s[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            s[i] = min(nums[i], s[i+1])
        m = 0
        for i in range(n):
            m = max(m, nums[i])
            if m - s[i] <= k:
                return i
        return -1

        
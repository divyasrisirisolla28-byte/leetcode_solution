class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x
        n = len(nums)

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        current_sum = 0
        max_len = -1

        for right in range(n):
            current_sum += nums[right]

            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return n - max_len
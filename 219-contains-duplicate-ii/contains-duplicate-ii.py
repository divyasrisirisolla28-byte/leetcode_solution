class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}
        for i in range(len(nums)):
            if nums[i] in last:
                    if i - last[nums[i]] <= k:
                        return True
            last[nums[i]] = i
        return False
                
        
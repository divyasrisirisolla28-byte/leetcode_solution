class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l +h) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[h]:
                l += 1
                h -= 1
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return False
                        
                       
        
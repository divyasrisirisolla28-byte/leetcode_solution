class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        total = 0
        ans = 0
        for num in nums:
            total += num
            rem = total % k
            if rem in mp:
                ans += mp[rem]
            mp[rem] = mp.get(rem, 0) + 1
        return ans
        
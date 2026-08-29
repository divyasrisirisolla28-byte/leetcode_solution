class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        h = sum(weights)
        while l < h:
            mid = (l+h) // 2
            if self.Canfinish(weights, days, mid):
                h = mid
            else:
                l = mid+1
        return l
    def Canfinish(self,weights,days,Cap):
        load= 0
        req_days = 1
        for weight in weights:
            if load+weight <= Cap:
                load += weight
            else:
                req_days += 1 
                load = weight
        return req_days <= days
        
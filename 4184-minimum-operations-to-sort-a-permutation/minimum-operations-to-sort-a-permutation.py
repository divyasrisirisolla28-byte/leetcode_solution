class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        def get_increasing_rotation_cost(arr):
            k = arr.index(0)
            for j in range(n):
                if arr[(k + j) % n] != j:
                    return -1
            return k

        def get_decreasing_rotation_cost(arr):
            k = arr.index(n - 1)
            for j in range(n):
                if arr[(k + j) % n] != (n - 1 - j):
                    return -1
            return k

        valid_costs = []

        # 1. Pure rotations to increasing order (Cost = k)
        cost_inc = get_increasing_rotation_cost(nums)
        if cost_inc != -1:
            valid_costs.append(cost_inc)

        # 2. Reverse first, then rotate to increasing order (Cost = 1 + k)
        rev_nums = nums[::-1]
        cost_rev_inc = get_increasing_rotation_cost(rev_nums)
        if cost_rev_inc != -1:
            valid_costs.append(1 + cost_rev_inc)

        # 3. Rotate first, then reverse (Cost = k + 1)
        cost_dec = get_decreasing_rotation_cost(nums)
        if cost_dec != -1:
            valid_costs.append(cost_dec + 1)

        # 4. Reverse -> Rotate -> Reverse trick (Cost = k_rev_dec + 2)
        cost_rev_dec = get_decreasing_rotation_cost(rev_nums)
        if cost_rev_dec != -1:
            valid_costs.append(1 + cost_rev_dec + 1)

        return min(valid_costs) if valid_costs else -1
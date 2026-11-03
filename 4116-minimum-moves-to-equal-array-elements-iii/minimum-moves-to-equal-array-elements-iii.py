class Solution:
    def minMoves(self, nums):
        maximum = max(nums)
        moves = 0

        for i in nums:
            moves += maximum - i

        return moves
        
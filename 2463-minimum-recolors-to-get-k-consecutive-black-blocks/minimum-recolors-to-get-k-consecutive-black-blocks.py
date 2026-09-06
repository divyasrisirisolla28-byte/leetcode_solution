class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        for i in range(len(blocks) - k +1):
            window = blocks[i:i+k]
            white = window.count('W')
            ans = min(ans, white)
        return ans
        
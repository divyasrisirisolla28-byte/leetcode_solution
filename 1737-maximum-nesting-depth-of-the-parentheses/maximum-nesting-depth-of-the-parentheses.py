class Solution:
    def maxDepth(self, s):
        d = m = 0
        for c in s:
            d += (c == '(') - (c == ')')
            m = max(m, d)
        return m
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        a = sorted((x[0], x[1], x[2], i) for i, x in enumerate(intervals))
        starts = [x[0] for x in a]
        dp = {}

        def f(i, k):
            if i == len(a) or k == 4:
                return 0, []

            if (i, k) in dp:
                return dp[i, k]

            s1, x1 = f(i + 1, k)

            l, r, w, idx = a[i]
            j = bisect_right(starts, r)

            s2, x2 = f(j, k + 1)
            s2 += w
            x2 = sorted([idx] + x2)

            if s2 > s1 or (s2 == s1 and x2 < x1):
                dp[i, k] = (s2, x2)
            else:
                dp[i, k] = (s1, x1)

            return dp[i, k]

        return f(0, 0)[1]
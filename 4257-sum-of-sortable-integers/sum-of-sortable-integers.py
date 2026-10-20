
class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        target = sorted(nums)
        ans = 0

        # Check whether b is a cyclic rotation of a using KMP
        def check(a, b):
            m = len(a)
            doubled = a + a
            lps = [0] * m
            j = 0

            for i in range(1, m):
                while j and b[i] != b[j]:
                    j = lps[j - 1]
                if b[i] == b[j]:
                    j += 1
                    lps[i] = j

            j = 0
            for i in range(2 * m - 1):
                x = doubled[i]
                while j and x != b[j]:
                    j = lps[j - 1]
                if x == b[j]:
                    j += 1
                if j == m:
                    return True

            return False

        for k in range(1, n + 1):
            if n % k:
                continue

            ok = True

            for start in range(0, n, k):
                a = nums[start:start + k]
                b = target[start:start + k]

                if not check(a, b):
                    ok = False
                    break

            if ok:
                ans += k

        return ans


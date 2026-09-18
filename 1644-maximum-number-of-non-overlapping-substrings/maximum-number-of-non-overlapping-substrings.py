class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        # Find the smallest valid interval starting from l
        def get_interval(l):
            r = last[ord(s[l]) - ord('a')]
            i = l

            while i <= r:
                x = ord(s[i]) - ord('a')

                # Character occurs before l -> invalid
                if first[x] < l:
                    return None

                r = max(r, last[x])
                i += 1

            return (l, r)

        intervals = []

        # Generate valid minimal intervals
        for i in range(n):
            if first[ord(s[i]) - ord('a')] == i:
                interval = get_interval(i)
                if interval is not None:
                    intervals.append(interval)

        # Greedy: choose interval with earliest ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result
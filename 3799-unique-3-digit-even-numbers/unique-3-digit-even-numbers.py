class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        for n in range(100, 1000, 2):
            a = [n // 100, (n // 10) % 10, n % 10]
            d = digits.copy()
            for x in a:
                if x in d:
                    d.remove(x)
                else:
                    break
            else:
                ans.add(n)
        return len(ans)

        
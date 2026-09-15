class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        for i in range(n):
            pal[i][i] = True

        # Check palindromes of length 2 and more
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = maximum number of palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            # Skip the current character
            dp[i] = dp[i - 1]

            # Try every substring ending at i-1
            for start in range(i):

                length = i - start

                if length >= k and pal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]
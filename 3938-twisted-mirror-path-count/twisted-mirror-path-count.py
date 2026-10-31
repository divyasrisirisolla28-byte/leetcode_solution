class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # State 0: Entered from left
        # State 1: Entered from above

        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                for d in range(2):

                    ways = dp[i][j][d]

                    if ways == 0:
                        continue

                    if grid[i][j] == 1:
                        # Mirror reflection
                        if d == 0:
                            ni, nj = i + 1, j
                        else:
                            ni, nj = i, j + 1

                    else:
                        # Empty cell: move right or down
                        if d == 0 or d == 1:
                            pass

                        # Handle both possible movements
                        if j + 1 < n:
                            dp[i][j + 1][0] = (
                                dp[i][j + 1][0] + ways
                            ) % MOD

                        if i + 1 < m:
                            dp[i + 1][j][1] = (
                                dp[i + 1][j][1] + ways
                            ) % MOD

                        continue

                    # Process reflected movement
                    if ni < m and nj < n:
                        if grid[ni][nj] == 0:
                            nd = 1 if ni > i else 0
                            dp[ni][nj][nd] = (
                                dp[ni][nj][nd] + ways
                            ) % MOD

                        else:
                            # Consecutive mirrors are handled
                            # when the next cell is processed.
                            nd = 1 if ni > i else 0
                            dp[ni][nj][nd] = (
                                dp[ni][nj][nd] + ways
                            ) % MOD

        return sum(dp[m-1][n-1]) % MOD
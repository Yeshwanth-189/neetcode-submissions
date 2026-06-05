class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # First row: only one way, keep moving right
        for j in range(n):
            dp[0][j] = 1

        # First column: only one way, keep moving down
        for i in range(m):
            dp[i][0] = 1

        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
        
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] = number of ways to decode s[:i]
        dp = [0] * (n + 1)

        # Empty string has 1 way as a base case
        dp[0] = 1

        # First character is valid only if it is not '0'
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, n + 1):
            # Check one-digit decode
            one_digit = s[i - 1]

            if one_digit != "0":
                dp[i] += dp[i - 1]

            # Check two-digit decode
            two_digit = s[i - 2:i]

            if 10 <= int(two_digit) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
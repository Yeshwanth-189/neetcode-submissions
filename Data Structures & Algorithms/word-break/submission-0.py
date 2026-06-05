class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # dp[i] means:
        # Can we split s[:i] into words from wordDict?
        dp = [False] * (n + 1)

        # Empty string is always valid.
        # This is the starting point before taking any word.
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(0, i):
                # If s[:j] is valid and s[j:i] is a dictionary word,
                # then s[:i] is also valid.
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]
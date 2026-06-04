class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(l, r):
            nonlocal count

            # Keep expanding while the substring s[l:r+1] is valid palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1      # found one palindrome substring
                l -= 1          # expand left
                r += 1          # expand right

        for i in range(len(s)):
            expand(i, i)        # odd length palindromes
            expand(i, i + 1)    # even length palindromes

        return count
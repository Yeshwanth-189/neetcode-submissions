class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n & 1   # checks if the last bit is 1
            n >>= 1          # shift right by 1 bit

        return count
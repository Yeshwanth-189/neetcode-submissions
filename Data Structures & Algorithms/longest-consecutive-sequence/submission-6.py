class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=list(sorted(set(nums)))
        print(num)
        n=len(num)
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            if num[1]==num[0]+1:
                return 2
            else:
                return 1
        max_streak=1
        streak=1
        for i in range(1,n):
            if num[i]==num[i-1]+1:
                streak+=1
                print(streak)
                max_streak=max(max_streak,streak)
            else:
                streak=1
        return max_streak

        
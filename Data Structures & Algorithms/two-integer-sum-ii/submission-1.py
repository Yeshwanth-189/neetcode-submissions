class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l=0
        r=1
        n=len(num)
        while l<n:
            if r==len(num):
                l=l+1
                r=l+1
            if num[l]+num[r]==target:
                return [l+1,r+1]
            elif num[l]+num[r]<target:
                r+=1
            else:
                l=l+1
                r=l+1
        return []

        
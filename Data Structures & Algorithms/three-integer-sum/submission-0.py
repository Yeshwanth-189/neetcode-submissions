class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num=sorted(nums)
        n=len(num)
        res=[]
        for i in range(0,n-2):
            if i > 0 and num[i] == num[i - 1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                if num[i]+num[left]+num[right]==0:
                    res.append([num[i],num[left],num[right]])
                    while left<right and num[left]==num[left+1] :
                        left+=1
                    while left<right and num[right]==num[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif num[i]+num[left]+num[right]<0:
                    left+=1
                else:
                    right-=1
        return res

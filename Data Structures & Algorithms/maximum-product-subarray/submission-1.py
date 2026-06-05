class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod=float('inf')
        max_prod=float('-inf')
        res=nums[0]
        for num in nums:

            if num<0:
                min_prod,max_prod=max_prod,min_prod
            min_prod=min(num,num*min_prod)
            max_prod=max(num,num*max_prod)

            res=max(res,max_prod)
        
        return res
        
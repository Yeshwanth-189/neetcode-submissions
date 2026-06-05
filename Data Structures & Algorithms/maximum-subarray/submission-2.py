class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums[0]==0 and len(nums)==1:
            return 0
        max_sum=float('-inf')
        cur_sum=nums[0]
        max_sum=max(max_sum,cur_sum)
        for num in nums[1:]:
            cur_sum=max(num,num+cur_sum)
            max_sum=max(max_sum,cur_sum)
        if max_sum==float('-inf'):
            return -1
        return max_sum
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        n=len(nums)
        for i in range(0,n):
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False

        
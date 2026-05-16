class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary=defaultdict(int)
        n=len(nums)
        for i in range(0,n):
            number=target-nums[i]
            if nums[i] in dictionary:
                return [dictionary[nums[i]], i]
            dictionary[number]=i
        return -1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        max_heap=[]
        for num,count in freq.items():
            heapq.heappush(max_heap,(-count,num))
        result=[]
        for i in range(0,k):
            count,num=heapq.heappop(max_heap)
            result.append(num)
        return result

        
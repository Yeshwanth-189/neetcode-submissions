class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        max_water=0
        water=0
        for i in range(0,n-1):
            if heights[l]<heights[r]:
                water=heights[l]*(r-l)
                l+=1
            else: 
                water=heights[r]*(r-l)
                r-=1
            max_water=max(max_water,water)
        return max_water


        
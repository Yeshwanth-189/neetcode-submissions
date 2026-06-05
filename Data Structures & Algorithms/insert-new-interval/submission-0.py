class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result=[]

        for start,end in intervals:
            if end<newInterval[0]:
                result.append([start,end])
            elif start>newInterval[1]:
                result.append(newInterval)
                result.append([start, end])
            
                index = intervals.index([start, end]) + 1
                result.extend(intervals[index:])
                return result
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        result.append(newInterval)

        return result    
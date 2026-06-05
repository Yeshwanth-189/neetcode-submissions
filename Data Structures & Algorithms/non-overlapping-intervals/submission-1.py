class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlap.
                # Remove the interval with larger end.
                count += 1
                prev_end = min(prev_end, end)
            else:
                # No overlap.
                # Keep this interval and update prev_end.
                prev_end = end

        return count
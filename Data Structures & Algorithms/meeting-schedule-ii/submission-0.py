"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort meetings by start time
        intervals.sort(key=lambda interval: interval.start)

        # Min-heap stores end times of meetings currently using rooms
        min_heap = []

        for interval in intervals:
            # If the earliest ending meeting is done before current starts,
            # we can reuse that room.
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            # Add current meeting's end time.
            # This means current meeting occupies a room.
            heapq.heappush(min_heap, interval.end)

        # Heap size = number of rooms needed at peak/current active meetings
        return len(min_heap)
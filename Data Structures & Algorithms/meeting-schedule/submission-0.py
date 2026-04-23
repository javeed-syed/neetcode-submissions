"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True

        heap = [ (x.start, x.end) for x in intervals ]
        heapq.heapify(heap)
        
        prev = heapq.heappop(heap)
        while heap:
            curr = heapq.heappop(heap)
            if curr[0] < prev[1]:
                return False
            else:
                prev = curr
        return True
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

        li = [(x.start, x.end) for x in intervals]
        li.sort(key = lambda x: x[0])
        heap = [li[0][1]]
        res = 1
        for idx in range(1, len(li)):
            print(heap, li[idx])
            start, end = li[idx]

            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
            res = max(res, len(heap))

        return len(heap)
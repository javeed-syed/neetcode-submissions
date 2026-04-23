class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        calucate = lambda x, y : (x**2 + y**2) ** 0.5
        for x, y in points:
            distance = calucate(x, y)
            heapq.heappush(heap, (-distance, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [co for x, co in heap]

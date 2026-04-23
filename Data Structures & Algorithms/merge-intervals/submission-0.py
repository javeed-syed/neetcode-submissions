class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        heap = intervals.copy()
        heapq.heapify(heap)

        while heap:
            curr = heapq.heappop(heap)

            if heap and heap[0][0] <= curr[1]:
                nxt = heapq.heappop(heap)
                new_interval = [min(curr[0], nxt[0]), max(curr[1], nxt[1])]
                heapq.heappush(heap, new_interval)
            else:
                res.append(curr)
        
        return res
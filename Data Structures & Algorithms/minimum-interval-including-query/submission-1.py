class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        heap = []
        res = {}
        idx = 0

        for query in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= query:
                start, end = intervals[idx]
                heapq.heappush(heap, (end - start + 1, end))
                idx += 1
                
            while heap and heap[0][1] < query:
                curr = heapq.heappop(heap)
                print(query, curr)

            res[query] = heap[0][0] if heap else -1
            # else -1 after while loop for first writing style
        
        return [res[q] for q in queries]
                
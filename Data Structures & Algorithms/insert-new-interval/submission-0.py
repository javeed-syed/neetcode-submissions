class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        curr = newInterval

        for i in range(len(intervals)):
            start, end = intervals[i]
            if curr[1] < start:
                res.append(curr)
                return res + intervals[i:]
            elif end < curr[0]:
                res.append([start, end])
            else:
                n_start = min(start, curr[0])
                n_end = max(end, curr[1])
                curr = [n_start, n_end]
        res.append(curr)
        return res
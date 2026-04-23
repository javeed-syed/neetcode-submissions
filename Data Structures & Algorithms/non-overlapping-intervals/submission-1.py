class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        res = 0

        prev = intervals[0]
        for idx in range(1, len(intervals)):
            prev_start, prev_end = prev
            curr_start, curr_end = intervals[idx]

            if curr_start < prev_end:
                res += 1
                if prev_end > curr_end:
                    prev = [curr_start, curr_end]
            else:
                prev = intervals[idx]

        return res
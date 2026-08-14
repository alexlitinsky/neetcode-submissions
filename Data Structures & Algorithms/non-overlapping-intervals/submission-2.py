class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0 
        lastEnd = intervals[0][1]

        # [1, 3], [1, 4], [2, 4]

        for s, e in intervals[1:]:
            if s < lastEnd:
                res += 1
                lastEnd = min(lastEnd, e)
            else:
                lastEnd = e
        
        return res
        
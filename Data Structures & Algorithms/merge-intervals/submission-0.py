class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        res.append(intervals[0])

        for start, end in intervals[1:]:
            lastStart, lastEnd = res[-1]
            if start > lastEnd:
                res.append([start, end])
            else:
                res[-1] = [lastStart, max(lastEnd, end)]
        
        return res


        
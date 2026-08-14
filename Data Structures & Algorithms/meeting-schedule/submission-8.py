"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda x : x.start)

        start, end = intervals[0].start, intervals[0].end

        for i in intervals[1:]:
            s, e = i.start, i.end
            if s < end:
                return False
            start, end = s, e

        return True

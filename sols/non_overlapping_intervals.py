# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x.end)
        
        cnt = 0
        end = -987654321
        for i in xrange(len(intervals)):
            if intervals[i].start < end:
                cnt += 1
            else:
                end = intervals[i].end
        return cnt
        
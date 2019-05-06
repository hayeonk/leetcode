class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[1])
        for i in xrange(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True
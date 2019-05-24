from collections import Counter
class Solution(object):
    def employeeFreeTime(self, schedule):
        C = Counter()
        
        for worker in schedule:
            for start, end in worker:
                C[start] += 1
                C[end] -= 1
        
        ans = []
        curSum = 0
        prevTime = None
        for time in sorted(C):
            curSum += C[time]
            if prevTime is not None:
                ans.append([prevTime, time])
                prevTime = None
            if curSum == 0:
                prevTime = time
        
        return ans
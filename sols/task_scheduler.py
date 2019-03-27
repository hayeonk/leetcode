from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        T = Counter(tasks).values()
        T.sort(reverse=True)
        maxVal = T[0]
        idleSlots = (maxVal-1) * n
        for i in xrange(1, len(T)):
            idleSlots -= min(T[i], maxVal - 1)
        return len(tasks) + idleSlots if idleSlots > 0 else len(tasks)
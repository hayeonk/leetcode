class Solution(object):
    def maxDistToClosest(self, seats):
        person = []
        for i, n in enumerate(seats):
            if n:
                person.append(i)
        
        ans = 0
        for i in xrange(1, len(person)):
            ans = max(ans, (person[i] - person[i-1]) / 2)
            
        ans = max(ans, person[0])
        ans = max(ans, len(seats) - person[-1] - 1)
        return ans
from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        d = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            d[f].append(t)
        
        ans = []
        def visit(u):
            while d[u]:
                visit(d[u].pop())
            ans.append(u)
        
        visit("JFK")
        return ans[::-1]
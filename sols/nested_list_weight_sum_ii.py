# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import defaultdict
class Solution(object):
    def depthSumInverse(self, nestedList):
        level = defaultdict(int)
        
        def getSum(nestedList, depth):
            for num in nestedList:
                if num.isInteger():
                    level[depth] += num.getInteger()
                else:
                    getSum(num.getList(), depth + 1)
        getSum(nestedList, 0)
        
        if not level:
            return 0
        
        ans = 0
        maxDepth = max(level.keys()) + 1
        for n in level:
            ans += (maxDepth - n) * level[n]
        return ans
        
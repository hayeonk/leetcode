import math

class Solution(object):
    def getPermutation(self, n, k):
        nums = range(1, n+1)
        ret = []
        for i in reversed(xrange(n)):
            case = math.factorial(i)
            idx = (k - 1) / case
            ret.append(nums[idx])
            del nums[idx]
            k -= case * idx
        ret = map(str, ret)
        return "".join(ret)
        
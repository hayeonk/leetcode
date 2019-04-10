from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        
        f = Counter(nums)
        A = sorted(f.keys())
        pick = []
        notpick = []
        
        for i, n in enumerate(A):
            if i == 0:
                pick.append(n * f[n])
                notpick.append(0)
            else:
                if A[i] == A[i-1] + 1:
                    pick.append(notpick[i-1] + n * f[n])
                    notpick.append(max(pick[i-1], notpick[i-1]))
                else:
                    pick.append(max(pick[i-1], notpick[i-1]) + n * f[n])
                    notpick.append(max(pick[i-1], notpick[i-1]))
        
        return max(pick[-1], notpick[-1])
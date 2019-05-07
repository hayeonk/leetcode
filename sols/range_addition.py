class Solution(object):
    def getModifiedArray(self, length, updates):
        update = [0] * length
        for s, e, d in updates:
            update[s] += d
            if e + 1 < length:
                update[e+1] -= d
            
        ans = []
        for v in update:
            if not ans:
                ans.append(v)
            else:
                ans.append(ans[-1] + v)
        return ans
class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) <= k:
            return "0"
        
        ans = []
        for c in num:
            if not ans:
                ans += [c]
                continue
            if k:
                while k and ans and ans[-1] > c:
                    ans.pop()
                    k -= 1
                ans += [c]
            else:
                ans += [c]
        if k:
            ans = ans[:-k]
        return str(int("".join(ans)))
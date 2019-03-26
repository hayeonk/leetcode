class Solution(object):
    def countBits(self, num):
        ans = [0]
        m = 0
        while (1<<m) <= num:
            for i in xrange((1<<m)):
                ans += [ans[i] + 1]
            m += 1
        return ans[:num+1]
class Solution(object):
    def maximumSwap(self, num):
        ans = num
        num = map(int, str(num))
        n = len(num)
        maxval, maxidx, minidx = 0, n-1, n-1
        
        for i in xrange(n-1, -1, -1):
            if num[i] > maxval:
                maxval = num[i]
                maxidx = i
            else:
                minidx = i
            if maxidx > minidx:
                num[maxidx], num[minidx] = num[minidx], num[maxidx]
                ans = max(ans, int("".join(map(str, num))))
                num[maxidx], num[minidx] = num[minidx], num[maxidx]
        
        return ans
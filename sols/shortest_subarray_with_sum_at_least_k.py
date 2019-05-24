from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        psum = [0]
        for n in A:
            psum.append(psum[-1] + n)
        
        ans = len(A) + 1
        q = deque([0])
        
        for i, n in enumerate(psum):
            while q and psum[q[-1]] >= n:
                q.pop()
            
            while q and n - psum[q[0]] >= K:
                ans = min(ans, i - q.popleft())
            
            q.append(i)
            
        return -1 if ans == len(A) + 1 else ans
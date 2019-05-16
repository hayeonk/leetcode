from collections import Counter
class Solution(object):
    def canReorderDoubled(self, A):
        def check(A):
            C = Counter(A)
            for n in sorted(C):
                while C[n] > 0:
                        if C[2*n] <= 0:
                            return False
                        C[n] -= 1
                        C[2*n] -= 1
            return True
        
        return check([x for x in A if x > 0]) and check([-x for x in A if x < 0]) and A.count(0) % 2 == 0
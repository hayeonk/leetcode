class Solution(object):
    def intervalIntersection(self, A, B):
        ans = []
        
        while A and B:
            if A[0][1] < B[0][0]:
                A.pop(0)
                continue
            elif B[0][1] < A[0][0]:
                B.pop(0)
                continue
            
            if A[0][0] <= B[0][0] <= A[0][1]:
                ans.append([B[0][0], min(A[0][1], B[0][1])])
            elif B[0][0] <= A[0][0] <= B[0][1]:
                ans.append([A[0][0], min(A[0][1], B[0][1])])
            
            if A[0][1] <= B[0][1]:
                A.pop(0)
            else:
                B.pop(0)
        return ans
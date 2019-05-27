class Solution(object):
    def peakIndexInMountainArray(self, A):
        n = len(A)
        lo, hi = 0, n - 1
        
        while lo <= hi:
            mid = (lo + hi) / 2
            if mid > 0 and A[mid-1] < A[mid] and mid < n - 1 and A[mid] > A[mid+1]:
                return mid
            
            if mid == 0 or (mid > 0 and A[mid-1] < A[mid]):
                lo = mid + 1
            
            else:
                hi = mid - 1
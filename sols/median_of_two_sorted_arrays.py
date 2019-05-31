class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(nums1), len(nums2)
        if m > n:
            A, B, m, n = B, A, n, m
        
        imin, imax, halfLen = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = halfLen - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    maxLeft = B[j-1]
                elif j == 0:
                    maxLeft = A[i-1]
                else:
                    maxLeft = max(A[i-1], B[j-1])
                
                if (m + n) % 2 == 1:
                    return maxLeft
                
                if i == m:
                     minRight = B[j]
                elif j == n:
                    minRight = A[i]
                else:
                    minRight = min(A[i], B[j])
                
                return (maxLeft + minRight) / 2.0
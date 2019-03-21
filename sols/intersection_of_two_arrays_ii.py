from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        ret = []
        for n in nums1:
            if n in nums2:
                ret += [n] * min(nums1[n], nums2[n])
        return ret
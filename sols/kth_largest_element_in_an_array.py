class Solution(object):
    def findKthLargest(self, nums, k):
        def partition(nums, l, r):
            low = l
            while l < r:
                if nums[l] > nums[r]:
                    nums[l], nums[low] = nums[low], nums[l]
                    low += 1
                l += 1
            nums[low], nums[r] = nums[r], nums[low]
            return low
            
        if nums:
            pos = partition(nums, 0, len(nums)-1)
            if k > pos + 1:
                return self.findKthLargest(nums[pos+1:], k-pos-1)
            elif k < pos + 1:
                return self.findKthLargest(nums[:pos], k)
            else:
                return nums[pos]
                
class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        
        count1, count2, cand1, cand2 = 0, 0, 0, 1
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                count1, cand1 = 1, n
            elif count2 == 0:
                count2, cand2 = 1, n
            else:
                count1, count2 = count1 - 1, count2 - 1
        
        return [x for x in (cand1, cand2) if nums.count(x) > len(nums)/3.0]
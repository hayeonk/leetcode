class NumArray(object):

    def __init__(self, nums):
        self.psum = [0]
        for n in nums:
            self.psum.append(n + self.psum[-1])
        
    def sumRange(self, i, j):
        return self.psum[j+1] - self.psum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
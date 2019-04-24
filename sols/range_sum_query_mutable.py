class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            self.add(i, nums[i])
        
    def add(self, i, val):
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += (i & -i)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        self.add(i, diff)
        
    def sumRange(self, i, j):
        return self.sum(j) - self.sum(i-1)
        
    def sum(self, i):
        i += 1
        ret = 0
        while i:
            ret += self.tree[i]
            i &= i - 1
        return ret


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
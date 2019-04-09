class Solution(object):
    def transpose(self, A):
        ret = []
        for col in zip(*A):
            ret.append(list(col))
        return ret
class Solution(object):
    def isStrobogrammatic(self, num):
        if set("23457") & set(num):
            return False
        
        i, j = 0, len(num)-1
        
        while i <= j:
            if i == j:
                if num[i] in ["1", "0", "8"]:
                    return True
                return False
            if num[i] + num[j] in ["69", "11", "88", "96", "00"]:
                i += 1
                j -= 1
            else:
                return False
            
        return True
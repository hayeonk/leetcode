class Solution(object):
    def addBinary(self, a, b):
        i = len(a)-1
        j = len(b)-1
        a = map(int, list(a))
        b = map(int, list(b))
        
        carry = 0
        ret = []
        while i >= 0 and j >= 0:
            ret += [(a[i] + b[j] + carry) % 2]
            carry = (a[i] + b[j] + carry) / 2
            i -= 1
            j -= 1
        
        while i >= 0:
            ret += [(a[i] + carry) % 2]
            carry = (a[i] + carry) / 2
            i -= 1
        
        while j >= 0:
            ret += [(b[j] + carry) % 2]
            carry = (b[j] + carry) / 2
            j -= 1
            
        if carry:
            ret.append(1)
        ret = map(str, ret)    
        return "".join(ret[::-1])
class Solution(object):
    def isLongPressedName(self, name, typed):
        n = len(name)
        m = len(typed)
        
        if m < n:
            return False
        
        i = j = 0
        while i < n:
            if j >= m:
                return False
            
            if name[i] == typed[j]:
                i += 1
                j += 1
                
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            
            else:
                while j < m and typed[j] == typed[j-1]:
                    j += 1
        
        return True
class Solution(object):
    def canTransform(self, start, end):
        if len(start) != len(end):
            return False
        
        if start.count("X") != end.count("X") or start.count("R") != end.count("R"):
            return False
        
        if [x for x in start if x != "X"] != [x for x in end if x != "X"]:
            return False
        
        l1 = [i for i, x in enumerate(start) if x == "L"]
        l2 = [i for i, x in enumerate(end) if x == "L"]
        for i, j in zip(l1, l2):
            if i < j:
                return False
        
        r1 = [i for i, x in enumerate(start) if x == "R"]
        r2 = [i for i, x in enumerate(end) if x == "R"]
        for i, j in zip(r1, r2):
            if i > j:
                return False
        
        return True
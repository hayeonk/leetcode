class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2
        
        bottomLeft = max(a1, x1), max(b1, y1)
        topRight = min(a2, x2), min(b2, y2)
        
        if bottomLeft[0] >= topRight[0] or bottomLeft[1] >= topRight[1]:
            return False
        return True
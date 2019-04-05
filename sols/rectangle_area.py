class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        area = (C - A) * (D - B) + (G - E) * (H - F)
        bottomLeft = [max(A, E), max(B, F)]
        topRight = [min(C, G), min(D, H)]
        if topRight[0] <= bottomLeft[0] or topRight[1] <= bottomLeft[1]:
            overlap = 0
        else:
            overlap = (topRight[0] - bottomLeft[0]) * (topRight[1] - bottomLeft[1])
        
        return area - overlap
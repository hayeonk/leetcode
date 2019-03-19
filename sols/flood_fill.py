class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        originColor = image[sr][sc]
        if originColor == newColor:
            return image
        
        m = len(image)
        n = len(image[0])
        
        def fill(i, j):
            if image[i][j] == originColor:
                image[i][j] = newColor
                if i > 0: fill(i-1, j)
                if j > 0: fill(i, j-1)
                if i < m-1: fill(i+1, j)
                if j < n-1: fill(i, j+1)
                    
        fill(sr, sc)
        return image
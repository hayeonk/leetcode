class Solution(object):
    def minCost(self, costs):
        if not costs:
            return 0
        
        red, blue, green = costs[0]
        for r, b, g in costs[1:]:
            nextRed = r + min(blue, green)
            nextBlue = b + min(red, green)
            nextGreen = g + min(red, blue)
            
            red, blue, green = nextRed, nextBlue, nextGreen
            
        return min(red, blue, green)
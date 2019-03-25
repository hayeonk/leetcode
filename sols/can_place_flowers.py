class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        cnt = 0
        for i in xrange(len(flowerbed)):
            if not any(flowerbed[max(0, i-1):i+2]):
                cnt += 1
                flowerbed[i] = 1
        return cnt >= n
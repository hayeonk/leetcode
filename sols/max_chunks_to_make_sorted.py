class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = 0
        i = j = 0
        while j < len(arr):
            if sorted(arr[i:j+1]) == range(i, j + 1):
                i = j + 1
                ans += 1
            j += 1
        return ans
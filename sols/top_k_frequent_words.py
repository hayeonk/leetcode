from collections import Counter
from heapq import *

class Solution(object):
    def topKFrequent(self, words, k):
        words = Counter(words)
        heap = [(-freq, word) for word, freq in words.items()]
        heapify(heap)
        return [x[1] for x in nsmallest(k, heap)]
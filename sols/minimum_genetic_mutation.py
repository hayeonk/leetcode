from collections import defaultdict
from collections import deque

class Solution(object):
    def minMutation(self, start, end, bank):
        if not bank or end not in bank:
            return -1
        
        n = len(start)
        d = defaultdict(list)
        visit = defaultdict(int)
        for word in bank:
            for i in xrange(n):
                d[word[:i] + "*" + word[i+1:]].append(word)
        
        q = deque([(start, 0)])
        visit[start] = 1
        while q:
            word, l = q.popleft()
            if word == end:
                return l
            for i in xrange(n):
                nextWord = word[:i] + "*" + word[i+1:]
                for w in d[nextWord]:
                    if not visit[w]:
                        visit[w] = 1
                        q.append((w, l + 1))
                d[nextWord] = []
        return -1
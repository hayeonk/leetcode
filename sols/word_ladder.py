from collections import defaultdict
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not wordList:
            return 0
        
        n = len(beginWord)
        visit = defaultdict(int)
        cdict = defaultdict(list)
        for word in wordList:
            for i in xrange(n):
                cdict[word[:i] + "*" + word[i+1:]].append(word)
            
        q = deque([(beginWord, 1)])
        
        while q:
            w, l = q.popleft()
            if visit[w]:
                continue
            if w == endWord:
                return l
            visit[w] = 1
            for i in xrange(n):
                nextWord = w[:i] + "*" + w[i+1:]
                for word in cdict[nextWord]:
                    if not visit[word]:
                        q.append((word, l+1))
                cdict[nextWord] = []
        return 0
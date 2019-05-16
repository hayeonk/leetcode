class Solution(object):
    def pushDominoes(self, dominoes):
        dominoes = list(dominoes)
        n = len(dominoes)
        left = [0] * n
        right = [0] * n
        
        cnt = 0
        for i in xrange(n):
            if dominoes[i] == "R":
                right[i] = 1
                cnt = 2
            elif dominoes[i] == "L":
                right[i] = 0
                cnt = 0
            else:
                right[i] = cnt
                if cnt:
                    cnt += 1
        
        cnt = 0
        for i in xrange(n-1, -1, -1):
            if dominoes[i] == "L":
                left[i] = 1
                cnt = 2
            elif dominoes[i] == "R":
                left[i] = 0
                cnt = 0
            else:
                left[i] = cnt
                if cnt:
                    cnt += 1
        
        for i in xrange(n):
            if dominoes[i] == "L" or dominoes[i] == "R" or left[i] == right[i]:
                continue
            
            if left[i] == 0 or (right[i] and left[i] > right[i]):
                dominoes[i] = "R"
            
            elif right[i] == 0 or (left[i] and left[i] < right[i]):
                dominoes[i] = "L"
            
        return "".join(dominoes)
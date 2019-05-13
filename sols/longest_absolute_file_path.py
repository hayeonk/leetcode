class Solution(object):
    def lengthLongestPath(self, input):
        input = input.split("\n")
        ans = 0
        
        cur = []
        for path in input:
            cnt = path.count("\t")
            while len(cur) > cnt:
                cur.pop()
            cur.append("".join(path.split("\t")))
            if "." in path:
                ans = max(ans, len("/".join(cur)))
                
        return ans
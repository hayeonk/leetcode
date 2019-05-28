from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        d = defaultdict(list)
        
        for path in paths:
            path = path.split()
            directory = path[0]
            files = path[1:]
            
            for f in files:
                name, content = f.split("(")
                d[content].append((directory, name))
        
        ans = []
        for content in d:
            if len(d[content]) > 1:
                sameFiles = []
                for directory, name in d[content]:
                    sameFiles.append("/".join([directory, name]))
                ans.append(sameFiles)
        return ans
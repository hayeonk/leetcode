class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        for i, word in enumerate(s):
            s[i] = "".join(reversed(word))
        return " ".join(s)
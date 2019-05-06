"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def read(self, buf, n):
        ans = 0
        while n:
            tmp = [' '] * 4
            cnt = read4(tmp)
            
            if n < cnt:
                for i in xrange(n):
                    buf[ans+i] = tmp[i]
                ans += n
                break
            
            elif cnt < 4:
                for i in xrange(cnt):
                    buf[ans+i] = tmp[i]
                ans += cnt
                break
            
            else:
                for i in xrange(4):
                    buf[ans+i] = tmp[i]
                n -= cnt
                ans += cnt
                
        return ans
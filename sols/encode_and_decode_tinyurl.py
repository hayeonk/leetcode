class Codec:
    def __init__(self):
        self.i = 0
        self.d = {}

    def encode(self, longUrl):
        self.d[self.i] = longUrl
        self.i += 1
        
        return "http://tinyurl.com/%d" % (self.i - 1)
        

    def decode(self, shortUrl):
        return self.d[int(shortUrl.split("http://tinyurl.com/")[1])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
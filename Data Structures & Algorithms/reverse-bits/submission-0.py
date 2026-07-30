class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0 
        for i in range(32): 
            x += (n - ((n >> 1) << 1)) << (31-i) 
            n = n >> 1 
        return x 
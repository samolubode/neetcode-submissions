class Solution:
    def hammingWeight(self, n: int) -> int:
        # n & (n - 1) clears out the lowest set bit of the binary
        # once all the lowest set bit is cleared out, the binary becomes zero

        count = 0 # counter to keep track of the 1-bits

        while n > 0:
            count += 1
            n = n & (n - 1)
        
        return count

        
class Solution:
    def reverseBits(self, n: int) -> int:
        # approach: while n is still greater than zero
        #           append lowest bit to a string;
        #           remove lowest bit (shift to right by 1)
        #         concate string with 0 * (32 - length of string)
        #         convert to int and return value

        res = ''

        while n > 0:
            lowest = n & 1
            res += str(lowest)
            n >>= 1

        leading_zeros = '0' * (32 - len(res))
        res += leading_zeros

        return int(res, 2)

        
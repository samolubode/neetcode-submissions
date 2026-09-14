class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointers: left and right
        # change letter to lower case: palindrome is case-insensitive
        # while left <= right
            # if left not in range ord(A) and ord(Z) Or Ord(a) and ord(z)
            # or ord('0') and ord('9'), increment left
            # if right not in same range, decrement right

            # if s[left] != s[right], return false
            # left+=1; right-=1
        # return true

        lowerS = s.lower()
        orda, ordz = ord('a'), ord('z')
        ord0, ord9 = ord('0'), ord('9')

        def isAlphanumeric(num):
            if not (ord0 <= ord(num) <= ord9 or orda <= ord(num) <= ordz):
                return False
            return True

        left, right = 0, len(s) - 1

        while left <= right:
            if not isAlphanumeric(lowerS[left]):
                left += 1
                continue
            if not isAlphanumeric(lowerS[right]):
                right -= 1
                continue
            if lowerS[left] != lowerS[right]:
                return False
            left += 1
            right -= 1

        return True
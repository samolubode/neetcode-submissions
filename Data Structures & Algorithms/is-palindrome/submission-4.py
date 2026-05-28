class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointers: left and right
        # while left <= right
            # if left not in range ord(A) and ord(Z) Or Ord(a) and ord(z)
            # increment left
            # if right not in range ord(A) and ord(Z) Or Ord(a) and ord(z)
            # decrement right

            # if s[left] != s[right], return false
            # left+=1; right-=1
        # return true
        lowerS = s.lower()
        orda, ordz = ord('a'), ord('z')
        ord0, ord9 = ord('0'), ord('9')

        left, right = 0, len(s) - 1

        while left <= right:
            if not (ord0 <= ord(lowerS[left]) <= ord9 or orda <= ord(lowerS[left]) <= ordz):
                left += 1
                continue
            if not (ord0 <= ord(lowerS[right]) <= ord9 or orda <= ord(lowerS[right]) <= ordz):
                right -= 1
                continue
            if lowerS[left] != lowerS[right]:
                return False
            left += 1
            right -= 1

        return True
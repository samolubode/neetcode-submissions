class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # this looks like a sliding window's problem
        # we can define the l & r end of a window, where r extends
        # until a repeating character is found in the window
        # then l is incremented, r resetted to l and the window begins expanding again(so does hashmap/set), checking 
        # or adding chars to a hashmap/set based on if it already exists or not

        l = r = 0
        hashmap = {}
        longest = 0

        while r < len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = True
                longest = max(longest, len(list(hashmap.keys())))
            else:
                longest = max(longest, len(list(hashmap.keys())))
                hashmap = {}
                l += 1
                r = l
                continue
            r += 1

        return longest
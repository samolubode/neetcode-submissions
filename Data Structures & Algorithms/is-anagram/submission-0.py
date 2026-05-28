class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return False if len(s) != len(t)
        # define two new dicts for s and t element resp
        # loop through s
            # increment the value of key if it doesn't exist: both
        # return True if dict1 == dict2, else return False

        if len(s) != len(t):
            return False

        dict1 = {} # hold keys for s
        dict2 = {} # hold keys for t

        length_of_arr = len(s)

        for i in range(length_of_arr):
            if s[i] in dict1:
                dict1[s[i]] += 1
            else:
                dict1[s[i]] = 1

            if t[i] in dict2:
                dict2[t[i]] += 1
            else:
                dict2[t[i]] = 1

        if dict1 != dict2:
            return False

        return True





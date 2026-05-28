class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # calculate freq(using arr) for each char in each str
        # check if the freq exists in a hashmap: add if not
        # append each str that match freq as value for the freq key
        # return list of the hashmap values

        if not strs:
            return []

        hashmap = {}

        for str in strs:
            freq_list = [0] * 26
            # loop through str and set char frequency
            for char in str:
                freq_list[ord(char) - ord('a')] += 1

            if tuple(freq_list) not in hashmap:
                hashmap[tuple(freq_list)] = [str]
            else:
                hashmap[tuple(freq_list)].append(str)
   
        return list(hashmap.values())

        
class Solution:

    def encode(self, strs: List[str]) -> str:
        # NOTE: 4#neet, not #4neet. we put the 
        # length of word first before the delimitier. 
        # That way, we can easily extract the word length 
        # irrespective of the size.
        # formular -> len(s) + # + s
        
        res = ''

        for s in strs:
            encoded_str = str(len(s)) + '#' + s
            res += encoded_str

        return res
        

    def decode(self, s: str) -> List[str]:
        str_len = len(s)
        res = []
        i = 0

        while i < str_len:
            j = i
            
            while s[j] != '#':
                j += 1

            indxh = j
            wl = int(s[i : j])
            fl_indx = indxh + 1
            i = fl_indx+wl
            word = s[fl_indx: i]
            res.append(word)

        return res


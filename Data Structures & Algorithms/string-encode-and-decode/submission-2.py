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

        print('encoded:', res)
        return res
        

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you
        # int i = j = 0
        # while i < len(s)
        # while char != "#", j += 1
        # indxh = j + 1
        # wl = s[i : indxh] -> to int
        # fl_indx = indxh + 1
        # i = fl_indx+wl
        # word = s[fl_indx: i]

        str_len = len(s)
        res = []
        i = 0
        # 4#neet4#code4#love3#you
        while i < str_len:
            j = i
            for ci in range(i, str_len):
                if s[ci] == "#":
                    break
                j += 1

            indxh = j
            wl = int(s[i : j])
            fl_indx = indxh + 1
            i = fl_indx+wl #6
            word = s[fl_indx: i]
            res.append(word)
            print('decoded:', res)

        return res


// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def count_chars(s):
            m = {}
            for c in s:
                if m.get(c):
                    m[c] += 1
                else:
                    m[c] = 1 
            return m

        res = 0
        cc = count_chars(chars)

        for word in words:

            good_word = True
            cw = count_chars(word)

            for key, val in cw.items():

                if val > cc.get(key, 0):
                    good_word = False
                    break
            
            if good_word:
                res += len(word) 

        return res
            


                    


                
            
        
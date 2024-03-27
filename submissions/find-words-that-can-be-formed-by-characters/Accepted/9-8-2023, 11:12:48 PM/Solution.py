// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        good_words = []
        cc = {}

        for c in chars:

            if cc.get(c):
                cc[c] += 1
            else:
                cc[c] = 1 
        
        for word in words: 
            
            l_cc = dict(cc)
            to_add = True
            
            for c in word:

                count = l_cc.get(c)
                if not count:
                    to_add = False
                    break
                    
                if count == 1:
                    l_cc.pop(c)
                else: 
                    l_cc[c] -= 1

            if to_add:
                good_words.append(word)

        res = 0 
        for word in good_words:
            res += len(word)

        return res
            


                    


                
            
        
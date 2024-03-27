// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def count_map(items):
            _ = {}

            for x in items:
                if _.get(x):
                    _[x] += 1
                else:
                    _[x] = 1

            return _
            

        res = 0
        cm_chars = count_map(chars)

        for word in words: 

            tmp = dict(cm_chars)
            exists = True
            
            for c in word: 

                if tmp.get(c, 0) > 0:
                    tmp[c] -= 1
                else: 
                    exists = False
                    break

            if exists:
                res += len(word)

        return res
                                    
                
                
            
            

            


         
        
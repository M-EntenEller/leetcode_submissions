// https://leetcode.com/problems/number-of-different-integers-in-a-string

class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        _s = set()
        tmp = []

        for c in word:

            if c.isdigit():
                tmp.append(c)
            elif tmp:
                _s.add(int("".join(tmp))) 
                tmp = []

        if tmp:
            _s.add(int("".join(tmp))) 

        return len(_s)

                   
            

        
        
// https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        res = True
        state = word[0].isupper()

        for i in range(1,len(word)):

            c = word[i]
            up = c.isupper()

            if state and up:
                continue
            elif not state and not up:
                continue
            elif state and not up and i == 1:
                state = up
                continue  
            else: 
                return False

        return True             

            
            
            
            
            
            
        
        
        
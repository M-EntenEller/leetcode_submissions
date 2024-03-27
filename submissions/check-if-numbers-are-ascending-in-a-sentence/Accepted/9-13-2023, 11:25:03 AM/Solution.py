// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence

class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        n = len(s)
        level = 0
        i = j = -1

        for idx, c in enumerate(s):
            
            if ord("0") <= ord(c) and ord(c) <= ord("9"):
                
                if i > -1:
                    j = idx
                else: 
                    i = j = idx

                if idx < n - 1:
                    continue

            if i > -1:
                num = int(s[i:j+1])
                if num <= level:
                    return False
                else:
                    level = num
                    i = j = -1

        return True


            
                




        
                

        
        
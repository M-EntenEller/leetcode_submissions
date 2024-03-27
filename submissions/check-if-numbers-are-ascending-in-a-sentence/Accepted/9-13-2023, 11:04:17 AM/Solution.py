// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence

class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        level = 0
        tmp = []

        for c in (s + " "):
            
            if ord("0") <= ord(c) and ord(c) <= ord("9"):
                tmp.append(c)
                continue
         
            if tmp:
                num = int("".join(tmp))
                if num <= level:
                    return False
                else:
                    level = num   

            tmp = []
        
        return True




        
                

        
        
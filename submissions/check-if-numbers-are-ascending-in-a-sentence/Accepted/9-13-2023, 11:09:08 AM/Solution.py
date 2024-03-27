// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence

class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        level = 0
        tmp = []
        ascii_0 = ord("0")
        ascii_9 = ord("9")

        for c in s:
            
            ascii_c = ord(c)

            if ascii_0 <= ascii_c and ascii_c <= ascii_9:
                tmp.append(c)
                continue
         
            if tmp:
                num = int("".join(tmp))
                if num <= level:
                    return False
                else:
                    level = num   

            tmp = []
        
        if tmp:
            num = int("".join(tmp))
            if num <= level:
                return False

        return True




        
                

        
        
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping

class Solution:
    def freqAlphabets(self, s: str) -> str:

        n = len(s)
        i = 0
        base1 = ord("a")
        base2 = ord("j")
        res = []


        while i < n:

            if i + 2 < n and s[i + 2] == "#":
                num = int( s[i: i+2] )
                res.append( chr(base2 + num - 10) )
                i += 3
            else:
                res.append( chr( base1 + int(s[i]) - 1))
                i += 1

        return "".join(res)   


                


                  
            
            


            

            

            


        

            
        
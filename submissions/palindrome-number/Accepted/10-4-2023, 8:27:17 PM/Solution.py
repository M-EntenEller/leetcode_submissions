// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def its(x):
            res = []

            while x > 0:
                
                res.append(str(x % 10))
                x = x // 10

            res.reverse()
            return "".join(res)
        
        if x < 0: 
            return False
        s = its(x)
        i = 0
        j = len(s) - 1

        while i <= j:

            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                return False

        return True
                        
            
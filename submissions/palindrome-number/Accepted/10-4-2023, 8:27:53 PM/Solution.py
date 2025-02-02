// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: 
            return False
        s = str(x)
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
                        
            
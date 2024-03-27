// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: 
            return False
        
        reverse = 0
        tmp = x

        while tmp > 0:

            reverse = reverse * 10 + tmp % 10
            tmp = tmp // 10

        return reverse == x
             

                        
            
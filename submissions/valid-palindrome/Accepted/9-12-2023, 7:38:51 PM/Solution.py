// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:

        def valid_char(c):
            pred = ord("0") <= ord(c) and ord(c) <= ord("9")
            pred2 = ord("A") <= ord(c) and ord(c) <= ord("Z")
            pred3 = ord("a") <= ord(c) and ord(c) <= ord("z")
            return pred or pred2 or pred3
                

        cs = []

        for c in s:
            if valid_char(c):
                cs.append(c.lower())

        cs = "".join(cs)
        
        j = len(cs) - 1
        i = 0

        while i < j:

            if cs[i] != cs[j]:
                return False

            i +=1
            j -=1

        return True



        
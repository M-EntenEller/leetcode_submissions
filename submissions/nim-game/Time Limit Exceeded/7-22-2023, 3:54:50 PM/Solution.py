// https://leetcode.com/problems/nim-game

class Solution:

    def canWinNim(self, n: int) -> bool:
        
        if n<=3:
            return True
        else: 
            return not (self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3))
        
        
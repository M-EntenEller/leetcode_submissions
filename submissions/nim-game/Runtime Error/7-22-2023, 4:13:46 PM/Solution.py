// https://leetcode.com/problems/nim-game

class Solution:

    def canWinNim(self, n: int) -> bool:

        memo_map = {}
        
        def cwn(n:int):
            if n<=3:
                return True        
            else: 
                p1 = memo_map.get(n-1, None)
                if not p1:
                    p1 = cwn(n-1)
                    memo_map[n-1] = p1

                p2 = memo_map.get(n-2, None)
                if not p2:
                    p2 = cwn(n-2)
                    memo_map[n-2] = p2

                p3 = memo_map.get(n-3, None)
                if not p3:
                    p3 = cwn(n-3)
                    memo_map[n-3] = p3
                    
                return not (p1 and p2 and p3)
        
        return cwn(n)
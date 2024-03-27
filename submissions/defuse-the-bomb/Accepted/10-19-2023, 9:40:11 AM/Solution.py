// https://leetcode.com/problems/defuse-the-bomb

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code)
        res = []

        if k == 0:
            return [0]*n

        for i in range(n):
            
            tmp = 0

            for j in range (k, 0, 1 if k<0 else -1):

                tmp += code[(i+j+n) % n]
                
            res.append(tmp)
            
        return res




            
        
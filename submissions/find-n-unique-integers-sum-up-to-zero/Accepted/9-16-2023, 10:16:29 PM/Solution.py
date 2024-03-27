// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero

class Solution:
    def sumZero(self, n: int) -> List[int]:

        half_size = n//2

        i = 0
        j = n-1
        res = [0 for _ in range(n)]

        for k in range(1, half_size + 1):

            res[i] = k
            res[j] = -k
            i += 1
            j -= 1

        return res        
            
            
        

            


        
        
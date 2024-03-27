// https://leetcode.com/problems/xor-operation-in-an-array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        agg = 0
        for i in range(n): 
            agg = agg ^ start + 2 * i

        return agg

        
// https://leetcode.com/problems/xor-operation-in-an-array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        nums = [start + 2 * i for i in range(n)]

        agg = 0
        for i in range(n): 
            agg = agg ^ nums[i]

        return agg

        
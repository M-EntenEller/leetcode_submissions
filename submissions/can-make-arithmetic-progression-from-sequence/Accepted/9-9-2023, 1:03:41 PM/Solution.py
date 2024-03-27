// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        n = len(arr)
        arr.sort()
        diff = arr[0] - arr[1]

        for i in range(1, n-1):
            
            if not arr[i] - arr[i+1] == diff:
                return False 

        return True
        
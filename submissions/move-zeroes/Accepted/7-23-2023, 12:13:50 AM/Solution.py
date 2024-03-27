// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        non_zeros = []
        zero_count = 0

        for i in range(n):
            tmp = nums[i]

            if tmp != 0:
                non_zeros.append(tmp)    
        
        n2 = len(non_zeros)

        for i in range(n):
            if i < n2:
                nums[i] = non_zeros[i]
            else: 
                nums[i] = 0

        return 

        
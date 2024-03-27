// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i=0
        h=None 

        for i in range(n):
            
            if nums[i] == 0:

                if not h:
                    h=i+1

                while h < n and nums[h] == 0:
                    h += 1

                if h == n:
                    return 
                else:
                    nums[i] = nums[h]
                    nums[h] = 0 
                    h += 1

        return 

        


                

                



        
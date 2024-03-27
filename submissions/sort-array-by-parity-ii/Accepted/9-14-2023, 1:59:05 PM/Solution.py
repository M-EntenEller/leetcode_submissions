// https://leetcode.com/problems/sort-array-by-parity-ii

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        lige = []
        ulige = []

        for num in nums: 
            
            if num % 2 == 0:
                lige.append(num)
            else:
                ulige.append(num)

        for idx, _ in enumerate(nums):

            if idx % 2 == 0:

                nums[idx] = lige.pop()

            else:

                nums[idx] = ulige.pop()

        return nums
            
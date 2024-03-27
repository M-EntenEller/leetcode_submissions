// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements

class Solution:
    def countElements(self, nums: List[int]) -> int:

        _min = 10**5
        _max = -10**5
        res = 0

        for num in nums: 
            
            if num < _min:
                _min = num
            if num > _max:
                _max = num
            
        for num in nums: 

            if num > _min and num < _max:
                    res += 1

        return res

                
        
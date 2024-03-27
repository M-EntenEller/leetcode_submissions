// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}

        for idx, x in enumerate(nums):
            
            c = m.get(x)
            if not c == None:
                return [c, idx]  

            m[target - x] = idx

        
        
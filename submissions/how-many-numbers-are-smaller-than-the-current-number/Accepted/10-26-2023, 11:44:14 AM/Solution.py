// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        res = []
        _map = {}
        s_nums = nums.copy()
        
        s_nums.sort()

        count = 0
        tmp = -1
        
        for num in s_nums: 
            
            count += 1

            if num == tmp: 
                continue
            else: 
                _map[num] = count - 1
                tmp = num
        
        for num in nums: 

            res.append(_map.get(num))

        return res
            
            

        

            

                

            



        
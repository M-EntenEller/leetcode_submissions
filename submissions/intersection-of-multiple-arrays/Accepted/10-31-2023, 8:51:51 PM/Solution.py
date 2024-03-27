// https://leetcode.com/problems/intersection-of-multiple-arrays

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        sect = set(nums[0])

        for i in range(1,len(nums)):
            
            tmp = set(nums[i])
            new_sect = set()

            while sect:
                
                num = sect.pop()
                if num in tmp:
                    new_sect.add(num)

            sect = new_sect

        res = [x for x in sect]
        res.sort()
        return res

              
        
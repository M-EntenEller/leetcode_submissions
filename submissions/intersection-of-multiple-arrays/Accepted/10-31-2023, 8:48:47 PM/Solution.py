// https://leetcode.com/problems/intersection-of-multiple-arrays

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        sect = set(nums[0])

        for i in range(1,len(nums)):
            
            tmp = set(nums[i])
            to_remove = []

            for num in sect:

                if not num in tmp:
                    to_remove.append(num)
                    
            for num in to_remove:
                sect.remove(num)

        res = [x for x in sect]
        res.sort()
        return res

              
        
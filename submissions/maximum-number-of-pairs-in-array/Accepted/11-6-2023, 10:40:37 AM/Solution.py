// https://leetcode.com/problems/maximum-number-of-pairs-in-array

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        pairs = 0
        seen = set()

        for num in nums: 

            if num in seen:
                pairs += 1
                seen.remove(num)
            else:
                seen.add(num)

        return [pairs, len(nums)-pairs*2]
            

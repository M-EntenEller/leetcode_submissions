// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}
        n = len(nums)
        
        for i in range(n):
            diff = target - nums[i]
            if not m.get(diff):
                m[diff] = [i]
            else:
                m[diff].append(i)
             

        for i in range(n):
            if m.get(nums[i]):
                for idx in m[nums[i]]:
                    if idx != i:
                        return [idx, i]

        return None
        
// https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        csum = 0
        m_csum = {} # idx -> sum
        
        for idx, num in enumerate(nums): 
            
            csum += num
            m_csum[idx] = csum

        for idx, num in enumerate(nums):

            if m_csum.get(idx - 1, 0) == csum - m_csum.get(idx, 0):
                return idx

        return -1
                  
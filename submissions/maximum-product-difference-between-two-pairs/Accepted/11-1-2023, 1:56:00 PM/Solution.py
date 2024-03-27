// https://leetcode.com/problems/maximum-product-difference-between-two-pairs

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        a = b = 0
        c = d = 10**4 + 1

        for i, num in enumerate(nums): 

            old_a = a
            a = max(a, num)
            if old_a != a:
                b = old_a
            else: 
                b = max(b, num)

            old_c = c
            c = min(c, num)
            if old_c != c:
                d = old_c
            else:
                d = min(d, num)

        return a*b - c*d
        

        
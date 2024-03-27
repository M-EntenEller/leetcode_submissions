// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        n = len(arr)

        for i in range(n):

            count = 1
            j = 1

            while i+j < n and arr[i+j] == arr[i]:
                
                count += 1
                j += 1

            if count / n > 0.25:
                return arr[i]
            

        
        
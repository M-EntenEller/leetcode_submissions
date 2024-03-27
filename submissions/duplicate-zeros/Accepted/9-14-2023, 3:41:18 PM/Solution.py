// https://leetcode.com/problems/duplicate-zeros

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        queue = []

        for num in arr:
            
            queue.append(num)
            if num == 0:
                queue.append(num)

        for i in range(len(arr)):
            arr[i] = queue[i]

        
        
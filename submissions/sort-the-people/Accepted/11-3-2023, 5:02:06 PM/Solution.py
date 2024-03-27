// https://leetcode.com/problems/sort-the-people

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)

        while n > 0:

            _min = 10**5+1
            _idx = 0

            for i in range(n):

                if heights[i] < _min:

                    _min = heights[i]
                    _idx = i

            tmp = names[n-1]
            names[n-1] = names[_idx]
            names[_idx] = tmp

            tmp = heights[n-1]
            heights[n-1] = heights[_idx]
            heights[_idx] = tmp

            n -= 1

        return names


            
        
        
// https://leetcode.com/problems/find-lucky-integer-in-an-array

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        

        count = {}
        _max = -1

        def count_item(x):
            if count.get(x):
                count[x] += 1
            else:
                count[x] = 1

        for x in arr:
            count_item(x)
        
        for key, val in count.items():
            if key == val:
                if key > _max:
                    _max = key 

        return _max
            
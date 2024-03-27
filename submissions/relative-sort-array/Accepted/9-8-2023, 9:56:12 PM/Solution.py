// https://leetcode.com/problems/relative-sort-array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        _m = {}
        def count_key(key):
            if _m.get(key):
                _m[key] += 1
            else:
                _m[key] = 1

        res = []
        remainder = []
            
        for x in arr1:
            count_key(x)

        for x in arr2: #arr2 in arr1
            for i in range(_m.pop(x)):
                res.append(x)

        for key in sorted(_m.keys()):
            for i in range(_m[key]):
                remainder.append(key)

        return res + remainder


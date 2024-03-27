// https://leetcode.com/problems/minimum-absolute-difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        n = len(arr)
        arr.sort()
        res = []
        _max = int(2*10**5)

        i = 0
        while i < n-1:

            l = arr[i]
            u = arr[i+1]
            if l > u:
                tmp = l
                l = u
                u = tmp
            diff = abs(l - u)

            if diff == _max:
                res.append([l,u])
            elif diff < _max:
                _max = diff
                res = [[l,u]]

            i += 1

        return res


                    
            

            
        

            
            
        
        
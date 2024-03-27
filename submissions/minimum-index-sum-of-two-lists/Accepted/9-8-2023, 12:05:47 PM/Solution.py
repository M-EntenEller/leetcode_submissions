// https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        n1 = len(list1)
        n2 = len(list2)

        msum = n1+n2 #max possible index sum
        res = []
        
        for i in range(n1):
            
            s = list1[i]
            
            for j in range(n2):
                
                if s == list2[j]:
                    if i+j == msum:
                        res.append(s)
                    elif i+j < msum:
                        msum = i+j
                        res = [s]

        return res

                        
                    


                
        
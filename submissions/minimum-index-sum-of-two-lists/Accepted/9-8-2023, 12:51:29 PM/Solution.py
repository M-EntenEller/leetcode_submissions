// https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        m1 = {}
        m2 = {}
        n1 = len(list1)
        n2= len(list2)
        msum = n1+n2
        res = []

        for idx, s in enumerate(list1):

            if not m1.get(s):
                m1[s] = idx

        for idx, s in enumerate(list2):
            
            if not m2.get(s):
                m2[s] = idx

                tmp = m1.get(s, -1)
                if tmp == -1:
                    continue
                
                idx_sum = tmp + idx
                
                if idx_sum == msum:
                    res.append(s)
                elif idx_sum < msum:
                    msum = idx_sum
                    res = [s]

        return res

        
            

            

                        
                    


                
        
// https://leetcode.com/problems/uncommon-words-from-two-sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        m1 = {}
        m2 = {}

        for s in s1.split():
            if m1.get(s):
                m1[s] += 1
            else:
                m1[s] = 1

        for s in s2.split():
            if m2.get(s):
                m2[s] += 1
            else:
                m2[s] = 1
                
        res = []

        for x, val in m1.items():
            if val == 1 and not m2.get(x): 
                res.append(x)

        for x, val in m2.items():
            if val == 1 and not m1.get(x):
                res.append(x)

        return res
            

        
        
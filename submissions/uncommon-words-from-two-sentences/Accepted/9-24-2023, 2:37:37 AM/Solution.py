// https://leetcode.com/problems/uncommon-words-from-two-sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        m = {}
        res = []

        for word in (s1 + " " + s2).split():

            if m.get(word):
                m[word] += 1
            else:
                m[word] = 1

        for key, val in m.items():

            if val == 1:
                res.append(key)

        return res
    
        

        

            

        
        
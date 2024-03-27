// https://leetcode.com/problems/minimum-string-length-after-removing-substrings

class Solution:
    def minLength(self, s: str) -> int:

        def remove_targets(s:str):
            n=len(s)
            res = []
            i = 0
            while i < n:
                if s[i] == "A":
                    if i < n - 1 and s[i+1] == "B":
                        print("b1")
                        i += 1
                        print("i now, ", i)
                    else:
                        res.append(s[i])
                elif s[i] == "C":
                    if i < n - 1 and s[i+1] =="D":
                        i += 1
                    else:
                        res.append(s[i])
                else: 
                    res.append(s[i])
                i += 1
            return "".join(res)

        tmp = remove_targets(s)

        while len(tmp) != len(s):
            s = tmp 
            tmp = remove_targets(s)

        return len(tmp)

        

        
        
// https://leetcode.com/problems/defanging-an-ip-address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        queue = []

        for c in address:
            
            if c == ".":
                queue.append("[.]")
            else:
                queue.append(c)

        return "".join(queue)
        
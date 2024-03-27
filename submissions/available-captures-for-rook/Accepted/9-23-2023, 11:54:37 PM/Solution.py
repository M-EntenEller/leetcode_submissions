// https://leetcode.com/problems/available-captures-for-rook

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        res = []

        def check(pos):
            item = board[pos[0]][pos[1]]
            if item == ".":
                return 0
            if item == "B":
                return -1
            if item == "p":
                res.append(1)
                return -1           

        pos = None
        for i in range(8):

                for j in range(8):

                    if board[i][j] == "R":
                        pos = (i,j)

        for i in range(pos[0] - 1, -1, -1):

            if check((i, pos[1])) == 0:
                continue
            else: 
                break

        for i in range(pos[0] + 1, 8):

            if check((i, pos[1])) == 0:
                continue
            else: 
                break

        for i in range(pos[1] - 1, -1, -1):

            if check((pos[0], i)) == 0:
                continue
            else: 
                break

        for i in range(pos[1] + 1, 8):

            if check((pos[0], i)) == 0:
                continue
            else: 
                break

        return sum(res)
            

        

            
            
            

        
     




        
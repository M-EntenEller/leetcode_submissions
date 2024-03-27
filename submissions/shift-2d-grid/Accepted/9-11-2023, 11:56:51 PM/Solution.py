// https://leetcode.com/problems/shift-2d-grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        # idx, k'th element. [i][j] = i*n + j
        # add k, then translate into array: [x // n % m][x%n] (looping around.) 
        # x 'th element to [x // n][x%n]

        m = len(grid)
        n = len(grid[0])

        res = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                lp = i*n + j + k
                res[ (lp // n) % m ][ lp % n] = grid[i][j]

        return res

        
        
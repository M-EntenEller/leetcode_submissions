// https://leetcode.com/problems/game-of-life

class Solution {

    private int updateDeadCell(int numNeighbors, int cellVal){

        return numNeighbors == 3 ? 1 : 0;

    }

    private int updateLiveCell(int numN, int cellV){

        if (numN < 2){
            return 0;
        }
        if (numN < 4){
            return 1;
        }
        return 0;

    }

    private int updateCell(int numN, int cellV){

        if (cellV == 1){
            return updateLiveCell(numN, cellV);
        }
        return updateDeadCell(numN, cellV);

    }

    private int getNumNeighbors(int[][] arr, int i, int j){
        
        int count = 0; 

        for (int r=i-1; r <= i+1; r++){

            if (r < 0 || r > arr.length-1){
                continue;
            }

            for (int c=j-1; c <= j+1; c++){

                if(c < 0 || c > arr[0].length-1){
                    continue;
                }
                if (r==i && c==j){
                    continue;
                }

                if (arr[r][c] == 1){
                    count++;
                }

            }

        }

        return count;

    }

    public void gameOfLife(int[][] board) {

        int[][] res = new int[board.length][board[0].length];
        
        for (int i=0; i<board.length; i++){

            for(int j=0; j<board[0].length; j++){

                res[i][j] = updateCell(getNumNeighbors(board, i,j), board[i][j]);
            }

        }

        for (int i=0; i<res.length; i++){
            for(int j=0; j<res[0].length;j++){
                board[i][j] = res[i][j];
            }
        }

        return;

    }
}
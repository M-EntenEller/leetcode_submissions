// https://leetcode.com/problems/furthest-point-from-origin

class Solution {
    public int furthestDistanceFromOrigin(String moves) {

        int ls = 0;
        int rs = 0; 

        for (int i=0; i<moves.length(); i++)
        {
            switch (moves.charAt(i))
            {
                case 'L':
                    ls++;
                    break;
                case 'R':
                    rs++;
                    break;
            }
        }

        return Math.abs(ls - rs) + (moves.length() - ls - rs);
        
    }
}
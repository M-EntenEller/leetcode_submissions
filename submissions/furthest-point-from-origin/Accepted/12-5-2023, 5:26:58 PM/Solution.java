// https://leetcode.com/problems/furthest-point-from-origin

class Solution {
    public int furthestDistanceFromOrigin(String moves) {

        int p = 0; 
        int count = 0;

        for (int i=0; i<moves.length(); i++)
        {
            switch (moves.charAt(i))
            {
                case 'L':
                    p--;
                    count++;
                    break;
                case 'R':
                    p++;
                    count++;
                    break;
            }
        }

        return Math.abs(p) + (moves.length() - count);
        
    }
}
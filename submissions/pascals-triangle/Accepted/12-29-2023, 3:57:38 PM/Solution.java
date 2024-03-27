// https://leetcode.com/problems/pascals-triangle

class Solution {
    public List<List<Integer>> generate(int numRows) {

        List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp;

        res.add(new ArrayList<Integer>());
        res.get(0).add(1);
        if (numRows==1){return res;}

        for (int i=1; i<numRows; i++)
        {
            tmp = new ArrayList<Integer>();
            tmp.add(1);
            
            for (int j=0; j<i-1; j++)
            {
                tmp.add(res.get(i-1).get(j) + res.get(i-1).get(j+1));
            }

            tmp.add(1);
            res.add(tmp);
        }

        return res;
    }
}
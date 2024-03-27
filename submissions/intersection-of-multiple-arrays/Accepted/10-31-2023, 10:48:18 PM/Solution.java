// https://leetcode.com/problems/intersection-of-multiple-arrays

class Solution {

    private Set<Integer> intersect(Set<Integer> x, Set<Integer> y){
        
        Set<Integer> res = new HashSet<Integer>();

        for (Integer e : x){
            
            if (y.contains(e)){
                res.add(e);
            }

        }

        return res;

    }

    private Set<Integer> newSetFilled(int[] fill){
        
        Set<Integer> res = new HashSet<Integer>();

        for (int i=0; i<fill.length; i++){
            res.add((Integer) fill[i]);
        }

        return res;

    }

    public List<Integer> intersection(int[][] nums) {

        Set<Integer> sect = newSetFilled(nums[0]);

        for (int i=1; i<nums.length; i++){

            Set<Integer> next = newSetFilled(nums[i]);
            sect = intersect(sect, next);

        }
        
        List<Integer> res = new ArrayList<Integer>(sect);
        res.sort(null);
        return res; 
    }
}
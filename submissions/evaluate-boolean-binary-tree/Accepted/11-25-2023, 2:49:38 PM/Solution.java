// https://leetcode.com/problems/evaluate-boolean-binary-tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    private boolean binOperator(boolean b1, boolean b2, int flag){

        if (flag == 2){
            return b1 || b2;
        }

        return b1 && b2;

    }

    public boolean evaluateTree(TreeNode root) {
        
        Set<TreeNode> seen = new HashSet<>();
        List<TreeNode> stack = new ArrayList<>();
        List<Boolean> res = new ArrayList<>();
        TreeNode tmp;
        int count = 0;

        stack.add(root);

        while (stack.size() > 0)
        {
            tmp = stack.get(stack.size()-1); //peek

            if (tmp.val < 2) //leaf
            { 
                res.add(tmp.val == 1);
                stack.remove(stack.size()-1);
            } 
            else if (!seen.contains(tmp))  // not leaf not seen
            {
                stack.add(tmp.right);
                stack.add(tmp.left);
                seen.add(tmp);
            } 
            else  // not leaf been seen
            {
                stack.remove(stack.size()-1);
                res.add( binOperator(res.remove(res.size()-1), res.remove(res.size()-1), tmp.val) );
            }
        }
        
        return (boolean) res.get(0); 

    }
}
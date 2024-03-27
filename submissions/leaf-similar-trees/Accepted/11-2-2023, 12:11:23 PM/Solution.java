// https://leetcode.com/problems/leaf-similar-trees

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

    private List<Integer> leafSequence(TreeNode root){
        
        if (root==null){
            return new ArrayList<Integer>();
        }

        if (root.left == null && root.right == null){
            return new ArrayList<Integer>(){{add(root.val);}};
        }
        
        return Stream.concat(leafSequence(root.left).stream(), leafSequence(root.right).stream()).toList();
    }

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {

        List<Integer> l = leafSequence(root1);
        List<Integer> r = leafSequence(root2);

        if (l.size() != r.size()){
            return false;
        } 

        for (int i=0; i<l.size(); i++){

            if (l.get(i) != r.get(i)){
                return false;
            }

        }
        
        return true;
    }
}
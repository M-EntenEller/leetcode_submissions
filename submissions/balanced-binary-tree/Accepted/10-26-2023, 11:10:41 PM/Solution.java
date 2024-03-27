// https://leetcode.com/problems/balanced-binary-tree

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

    class Dat{
        int height;
        boolean balanced;
        public Dat(int x, boolean b){
            this.height = x;
            this.balanced = b;
        }
    }

    public Dat hb(TreeNode node){

        if (node==null){
            return new Dat(0, true);
        }

        Dat l = hb(node.left);
        Dat r = hb(node.right);

        boolean balancedKids = l.balanced && r.balanced;
        int heightDelta = l.height - r.height >= 0 ? l.height - r.height : -(l.height - r.height);
        boolean balancedNode = heightDelta <= 1 && balancedKids;
        int heightNode = l.height <= r.height ? r.height + 1 : l.height + 1;

        return new Dat(heightNode, balancedNode);

    }

    public boolean isBalanced(TreeNode root) {

        return hb(root).balanced;
        
    }
}
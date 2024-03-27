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

    private int[] mergeArrays(int[] a, int[] b){
        int[] res = new int[a.length + b.length];
        for(int i=0; i<a.length; i++){
            res[i] = a[i];
        }
        for (int i=a.length; i<b.length + a.length; i++){
            res[i] = b[i-a.length];
        }
        return res;
    }

    private int[] leafSequence(TreeNode root){
        
        if (root==null){
            return new int[0];
        }

        if (root.left == null && root.right == null){
            return new int[]{root.val};
        }

        return mergeArrays(leafSequence(root.left), leafSequence(root.right));
    }

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {

        int[] l = leafSequence(root1);
        int[] r = leafSequence(root2);

        if (l.length != r.length){
            return false;
        } 

        for (int i=0; i<l.length; i++){

            if (l[i] != r[i]){
                return false;
            }

        }
        
        return true;
    }
}
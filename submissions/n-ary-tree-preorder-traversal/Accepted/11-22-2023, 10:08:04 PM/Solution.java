// https://leetcode.com/problems/n-ary-tree-preorder-traversal

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {

    public List<Integer> preorder(Node root) {

        if (root==null){
            return new ArrayList<Integer>();
        }

        List<Integer> res = new ArrayList();
        List<Node> stack = new ArrayList<>();
        stack.add(root);
       
        while(!stack.isEmpty()){

            Node p = stack.remove(stack.size()-1);
            res.add(p.val);
            
            for(int i=p.children.size()-1; i>=0; i--){

                stack.add(p.children.get(i));

            }

        }

        return res;

    }
}
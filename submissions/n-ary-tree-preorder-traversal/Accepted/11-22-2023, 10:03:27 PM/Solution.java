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

            Node pop = stack.remove(stack.size()-1);
            res.add(pop.val);
            Collections.reverse(pop.children);
            pop.children.stream().forEach(node -> stack.add(node));

        }

        return res;

    }
}
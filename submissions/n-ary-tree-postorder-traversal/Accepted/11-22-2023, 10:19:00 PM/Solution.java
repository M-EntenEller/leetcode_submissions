// https://leetcode.com/problems/n-ary-tree-postorder-traversal

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

    List<Integer> res = new ArrayList<>();

    private void _postorder(Node root){

        if (root ==null){
            return; 
        }

        root.children.stream().forEach(node -> _postorder(node));
        this.res.add(root.val);

    }

    public List<Integer> postorder(Node root) {

        _postorder(root);
        return res;
        
    }
}
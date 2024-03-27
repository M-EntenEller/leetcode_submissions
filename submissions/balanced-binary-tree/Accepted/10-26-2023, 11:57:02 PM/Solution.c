// https://leetcode.com/problems/balanced-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct HB{
    int h;
    char b;
};

struct HB get_hb(struct TreeNode* node){
    
    if (node==NULL){
        struct HB res = {0, 1};
        return res;
    }

    struct HB l = get_hb(node->left);
    struct HB r = get_hb(node->right);
    
    if (l.h < r.h){
        struct HB tmp = l;
        l = r;
        r = tmp;
    }

    char kidsBalanced = l.b && r.b;
    char nodeBalanced = kidsBalanced && (l.h - r.h <= 1);
    
    struct HB res = {l.h + 1, nodeBalanced};
    return res;
}

bool isBalanced(struct TreeNode* root){

    return get_hb(root).b;

}
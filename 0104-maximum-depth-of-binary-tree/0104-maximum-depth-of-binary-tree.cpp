/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
    if (root == nullptr) return 0; // Base case to stop recursion
    int left = maxDepth(root->left);  // Recursive call on left subtree
    int right = maxDepth(root->right); // Recursive call on right subtree
    return max(left, right) + 1;  // Take the max depth and add 1 (for current node)
}

};
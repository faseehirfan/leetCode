# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left,right) + 1
        
        dfs(root)
        return res

### BRUTE FORCE SOLUTION ###

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.maxDepth(root.right) 
        right = self.maxDepth(root.left)
        return max(left+right, self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))

    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
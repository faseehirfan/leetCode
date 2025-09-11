# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def find(root, target, path):
            if root is None:
                return False
            if root.val == target:
                return True

            path.append('L')
            if root.left and find(root.left, target, path):
                return True
            path.pop()

            path.append('R')
            if root.right and find(root.right, target, path):
                return True
            path.pop()

            return False

        start_path, dest_path = [], []
        find(root, startValue, start_path)
        find(root, destValue, dest_path)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        start_path = start_path[i:]
        dest_path = dest_path[i:]
        return 'U' * len(start_path) + ''.join(dest_path)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = root.val

        def dfs(root):
            if not root: return 0

            old_root_val = root.val
            left = dfs(root.left)
            right = dfs(root.right)
            root.val = max(root.val, root.val + left, root.val + right)
            self.res = max(self.res, root.val, old_root_val + right + left)

            return root.val
        

        dfs(root)


        return self.res
        
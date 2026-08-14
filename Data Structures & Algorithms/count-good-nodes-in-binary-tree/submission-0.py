# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node: return 0
            left = dfs(node.left, max(node.val, maxVal))
            right = dfs(node.right, max(node.val, maxVal))
            
            return 1 + left + right if node.val >= maxVal else 0 + left + right



        return dfs(root, float('-inf'))

        #   3 

        # 3  null

        # 4 2
        
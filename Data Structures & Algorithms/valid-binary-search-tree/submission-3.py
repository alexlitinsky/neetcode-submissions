# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid_bst(node, left, right):
            if not node: return True
            if left < node.val < right:
                return valid_bst(node.left, left, node.val) and valid_bst(node.right, node.val, right)
            return False

        

        return valid_bst(root.left, float('-inf'), root.val) and valid_bst(root.right, root.val, float('inf'))
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        def dfs(root):
            if not root: 
                preorder.append("#")
                return
            preorder.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        return ",".join(preorder)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        print(vals)

        root = TreeNode()
        i = 0

        def helper():
            nonlocal i
            if i == len(vals): return None  
            if vals[i] == "#": return None

            node = TreeNode(vals[i])
            i += 1
            node.left = helper()
            i += 1
            node.right = helper()

            return node
            
        return helper()



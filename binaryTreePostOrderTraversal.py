# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node):
            if not node:
                return []
            # Traverse left subtree, then right subtree, then visit node
            return helper(node.left) + helper(node.right) + [node.val]
        
        return helper(root)

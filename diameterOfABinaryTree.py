# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def getDepth(node):
            nonlocal diameter
            if not node:
                return 0

            left_depth = getDepth(node.left)
            right_depth = getDepth(node.right)

            diameter = max(diameter, left_depth+right_depth)
            return 1 + max(left_depth, right_depth)
        
        getDepth(root)
        return diameter

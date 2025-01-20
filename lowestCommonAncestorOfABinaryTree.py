# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def search(node):
            if not node:
                return None
            
            if node==p or node==q:
                return node
            
            left_search = search(node.left)
            right_search = search(node.right)

            if left_search and right_search:
                return node

            if left_search:
                return left_search

            return right_search
        
        return search(root)

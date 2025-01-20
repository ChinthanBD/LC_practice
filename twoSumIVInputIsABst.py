# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lookup_set = set()

        def dfs(node):
            if not node:
                return False
            
            complement = k - node.val
            if complement in lookup_set:
                return True
            
            lookup_set.add(complement)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

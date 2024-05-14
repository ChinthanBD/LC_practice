# https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            return 1 + dfs(node.left) + dfs(node.right)

        return dfs(root)

# https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, current_sum):
            current_sum += node.val
            if not node.left and not node.right:
                if current_sum == targetSum:
                    return True
            
            if node.left and dfs(node.left, current_sum):
                return True
            if node.right and dfs(node.right, current_sum):
                return True
            
            return False
            
        return dfs(root, 0)
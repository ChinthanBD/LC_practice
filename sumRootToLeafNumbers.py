#https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path_sum):
            if not node:
                return 0
            
            # Update the current path sum considering the value of the current node
            path_sum = path_sum * 10 + node.val
            
            # If the current node is a leaf node, return the path sum
            if not node.left and not node.right:
                return path_sum
            
            # Otherwise, continue DFS traversal
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)
        
        # Start DFS traversal from the root with an initial path sum of 0
        return dfs(root, 0)


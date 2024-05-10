# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([(root, 0)])  # Storing depth along with node
        rightmost_values = []

        while queue:
            node, depth = queue.popleft()
            if depth == len(rightmost_values):
                rightmost_values.append(node.val)
            else:
                rightmost_values[depth] = node.val

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return rightmost_values

# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            curr_sum = 0
            curr_len = len(queue)
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                curr_sum +=curr_node.val
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                
            ans.append(curr_sum/curr_len)
        return ans
# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Dictionary to map the operations to their respective changes in folder depth
        mpp = {'../': -1, './': 0}
        ans = 0
        
        # Iterate through each log operation
        for operation in logs:
            # Get the corresponding change in depth from the dictionary,
            # default to 1 if the operation is a folder name (i.e., not '../' or './')
            ans += mpp.get(operation, 1)
            
            # Ensure that the folder depth doesn't go below 0
            if ans < 0:
                ans = 0
        
        # Return the final folder depth
        return ans if ans > 0 else 0

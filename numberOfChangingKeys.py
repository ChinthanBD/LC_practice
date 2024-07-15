# https://leetcode.com/problems/number-of-changing-keys/description/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s or len(s)<2:
            return 0
        count = 0
        s_list = list(s)
        prev_char = s_list[0]
        for i in range(1, len(s_list)):
            if s_list[i].lower() != prev_char.lower():
                count+=1
            prev_char = s_list[i]

        return count            
        
        
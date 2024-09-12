# https://leetcode.com/problems/count-the-number-of-consistent-strings/?envType=daily-question&envId=2024-09-12
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for word in words:
            is_valid = True
            for char in word:
                if char not in allowed:
                    is_valid = False
                    continue
                
            if is_valid:
                ans+=1
        
        return ans

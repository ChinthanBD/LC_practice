# https://leetcode.com/problems/determine-if-two-strings-are-close/submissions/1374435679/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Check if the lengths are the same
        if len(word1) != len(word2):
            return False
        
        # Step 2: Check if both strings have the same set of characters
        if set(word1) != set(word2):
            return False
        
        # Step 3: Compare sorted frequency distributions
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())



        

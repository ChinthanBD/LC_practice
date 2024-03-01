# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_mpp = Counter(ransomNote)
        magazine_mpp = Counter(magazine)
        for letter, frequency in ransomNote_mpp.items():
            if magazine_mpp[letter] < frequency:
                return False
        return True

# Not my code below :(
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
            else:
                return False
        return True
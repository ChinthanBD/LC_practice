# https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        pattern_map = {}
        word_map = {}
        
        for char, word in zip(pattern, words):
            if char not in pattern_map:
                if word in word_map:
                    return False
                pattern_map[char] = word
                word_map[word] = char
            elif pattern_map[char] != word:
                return False
        
        return True

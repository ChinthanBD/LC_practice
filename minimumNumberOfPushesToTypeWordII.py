# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/?envType=daily-question&envId=2024-08-06
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each letter in the word
        freq = Counter(word)
        
        # Sort the letters by frequency in descending order
        sorted_letters = sorted(freq.items(), key=lambda x: -x[1])
        
        # Initialize total key presses
        total_presses = 0
        # Start with the least number of presses, i.e., 1
        presses = 1
        # Start assigning letters from the highest frequency
        for i, (letter, count) in enumerate(sorted_letters):
            total_presses += presses * count
            # After every 8 letters (keys from 2 to 9), we increase the number of presses
            if (i + 1) % 8 == 0:
                presses += 1
        
        return total_presses

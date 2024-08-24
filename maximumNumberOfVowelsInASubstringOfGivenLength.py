# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/1366561978/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        current_count = 0
        
        # Calculate the number of vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        max_count = current_count
        
        # Slide the window across the string
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1  # Remove the effect of the outgoing character
            if s[i] in vowels:
                current_count += 1  # Add the effect of the incoming character
            max_count = max(max_count, current_count)
        
        return max_count

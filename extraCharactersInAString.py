# https://leetcode.com/problems/extra-characters-in-a-string/submissions/1399731537/?envType=daily-question&envId=2024-09-23
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        word_set = set(dictionary)  # Use a set for O(1) lookup time.
        
        # Initialize dp array where dp[i] is the minimum extra chars for s[0:i].
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No characters to process, no extra chars.
        
        # Iterate over the string.
        for i in range(1, n + 1):
            # Assume the current character is not part of any word.
            dp[i] = dp[i - 1] + 1  # Extra char at position i-1
            
            # Check if any substring ending at index i is a word in the dictionary.
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])  # If s[j:i] is a word, no extra chars needed for this part.
        
        # The result is the minimum extra characters when breaking the whole string.
        return dp[n]

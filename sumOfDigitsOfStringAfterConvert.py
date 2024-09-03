# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1377954704/?envType=daily-question&envId=2024-09-03
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2: Transform the integer by summing its digits k times
        for _ in range(k):
            num_str = str(sum(int(digit) for digit in num_str))
        
        # The result after k transformations
        return int(num_str)

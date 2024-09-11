# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/submissions/1386702165/?envType=daily-question&envId=2024-09-11
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR the two numbers to get the differing bits
        xor_result = start ^ goal
        
        # Count the number of 1's in the XOR result
        return bin(xor_result).count('1')

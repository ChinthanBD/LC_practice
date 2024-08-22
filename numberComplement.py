# https://leetcode.com/problems/number-complement/submissions/1364792401/?envType=daily-question&envId=2024-08-22
class Solution:
    def findComplement(self, num: int) -> int:
        # Create a temporary variable to store the value of num
        temp = num
        
        # Initialize the bit variable to 1 (binary 0001)
        bit = 1

        # Loop until temp becomes 0
        while temp:
            # XOR num with bit. This flips the bit in num where the bit is set to 1.
            num = num ^ bit
            
            # Left shift bit by 1 to move to the next higher bit position
            bit = bit << 1
            
            # Right shift temp by 1 to move to the next lower bit position
            temp = temp >> 1

        # Return the final modified num, which is the complement of the original number
        return num

# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0
        i = 0
        
        while i < len(chars):
            char = chars[i]
            count = 0
            
            # Count the number of occurrences of the current character
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            
            # Write the character to the array
            chars[write_index] = char
            write_index += 1
            
            # Write the count to the array if greater than 1
            if count > 1:
                for c in str(count):
                    chars[write_index] = c
                    write_index += 1
        
        return write_index

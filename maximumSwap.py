# https://leetcode.com/problems/maximum-swap/?envType=daily-question&envId=2024-10-17
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}

        for i, d in enumerate(digits):
            # Check for a larger digit that can be swapped
            for x in range(9, int(d), -1):
                if last.get(x, -1) > i:
                    # Swap the digits and return immediately
                    digits[i], digits[last[x]] = digits[last[x]], digits[i]
                    return int(''.join(digits))

        return num  # Return the original number if no swap was made
        

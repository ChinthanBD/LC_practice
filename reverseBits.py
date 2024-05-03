# https://leetcode.com/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans<<1) | (n & 1)  # (shift ans to one bit to right) or (get the last bit of n)
            n >>=1
        return ans
# https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1
        return result

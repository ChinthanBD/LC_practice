# https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isHappy(self, n: int) -> bool:
        mpp = set()
        while n > 0:
            square_sum = 0
            while n > 0:
                rem = n % 10
                square_sum += rem * rem
                n //= 10
            if square_sum == 1:
                return True
            if square_sum in mpp:
                return False
            mpp.add(square_sum)
            n = square_sum
        return False
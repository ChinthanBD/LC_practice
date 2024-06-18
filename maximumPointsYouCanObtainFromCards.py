# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/1291908762/
from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum, rsum = 0, 0
        n = len(cardPoints)
        for i in range(k):
            lsum += cardPoints[i]
        maxSum = lsum
        for j in range(k):
            lsum -= cardPoints[k-1-j]
            rsum += cardPoints[n-1-j]
        
            currSum = lsum + rsum 
            maxSum = max(currSum, maxSum)
        return maxSum

            

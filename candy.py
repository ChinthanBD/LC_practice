# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # create a sorted tuple of each child's rating and index/position where the child is in
        data = sorted((x,i) for i,x in enumerate(ratings))

        candy = [1] * len(ratings)

        for _, i in data:
            if i > 0 and ratings[i] > ratings[i - 1]:
                candy[i] = max(candy[i], candy[i - 1] + 1)

            if i < len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)
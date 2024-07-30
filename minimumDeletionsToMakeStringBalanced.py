# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2024-07-30
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        # Initialize prefix and suffix arrays
        prefix_b_count = [0] * (n + 1)
        suffix_a_count = [0] * (n + 1)

        # Fill prefix_b_count: number of 'b's up to index i
        for i in range(n):
            prefix_b_count[i + 1] = prefix_b_count[i] + (1 if s[i] == 'b' else 0)

        # Fill suffix_a_count: number of 'a's from index i to end
        for i in range(n - 1, -1, -1):
            suffix_a_count[i] = suffix_a_count[i + 1] + (1 if s[i] == 'a' else 0)

        ans = float('inf')

        # Calculate minimum deletions
        for i in range(n + 1):
            ans = min(ans, prefix_b_count[i] + suffix_a_count[i])
        return ans



        ### TLE
        # ans = float("inf")

        # s_list = list(s)
        
        # for i in range(len(s)):
        #     current_deletion_count = 0
        #     current_deletion_count += s_list[:i].count('b')
        #     current_deletion_count += s_list[i+1:].count('a')

        #     ans = min(ans, current_deletion_count)
        # return ans

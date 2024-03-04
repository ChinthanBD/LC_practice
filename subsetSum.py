# https://www.geeksforgeeks.org/problems/subset-sums2234/1

class Solution:
    def subsetSums(self, arr, N):
        ans = []

        def subset_sum(index, sum):
            if index == N:
                ans.append(sum)
                return
            subset_sum(index + 1, sum + arr[index])

            subset_sum(index + 1, sum)

        subset_sum(0, 0)
        return ans

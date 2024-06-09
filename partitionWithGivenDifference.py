
from typing import List

MOD = 10**9 + 7

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    
    
  #  S = s1  + s2, s1 = S - s2
  #  d = s1 - s2-> 2
  # 2 in 1
  # d = (S - s2)- s2 , d = S - 2s2, s2 = (S - d)/2
  
    total_sum = sum(arr)
    
    # Calculate target sum
    if (total_sum - d) % 2 != 0 or (total_sum - d) < 0:
        return 0
    target_sum = (total_sum - d) // 2


    dp = {}
    def findways(target, row):
        if target == 0:
            return 1
            
        if row < 0:
            return 0

        if (row, target) in dp:
            return dp[(row, target)]

        # Choose not to include the current element
        nontake = findways(target, row - 1) % MOD

        # Choose to include the current element if it's not greater than the target
        take = 0
        if arr[row] <= target:
            take = findways(target - arr[row], row - 1) % MOD

        dp[(row, target)] = (take + nontake) % MOD
        return dp[(row, target)]

    return findways(target_sum, n - 1)


### stack overflow with above memoization sol




from typing import List

MOD = 10**9 + 7

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    total_sum = sum(arr)
    
    # Calculate target sum
    if (total_sum - d) % 2 != 0 or (total_sum - d) < 0:
        return 0
    target_sum = (total_sum - d) // 2
    
    if n == 0 or target_sum < 0:
        return 0

    # Initializing the previous row with base cases
    prev_row = {0: 1}  # There's one way to make the sum 0 (by picking nothing)
    if arr[0] <= target_sum:
        prev_row[arr[0]] = prev_row.get(arr[0], 0) + 1

    # Iterate through the rest of the array
    for i in range(1, len(arr)):
        curr_row = {}
        for target in range(target_sum + 1):
            nonPick = prev_row.get(target, 0)  # Number of ways to get `target` without current element
            pick = 0
            if target >= arr[i]:
                pick = prev_row.get(target - arr[i], 0)  # Number of ways to get `target` with current element

            curr_row[target] = (pick + nonPick) % MOD
        prev_row = curr_row

    return prev_row.get(target_sum, 0)

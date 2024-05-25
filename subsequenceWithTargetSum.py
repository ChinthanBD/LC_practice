# https://www.naukri.com/code360/problems/subset-sum-equal-to-k_1550954?leftPanelTab=1%3Fsource%3Dyoutube&campaign=striver_dp_videos&leftPanelTabValue=SUBMISSION

def subsetSumToK(n, k, arr):
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp = {}
    def findSubSequence(i, target):
        if target == 0:
            return True
        
        if i == 0:
            return arr[0] == target

        if dp.get((i,target)):
            return dp[(i,target)]
        
        notTake = findSubSequence(i-1, target)
        take = False
        if arr[i]<=target:
            take = findSubSequence(i-1, target-arr[i])
        
        dp[(i,target)] =  take | notTake
        return dp[(i,target)]
    
    return findSubSequence(n-1, k)

### TLE for above even with memoization 

from typing import List

def subsetSumToK(n: int, k: int, arr: List[int]) -> bool:
    # Initialize a dictionary to keep track of achievable sums with an empty subset.
    prev = {0: True}
    
    # If the first element is less than or equal to k, we can achieve the sum arr[0].
    if arr[0] <= k:
        prev[arr[0]] = True

    # Iterate over the elements of arr starting from the second element.
    for i in range(1, n):
        # Initialize a new dictionary for the current state.
        curr = {}
        # Iterate over all possible target sums from 0 to k.
        for target in range(k + 1):
            # Determine if the target sum can be achieved without including the current element.
            notTake = prev.get(target, False)
            # Determine if the target sum can be achieved by including the current element.
            take = False
            if target >= arr[i]:
                take = prev.get(target - arr[i], False)
            
            # The current target sum can be achieved if either 'take' or 'notTake' is True.
            curr[target] = take or notTake
        
        # Update prev to be the current state for the next iteration.
        prev = curr

    # Return whether the sum k is achievable.
    return prev.get(k, False)

        
    
    


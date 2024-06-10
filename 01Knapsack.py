# https://www.naukri.com/code360/problems/0-1-knapsack_920542?source=youtube&campaign=striver_dp_videos
## Read input as specified in the question.
## Print output as specified in the question.
def knapsack_max_value(weights, values, W):
    dp = {}
    def max_val(remWeightCapacity, i):
        if (remWeightCapacity, i) in dp:
            return dp[(remWeightCapacity, i)]

        if i == 0:
            if weights[0] <= remWeightCapacity:
                return values[0]
            else:
                return 0
        
        nonPick = max_val(remWeightCapacity, i-1)
        pick = float("-inf")

        if weights[i] <= remWeightCapacity:
            pick = max_val(remWeightCapacity - weights[i], i - 1) +  + values[i]
        dp[(remWeightCapacity, i)] = max(pick, nonPick)
        return max(pick, nonPick)

    return max_val(W, len(weights)-1)






def knapsack_max_value(weights, values, W):
    prev = {0: 0}
    if weights[0] <= W:
        prev[weights[0]] = prev.get(weights[0], 0) + values[0]

    for i in range(1, len(weights)+1):
        curr = {}
        for wgt in range(W+1):
            nonPick = prev.get(wgt, 0)
            pick = float("-inf")
            if weights[i] <= wgt:
                pick = prev.get(wgt - weights[i], 0) + values[i]
            
            curr[wgt] = max(pick, nonPick)
        
        prev = curr

    return prev.get(W, 0)






















# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        i = 0
        j = 0
        max_platforms = 0
        current_occupied_platforms = 0
        while i < n:
            current_occupied_platforms +=1
            if dep[j] < arr[i]:
                j+=1
                current_occupied_platforms -=1
                
            i+=1
            max_platforms = max(current_occupied_platforms, max_platforms)
            
        return max_platforms
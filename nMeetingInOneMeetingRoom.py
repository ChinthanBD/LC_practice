# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        temp = [(s, e) for s, e in zip(start, end)]
        temp.sort(key=lambda x :x[1])
        # temp.sort(key=lambda x: x[1])
        count = 1 
        prev = temp[0][1]
        for i in range(1, len(temp)):
            if temp[i][0]> prev:
                count+=1
                prev = temp[i][1]
        return count
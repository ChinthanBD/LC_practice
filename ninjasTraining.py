# https://www.codingninjas.com/studio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from typing import *

# def ninjaTraining(n: int, points: List[List[int]]) -> int:

#     # Write your code here.
    # def maxMerit(day, prev_task):
    #     if day == 0:
    #         maxi = 0
    #         for i in range(3):
    #             if i != prev_task:
    #                 maxi = max(points[0][i], maxi)
    #         return maxi
    #     maxi = 0
    #     for i in range(3):
    #         if i != prev_task:
    #             current_point = points[day][i] + maxMerit(day - 1, i)
    #             maxi = max(maxi, current_point)
    #     return maxi

    # return maxMerit(n - 1, 3)


###TLE for Above####

def ninjaTraining(n: int, points: List[List[int]]) -> List[int]:
    dp = [[-1] * 3 for _ in range(n)]

    def maxMerit(day, prev_task):
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != prev_task:
                    maxi = max(points[0][i], maxi)
            dp[0][prev_task] = maxi
            return dp[0][prev_task]
        
        if dp[day][prev_task] != -1:
            return dp[day][prev_task]
        
        maxi = 0
        for i in range(3):
            if i != prev_task:
                current_point = points[day][i] + maxMerit(day - 1, i)
                maxi = max(maxi, current_point)
        dp[day][prev_task] = maxi
        return dp[day][prev_task]

    return maxMerit(n - 1, -1) 

	
################space optimization ##########

def ninjaTraining(n, points):
    # Initialize a list 'prev' to store the maximum points for each possible last activity on the previous day.
    prev = [0] * 4

    # Initialize 'prev' with the maximum points for the first day's activities.
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))

    # Loop through the days starting from the second day.
    for day in range(1, n):
        # Initialize a temporary list 'temp' to store the maximum points for each possible last activity on the current day.
        temp = [0] * 4

        for last in range(4):
            # Initialize 'temp' for the current last activity.
            temp[last] = 0

            for task in range(3):
                if task != last:
                    # Calculate the total points for the current day's activity and the previous day's maximum points.
                    activity = points[day][task] + prev[task]
                    # Update 'temp' with the maximum points for the current last activity.
                    temp[last] = max(temp[last], activity)

        # Update 'prev' with 'temp' for the next iteration.
        prev = temp

    # Return the maximum points achievable after the last day with any activity.
    return prev[3]

def main():
    # Define the points matrix for each day.
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]
    n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find and print the maximum points.
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()

'''Q1. Unique Paths in a Grid
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.



Problem Constraints

1 <= n, m <= 100
A[i][j] = 0 or 1



Input Format

Firts and only argument A is a 2D array of size n * m.



Output Format

Return an integer denoting the number of unique paths from (1, 1) to (n, m).



Example Input

Input 1:

 A = [
        [0, 0, 0]
        [0, 1, 0]
        [0, 0, 0]
     ]
Input 2:

 A = [
        [0, 0, 0]
        [1, 1, 1]
        [0, 0, 0]
     ]


Example Output

Output 1:

 2
Output 2:

 0


Example Explanation

Explanation 1:

 Possible paths to reach (n, m): {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)} and {(1 ,1), (2, 1), (3, 1), (3, 2), (3, 3)}  
 So, the total number of unique paths is 2. 
Explanation 2:

 It is not possible to reach (n, m) from (1, 1). So, ans is 0.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):

        # ways(i+1, j) + ways(i, j+1)
        # store ans in a 2D array of size n X m

        dp = [[-1] * len(A[0]) for i in range(len(A))]

        return self.helper(A, 0, 0, dp)

        # return self.bottom_up(A)

    def helper(self, arr, i, j, dp):

        if i == len(arr) or j == len(arr[0]) or arr[i][j] == 1:
            return 0
        
        if i == len(arr) - 1 and j == len(arr[0]) - 1:
            return 1
        
        if dp[i][j] == -1:
            dp[i][j] = self.helper(arr, i + 1, j, dp) + self.helper(arr, i, j + 1, dp)

        return dp[i][j]
    
    def bottom_up(self, arr):

        n, m = len(arr), len(arr[0])

        dp = [[0] * m for i in range(n)]

        for i in range(n):

            for j in range(m):

                if arr[i][j]:
                    continue
                
                if not i and not j:
                    dp[0][0] = 1

                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        
        return dp[n - 1][m - 1]
'''Q3. Dungeon Princess
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Given a 2D array of integers A of size M x N. Find and return the knight's minimum initial health so that he is able to rescue the princess.



Problem Constraints

1 <= M, N <= 500

-100 <= A[i] <= 100



Input Format

First and only argument is a 2D integer array A denoting the grid of size M x N.



Output Format

Return an integer denoting the knight's minimum initial health so that he is able to rescue the princess.



Example Input

Input 1:

 A = [ 
       [-2, -3, 3],
       [-5, -10, 1],
       [10, 30, -5]
     ]
Input 2:

 A = [ 
       [1, -1, 0],
       [-1, 1, -1],
       [1, 0, -1]
     ]


Example Output

Output 1:

 7
Output 2:

 1


Example Explanation

Explanation 1:

 Initially knight is at A[0][0].
 If he takes the path RIGHT -> RIGHT -> DOWN -> DOWN, the minimum health required will be 7.
 At (0,0) he looses 2 health, so health becomes 5.
 At (0,1) he looses 3 health, so health becomes 2.
 At (0,2) he gains 3 health, so health becomes 5.
 At (1,2) he gains 1 health, so health becomes 6.
 At (2,2) he looses 5 health, so health becomes 1.
 At any point, the health point doesn't drop to 0 or below. So he can rescue the princess with minimum health 7.
 
Explanation 2:

 Take the path DOWN -> DOWN ->RIGHT -> RIGHT, the minimum health required will be 1.'''

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def calculateMinimumHP(self, A):

        return self.tabular(A)
    
    def tabular(self, arr):

        n, m = len(arr), len(arr[0])

        dp = [[0 for i in range(m)] for j in range(n)]

        for row in range(n - 1, -1, -1):

            for col in range(m - 1, -1, -1):

                if row == n - 1 and col == m - 1:

                    if arr[row][col] <= 0:
                        dp[row][col] = abs(arr[row][col]) + 1
                    
                    else:
                        dp[row][col] = 1
                
                elif row == n - 1:

                    dp[row][col] = dp[row][col + 1] - arr[row][col]

                    # Last row, can only move left
                    # if dp[row][col + 1] < arr[row][col]:
                    #     dp[row][col] = 1
                    # else:
                    #     dp[row][col] = dp[row][col + 1] - arr[row][col] 
                
                elif col == m - 1:

                    # if dp[row + 1][col] < arr[row][col]:
                    #     dp[row][col] = 1
                    # else:
                    #     dp[row][col] = dp[row + 1][col + 1] - arr[row][col]

                    dp[row][col] = dp[row + 1][col] - arr[row][col]
                
                else:
                    dp[row][col] = min(dp[row][col + 1], dp[row + 1][col]) - arr[row][col]

                if dp[row][col] <= 0:
                    dp[row][col] = 1
        
        return dp[0][0]
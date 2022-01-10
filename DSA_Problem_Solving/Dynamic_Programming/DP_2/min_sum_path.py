'''Q2. Min Sum Path in Matrix
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a M x N grid A of integers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Return the minimum sum of the path.

NOTE: You can only move either down or right at any point in time.



Problem Constraints

1 <= M, N <= 2000

-1000 <= A[i][j] <= 1000



Input Format

First and only argument is a 2-D grid A.



Output Format

Return an integer denoting the minimum sum of the path.



Example Input

Input 1:

 A = [
       [1, 3, 2]
       [4, 3, 1]
       [5, 6, 1]
     ]
Input 2:

 A = [
       [1, -3, 2]
       [2, 5, 10]
       [5, -5, 1]
     ]


Example Output

Output 1:

 8
Output 2:

 -1


Example Explanation

Explanation 1:

 The path will be: 1 -> 3 -> 2 -> 1 -> 1.
Input 2:

 The path will be: 1 -> -3 -> 5 -> -5 -> 1.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):

        return self.tabular(A)
    
    def tabular(self, matrix):

        n, m = len(matrix), len(matrix[0])

        for r in range(n):

            for c in range(m):

                if not r and not c:
                    continue
                
                elif r == 0:
                    matrix[r][c] = matrix[r][c] + matrix[r][c - 1]
                
                elif c == 0:
                    matrix[r][c] = matrix[r][c] + matrix[r - 1][c]
                
                else:
                    matrix[r][c] = matrix[r][c] + min(matrix[r][c - 1], matrix[r - 1][c])
            
        return matrix[n - 1][m - 1]

        # dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # for r in range(1, n + 1):

        #     for c in range(1, m + 1):
                
        #         if r == 1:
        #             dp[r][c] = dp[r][c - 1] + matrix[r - 1][c - 1]
                
        #         elif c == 1:
        #             dp[r][c] = dp[r - 1][c] + matrix[r - 1][c - 1]
                
        #         else:
        #             dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + matrix[r - 1][c - 1]
        
        # return dp[n][m]
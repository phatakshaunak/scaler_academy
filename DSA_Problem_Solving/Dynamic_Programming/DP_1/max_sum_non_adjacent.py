'''Q5. Max Sum Without Adjacent Elements
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Note: You can choose more than 2 numbers.



Problem Constraints

1 <= N <= 20000
1 <= A[i] <= 2000



Input Format

The first and the only argument of input contains a 2d matrix, A.



Output Format

Return an integer, representing the maximum possible sum.



Example Input

Input 1:

 A = [   
        [1]
        [2]    
     ]
Input 2:

 A = [   
        [1, 2, 3, 4]
        [2, 3, 4, 5]    
     ]


Example Output

Output 1:

 2
Output 2:

 8


Example Explanation

Explanation 1:

 We will choose 2.
Explanation 2:

 We will choose 3 and 5.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):

        '''
        For top and bottom positions, either select that element or not.
        If element is selected, the max sum at A[i][n] will use max(A[i][n] + A[i-2][0], A[i][n] + A[i-2][1]). Do for top and bottom rows, and update answer with max value
        If not selected, ans will be taken from A[i-1][n]
        Extension of the house robber problem
        To store answers, use a dp array of size 2 X N
        If i - 1 or i - 2 < 0 choose the element A[i][n] as the answer

        This is a slight modification of the house robber problem, to reduce it, select the max value in a column and then follow the same logic as in house robber
        '''

        n = len(A[0])

        dp = [0 for i in range(n)]

        ans = float('-inf')
        for i in range(n):
            
            # We need to only choose the maximum element of a column
            curr = max(A[0][i], A[1][i])

            if i == 0:
                dp[i] = curr
            
            elif i == 1:
                dp[i] = max(curr, dp[i-1])
            
            else:
                # Select element
                sel = curr + dp[i-2]
                # Don't select element
                n_sel = dp[i-1]

                dp[i] = max(sel, n_sel)
            
            ans = max(ans, dp[i])
        
        return ans

        # dp = [[0 for i in range(n)] for i in range(2)]
        # ans = float('-inf')
        # for i in range(n):

        #     # Iterate rows
        #     for j in range(2):
                
        #         # Edge Cases for i in (0, 1)
        #         if i == 0:
        #             # print(j, i)
        #             dp[j][i] = max(A[0][i], A[1][i])
                
        #         elif i == 1:
        #             dp[j][i] = max(A[0][i], A[1][i], A[0][i-1], A[1][i-1])
                    
        #         else:
        #             # Select element at A[j][i] and dp[j][i-2]
        #             a1 = A[j][i] + dp[0][i-2]
        #             a2 = A[j][i] + dp[1][i-2]
        #             # Don't select element at A[j][i]
        #             a3 = dp[0][i-1]
        #             a4 = dp[1][i-1]

        #             # Update with maximum value
        #             dp[j][i] = max(a1, a2, a3, a4)
                    
        #         ans = max(ans, dp[j][i])
        #     # print(dp, 'storage array')
        
        # return ans
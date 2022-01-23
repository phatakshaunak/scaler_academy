'''Q5. 0-1 Knapsack
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE:

You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


Problem Constraints

1 <= N <= 103

1 <= C <= 103

1 <= A[i], B[i] <= 103



Input Format

First argument is an integer array A of size N denoting the values on N items.

Second argument is an integer array B of size N denoting the weights on N items.

Third argument is an integer C denoting the knapsack capacity.



Output Format

Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.



Example Input

Input 1:

 A = [60, 100, 120]
 B = [10, 20, 30]
 C = 50
Input 2:

 A = [10, 20, 30, 40]
 B = [12, 13, 15, 19]
 C = 10


Example Output

Output 1:

 220
Output 2:

 0


Example Explanation

Explanation 1:

 Taking items with weight 20 and 30 will give us the maximum value i.e 100 + 120 = 220
Explanation 2:

 Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        # n = len(A)

        # dp = [[0 for i in range(C + 1)] for j in range(n + 1)]

        # for i in range(1, n + 1):

        #     for j in range(1, C + 1):

        #         # Pick
        #         if j - B[i - 1] >= 0:

        #             dp[i][j] = max(dp[i - 1][j - B[i - 1]] + A[i - 1], dp[i - 1][j])
                
        #         else:
        #             # Don't pick
        #             dp[i][j] = dp[i - 1][j]
        
        # return dp[n][C]
        return self.space(A, B, C)

    def space(self, V, W, w):

        n = len(V)

        dp1 = [0 for i in range(w + 1)]

        dp2 = [0 for i in range(w + 1)]

        for i in range(1, n + 1):

            for j in range(1, w + 1):

                if j - W[i - 1] >= 0:

                    dp2[j] = max(dp1[j - W[i - 1]] + V[i - 1], dp1[j])
                
                else:
                    dp2[j] = dp1[j]
            
            ans = dp2[-1]

            dp1, dp2 = dp2, dp1
        
        return ans
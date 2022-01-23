'''Q6. Unbounded Knapsack
Attempted
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate maximum amount that could fit in this quantity.

This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.



Problem Constraints

1 <= A <= 1000

1 <= |B| <= 1000

1 <= B[i] <= 1000

1 <= C[i] <= 1000



Input Format

First argument is the Weight of knapsack A

Second argument is the vector of values B

Third argument is the vector of weights C



Output Format

Return the maximum value that fills the knapsack completely



Example Input

Input 1:

A = 10
B = [5]
C = [10]
Input 2:

A = 10
B = [6, 7]
C = [5, 5]


Example Output

Output 1:

 5
Output 2:

14


Example Explanation

Explanation 1:

Only valid possibility is to take the given item.
Explanation 2:

Take the second item twice.'''

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        dp = [[-1 for i in range(A + 1)] for j in range(len(B))]
        
        return self.recursive(B, C, A, dp, 0, A)
        # return self.tabular(B, C, A)
    
    def tabular(self, V, W, w):

        n = len(V)

        dp = [[0 for i in range(w + 1)] for j in range(n + 1)]

        for i in range(1, n + 1):

            for j in range(1, w + 1):

                # Pick and stay at same index
                if j - W[i - 1] >= 0:

                    dp[i][j] = max(dp[i][j - W[i - 1]] + V[i - 1], dp[i - 1][j])
                
                else:
                    # Don't pick
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][w]

    def recursive(self, V, W, w, dp, i, j):

        if i == len(V):
            return 0
        
        if dp[i][j] == -1:

            if j - W[i] >= 0:

                ans = max(self.recursive(V, W, w, dp, i, j - W[i]) + V[i], self.recursive(V, W, w, dp, i + 1, j))
            
            else:
                ans = self.recursive(V, W, w, dp, i + 1, j)
        
            dp[i][j] = ans

        return dp[i][j]
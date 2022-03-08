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
        
        return self.knapsack_01_space(A, B, C)

    def knapsack_01_recursive(self, A, B, C, i, j, dp):

        if i == len(A):
            return 0

        if dp[i][j] == -1:

            pick = float('-inf')
            skip = self.knapsack_01(A, B, C, i + 1, j, dp)

            if j - B[i] >= 0:
                pick = A[i] + self.knapsack_01(A, B, C, i + 1, j - B[i], dp)

            dp[i][j] = max(skip, pick)

        return dp[i][j]
    
    def knapsack_01_space(self, A, B, C):
        
        dp1, dp2 = [0 for i in range(C + 1)], [0 for i in range(C + 1)]
        
        ans = 0
        
        for i in range(len(A)):
            
            for j in range(1, C + 1):
                
                if j - B[i] >= 0:
                    dp2[j] = max(dp1[j], A[i] + dp1[j - B[i]])
                
                else:
                    dp2[j] = dp1[j]
                
            ans = dp2[-1]
            
            dp1, dp2 = dp2, dp1
        
        return ans
    
    def knap_sack_01_tabular(self, A, B, C):
        
        n = len(A)
        dp = [[0 for i in range(C + 1)] for j in range(n)]
        
        for i in range(n):
            
            for j in range(1, C + 1):
                
                if j - B[i] >= 0:
                    
                    dp[i][j] = max(dp[i - 1][j], A[i] + dp[i - 1][j - B[i]])
                
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # Check what elements were picked
        i, j = len(dp) - 1, len(dp[0]) - 1
        
        ans = []
        
        while i > 0 and j > 0:
            
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            
            else:
                ans.append(i)
                j = j - B[i]
                i -= 1
        
        ans.reverse()
        
        print('values', [A[i] for i in ans])
        print('weights', [B[i] for i in ans])
        
        # Final value
        return dp[-1][-1]
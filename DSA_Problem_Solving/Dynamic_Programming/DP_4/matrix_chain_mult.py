'''Q3. Matrix Chain Multiplication
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A representing chain of 2-D matices such that the dimensions of ith matrix is A[i-1] x A[i].

Find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

Return the minimum number of multiplications needed to multiply the chain.



Problem Constraints

1 <= length of the array <= 1000
1 <= A[i] <= 100



Input Format

The only argument given is the integer array A.



Output Format

Return an integer denoting the minimum number of multiplications needed to multiply the chain.



Example Input

Input 1:

 A = [40, 20, 30, 10, 30]
Input 2:

 A = [10, 20, 30]


Example Output

Output 1:

 26000
Output 2:

 6000


Example Explanation

Explanation 1:

 Dimensions of A1 = 40 x 20
 Dimensions of A2 = 20 x 30
 Dimensions of A3 = 30 x 10
 Dimensions of A4 = 10 x 30
 First, multiply A2 and A3 ,cost = 20*30*10 = 6000
 Second, multilpy A1 and (Matrix obtained after multilying A2 and A3) =  40 * 20 * 10 = 8000
 Third, multiply (Matrix obtained after multiplying A1, A2 and A3) and A4 =  40 * 10 * 30 = 12000
 Total Cost = 12000 + 8000 + 6000 =26000
Explanation 2:

 Cost to multiply two matrices with dimensions 10 x 20 and 20 x 30 = 10 * 20 * 30 = 6000.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        return self.mcm_tabular(A)
    
    def mcm_tabular(self, arr):
    
        n = len(arr)
        
        # Number of matrices will be n - 1, the first matrix starts from dp[1, 1]
        dp = [[0 for i in range(n)] for j in range(n)]
        
        # Iterate through possible subarray lengths (single matrix, double matrix and so on)
        for l in range(2, n):
            
            for s in range(1, n - l + 1):
                
                e = l + s - 1
                
                # Simple multiplication for three matrices
                if l == 2:
                    dp[s][e] = arr[s - 1] * arr[s] * arr[e]
                
                else:
                    ans = float('inf')

                    # Get minimum possible value for all cuts
                    for k in range(s, e):
                        
                        # First two terms come from previous computation, final term is the cost of multiplying the two matrices obtained from the dp table
                        cost = dp[s][k] + dp[k + 1][e] + arr[s - 1] * arr[k] * arr[e]
                        
                        ans = min(ans, cost)
                    
                    # Update minimum cost
                    dp[s][e] = ans
        
        # Answer will be stored at the end of the first row as first row/column is padding
        return dp[1][n - 1]

        # TC O(N^3), SC O(N^2)
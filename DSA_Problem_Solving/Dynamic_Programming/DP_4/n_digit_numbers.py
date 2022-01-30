'''Q1. N digit numbers
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Find out the number of A digit positive numbers, whose digits on being added equals to a given number B.

Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.

Since the answer can be large, output answer modulo 1000000007



Problem Constraints

1 <= A <= 1000

1 <= B <= 10000



Input Format

First argument is the integer A

Second argument is the integer B



Output Format

Return a single integer, the answer to the problem



Example Input

Input 1:

 A = 2
 B = 4
Input 2:

 A = 1
 B = 3


Example Output

Output 1:

 4
Output 2:

 1


Example Explanation

Explanation 1:

 Valid numbers are {22, 31, 13, 40}
 Hence output 4.
Explanation 2:

 Only valid number is 3'''

import sys
sys.setrecursionlimit(int(1e6))
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def solve(self, A, B):

        # return self.tabular_space(A, B)
        # dp = [[-1 for i in range(B + 1)] for j in range(A + 1)]
            
        # ans = self.recursive(A, B, A, B, dp)
        # return ans % int(1e9 + 7)
        return self.tabular_practice(A, B) % int(1e9 + 7)

    def tabular_practice(self, N, S):
        
        dp = [[0 for i in range(S + 1)] for j in range(N + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, N + 1):
            for j in range(1, S + 1):
                
                for k in range(10):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]
        
        return dp[N][S]
    
    def tabular_practice_space(self, N, S):
        
        # dp = [[0 for i in range(S + 1)] for j in range(N + 1)]
        
        # dp[0][0] = 1
        dp1, dp2 = [0 for i in range(S + 1)], [0 for i in range(S + 1)]

        dp1[0] = 1

        for i in range(1, N + 1):
            for j in range(1, S + 1):
                
                for k in range(10):
                    if j - k >= 0:
                        dp2[j] += dp1[j - k]
            
            dp1, dp2 = dp2, dp1
            dp1[0] = 0
        
        return dp1[-1]

    def recursive(self, i, j, A, B, dp):
        
        if i == 0 and j == 0:
            return 1
        
        if i == 0:
            return 0
        
        if dp[i][j] == -1:
            tmp = 0
            for k in range(10):

                    # if i == A and k == 0:
                    #     # First digit cannot be zero
                    #     continue

                    if not(i == A and k == 0):

                        if j - k >= 0:
                            
                            tmp += self.recursive(i - 1, j-k, A, B, dp)

            dp[i][j] = tmp
        
        return dp[i][j]
    
    def tabular(self, N, B):

        dp = [[0 for i in range(B + 1)] for j in range(N + 1)]

        dp[0][0] = 1

        for i in range(1, N + 1):

            for j in range(1, B + 1):

                # Iterate over 0-9 places of minimum from last column to j
                # Start 10 places until current column from previous row
                col = max(0, j - 9)

                for k in range(col, j + 1):
                    dp[i][j] = dp[i][j] + dp[i - 1][k]

        return dp[N][B] % int(1e9 + 7)
    
    # TC O(N * S), SC O(S) where N are digits and S is the sum
    def tabular_space(self, N, B):
        
        dp1 = [0 for i in range(B + 1)]
        dp2 = [0 for i in range(B + 1)]

        dp1[0] = 1
        ans = 0
        for i in range(1, N + 1):
            
            for j in range(1, B + 1):
                
                # Since dp2's value comes from all values from the row above it
                dp2[j] = 0
                # Iterate over 0-9 places of minimum from last column to j
                # Start 10 places until current column from previous row
                col = max(0, j - 9)

                for k in range(col, j + 1):

                    dp2[j] = dp2[j] + dp1[k]
            
            ans = dp2[-1]
            dp1, dp2 = dp2, dp1
            dp2[0] = 0
            
        return ans % int(1e9 + 7)

        # TC O(10*N*S) --> O(N * S) where N are digits and S is the sum
        # SC O(N * S)
'''Q1. Coin Sum Infinite
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given a set of coins A. In how many ways can you make sum B assuming you have infinite amount of each coin in the set.

NOTE:

Coins in set A will be unique. Expected space complexity of this problem is O(B).
The answer can overflow. So, return the answer % (106 + 7).


Problem Constraints

1 <= A <= 500
1 <= A[i] <= 1000
1 <= B <= 50000



Input Format

First argument is an integer array A representing the set.
Second argument is an integer B.



Output Format

Return an integer denoting the number of ways.



Example Input

Input 1:

 A = [1, 2, 3]
 B = 4
Input 2:

 A = [10]
 B = 10


Example Output

Output 1:

 4
Output 2:

 1


Example Explanation

Explanation 1:

 The 4 possible ways are:
 {1, 1, 1, 1}
 {1, 1, 2}
 {2, 2}
 {1, 3} 
Explanation 2:

 There is only 1 way to make sum 10.
'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):

		# dp = [[-1 for i in range(B + 1)] for j in range(len(A))]

		# return self.ways_recursive(B, 0, dp, A)

		# TC O(B * len(A))
		# SC O(B * len(A))

		# return self.coin_inf_tab(A, B)

        return self.coin_inf_tab_space(A, B)

	def ways_recursive(self, N, idx, dp, A):
    
		if N == 0: 
			return 1

		if dp[idx][N] == -1:
			
			w1, w2 = 0, 0
			
			if N - A[idx] >= 0:
				w1 = self.ways_recursive(N - A[idx], idx, dp, A)
				
			if idx + 1 < len(A):
				w2 = self.ways_recursive(N, idx + 1, dp, A)
			
			dp[idx][N] = w1 + w2
		
		return dp[idx][N] % int(1e6 + 7)
	
	def coin_inf_tab(self, A, N):
    
        n = len(A)
        
        # Extra row/column pad for base cases
        dp = [[0 for i in range(N + 1)] for j in range(n + 1)]
        
        # dp[0][0] = 1, i.e. 1 way to make 0 with 0 coins
        # First column is all 1 as it is the base case, we do not include any coin, then sum is zero
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill table left to right, top to bottom
        for i in range(1, n + 1):
            
            for j in range(1, N + 1):
                
                # Include current coin only if j - A[i - 1] >= 0
                if j - A[i - 1] >= 0:
                    dp[i][j] = dp[i][j - A[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][N] % int(1e6 + 7)
        
	def coin_inf_tab_space(self, A, N):
        
        # Tabular bottom up approach using a single array

		n = len(A)
		
		dp = [0 for i in range(N + 1)]
		dp[0] = 1
		
		for i in range(1, n + 1):
			
			for j in range(1, N + 1):
				
				if j - A[i - 1] >= 0:
					dp[j] = dp[j - A[i - 1]] + dp[j]
		
		return dp[-1] % int(1e6 + 7)

        # TC O(N * len(A)), SC O(N)
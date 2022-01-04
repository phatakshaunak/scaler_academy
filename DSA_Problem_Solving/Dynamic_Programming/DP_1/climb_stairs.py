'''Q2. Stairs
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are climbing a stair case and it takes A steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Problem Constraints

1 <= A <= 36



Input Format

The first and the only argument contains an integer A, the number of steps.



Output Format

Return an integer, representing the number of ways to reach the top.



Example Input

Input 1:

 A = 2
Input 2:

 A = 3


Example Output

Output 1:

 2
Output 2:

 3


Example Explanation

Explanation 1:

 Distinct ways to reach top: [1, 1], [2].
Explanation 2:

 Distinct ways to reach top: [1 1 1], [1 2], [2 1].'''

class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):

        memo = {1: 1, 2: 2}

        return self.cl_dp(A, memo)

    def cl_dp(self, N, memo):
        
        if N < 1:
            return
        # if N == 1:
        #     return 1
        
        # if N == 2:
        #     return 2
        
        if N not in memo:
            memo[N] = self.cl_dp(N-1, memo) + self.cl_dp(N-2, memo)
        
        return memo[N]
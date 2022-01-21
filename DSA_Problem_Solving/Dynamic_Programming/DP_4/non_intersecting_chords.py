'''Q3. Intersecting Chords in a Circle
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a number A, return number of ways you can draw A chords in a circle with 2 x A points such that no 2 chords intersect.

Two ways are different if there exists a chord which is present in one way and not in other.
Return the answer modulo 109 + 7.



Problem Constraints

1 <= A <= 103



Input Format

The first and the only argument contains the integer A.



Output Format

Return an integer answering the query as described in the problem statement.



Example Input

Input 1:

 A = 1
Input 2:

 A = 2


Example Output

Output 1:

 1
Output 2:

 2


Example Explanation

Explanation 1:

 If points are numbered 1 to 2 in clockwise direction, then different ways to draw chords are: {(1-2)} only. So, we return 1.
Explanation 2:

 If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:{(1-2), (3-4)} and {(1-4), (2-3)}.
 So, we return 2.'''

import sys
sys.setrecursionlimit(int(1e6))

class Solution:
	# @param A : integer
	# @return an integer
	def chordCnt(self, A):

        memo = {0: 1}

        # return self.recur(2 * A, memo) % int(1e9 + 7)
        # return self.tabular(A)
        dp = [-1 for i in range(A + 1)]

        return self.recur1(A, dp) % int(1e9 + 7)
    
    def recur1(self, N, dp):

        if N == 0:
            dp[N] = 1
            return 1
        
        if dp[N] == -1:

            dp[N] = 0
            
            for i in range(N):
                dp[N] += self.recur1(i, dp) * self.recur1(N - i - 1, dp)
        
        return dp[N]
    
    def recur(self, N, dp):

        if N == 0:
            return 1

        if N not in dp:
            
            dp[N] = 0

            for i in range(0, N - 1, 2):
                
                dp[N] += self.recur(i, dp) * self.recur(N - i - 2, dp)
            
        return dp[N]
    
    def tabular(self, N):

        dp = [0 for i in range(N + 1)]

        dp[0] = 1

        for i in range(1, N + 1):

            for j in range(i):

                dp[i] += dp[j] * dp[i - j - 1]

        return dp[N] % int(1e9 + 7)
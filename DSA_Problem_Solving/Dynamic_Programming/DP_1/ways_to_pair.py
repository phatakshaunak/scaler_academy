'''Q3. Let's Party
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

In Danceland, one person can party either alone or can pair up with another person.

Can you find in how many ways they can party if there are A people in Danceland?

Note: Return your answer modulo 10003, as the answer can be large.



Problem Constraints

1 <= A <= 105



Input Format

Given only argument A of type Integer, number of people in Danceland.



Output Format

Return an integer denoting the number of ways people of Danceland can party.



Example Input

Input 1:

 A = 3
Input 2:

 A = 5


Example Output

Output 1:

 4
Output 2:

 26


Example Explanation

Explanation 1:

 Let suppose three people are A, B, and C. There are only 4 ways to party
 (A, B, C) All party alone
 (AB, C) A and B party together and C party alone
 (AC, B) A and C party together and B party alone
 (BC, A) B and C party together and A
 here 4 % 10003 = 4, so answer is 4.
 
Explanation 2:

 Number of ways they can party are: 26.'''

import sys
sys.setrecursionlimit(int(1e6))
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        # if A <= 2:
        #     return A
        
        # memo = [0] * (A + 1)
        # memo[1] = 1
        # memo[2] = 2

        # for i in range(3, A + 1):
        #     memo[i] = (memo[i-1] + (i-1) * memo[i-2]) % 10003
        
        # return memo[A]

        memo, mod = {}, 10003
        return self.helper(A, memo, mod)
    
    def helper(self, N, memo, mod):
        
        if N <= 2:
            return N
        
        if N not in memo:
            memo[N] = (self.helper(N - 1, memo, mod) % mod + ((N - 1) % mod * self.helper(N - 2, memo, mod) % mod) % mod) % mod
        
        return memo[N]
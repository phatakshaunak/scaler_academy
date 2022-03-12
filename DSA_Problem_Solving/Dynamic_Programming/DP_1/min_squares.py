'''Q4. Minimum Number of Squares
Attempted
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.



Problem Constraints

1 <= A <= 105



Input Format

First and only argument is an inetegr A.



Output Format

Return an integer denoting the minimum count.



Example Input

Input 1:

 A = 6
Input 2:

 A = 5


Example Output

Output 1:

 3
Output 2:

 2


Example Explanation

Explanation 1:

 Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
 Minimum count of numbers, sum of whose squares is 6 is 3. 
Explanation 2:

 We can represent 5 using only 2 numbers i.e. 12 + 22 = 5


See Expected Output
Your input
10000
Output
1'''

import sys
sys.setrecursionlimit(int(1e6))

class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A):

        return self.tabular(A)
        # dp = [-1 for i in range(A + 1)]

        # return self.recursive(A, dp)

    def recursive(self, i, dp):

        if i == 0:
            return 0

        if dp[i] == -1:
            
            dp[i] = float('inf')

            j = 1

            while j * j <= i:
                dp[i] = min(dp[i], 1 + self.recursive(i - j * j, dp))
                j += 1
        
        return dp[i]
    
    def tabular(self, A):
        
        # Initially, the answer can be assumed to be a sum of 1s i times
        dp = [i for i in range(A + 1)]

        '''
        State of any A dp[A] is the minimum number of squares needed to sum to A
        A greedy approach involves choosing the square root of A each time and repeating until A reaches 0.
        This does not always work, eg. for 12 greedily the answer is 4 while optimally it is 3
        Explore all possibilities (recursion/backtracking) but store previous states
        A recurrence formula for this approach
        dp[i] = 1 + {x = 1, x = sq.root(i)} min(dp[i - x ^ 2])
        This is a NN^0.5 time complexity and O(N) space for the tabulation
        '''

        for i in range(1, A + 1):

            # curr = float('inf')
            j = 1

            # Try all possible squares (greedy would pick the largest square root)
            while j * j <= i:

                # Trying all possible transitions (not just largest square root)
                dp[i] = min(dp[i], 1 + dp[i - j * j])
                # curr = min(curr, dp[i - j * j])
                j += 1
            # dp[i] = 1 + curr
        
        return dp[A]

        # TC O(N*N^0.5), SC O(N)
'''Q4. Longest Increasing Subsequence
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.

In this case, return the length of the longest increasing subsequence.



Problem Constraints

0 <= length(A) <= 2500
1 <= A[i] <= 2500



Input Format

The first and the only argument is an integer array A.



Output Format

Return an integer representing the length of the longest increasing subsequence.



Example Input

Input 1:

 A = [1, 2, 1, 5]
Input 2:

 A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


Example Output

Output 1:

 3
Output 2:

 6


Example Explanation

Explanation 1:

 The longest increasing subsequence: [1, 2, 5]
Explanation 2:

 The possible longest increasing subsequences: [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):

        # 1 + max(all j = 0 to j- 1 where A[j] < A[i])

        dp = [0] * len(A)
        dp[0] = 1

        for i in range(1, len(A)):
            
            # ans = float('-inf')
            ans = 1
            
            for j in range(i):
                if A[j] < A[i]:
                    ans = max(ans, 1 + dp[j])
            
            dp[i] = ans
        
        return max(dp)
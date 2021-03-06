'''Q4. Length of Longest Fibonacci Subsequence
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a strictly increasing array A of positive integers forming a sequence.

A sequence X1, X2, X3, ..., XN is fibonacci like if


N > =3
Xi + Xi+1 = Xi+2 for all i+2 <= N
Find and return the length of the longest Fibonacci-like subsequence of A.

If one does not exist, return 0.

NOTE: A subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.



Problem Constraints

3 <= length of the array <= 1000

1 <= A[i] <= 109



Input Format

The only argument given is the integer array A.



Output Format

Return the length of the longest Fibonacci-like subsequence of A.
If one does not exist, return 0.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5, 6, 7, 8]
Input 2:

 A = [1, 3, 7, 11, 12, 14, 18]


Example Output

Output 1:

 5
Output 2:

 3


Example Explanation

Explanation 1:

 The longest subsequence that is fibonacci-like: [1, 2, 3, 5, 8].
Explanation 2:

 The longest subsequence that is fibonacci-like: [1, 11, 12], [3, 11, 14] or [7, 11, 18].
 The length will be 3.'''

 class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)

        dp = [[0 for i in range(n)] for j in range(n)]
        
        # Similar to the definition of a fibonacci sequence, dp[i][j] represents the count of elements in a fibonacci sequence with the last two elements as A[i] and A[j]

        # Values on and below the diagonal are not valid, initialize the remaining cells with 2 as that can be the minimum sequence length

        # Recurrence Relation: if A[i] + A[j] == A[k], dp[j][k] = 1 + dp[i][j]. Get the maximum of all dp[j][k]
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = 2
        
        ans = 2

        for i in range(2, n):
            
            # Two sum approach (Using two pointers as array is sorted), otherwise use a map
            l, r = 0, i - 1

            while l < r:

                target = A[l] + A[r]

                if target > A[i]:
                    r -= 1
                
                elif target < A[i]:
                    l += 1
                
                else:
                    dp[r][i] = 1 + dp[l][r]
                    ans = max(ans, dp[r][i])
                    
                    l += 1
                    r -= 1
        
        return ans if ans > 2 else 0
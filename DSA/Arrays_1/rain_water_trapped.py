'''Q5. Rain Water Trapped
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints

1 <= |A| <= 100000



Input Format

First and only argument is the vector A



Output Format

Return one integer, the answer to the question



Example Input

Input 1:

A = [0, 1, 0, 2]
Input 2:

A = [1, 2]


Example Output

Output 1:

1
Output 2:

0


Example Explanation

Explanation 1:

1 unit is trapped on top of the 3rd element.
Explanation 2:

No water is trapped.'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):

        N = len(A)

        # L = [0 for i in range(N)]
        R = [0 for j in range(N)]
        # L[0] = A[0]

        R[N - 1] = A[N - 1]

        # for idx in range(1, N):
        #     L[idx] = max(L[idx - 1], A[idx])
        
        for s in range(N - 2, -1, -1):
            R[s] = max(R[s + 1], A[s])

        L = 0
        ans = 0

        for f in range(N):
            L = max(L, A[f])
            ans = ans + min(L, R[f]) - A[f]
        
        return ans


'''Q4. Assign Mice to Holes
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

There are N Mice and N holes that are placed in a straight line. Each hole can accomodate only 1 mouse.

The positions of Mice are denoted by array A and the position of holes are denoted by array B.

A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1. Any of these moves consumes 1 minute.

Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.



Problem Constraints

1 <= N <= 105

-109 <= A[i], B[i] <= 109



Input Format

First argument is an integer array A.

Second argument is an integer array B.



Output Format

Return an integer denoting the minimum time when the last nouse gets inside the holes.



Example Input

Input 1:

 A = [-4, 2, 3]
 B = [0, -2, 4]
Input 2:

 A = [-2]
 B = [-6]


Example Output

Output 1:

 2
Output 2:

 4


Example Explanation

Explanation 1:

 Assign the mouse at position (-4 to -2), (2 to 0) and (3 to 4).
 The number of moves required will be 2, 2 and 1 respectively.
 So, the time taken will be 2.
Explanation 2:

 Assign the mouse at position -2 to -6.
 The number of moves required will be 4.
 So, the time taken will be 4.'''

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def mice(self, A, B):
        
        A.sort()
        B.sort()

        ans = 0
        n = len(A)

        for i in range(n):

            curr = abs(A[i] - B[i])
            ans = max(curr, ans)
        
        return ans
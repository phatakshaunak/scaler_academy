'''Q2. N max pair combinations
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two integers arrays A and B of size N each.

Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.



Problem Constraints

1 <= N <= 2 * 105

-1000 <= A[i], B[i] <= 1000



Input Format

First argument is an integer array A.
Second argument is an integer array B.



Output Format

Return an intger array denoting the N maximum element in descending order.



Example Input

Input 1:

 A = [1, 4, 2, 3]
 B = [2, 5, 1, 6]
Input 2:

 A = [2, 4, 1, 1]
 B = [-2, -3, 2, 4]


Example Output

Output 1:

 [10, 9, 9, 8]
Output 2:

 [8, 6, 6, 5]


Example Explanation

Explanation 1:

 4 maximum elements are 10(6+4), 9(6+3), 9(5+4), 8(6+2).
Explanation 2:

 4 maximum elements are 8(4+4), 6(4+2), 6(4+2), 5(4+1).'''

import heapq
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return a list of integers
	def solve(self, A, B):

        A.sort()
        B.sort()
        N = len(A)

        i, j = N - 1, N - 1

        ops = N
        ans = []
        tmp = []
        tmp.append((-1*(A[i] + B[j]), i, j))
        heapq.heapify(tmp)
        seen = set()
        seen.add((i, j))
        while ops > 0:
            
            top, i, j = heapq.heappop(tmp)

            if i - 1 >= 0:
                if (i - 1, j) not in seen:
                    seen.add((i - 1, j))
                    heapq.heappush(tmp, (-1*(A[i-1] + B[j]), i-1, j))
            
            if j - 1 >= 0:
                if (i, j - 1) not in seen:
                    seen.add((i, j - 1))
                    heapq.heappush(tmp, (-1*(A[i] + B[j-1]), i, j - 1))
                
            ans.append(-1*top)
            ops -= 1
        
        return ans
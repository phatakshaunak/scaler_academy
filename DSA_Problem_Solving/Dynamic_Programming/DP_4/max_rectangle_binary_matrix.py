'''Q1. Max Rectangle in Binary Matrix
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a 2-D binary matrix A of size N x M filled with 0's and 1's, find the largest rectangle containing all ones and return its area.



Problem Constraints

1 <= N, M <= 100



Input Format

First argument is an 2-D binary array A.



Output Format

Return an integer denoting the area of largest rectangle containing all ones.



Example Input

Input 1:

 A = [
       [1, 1, 1]
       [0, 1, 1]
       [1, 0, 0] 
     ]
Input 2:

 A = [
       [0, 1, 0]
       [1, 1, 1]
     ] 


Example Output

Output 1:

 4
Output 2:

 3


Example Explanation

Explanation 1:

 As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2).
Explanation 2:

 As the max area rectangle is created by the 1x3 rectangle created by (1,0), (1,1) and (1,2).'''

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
        
        n, m = len(A), len(A[0])
        
        # Prefix Matrix
        for i in range(1, n):
            for j in range(m):
                if A[i][j] == 1:
                    A[i][j] += A[i - 1][j]
        
        ans = 0

        nsl, nsr = [0] * m, [0] * m
        st = []
        for i in range(n):
            
            # Get nearest smaller indices on the left
            for j in range(m):

                while st and A[i][st[-1]] >= A[i][j]:
                    st.pop()

                if st:
                    nsl[j] = st[-1]

                else:
                    nsl[j] = -1
                
                st.append(j)

            while st: st.pop()

            # Get nearest smaller indices on the right
            for j in range(m - 1, -1, -1):

                while st and A[i][st[-1]] >= A[i][j]:
                    st.pop()

                if st:
                    nsr[j] = st[-1]

                else:
                    nsr[j] = m
                
                st.append(j)

            while st: st.pop()

            # Compute maximum area for current row
            for j in range(m):

                w = (nsr[j] - 1) - (nsl[j] + 1) + 1

                area = w * A[i][j]

                ans = max(area, ans)

                nsr[j], nsl[j] = 0, 0
        
        return ans

        # TC O(N*M), SC O(M)
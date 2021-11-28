'''Q3. Maximum Rectangle
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.

Find the largest rectangle containing only 1's and return its area.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.


Input Format

The only argument given is the integer matrix A.
Output Format

Return the area of the largest rectangle containing only 1's.
Constraints

1 <= N, M <= 1000
0 <= A[i] <= 1
For Example

Input 1:
    A = [   [0, 0, 1]
            [0, 1, 1]
            [1, 1, 1]   ]
Output 1:
    4

Input 2:
    A = [   [0, 1, 0, 1]
            [1, 0, 1, 0]    ]
Output 2:
    1'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        r, c = len(A), len(A[0])

        # Prefix matrix to apply max rectangle function for each row
        for i in range(1,r):
            for j in range(c):

                # Add only if A[i][j] is 1, as won't be applicable if zero.
                if A[i][j] == 1:
                    A[i][j] = A[i-1][j] + A[i][j]
        
        ans = 0
        # print(A)
        nsl, nsr, st = [0] * c, [0] * c, []

        for i in range(r):
            
            for j in range(c):
                
                while st and  A[i][st[-1]] >= A[i][j]:
                    st.pop()
                if st:
                    nsl[j] = st[-1]
                else:
                    nsl[j] = -1
                
                st.append(j)
            
            while st: st.pop()

            for k in range(c-1, -1, -1):

                while st and A[i][st[-1]] >= A[i][k]:
                    st.pop()
                if st:
                    nsr[k] = st[-1]
                else:
                    nsr[k] = c
                st.append(k)
            
            # print(nsl)
            # print(nsr)
            for idx in range(c):

                l, r = nsl[idx] + 1, nsr[idx] - 1
                w = r - l + 1
                area = w * A[i][idx]
                # print(w, A[i][idx])
                ans = max(area, ans)
                
                # Clear nsl and nsr for next row
                nsl[idx], nsr[idx] = 0, 0
            
            while st: st.pop()
        
        return ans
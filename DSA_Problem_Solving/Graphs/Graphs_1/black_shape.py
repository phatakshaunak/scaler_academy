'''Q2. Black Shapes
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)



Problem Constraints

1 <= |A|,|A[0]| <= 1000

A[i][j] = 'X' or 'O'



Input Format

The First and only argument is character matrix A.



Output Format

Return a single integer denoting number of black shapes.



Example Input

Input 1:

 A = [ [X, X, X], [X, X, X], [X, X, X] ]
Input 2:

 A = [ [X, O], [O, X] ]


Example Output

Output 1:

 1
Output 2:

 2


Example Explanation

Explanation 1:

 All X's belong to single shapes
Explanation 2:

 Both X's belong to different shapes


See Expected Output
Your input
4 X O O X
Output
2'''

from collections import deque

class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):

        n, m = len(A), len(A[0])

        drc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ans = 0

        for i in range(len(A)):
            
            A[i] = [char for char in A[i]]

        # Initialize a queue
        q = deque()

        for i in range(n):
            
            for j in range(m):

                # If an X is encountered, increment ans by 1 as one black shape and bfs to complete all connected components. Mark as # to avoid future traversal
                if A[i][j] == 'X':

                    q.append((i, j))

                    self.bfs(q, A, n, m, drc)

                    ans += 1
        
        return ans
    
    def bfs(self, q, arr, n, m, drc):
        
        while q:
            x, y = q.popleft()

            # Mark cell as visited
            arr[x][y] = '#'

            # Try all four directions
            for d in drc:

                c_x, c_y = x + d[0], y + d[1]

                if self.check(c_x, c_y, n, m, arr):

                    # Mark as visited and add to queue for further traversal
                    arr[c_x][c_y] = '#'
                    q.append((c_x, c_y))


    def check(self, r, c, n, m, arr):

        return r >= 0 and r < n and c >= 0 and c < m and arr[r][c] == 'X'
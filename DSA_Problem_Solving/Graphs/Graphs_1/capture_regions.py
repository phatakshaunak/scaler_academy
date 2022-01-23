'''Q4. Capture Regions on Board
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Problem Constraints

1 <= N, M <= 1000



Input Format

First and only argument is a N x M character matrix A.



Output Format

Make changes to the the input only as matrix is passed by reference.



Example Input

Input 1:

 A = [ 
       [X, X, X, X],
       [X, O, O, X],
       [X, X, O, X],
       [X, O, X, X] 
     ]
Input 2:

 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]


Example Output

Output 1:

 After running your function, the board should be:
 A = [
       [X, X, X, X],
       [X, X, X, X],
       [X, X, X, X],
       [X, O, X, X]
     ]
Output 2:

 After running your function, the board should be:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]


Example Explanation

Explanation 1:

 O in (4,2) is not surrounded by X from below.
Explanation 2:

 No O's are surrounded.'''

from collections import deque
class Solution:
    # @param A : list of list of chars
    def solve(self, A):

        # Mark all boundary O's as obstacles
        n, m = len(A), len(A[0])

        # Initialize a deque
        q = deque()

        for i in range(n):

            for j in range(m):

                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and A[i][j] == 'O':

                    # Mark as obstacles
                    A[i][j] = -1

                    q.append((i, j))
        
        drc = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # BFS from all boundary Os and mark as obstacles all Os connected to them
        while q:

            x, y = q.popleft()

            for d in drc:

                c_x, c_y = x + d[0], y + d[1]

                # Check if indices valid and we are at an 'O'
                if self.check(c_x, c_y, n, m, A):
                    
                    # Add to the queue
                    q.append((c_x, c_y))

                    # Mark as obstacle
                    A[c_x][c_y] = -1

        # For all remaining O's flip to X. Then run loop and change -1 to X

        for i in range(n):

            for j in range(m):

                if A[i][j] == 'O':
                    A[i][j] = 'X'
                
                if A[i][j] == -1:
                    A[i][j] = 'O'
        
        return A
        
    def check(self, x, y, r, c, arr):

        return x >= 0 and x < r and y >= 0 and y < c and arr[x][y] == 'O'
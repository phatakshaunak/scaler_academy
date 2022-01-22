'''Q3. Rotten Oranges
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

The value 0 representing an empty cell.

The value 1 representing a fresh orange.

The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.



Problem Constraints

1 <= N, M <= 1000

0 <= A[i][j] <= 2



Input Format

The first argument given is the integer matrix A.



Output Format

Return the minimum number of minutes that must elapse until no cell has a fresh orange.

If this is impossible, return -1 instead.



Example Input

Input 1:

A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]
Input 2:

 
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]


Example Output

Output 1:

 4
Output 2:

 -1


Example Explanation

Explanation 1:

 Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)
Explanation 2:

 Task is impossible'''

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        q = deque()

        one_cnt, ans, rotted = 0, 0, 0

        drc = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        n, m = len(A), len(A[0])

        for i in range(n):

            for j in range(m):

                # Append all rotten orange locations to queue
                if A[i][j] == 2:
                    # Append cell and distance to queue
                    q.append((i, j, 0))
                
                elif A[i][j] == 1:
                    # Counts fresh oranges
                    one_cnt += 1
        
        # Do a BFS from all rotten oranges
        while q:

            x, y, dist = q.popleft()

            tmp = 0
            # Move in all four directions
            for d in drc:
                
                c_x, c_y = x + d[0], y + d[1]

                # Check if indices are in range and cell not already visited
                if self.check(c_x, c_y, A) and A[c_x][c_y] == 1:

                    q.append((c_x, c_y, dist + 1))

                    ans = dist + 1
                    # Mark cell as rotted
                    A[c_x][c_y] = 2

                    # Increment rotted
                    tmp += 1

            if tmp != 0:
                
                rotted += tmp
        
        if rotted == one_cnt:
            return ans
        
        return -1
    
    def check(self, x, y, A):

        return x >= 0 and y >= 0 and x < len(A) and y < len(A[0])
        
        # Not possible
        return -1
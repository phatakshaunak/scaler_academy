'''Q4. Valid Path
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

There is a rectangle with left bottom as (0, 0) and right up as (x, y).

There are N circles such that their centers are inside the rectangle.

Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.



Problem Constraints

0 <= x , y, R <= 100

1 <= N <= 1000

Center of each circle would lie within the grid



Input Format

1st argument given is an Integer x , denoted by A in input.

2nd argument given is an Integer y, denoted by B in input.

3rd argument given is an Integer N, number of circles, denoted by C in input.

4th argument given is an Integer R, radius of each circle, denoted by D in input.

5th argument given is an Array A of size N, denoted by E in input, where A[i] = x cordinate of ith circle

6th argument given is an Array B of size N, denoted by F in input, where B[i] = y cordinate of ith circle



Output Format

Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).



Example Input

Input 1:

 x = 2
 y = 3
 N = 1
 R = 1
 A = [2]
 B = [3]
Input 2:

 x = 1
 y = 1
 N = 1
 R = 1
 A = [1]
 B = [1]


Example Output

Output 1:

 NO
Output 2:

 NO


Example Explanation

Explanation 1:

 There is NO valid path in this case
Explanation 2:

 There is NO valid path in this case'''
from collections import deque
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        
        M = [[1 for i in range(A + 1)] for j in range(B + 1)]
        
        n, m = B + 1, A + 1
        
        drc = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
        src, dest = (B, 0), (0, A)
        
        q = deque([(src)])
        
        while q:
            
            x, y = q.popleft()
            
            for d in drc:
                
                c_x, c_y = x + d[0], y + d[1]
                
                if self.check(c_x, c_y, n, m, M, E, F, A, B, D) and M[c_x][c_y] == 1:
                    
                    q.append((c_x, c_y))
                    
                    M[c_x][c_y] = 0
                
                    if c_x == 0 and c_y == A:
                        return 'YES'
            
        return 'NO'
                
    def check(self, x, y, n, m, M, E, F, A, B, D):
        
        if x >= 0 and y >= 0 and x < n and y < m :
                
            for r in range(len(E)):

                r_y, r_x = E[r], F[r]

                r_x = B - r_x
                
                dist = ((x - r_x) * (x - r_x)) + ((y - r_y) * (y - r_y))

                if (r_x, r_y) == (B, 0) or (r_x, r_y) == (0, A) or dist <= (D * D):
                    M[x][y] = 0
                    return False
        
            return True
        
        return False
        
# from collections import deque
# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : integer
#     # @param D : integer
#     # @param E : list of integers
#     # @param F : list of integers
#     # @return a strings
#     def solve(self, A, B, C, D, E, F):
        
#         M = [[1 for i in range(A + 1)] for j in range(B + 1)]
        
#         n, m = B + 1, A + 1
        
# #         drc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
#         drc = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
#         vis = [[0 for i in range(m)] for j in range(n)]
        
#         src, dest = (B, 0), (0, A)
        
#         q = deque([(src)])
        
#         while q:
            
#             x, y = q.popleft()
            
#             vis[x][y] = 1
            
#             for d in drc:
                
#                 c_x, c_y = x + d[0], y + d[1]
                
#                 if self.check(c_x, c_y, n, m, vis, M, E, F, A, B, D) and vis[c_x][c_y] == 0:
                    
#                     q.append((c_x, c_y))
#                     vis[c_x][c_y] = 1
                
#                     if c_x == 0 and c_y == A:
#                         return 'YES'
            
#         return 'NO'
                
#     def check(self, x, y, n, m, vis, M, E, F, A, B, D):
        
#         if x >= 0 and y >= 0 and x < n and y < m :
                
#             for r in range(len(E)):

#                 r_y, r_x = E[r], F[r]

#                 r_x = B - r_x
                
#                 dist = ((x - r_x) * (x - r_x)) + ((y - r_y) * (y - r_y))

#                 if (r_x, r_y) == (B, 0) or (r_x, r_y) == (0, A) or dist <= (D * D):
#                     M[x][y] = 0
#                     return False
        
#             return True
        
#         return False
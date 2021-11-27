'''Q4. Count Rectangles
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2-D Cartesian plane.

Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.



Problem Constraints

1 <= N <= 2000
0 <= A[i], B[i] <= 109



Input Format

The first argument given is the integer array A.
The second argument given is the integer array B.



Output Format

Return the number of unordered quadruplet that form a rectangle.



Example Input

Input 1:

 A = [1, 1, 2, 2]
 B = [1, 2, 1, 2]
Input 1:

 A = [1, 1, 2, 2, 3, 3]
 B = [1, 2, 1, 2, 1, 2]


Example Output

Output 1:

 1
Output 2:

 3


Example Explanation

Explanation 1:

 All four given points make a rectangle. So, the answer is 1.
Explanation 2:

 3 quadruplets which make a rectangle are: (1, 1), (2, 1), (2, 2), (1, 2)
                                           (1, 1), (3, 1), (3, 2), (1, 2)
                                           (2, 1), (3, 1), (3, 2), (2, 2)'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        ans, N = 0, len(A)
        #Create a tuple map and initialize with zeros
        hs = {}
        for idx in range(N):
            hs[(A[idx], B[idx])] = 1
        
        # Fix two diagonals (x1,y1) and (x2,y2) and then find if (x1,y2) and (x2,y1) exist in the set. If set it is a valid rectangle, increment count and mark diagonals as seen

        for i in range(N):

            for j in range(i + 1,N):

                #Ensure diagonals are valid, i.e. their x and y co-ordinates are not equal
                if (A[i] != A[j]) and (B[i] != B[j]):

                    # Check if (A[i1], B[j1]) and (B[i1], A[j1]) exist in the map and are not seen (i.e both are not 1)

                    # We will double count the rectangles as there are two unique pairs of diagonals that define the same rectangle. The ans can be returned by halving it 
                    if ((A[i], B[j]) in hs) and ((A[j], B[i]) in hs):
                        ans += 1
            #             # Ensuring one of these is unseen
            #             if hs[(A[i], B[j])] == 0 or hs[(A[j], B[i])] == 0:
            #                 #Increment count
            #                 ans += 1
                
            #                 # Mark diagonal as seen
            #                 hs[(A[j], B[j])] = 1
            
            # # Mark diagonal as seen
            # hs[(A[i], B[i])] = 1
        
        return ans // 2
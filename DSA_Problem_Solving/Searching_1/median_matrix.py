'''Q3. Matrix Median
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x M in which each row is sorted.

Find and return the overall median of the matrix A.

NOTE: No extra memory is allowed.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

1 <= N, M <= 10^5

1 <= N*M <= 10^6

1 <= A[i] <= 10^9

N*M is odd



Input Format

The first and only argument given is the integer matrix A.



Output Format

Return the overall median of the matrix A.



Example Input

Input 1:

A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ]
Input 2:

A = [   [5, 17, 100]    ]


Example Output

Output 1:

 5
Output 2:

 17


Example Explanation

Explanation 1:

 
A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5.
Explanation 2:

 
Median is 17.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):

        # Assuming N X M is odd. We have to find NXM//2 + 1 elements <= search value (+1 for the element itself)

        N, M = len(A), len(A[0])
        # Find min and max bound
        s, e = float('inf'), float('-inf')

        for j in range(N):
            s = min(s, A[j][0])
            e = max(e, A[j][M-1])

        # Binary search between s and e
        ans = -1
        # Based on median definition, find if if the # of elements in the A <= mid are equal to target. If yes, that is the median
        target = (N * M) // 2 + 1
        
        while s <= e:
            mid = s + (e - s) // 2

            # Find count <= mid
            val = self.find_elems(A, mid, N, M)

            # Now find the total number of elements in A equal = target
            if val >= target:
                e = mid - 1
            
            # elif val > target:
            #     # We are to the right of a sorted array. Move left
            #     e = mid - 1
            
            else:
                # We are in the left half of a sorted array. Move right
                s = mid + 1

        return s
        
    
    def find_elems(self,A, key, N, M):

        # Apply binary search on all rows. Iterate on N.
        ans = 0
        for i in range(N):
            # Bounds are the col dimensions
            s, e = 0, M - 1
            count = 0
            while s <= e:
                mid = s + (e - s) // 2

                if A[i][mid] <= key:
                    # Move right to check if more values are possible.
                    count = mid + 1
                    s = mid + 1
                
                else:
                    # As values are greater than key, move left.
                    e = mid - 1
            
            ans = ans + count
        
        return ans

# TC

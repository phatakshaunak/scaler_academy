'''
Q1. Range Minimum Query
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N.

You have to perform two types of query, in each query you are given three integers x,y,z.

If x = 0, then update A[y] = z.
If x = 1, then output the minimum element in the array A between index y and z inclusive.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.



Problem Constraints

1 <= N, M <= 105

1 <= A[i] <= 109

If x = 0, 1<= y <= N and 1 <= z <= 109

If x = 1, 1<= y <= z <= N



Input Format

First argument is an integer array A of size N.

Second argument is a 2-D array B of size M x 3 denoting queries.



Output Format

Return an integer array denoting the output of each query where value of x is 1.



Example Input

Input 1:

 A = [1, 4, 1]
 B = [ 
        [1, 1, 3]
        [0, 1, 5]
        [1, 1, 2] 
     ]
Input 2:

 A = [5, 4, 5, 7]
 B = [ 
        [1, 2, 4]
        [0, 1, 2]
        [1, 1, 4]
     ]


Example Output

Output 1:

 [1, 4]
Output 2:

 [4, 2]


Example Explanation

Explanation 1:

 For 1st query, the minimum element from range (1, 3) is 1.
 For 2nd query, update A[1] = 5, now A = [5, 4, 1].
 For 3rd query, the minimum element from range (1, 2) is 4.
Explanation 2:

 For 1st query, the minimum element from range (2, 4) is 4.
 For 2nd query, update A[1] = 2, now A = [2, 4, 5, 7].
 For 3rd query, the minimum element from range (1, 4) is 2.
'''
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        n = len(A)

        T = [0] * (4 * n)

        # Build segment tree
        self.build_tree(0, n - 1, 0, T, A)
        ans = []
        for q in B:

            if q[0] == 0:
                self.update(0, n - 1, 0, q[1] - 1, q[2], T)
            
            else:
                curr = self.query(0, n - 1, 0, q[1] - 1, q[2] - 1, T)

                ans.append(curr)
        
        return ans
    
    def build_tree(self, s, e, idx, T, A):

        # Base case, when range becomes 1
        if s == e:
            # Fill value at idx
            T[idx] = A[s]
            return
        
        # Make left and right calls with changes s and e range
        mid = (s + e) // 2

        l = 2 * idx + 1
        r = l + 1

        # Left and right calls
        self.build_tree(s, mid, l, T, A)
        self.build_tree(mid + 1, e, r, T, A)

        # Populate T[idx] with minimum of it's left and right child nodes
        T[idx] = min(T[l], T[r])

    def query(self, s, e, idx, L, R, T):

        # Three cases, no overlap, complete overlap else partial overlap

        # No overlap
        if s > R or e < L:
            # Return inf to avoid being used in the calculation
            return float('inf')
        
        # Complete overlap
        if s >= L and e <= R:
            # Here return the value at index
            return T[idx]
        
        # Else, make left and right calls for partial overlap
        else:
            # Similar to mid calculation and calls
            mid = (s + e) // 2
            l  = 2 * idx + 1
            r = l + 1

            # Get left and right calls
            left = self.query(s, mid, l, L, R, T)
            right = self.query(mid + 1, e, r, L, R, T)

            # Return min of left and right
            return min(left, right)
    
    def update(self, s, e, idx, idx1, val, T):

        #Base case, when s and e are the same
        if s == e:
            T[idx] = val
            return
        
        # Calculate mid, check where to call
        mid = (s + e) // 2
        l = 2 * idx + 1
        r = l + 1

        if idx1 <= mid:
            self.update(s, mid, l, idx1, val, T)
        
        else:
            self.update(mid + 1, e, r, idx1, val, T)
        
        # Update parent minimum
        T[idx] = min(T[l], T[r])
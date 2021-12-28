'''Q1. Special Sums
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an array A of size N.

You need to process Q queries of following types on it:

X val, change the value of the Xth element of array A to val.
L R, find the sum: 1*a[L] + 2*a[L+1] + . . . + (R-L+1)*a[R].
Since, the result can be large, print it modulo 109 + 7



Problem Constraints

1 ≤ N, Q ≤ 105
1 ≤ A[i] ≤ 105
For query of the 1st type,

1 ≤ X ≤ N
1 ≤ val ≤ 105
For query of the 2nd type,

1 ≤ L ≤ R ≤ N


Input Format

The first argument of the input is the array A.

The second argument of the input is a 2-D array B containing the description of the queries.

Each query is an array of 3 elements, representing either (1 X val) or (2 L R).



Output Format

Return an array of answers to each query of the 2nd type, in the same order they were asked in the input.



Example Input

Input 1:

A: [2, 1, 4, 3]
B:  [
        [2, 1, 3], 
        [1, 2, 5], 
        [2, 1, 3]
    ]
Input 2:

A: [5, 6, 3, 7, 9]
B:  [    
        [2, 1, 5], 
        [2, 3, 4], 
        [1, 3, 7], 
        [2, 2, 4]
    ]


Example Output

Output 1:

[16, 24]
Output 2:

[99, 17, 41]


Example Explanation

Explanation 1:


For the 1st query, the sum is: 1*2 + 2*1 + 3*4 = 16.

After the 2nd query, the array becomes: [2, 5, 4, 3].

For the 3rd query, the sum is: 1*2 + 2*5 + 3*4 = 24.


Explanation 2:


For the 1st query, the sum is: 1*5 + 2*6 + 3*3 + 4*7 + 5*9 = 99.

For the 2nd query, the sum is: 1*3 + 2*7 = 17.

After the 3rd query, the array becomes: [5, 6, 7, 7, 9].

For the 4th query, the sum is: 1*6 + 2*7 + 3*7 = 41.'''

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        n = len(A)

        # Create new array for second segment tree
        A1 = [(i + 1) * A[i] for i in range(n)]

        t = 4 * n

        T1, T2 = [0] * t, [0] * t

        # Create both segment trees
        self.build(0, n - 1, 0, T1, A)
        self.build(0, n - 1, 0, T2, A1)
        
        # Answer array
        ans = []

        # Check all queries
        for i in range(len(B)):

            a, b, c = B[i]

            if a == 1:
                self.update(0, n - 1, 0, b - 1, c, T1, T2)
            
            else:
                v1 = self.range_query(0, n - 1, 0, b - 1, c - 1, T1)
                v2 = self.range_query(0, n - 1, 0, b - 1, c - 1, T2)
                
                curr = (v2 - (b - 1) * v1) % int(1e9 + 7)

                ans.append(curr)
        
        return ans
    
    def build(self, s, e, idx, T, arr):

        # Base case
        if s == e:
            T[idx] = arr[s]
            return
        
        # Split
        mid = s + (e - s) // 2

        # Calculate child indices
        l_c = 2 * idx + 1
        r_c = l_c + 1

        # Call on both sides
        self.build(s, mid, l_c, T, arr)
        self.build(mid + 1, e, r_c, T, arr)

        # Update T[idx]
        T[idx] = T[l_c] + T[r_c]
    
    def update(self, s, e, idx, idx1, val, T1, T2):

        # Base case
        if s == e:
            # Update regular tree values
            T1[idx] = val
            # Update i*A[i] type tree values
            T2[idx] = (idx1 + 1) * val
            return
        
        # Calculate left and right indices
        l_c = 2 * idx + 1
        r_c = l_c + 1

        # Split
        mid = s + (e - s) // 2

        # Check where idx1 lies
        if idx1 <= mid:
            # Go left
            self.update(s, mid, l_c, idx1, val, T1, T2)
        
        else:
            # Go right
            self.update(mid + 1, e, r_c, idx1, val, T1, T2)
        
        # Update T1[idx] and T2[idx]
        T1[idx] = T1[l_c] + T1[r_c]
        T2[idx] = T2[l_c] + T2[r_c]
    
    def range_query(self, s, e, idx, L, R, T):

        # Three cases, complete overlap, no overlap else partial overlap
        
        # Full overlap
        if s >= L and e <= R:
            return T[idx]
        
        # No overlap
        if L > e or R < s:
            return 0
        
        # Partial overlap
        mid = s + (e - s) // 2

        # Child indices
        l_c = 2 * idx + 1
        r_c = l_c + 1

        # Left and right calls
        left = self.range_query(s, mid, l_c, L, R, T)
        right = self.range_query(mid + 1, e, r_c, L, R, T)

        # Return sum of left and right
        return left + right
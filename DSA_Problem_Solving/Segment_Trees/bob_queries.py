'''Q2. Bob and Queries
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Bob has an array A of N integers. Initially, all the elements of the array are zero. Bob asks you to perform Q operations on this array.

You have to perform three types of query, in each query you are given three integers x, y and z.

if x = 1: Update the value of A[y] to 2 * A[y] + 1.
if x = 2: Update the value A[y] to ⌊A[y]/2⌋ , where ⌊⌋ is Greatest Integer Function.
if x = 3: Take all the A[i] such that y <= i <= z and convert them into their corresponding binary strings. Now concatenate all the binary strings and find the total no. of '1' in the resulting string.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.



Problem Constraints

1 <= N, Q <= 100000
1 <= y, z <= N
1 <= x <= 3



Input Format

The first argument has the integer A.
The second argument is a 2d matrix B, of size Q x 3, representing the queries.



Output Format

Return an array of integers where ith index represents the answer of the ith type 3 query.



Example Input

Input 1:

 A = 5
 B = [   
        [1, 1, -1]
        [1, 2, -1]
        [1, 3, -1]   
        [3, 1, 3] 
        [3, 2, 4]   
     ]
Input 2:

 A = 5
 B = [   
        [1, 1, -1]
        [1, 2, -1]
        [3, 1, 3]
        [2, 1, -1]
        [3, 1, 3]   
     ]


Example Output

Output 1:

 [3, 2]
Output 2:

 [2, 1]


Example Explanation

Explanation 1:

 Initial array A = [0, 0, 0, 0, 0]
 After query 1, A => [1, 0, 0, 0, 0]
 After query 2, A => [1, 1, 0, 0, 0]
 After query 3, A => [1, 1, 1, 0, 0]
 For query 4, Concatenation of Binary String between index 1 and 3 : 111. So, number of 1's = 3
 For query 5, Concatenation of Binary String between index 2 and 4 : 110. So, number of 1's = 2
 So, output array is [3, 2].
Explanation 2:

 Initial array A = [0, 0, 0, 0, 0]
 After query 1, A => [1, 0, 0, 0, 0]
 After query 2, A => [1, 1, 0, 0, 0]
 For query 3, Concatenation of Binary String between index 1 and 3 : 110. So, number of 1's = 2
 After query 4, A => [0, 1, 0, 0, 0]
 For query 5, Concatenation of Binary String between index 2 and 4 : 010. So, number of 1's = 1.
 So, output array is [2, 1].'''

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        # Initialize segment tree
        T = [0] * (4 * A)
        arr = [0] * A
        ans = []

        for q in B:
            x = q[0]
            y = q[1]
            z = q[2]

            if x != 3:
                self.update(0, A - 1, 0, y - 1, arr, T, x)
            
            else:
                curr = self.query(0, A - 1, 0, y-1, z-1, T)
                ans.append(curr)
            
        return ans

    def query(self, s, e, idx, L, R, T):

        # Three cases, no overlap, complete overlap else partial overlap
        # No overlap
        if s > R or e < L:
            # Return 0 to avoid being used in the calculation
            return 0
        
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
            return left + right
    
    def update(self, s, e, idx, idx1, arr, T, q):

        #Base case, when s and e are the same
        if s == e:

            if q == 1:
                arr[idx1] = 2 * arr[idx1] + 1
            
            if q == 2:
                arr[idx1] = arr[idx1] // 2
            
            # Calculate count of ones
            curr = self.get_ones(arr[idx1])
            
            # Storing single cell changes if value changes
            T[idx] = curr
            
            return
        
        # Calculate mid, check where to call
        mid = (s + e) // 2
        l = 2 * idx + 1
        r = l + 1

        if idx1 <= mid:
            self.update(s, mid, l, idx1, arr, T, q)
        
        else:
            self.update(mid + 1, e, r, idx1, arr, T, q)
        
        # Update idx after left and right calls
        T[idx] = T[l] + T[r]
        
    def get_ones(self, num):
        # ans = ''
        ans = 0
        while num:
            if num&1:
                ans += 1
            num = num >> 1
        return ans
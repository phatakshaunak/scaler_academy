'''Q5. MAX and MIN
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A .

value of a array = max(array) - min(array).

Calculate and return the sum of values of all possible subarrays of A % 109+7.



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 1000000



Input Format

The first and only argument given is the integer array A.



Output Format

Return the sum of values of all possible subarrays of A % 10^9+7.



Example Input

Input 1:

 A = [1]
Input 2:

 A = [4, 7, 3, 8]


Example Output

Output 1:

 0
Output 2:

 26


Example Explanation

Explanation 1:

Only 1 subarray exists. Its value is 0.
Explanation 2:

value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 10^9+7 = 26'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        N = len(A)

        # Initialize nearest smaller and greater arrays, stack

        nsl, nsr, ngl, ngr = [0] * N, [0] * N, [0] * N, [0] * N
        st = []

        # Populate NSL array

        for i in range(N):
            
            # Avoid double counting, remove duplicates
            while st and A[st[-1]] >= A[i]:
                st.pop()
            
            if st:
                nsl[i] = st[-1]
            
            else:
                nsl[i] = -1
            
            st.append(i)
        
        # Clear stack
        while st: st.pop()

        # Populate NSR array

        for i in range(N - 1, -1, -1):
            
            # Consider strictly increasing criteria to pop, to count all subarrays
            while st and A[st[-1]] > A[i]:
                st.pop()
            
            if st:
                nsr[i] = st[-1]
            
            else:
                nsr[i] = N
            
            st.append(i)
        
        # Clear stack
        while st: st.pop()

        # Populate NGL array

        for i in range(N):
            
            # Avoid double counting, remove duplicates
            while st and A[st[-1]] <= A[i]:
                st.pop()
            
            if st:
                ngl[i] = st[-1]
            
            else:
                ngl[i] = -1
            
            st.append(i)
        
        # Clear stack
        while st: st.pop()

        # Populate NGR array

        for i in range(N - 1, -1, -1):
            
            # Consider strictly increasing criteria to pop, to count all subarrays
            while st and A[st[-1]] < A[i]:
                st.pop()
            
            if st:
                ngr[i] = st[-1]
            
            else:
                ngr[i] = N
            
            st.append(i)
        
        # Clear stack
        while st: st.pop()

        ans, m = 0, int(1e9 + 7)

        for idx in range(N):

            l_min = nsl[idx] + 1
            r_min = nsr[idx] - 1

            l_max = ngl[idx] + 1
            r_max = ngr[idx] - 1

            # Subtract contribution to the minimum

            ans = (ans % m - (A[idx] % m * (idx - l_min + 1) % m * (r_min - idx + 1) % m) % m) % m

            # Add contribution to the maximum

            ans = (ans % m + (A[idx] % m * (idx - l_max + 1) % m * (r_max - idx + 1) % m) % m) % m
        
        return ans
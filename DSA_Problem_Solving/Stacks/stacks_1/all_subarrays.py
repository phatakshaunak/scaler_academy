'''Q3. All Subarrays
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N. You have to generate it's all subarrays having the size greater than 1.

Then for each subarray find Bitwise XOR of its maximum and second maximum element.

Find and return the maximum value of XOR among all subarrays.



Problem Constraints

2 <= N <= 105

1 <= A[i] <= 107



Input Format

Only argument is an integer array A.



Output Format

Return an integer, i.e maximum value of XOR of maximum and 2nd maximum element among all subarrays.



Example Input

Input 1:

 A = [2, 3, 1, 4]
Input 2:

 A = [1, 3]


Example Output

Output 1:

 7
Outnput 2:

 2


Example Explanation

Explanation 1:

 All subarrays of A having size greater than 1 are:
 Subarray            XOR of maximum and 2nd maximum no.
 1. [2, 3]           1
 2. [2, 3, 1]        1
 3. [2, 3, 1, 4]     7
 4. [3, 1]           2
 5. [3, 1, 4]        7
 6. [1, 4]           5
So maximum value of Xor among all subarrays is 7.
Explanation 2:

 Only subarray is [1, 3] and XOR of maximum and 2nd maximum is 2.'''

 class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        n = len(A)
        #ngl, ngr = [0] * n, [0] * n
        st = []
        ans = 0

        for i in range(n):

            while st and A[st[-1]] < A[i]:
                st.pop()
            
            if st:
                #ngl[i] = st[-1]
                ans = max(ans, A[i]^A[st[-1]])
            
            # else:
            #     ngl[i] = -1
            
            st.append(i)
        
        while st: st.pop()

        for j in range(n - 1, -1, -1):

            while st and A[st[-1]] < A[j]:
                st.pop()
            
            if st:
                # ngr[j] = st[-1]
                ans = max(ans, A[j]^A[st[-1]])
            
            # else:
            #     ngr[j] = -1
            
            st.append(j)
        
        return ans
        # ans = 0

        # for k in range(n):

        #     if ngl[k] != -1:
        #         ans = max(ans, A[k] ^ A[ngl[k]])
            
        #     if ngr[k] != -1:
        #         ans = max(ans, A[k] ^ A[ngr[k]])
        
        # return ans


    #     [2, 3, 1, 4]

    # ngl [-1, -1, 1, -1]
    # ngr [1, 3, 3, -1]

    # 2^3, 3^4, 1^4

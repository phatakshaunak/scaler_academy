'''Q2. Xor queries
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an array A (containing only 0 and 1) as element of N length.
Given L and R, you need to determine value of XOR of all elements from L to R (both inclusive) and number of unset bits (0's) in the given range of the array.



Problem Constraints

1<=N,Q<=100000
1<=L<=R<=N


Input Format

First argument contains the array of size N containing 0 and 1 only. 
Second argument contains a 2D array with Q rows and 2 columns, each row represent a query with 2 columns representing L and R.


Output Format

Return an 2D array of Q rows and 2 columns i.e the xor value and number of unset bits in that range respectively for each query.


Example Input

A=[1,0,0,0,1]
B=[ [2,4],
    [1,5],
    [3,5] ]


Example Output

[[0 3]
[0 3]
[1 2]]


Example Explanation

In the given case the bit sequence is of length 5 and the sequence is 1 0 0 0 1. 
For query 1 the range is (2,4), and the answer is (array[2] xor array[3] xor array[4]) = 0, and number of zeroes are 3, so output is 0 3. 
Similarly for other queries.'''

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        
        M = len(A)
        N = len(B)
        
        ans = [[] for i in range(N)]
        
        # Build prefix sum array
        
        ps_a = [0 for g in range(M+1)]
        
        for idx in range(M):
            
            ps_a[idx+1] = ps_a[idx] + A[idx]
        
        for q_i in range(N):
            
            #Left and right indices (Subtract one as input indices are 1-based, i.e. array starts at 1)
            q_l = B[q_i][0] - 1
            q_r = B[q_i][1] - 1
            
            #Subarray length
            sa_len = q_r - q_l + 1
            q_sum = ps_a[q_r+1] - ps_a[q_l]
            
            # XOR is zero if even number of ones in the sub-array
            if q_sum % 2 == 0:
                ans[q_i].append(0)
                ans[q_i].append((sa_len - q_sum))
                
            # XOR is one if odd number of ones in the sub-array
            else:
                ans[q_i].append(1)
                ans[q_i].append((sa_len - q_sum))
        
        return ans
                
                
'''
  [0,0,1,1,0,0,1]
[0,0,0,1,2,2,2,3]

l = 1, r = 4
ps[r+1]-ps[l]--> ps[5]-ps[1]
'''
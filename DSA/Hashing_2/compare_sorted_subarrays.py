'''Q2. Compare Sorted Subarrays
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A of length N. You have to answer Q queires.

Each query will contain 4 integers l1, r1, l2 and r2. If sorted segment from [l1, r1] is same as sorted segment from [l2 r2] then answer is 1 else 0.

NOTE The queries are 0-indexed.



Problem Constraints

0 <= A[i] <= 100000
1 <= N <= 100000
1 <= Q <= 100000



Input Format

First argument is an array A.
Second will be 2-D array B denoting queries with dimension Q * 4.
Consider ith query as l1 = B[i][0], r1 = B[i][1], l2 = A[i][2], r2 = B[i][3].



Output Format

Return an array of length Q with answer of the queries in the same order in input.



Example Input

Input 1:

 A = [1, 7, 11, 8, 11, 7, 1]
 B = [ 
       [0, 2, 4, 6]
     ]
Input 2:

 A = [1, 3, 2]
 B = [
       [0, 1, 1, 2]
     ] 


Example Output

Output 1:

 [1]
Output 2:

 [0]


Example Explanation

Explanation 1:

 (0, 2) -> [1, 7, 11]
 (4, 6) -> [11, 7, 1]
 Both are same when sorted hence 1.
Explanation 2:

 (0, 1) -> [1, 3]
 (1, 2) -> [3, 2] 
 Both are different when sorted hence -1.'''

class Solution:
	# @param A : list of integers
	# @param B : list of list of integers
	# @return a list of integers
	def solve(self, A, B):

        '''
        For each query, add elements from first subarray to a set, check all elements of other subarray in the set. If present append 0, else append 1. 
        Clear for each Q iteration
        TC O(Q*N), SC O(N) as we can clear set each time
        Above approach gives TLE.
        Optimization:
        Generate a hash value for strings of elements in array A. Then compute prefix sum array of the hashes and check if the sums are equal for both subararrays.
        O(N+Q) for time and space, O(N) for space if ans array not considered.
        '''

        hm = {}
        ans = []
        for val in A:

            if val not in hm:
                hm[val] = hash(str(val))
        
        ps = [0] * (len(A) + 1)

        for i in range(len(A)):

            ps[i+1] = ps[i] + hm[A[i]]
        
        for q in B:
            l1, r1, l2, r2 = q[0], q[1], q[2], q[3]

            if (ps[r1+1] - ps[l1]) == (ps[r2+1] - ps[l2]):
                ans.append(1)
            else:
                ans.append(0)
        
        return ans

        '''1, 7, 11, 8, 11, 7, 1
        0, 1, 8, 19, 27, 38, 45, 46'''


        # hm = {}
        # ans = []
        # for q in B:
        #     l1, r1, l2, r2 = q[0], q[1], q[2], q[3]

        #     # Map for first subarray
        #     for idx in range(l1, r1+1):
        #         if A[idx] not in hm:
        #             hm[A[idx]] = 1
        #         else:
        #             hm[A[idx]] += 1
            
        #     for i in range(l2, r2+1):
        #         if A[i] in hm:
        #             hm[A[i]] -= 1
            
        #     # Check if all frequencies are zero, if yes, then subarrays match
            
        #     #Flag to check if ans already filled with a 0
        #     no = False

        #     for key in hm:
        #         if hm[key] != 0:
        #             ans.append(0)
        #             no = True
        #             break
            
        #     if not no:
        #         ans.append(1)
            
        #     # Clear map for next query
        #     hm.clear()
        
        # return ans
'''Q5. Length of LIS
Attempted
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an array A. You need to find the length of the Longest Increasing Subsequence in the array.

In other words, you need to find a subsequence of array A in which the elements are in sorted order, (strictly increasing) and as long as possible.



Problem Constraints

1 ≤ length(A), A[i] ≤ 105



Input Format

The first and only argument of the input is the array A.



Output Format

Output a single integer, the length of the longest increasing subsequence in array A.



Example Input

Input 1:

A: [2, 1, 4, 3]
Input 2:

A: [5, 6, 3, 7, 9]


Example Output

Output 1:

2
Output 2:

4


Example Explanation

Explanation 1:

 [2, 4] and [1, 3] are the longest increasing sequences of size 2. 
Explanation 2:

The longest increasing subsequence we can get is [5, 6, 7, 9] of size 4.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def findLIS(self, A):
        
        # 1 + max(all j = 0 to j- 1 where A[j] < A[i])

        # dp = [0] * len(A)
        # dp[0] = 1

        # for i in range(1, len(A)):
            
        #     # ans = float('-inf')
        #     ans = 1
            
        #     for j in range(i):
        #         if A[j] < A[i]:
        #             ans = max(ans, 1 + dp[j])
            
        #     dp[i] = ans
        
        # return max(dp)

        store = [A[0]]

        n = len(A)

#         lis = 1
        for i in range(1, n):

            idx = self.upper_bound(store, 0, len(store) - 1, A[i])
            
            # print('upper bound', idx, A[i], store)
            if idx == len(store):
                store.append(A[i])
            
            else:
                store[idx] = A[i]
        
        # print(store, idx)
        return len(store)
    
    # Upper bound should be the index where key should be inserted. If key is present in the array, return leftmost index for key, else return the index of the smallest larger element
    # If no upper bound, return length of the array
    def upper_bound(self, arr, s, e, key):
        
        ans = len(arr)

        while s <= e:
            mid = s + (e - s) // 2

            if arr[mid] >= key:
                ans = mid
                e = mid - 1
            
            else:
                s = mid + 1
        
        return ans
    
    # TC O(N^2), SC O(N)
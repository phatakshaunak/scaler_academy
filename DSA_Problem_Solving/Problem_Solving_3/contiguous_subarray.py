'''Q1. Contiguous Array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given an array of integers A consisting of only 0 and 1.

Find the maximum length of a contiguous subarray with equal number of 0 and 1.



Input Format

The only argument given is the integer array A.
Output Format

Return the maximum length of a contiguous subarray with equal number of 0 and 1.
Constraints

1 <= length of the array <= 100000
0 <= A[i] <= 1
For Example

Input 1:
    A = [1, 0, 1, 0, 1]
Output 1:
    4
    Explanation 1:
        Subarray from index 0 to index 3 : [1, 0, 1, 0]
        Subarray from index 1 to index 4 : [0, 1, 0, 1]
        Both the subarrays have equal number of ones and equal number of zeroes.

Input 2:
    A = [1, 1, 1, 0]
Output 2:
    2'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        # Return zero if all elements of array are zero
        
        if sum(A) == 0:
            return 0
        
        # First calculate a prefix sum array substituting 0's with -1. This will help take advantage of the fact that a sub array with equal 1's and 0s(sub -1) will have a sum of zero.
        
        PS = [0]*(len(A)+1)
            
        for i in range(1,len(A)+1):
            if A[i-1] == 0:
                PS[i] = PS[i-1] - 1
            else:
                PS[i] = PS[i-1] + A[i-1]
        
        hash_map = {}
        
        #Initialize hash map to the 0th index for 0 value
        
        hash_map[0] = 0
        
        ''' Next we should maintain a hash map storing the first occurence of an element in the prefix sum array and the corresponding index in the given array A. As we traverse the prefix sum array, we can calculate lengths if we encounter an element already
            present in the array as we are storing th index of its initial occurence. This length can be continually updated to return a maximum length value.
        '''
        maxi = -1
        for j in range(1,len(A)+1):
            
            if PS[j] not in hash_map:
                hash_map[PS[j]] = j
            
            else:
                curr = j - hash_map[PS[j]]
                
                maxi = max(maxi, curr)
        
        return PS
            
### This solution does it without a prefix sum array https://leetcode.com/problems/contiguous-array/solution/
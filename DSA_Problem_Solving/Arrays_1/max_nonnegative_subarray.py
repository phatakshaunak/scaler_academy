'''Q5. Max Non Negative SubArray
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.


Input Format:

The first and the only argument of input contains an integer array A, of length N.
Output Format:

Return an array of integers, that is a subarray of A that satisfies the given conditions.
Constraints:

1 <= N <= 1e5
-INT_MAX < A[i] <= INT_MAX
Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]

Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        
        start, s = 0, 0
        curr, max_sum = 0, 0
        end = None
        
        for i in range(len(A)):
            
            curr += A[i]
            
            if A[i] < 0:
                curr = 0
                s = i+1
            
            elif max_sum < curr:
                max_sum = curr
                start = s
                end = i
            
            elif max_sum == curr:
                
                #If end is not defined and we encounter the first value as zero itself.
                if not end:
                    start = s
                    end = i
                
                if (end - start + 1) < (s - i + 1) or start > s:
                    start = s
                    end = i
        
        if max(A) < 0:
            return []
            
        return A[start:end+1]
        
            
#Time O(N), space O(1) ; applied Kadane'e algorithm with a tweaked condition to shift the start if encountering a negative values instead of shifting if the current sum becomes zero as in the original max subarray sum problem
            
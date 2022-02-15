'''Q5. Running Median
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A denoting a stream of integers. New arrays of integer B and C are formed. Each time an integer is encountered in a stream, append it at the end of B and append median of array B at the C.

Find and return the array C.

NOTE:

If the number of elements are N in B and N is odd then consider medain as B[N/2] ( B must be in sorted order).
If the number of elements are N in B and N is even then consider medain as B[N/2-1]. ( B must be in sorted order).


Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 109



Input Format

The only argument given is the integer array A.



Output Format

Return an integer array C, C[i] denotes the median of first i elements.



Example Input

Input 1:

 A = [1, 2, 5, 4, 3]
Input 2:

 A = [5, 17, 100, 11]


Example Output

Output 1:

 [1, 1, 2, 2, 3]
Output 2:

 [5, 5, 17, 11]


Example Explanation

Explanation 1:

 stream          median
 [1]             1
 [1, 2]          1
 [1, 2, 5]       2
 [1, 2, 5, 4]    2
 [1, 2, 5, 4, 3] 3
Explanation 2:

 stream          median
 [5]              5
 [5, 17]          5
 [5, 17, 100]     17
 [5, 17, 100, 11] 11'''

import heapq
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        # We will maintain larger length only in the max (left) heap. Hence push any value to it and then push its top to the right heap to ensure left and right half validity
        # If the left heap's length is less than the right, in this case push min heap's top to the left (max) heap

        lh, rh = [], []

        ans = []

        for val in A:

            heappush(lh, -1 * val)
            heappush(rh, -1 * heappop(lh))

            if len(lh) < len(rh):

                heappush(lh, -1 * heappop(rh))
            
            ans.append(-1 * lh[0])
        
        return ans

        #     # Another approach
        #     if not lh or -1 * lh[0] > val:
        #         heappush(lh, -1 * val)
        #     else:
        #         heappush(rh, val)
            
        #     # Rebalance lengths
        #     if len(lh) > len(rh) + 1:
        #         heappush(rh, -1 * heappop(lh))
            
        #     if len(rh) > len(lh) + 1:
        #         heappush(lh, -1 * heappop(rh))
            
        #     # Ans will be in the larger heap, if equal lengths, choose the value in the max (left heap)
        #     if (len(lh) > len(rh)) or (len(lh) == len(rh)): ans.append(-1 * lh[0])

        #     else: ans.append(rh[0])

        # return ans

        ################################################################################################ Previous code ################################################################################################

        # Define two heaps for the left half (max) and right half (min)
        l, r = [], []
        ans = []
        # Insert into the min heap each time, check if order is maintained(i.e. right's top > left's top)

        n = len(A)
        for i in range(n):

            # if not r or r[0] < A[i]:
            #     heapq.heappush(r, A[i])
            # else:
            #     heapq.heappush(l, -1 * A[i])
            
            # Add to min heap
            heapq.heappush(r, A[i])
            
            # Check if the top element is in the wrong heap
            if l and r and (-1 * l[0]) > r[0]:
                # Need to add r's top to l
                val = heapq.heappop(r)
                heapq.heappush(l, -1 * val)
            
            # Rebalance if length difference exceeds 1 in either cases
            if len(l) > len(r) + 1:
                top = heapq.heappop(l)
                heapq.heappush(r, (-1 * top))
            
            if len(r) > len(l) + 1:
                top = heapq.heappop(r)
                heapq.heappush(l, (-1 * top))
            
            # If both heaps have same length, return max's top, else min's top
            if len(l) == len(r):
                ans.append(-1 * l[0])
            
            # If the left contains one more element
            elif len(l) > len(r):
                ans.append(-1 * l[0])
            
            # If right contains one more element
            else:
                ans.append(r[0])
        
        return ans

# Ref: https://www.youtube.com/watch?v=EcNbRjEcb14
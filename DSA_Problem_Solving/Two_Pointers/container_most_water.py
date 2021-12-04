'''Q5. Container With Most Water
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given n non-negative integers A[0], A[1], …, A[n-1] , where each represents a point at coordinate (i, A[i]).

N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.



Problem Constraints

0 <= N <= 105

1 <= A[i] <= 105



Input Format

Single Argument representing a 1-D array A.



Output Format

Return single Integer denoting the maximum area you can obtain.



Example Input

Input 1:

A = [1, 5, 4, 3]
Input 2:

A = [1]


Example Output

Output 1:

 6
Output 2:

 0


Example Explanation

Explanation 1:

 
5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
So total area = 3 * 2 = 6
Explanation 2:

 
No container is formed.'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def maxArea(self, A):

        i, j = 0, len(A) - 1

        ans = 0
        while i < j:

            curr = min(A[i], A[j]) * (j - i)

            ans = max(ans, curr)

            # Move min pointer
            if A[i] <= A[j]:
                i += 1
            else:
                j -= 1
        
        return ans
	    
	    # i, j, ans = 0, len(A)-1, 0
	    
	    # while i < j:
	    #     curr = (j-i) * min(A[i], A[j])
	    #     ans = max(ans, curr)
	        
        #     if A[i] == A[j]:
        #         i += 1
        #         j -= 1
        #     elif A[i] < A[j]:
        #         i += 1
        #     else:
        #         j -= 1
	    #     # if A[i] <= A[j]:
	    #     #     i += 1
	    #     # else:
	    #     #     j -= 1
	    
	    # return ans

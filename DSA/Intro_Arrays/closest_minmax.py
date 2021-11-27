'''Q2. Closest MinMax
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A. Find the size of the smallest subarray such that it contains atleast one occurrence of the maximum value of the array

and atleast one occurrence of the minimum value of the array.



Problem Constraints

1 <= |A| <= 2000



Input Format

First and only argument is vector A



Output Format

Return the length of the smallest subarray which has atleast one occurrence of minimum and maximum element of the array



Example Input

Input 1:

A = [1, 3]
Input 2:

A = [2]


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 Only choice is to take both elements.
Explanation 2:

 Take the whole array.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        min_A = min(A)
        max_A = max(A)
        size = len(A)
        
        # Edge cases
        if len(A) == 1 or min_A == max_A:
            return 1
        
        min_ind = -1
        max_ind = -1
        
        for i in range(len(A)):
            
            if A[i] == min_A:
                min_ind = i
                
                #Don't calculate size until you can find max index
                if (max_ind != -1):
                    size = min(size, (i - max_ind + 1))
                
            elif A[i] == max_A:
                max_ind = i
                # Don't calculate size until you can find min index
                if (min_ind != -1):
                    size = min(size, (i - min_ind + 1))
                    
        return size
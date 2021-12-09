'''Q3. Minimum Swaps
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.



Problem Constraints

1 <= length of the array <= 100000
-109 <= A[i], B <= 109



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return the minimum number of swaps.



Example Input

Input 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8
Input 2:

 A = [5, 17, 100, 11]
 B = 20


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.
Explanation 2:

 A = [5, 17, 100, 11]
 After swapping 100 and 11, A => [5, 17, 11, 100].
 Now, all elements less than or equal to 20 are together.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        #This solution works only if you want to bring all elements <= B to the front.
        # i, j, count = 0, 0, 0
        
        # while j < len(A):
            
        #     if A[i] <= B:
        #         i += 1
                
        #     elif (A[j] <= B) and (A[i] > B):
        #         A[i], A[j] = A[j], A[i]
        #         count += 1
        #         i += 1
            
        #     j += 1
        
        '''The question asks the minimum number of swaps needed. The goal is to count the number of values <= B and then find a window 
        of that size with the maximum number of values <= B. The count of values > B in that window is the answer. 
        The window of size of count of values <= B needs to slided across the array
        '''
        
        c_b, swaps = 0, 0
        ans = float("inf")
        
        for i in range(len(A)):
            if A[i] <= B:
                c_b += 1
        
        for j in range(c_b):
            
            if A[j] > B:
                swaps += 1
        
        ans = min(ans, swaps)
        
        for k in range(c_b, len(A)):
            
            if A[k-c_b] > B:
                swaps -= 1
            
            if A[k] > B:
                swaps += 1
            
            ans = min(ans, swaps)
            
        return ans
        # return count

    def solve1(self, A, B):

        # Find count of values <= B
        count = 0
        for val in A:
            if val <= B:
                count += 1
        
        # Slide window of size count across the array, and find a window that requires minimum changes, i.e min. elements
        # in that window violate the condition of > B

        ans = float('inf')
        curr = 0
        for i in range(len(A)):

            # Condition for first window
            if i <= count - 1:
                if A[i] > B:
                    curr += 1
            
            else:
                # For all others, remove count - ith element, and add ith element
                if A[i-count] > B:
                    curr -= 1
                # Add ith element if > B
                if A[i] > B:
                    curr += 1
            
            # Check for possible answer if i >= count - 1
            if i >= count - 1:
                ans = min(ans, curr)
        
        return ans
'''Q5. Special Integer
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.



Problem Constraints

1 <= |A| <= 100000
1 <= A[i] <= 10^9

1 <= B <= 10^9



Input Format

The first argument given is the integer array A.

The second argument given is integer B.



Output Format

Return the maximum value of K (sub array length).



Example Input

Input 1:

A = [1, 2, 3, 4, 5]
B = 10
Input 2:

A = [5, 17, 100, 11]
B = 130


Example Output

Output 1:

 2
Output 2:

 3


Example Explanation

Explanation 1:

Constraints are satisfied for maximal value of 2.
Explanation 2:

Constraints are satisfied for maximal value of 3.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        '''Search space is between a subarray of size 0 (i.e no subarray is possible) to N which is the size of the array
           Binary search on this space and then iterating to check all sub arrays can give us the maximum size
           A = [1, 2, 3, 4, 5]
           B = 10
        
           0 to 5
           mid = 2
           ps = [0, 1, 3, 6, 10, 15]
           start at mid and go till the end checking all sub arrays. that would be ps[mid_pointer] - ps[mid_pointer - mid]
        '''
        
        ps = [0] * (len(A) + 1)
        ans = -1
        for i in range(len(A)):
            ps[i+1] = ps[i] + A[i]
            
        # Define the search space
        s, e = 0, len(A)
        
        while s <= e:
            
            mid = s + (e - s) // 2
            
            # Iterate over prefix sum array to check all possible subarrays
            
            j = mid
            
            while j <= len(A):
                
                if ps[j] - ps[j - mid] > B:
                    break
                j += 1
            
            if j > len(A):
                ans = mid
                #Then move right or try a larger sized subarray
                s = mid + 1
            else:
                # Move left as the current size is not satisfied
                e = mid - 1
        
        return ans
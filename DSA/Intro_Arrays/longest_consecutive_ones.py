'''Q4. Length of longest consecutive ones
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.


Input Format

The only argument given is string A.
Output Format

Return the length of the longest consecutive 1’s that can be achieved.
Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        A = [int(i) for i in A]
        
        if sum(A) == len(A):
            return sum(A)
        
        left, right = [0]*len(A), [0]*len(A)

        for i in range(len(A)):
            if i == 0 or A[i] == 0:
                left[i] = A[i]
    
            else:
                left[i] = left[i-1]+A[i]
    
        for i in range(len(A)-1, -1, -1):
            if i == len(A) - 1 or A[i] == 0:
                right[i] = A[i]
    
            else:
                right[i] = right[i+1] + A[i]
    
        max_count = float('-inf')
        max_one = sum(A)
    
        # print(A)
        # print(left)
        # print(right)
        
        for i in range(len(A)):
    
            if i == 0 and A[i] == 0:
                max_count = max(max_count, (1+right[i+1]))
    
            elif i == len(A) - 1 and A[i] == 0:
                max_count = max(max_count, (left[i-1]+1))
    
            else:
                if A[i] == 0:
                    max_count = max(max_count, (left[i-1] + 1 + right[i+1]))
    
            if max_count > max_one:
                max_count = max_one
    
        return max_count

'''Q3. First Missing Integer
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an unsorted integer array A of size N. Find the first missing positive integer.

Note: Your algorithm should run in O(n) time and use constant space.



Problem Constraints

1 <= N <= 1000000

-109 <= A[i] <= 109



Input Format

First argument is an integer array A.



Output Format

Return an integer denoting the first missing positive integer.



Example Input

Input 1:

[1, 2, 0]
Input 2:

[3, 4, -1, 1]
Input 3:

[-8, -7, -6]


Example Output

Output 1:

3
Output 2:

2
Output 3:

1


Example Explanation

Explanation 1:

A = [1, 2, 0]
First positive integer missing from the array is 3.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):

        n = len(A)
        
        for i in range(n):
            
            # Numbers that do not matter in finding the first missing positive value
            if A[i] <= 0 or A[i] > n:
                A[i] = n + 1
        
        for i in range(n):
            
            if 1 <= abs(A[i]) <= n:
                
                # If the array was sorted, A[i] would be located at A[i] - 1, thus mark A[i] - 1 with a negative sign as visited if not negative
                idx = abs(A[i]) - 1
                
                if A[idx] > 0:
                    A[idx] *= -1
        
        for i in range(n):
            
            # The first non-negative element indicates the missing value
            if A[i] > 0:
                return i + 1
        # If all negative, n + 1 is the next number to be missing
        return n + 1

        # for i in range(n):

        #     while 1 <= A[i] <= n and A[A[i] - 1] != A[i]:

        #         A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
    
        # for i in range(n):

        #     if A[i] != i + 1:
        #         return i + 1
        
        # return n + 1

        # freq = [0 for i in range(n + 1)]

        # for val in A:

        #     if 1 <= val <= n and not freq[val]:
        #         freq[val] = 1
        
        # for i in range(1, n + 1):

        #     if freq[i] == 0:
        #         return i

        # return n + 1
        
        # chain = set()

        # for val in A:
        #     chain.add(val)
        
        # curr = 1

        # while curr in chain:
        #     curr += 1
        
        # return curr
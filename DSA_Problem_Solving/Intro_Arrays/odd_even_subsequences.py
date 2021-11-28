'''Q3. Odd Even Subsequences
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given an array of integers A of size N. Find the longest subsequence of A which is odd-even.

A subsequence is said to odd-even in the following cases:

The first element of the subsequence is odd, second element is even, third element is odd and so on. For example: [5, 10, 5, 2, 1, 4], [1, 2, 3, 4, 5]

The first element of the subsequence is even, second element is odd, third element is even and so on. For example: [10, 5, 2, 1, 4, 7], [10, 1, 2, 3, 4]

Return the maximum possible length of odd-even subsequence.

Note: An array B is a subsequence of an array A if B can be obtained from A by deletion of several (possibly, zero or all) elements.


Input Format

The only argument given is the integer array A.
Output Format

Return the maximum possible length of odd-even subsequence.
Constraints

1 <= N <= 100000
1 <= A[i] <= 10^9 
For Example

Input 1:
    A = [1, 2, 2, 5, 6]
Output 1:
    4
    Explanation 1:
        Maximum length odd even subsequence is [1, 2, 5, 6]

Input 2:
    A = [2, 2, 2, 2, 2, 2]
Output 2:
    1
    Explanation 2:
        Maximum length odd even subsequence is [2]'''
    
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #  subseq = []
        prev = A[0]
        count = 1
        #  subseq.append(A[0])
        for i in range(1,len(A)):
            if (prev % 2 == 0) and (A[i] % 2 != 0):
                count += 1
                prev = A[i]
                 
            elif (prev % 2 != 0) and (A[i] % 2 == 0):
                count += 1
                prev = A[i]
         
        return count    
         
        #     #  if (A[i-1] % 2 == 0) and (A[i] % 2 != 0):
            
        #          subseq.append(A[i])
                 
        #      elif (A[i-1] % 2 != 0) and (A[i] % 2 == 0):
        #          subseq.append(A[i])
                 
        #  return len(subseq)

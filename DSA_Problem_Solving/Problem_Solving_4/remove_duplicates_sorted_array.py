'''Q3. Remove Duplicates from Sorted Array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a sorted array A consisting of duplicate elements.

Your task is to remove all the duplicates and return a sorted array of distinct elements consisting of all distinct elements present in A.

NOTE: The input format has been changed from previous versions.



Problem Constraints

1 <= |A| <= 106

1 <= A[i] <= 2*109



Input Format

First and only argurment containing the integer array A.



Output Format

Return an array/vector from the function as per the question.



Example Input

Input 1:

A = [1, 1, 2]
Input 2:

A = [1, 2, 2, 3, 3]


Example Output

Output 1:

[1, 2]
Output 2:

[1, 2, 3]


Example Explanation

Explanation 1:

Updated Array: [1, 2] after removing the 2nd element.
Explanation 2:

Updated Array: [1, 2, 3] after removing the 3rd and 5th element.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        # ans = []
        # ans.append(A[0])
        # index = 0
        
        # for i in range(1, len(A)):
            
        #     if A[i] != ans[index]:
        #         ans.append(A[i])
        #         index += 1
        
        i, j = 0, 1
        
        for j in range(1, len(A)):
            
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
            
        return A[:i+1]

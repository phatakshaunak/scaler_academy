'''Q2. Multiplication of previous and next
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given an array of integers A, update every element with multiplication of previous and next elements with following exceptions. a) First element is replaced by multiplication of first and second. b) Last element is replaced by multiplication of last and second last.


Input Format

The only argument given is the integer array A.
Output Format

Return the updated array.
Constraints

1 <= length of the array <= 100000
-10^4 <= A[i] <= 10^4 
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    [2, 3, 8, 15, 20]

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    [85, 500, 187, 1100]'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        result = [0] * len(A)
        if len(A) <= 2:
            return A
            
        for i in range(len(A)):
            if i == 0:
                result[i] = A[0] * A[1]
            elif i == len(A) - 1:
                result[i] = A[len(A)-1] * A[len(A)-2]
            else:
                result[i] = A[i-1] * A[i+1]
        
        return result


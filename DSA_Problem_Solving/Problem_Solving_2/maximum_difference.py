'''Q3. Maximum Difference
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given an array of integers A and an integer B. Find and return the maximum value of | s1 - s2 |

where s1 = sum of any subset of size B, s2 = sum of elements of A - sum of elemets of s1

Note |x| denotes the absolute value of x.


Input Format

The arguments given are the integer array A and integer B.
Output Format

Return the maximum value of | s1 - s2 |.
Constraints

1 <= B < length of the array <= 100000
1 <= A[i] <= 10^5 
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 2
Output 1:
    9

Input 2:
    A = [5, 17, 100, 11]
    B = 3
Output 2:
    123'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        '''
        Simply sorting, selecting sum of first B elements as s1 works in case of only won't work in case of having a mixture of positive and negative numbers. For this case, we need to slide a window of size B across the array and compare values for |s1-s2|
        |s1-s2| is simply |2*s1-arr_sum|. Since arr_sum is fixed, we need to find a maximum value for s1, 
        '''
        A.sort()
        
        arr_sum = sum(A)
        sum1 = sum(A[0:B])
        
        max_val = abs((2*sum1)-arr_sum)
        
        for i in range(B,len(A)):
            sum1 = sum1 + A[i] - A[i-B]
            max_val = max(max_val, ((2*sum1)-arr_sum))
        
        return max_val
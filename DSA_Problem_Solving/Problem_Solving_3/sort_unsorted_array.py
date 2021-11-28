'''Q5. Sort the Unsorted Array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an integer array A having N integers.

You have to find the minimum length subarray A[l..r] such that sorting this subarray makes the whole array sorted.



Problem Constraints

1 <= N <= 105

-109 <= A[i] <= 109



Input Format

First and only argument is an integer array A.



Output Format

Return an integer denoting the minimum length.



Example Input

Input 1:

 A = [0, 1, 15, 25, 6, 7, 30, 40, 50] 
Input 2:

 A = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60] 


Example Output

Output 1:

 4 
Output 2:

 6 


Example Explanation

Explanation 1:

 The smallest subarray to be sorted to make the whole array sorted =  A[3..6] i.e, subarray lying between positions 3 and 6. 
Explanation 2:

 The smallest subarray to be sorted to make the whole array sorted =  A[4..9] i.e, subarray lying between positions 4 and 9.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        if len(A) == 1:
            return 0
        
        ''' We can construct a sorted array ; then find the start and end indices by traversing left --> right and breaking out after first mismatch and similarly from right --> left to get the start and end index respectively. The idea is that elements to the left
            or right of the subarray are going to be sorted
        '''
        
        A_sort = sorted(A)
        
        s, e = -1, -1
        
        for i in range(len(A)):
            if A[i] != A_sort[i]:
                s = i
                break
        
        for j in range(len(A)-1,-1,-1):
            if A[j] != A_sort[j]:
                e = j
                break
        
        if s == e:
            return 0
        
        return (e - s + 1)
        
'''Another optimum solution can be a 2-pointer approach for this case which will be an O(N) time, O(1) space solution as well
   Here the time complexity is O(NlogN) and O(N) space'''
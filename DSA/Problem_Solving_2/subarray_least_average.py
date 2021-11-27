'''Q4. Subarray with least average
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description
Given an array of size N, Find the subarray with least average of size k.



Problem Constraints
1<=k<=N<=1e5
-1e5<=A[i]<=1e5


Input Format
First argument contains an array A of integers of size N.
Second argument contains integer k.


Output Format
Return the index of the first element of the subarray of size k that has least average.
Array indexing starts from 0.


Example Input
Input 1:
A=[3, 7, 90, 20, 10, 50, 40]
B=3
Input 2:

A=[3, 7, 5, 20, -10, 0, 12]
B=2


Example Output
Output 1:
3
Output 2:

4


Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.
Explanation 2:

 Subarray between [4, 5] has minimum average'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        curr_sum = 0
        ind = 0
        for j in range(B):
            curr_sum += A[j]
        
        min_sum = curr_sum
        
        for k in range(B, len(A)):
            curr_sum = curr_sum - A[k-B] + A[k]
            
            if curr_sum < min_sum:
                min_sum = curr_sum
                ind = k - B + 1
        
        return ind

'''An important observation is that this problem is the same as finding minimum sum. Minimum average for a fixed window implies 
you are dividing by the same B, thus constant. Hence it is better to just compare sliding sums instead of averages.'''
'''Q2. Max Distance
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A of integers of size N. Find the maximum of value of j - i such that A[i] <= A[j].



Problem Constraints

1 <= N <= 1000000

-109 <= A[i] <= 109



Input Format

First argument is an integer array A of size N.



Output Format

Return an integer denoting the maximum value of j - i.



Example Input

Input 1:

A = [3, 5, 4, 2]


Example Output

Output 1:

2


Example Explanation

Explanation 1:

For A[0] = 3 and A[2] = 4, the ans is (2 - 0) = 2.'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    
    def maximumGap(self, A):
        '''
        Create a pair of value and index, sort on value ; Iterate to find max value of j-i TC: O(NlogN), SC: O(N)
        [3,5,4,2]
        [[3,0], [5,1], [4,2], [2,3]]
        [[2,3], [3,0], [4,2], [5,1]]
        
        Next, need to find a min i and max j where A[j] >= A[i] ; array is sorted, thus we can try all values to the right as j and generate the maximum value. Keep updating minimum value and a maximum of index-minimum value.
        '''
        if len(A) == 1 or not A:
            return 0
            
        pair = [[-1,-1] for i in range(len(A))]

        for i in range(len(A)):
            pair[i][0] = A[i]
            pair[i][1] = i
        
        pair = sorted(pair)
        
        min_val = float('inf')
        max_val = float('-inf')
        ans = 0
        for j in range(len(A)):
            
            min_val = min(min_val, pair[j][1])
            
            ans = max(ans, pair[j][1] - min_val)
        
        return ans
            
    #TC O(NlogN), SC O(N)
        
'''
3 5 4 2
[2,3], [3,0], [4,2], [5,1]

Sorting ensures A[i] <= A[j] ; Next we need to find a maximum value for (j-i)

Need to try a binary search approach maintaining a right maximum array and finding largest maximum satisfying the condition-- Array traversal and binary search each time will be O(NLogN)
'''
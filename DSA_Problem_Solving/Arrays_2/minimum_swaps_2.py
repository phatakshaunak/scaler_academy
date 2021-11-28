'''Q4. Minimum Swaps 2
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A of size N that is a permutation of [0, 1, 2, …, (N-1)]. It is allowed to swap any two elements (not necessarily consecutive).

Find the minimum number of swaps required to sort the array in ascending order.



Problem Constraints

1 <= N <= 100000
0 <= A[i] < N



Input Format

The only argument given is the integer array A.



Output Format

Return the minimum number of swaps.



Example Input

Input 1:

A = [1, 2, 3, 4, 0]
Input 2:

A = [2, 0, 1, 3]


Example Output

Output 1:

4
Output 2:

2


Example Explanation

Explanation 1:

 If you swap (1, 2) -> (2, 3) -> (4, 0) -> (3, 0). You will get a sorted array.
 You cannot sort it with lesser swaps.
Explanation 2:

 You cannot sort it with lesser than 2 swaps.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        swap = 0
        for i in range(len(A)):
            
            if A[i] != i:
                while A[i] != i:
                    temp = A[i]
                    A[i] = A[temp]
                    A[temp] = temp
                    swap += 1
        return swap
            
'''
1 2 3 4 0
0 1 2 3 4

2 1 3 4 0
0 1 2 3 4

3 1 2 4 0
0 1 2 3 4

4 1 2 3 0
0 1 2 3 4


Each number must match with its index to be sorted. 

2 0 1 3
0 1 2 3

if A[i] != i:
    A[i], A[A[i]] = A[A[i]], A[i] ...won't work
    swap += 1
    
4 2 3 5 1 0
0 1 2 3 4 5

1 2 3 5 4 0
0 1 2 3 4 5

1 3 2 5 4 0
0 1 2 3 4 5

1 3 2 0 4 5
0 1 2 3 4 5

4 3 2 1 0
0 1 2 3 4


0 3 2 1 4
0 1 2 3 4

'''
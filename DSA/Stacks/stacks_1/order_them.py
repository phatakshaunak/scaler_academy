'''Q3. Order them
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A describing ranking of trucks. Your task is to insert these rank in another array B by some means of operations such that B is sorted in ascending order. For performing these operations you can use one stack C.

In one Operation you can perform any of the following steps:

Remove the first element from A and append at the back of C.
Remove the last element from C and append at the back of B.
Remove the first element from A and append at the back of B.
you can perform these operations any number of times (possibly zero).

Return 1 if B can be formed in ascending order using some operations else return 0.



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= length of Array
All elements of A are distinct.



Input Format

The only argument given is the integer array A.



Output Format

Return 1 if B can be formed in ascending order using some operations else return 0.



Example Input

Input 1:

A = [5, 1, 2, 4, 3]
Input 2:

A = [5, 3, 1, 4, 2]


Example Output

Output 1:

1


0


Example Explanation

Explanation 1:

Given array A = [5, 1, 2, 4, 3], stack C = [] , array B = []
step 1: A = [5, 1, 2, 4, 3]
        C = []
        B = []
step 2: A = [1, 2, 4, 3]
        C = [5]
        B = []
step 3: A = [2, 4, 3]
        C = [5]
        B = [1]
step 4: A = [4, 3]
        C = [5]
        B = [1, 2]
step 5: A = [3]
        C = [5, 4]
        B = [1, 2]
step 6: A = []
        C = [5, 4]
        B = [1, 2, 3]
step 7: A = []
        C = [5]
        B = [1, 2, 3, 4]
step 8: A = []
        C = []
        B = [1, 2, 3, 4, 5]
Array B is in ascending order. So, return 1.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        B, C = [], []

        for val in A:

            if not C or C[-1] > val:
                C.append(val)
            
            elif C and C[-1] < val:

                while C and C[-1] < val:
                    
                    # Assuming array A contains unique and consecutive elements
                    if B and (C[-1] - B[-1]) != 1:
                        return 0
                    else:
                        B.append(C.pop())
                
                C.append(val)
        
        while C:
            if B and (C[-1] - B[-1]) != 1:
                return 0
            else:
                B.append(C.pop())
        
        return 1

        '''
        A's first can be appended to B or C
        C's last can be appended to B
        B needs to be returned

        A: [5, 1, 2, 4, 3]

        B: [1, 2, ]

        C: [5, 4, 3]
        '''
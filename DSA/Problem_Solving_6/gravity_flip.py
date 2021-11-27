'''Q1. Gravity Flip
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Little Chris is bored during his physics lessons (too easy), so he has built a toy box to keep himself occupied. The box is special, since it has the ability to change gravity.

There are n columns of toy cubes in the box arranged in a line. The i-th column contains ai cubes. At first, the gravity in the box is pulling the cubes downwards. When Chris switches the gravity, it begins to pull all the cubes to the right side of the box. The figure shows the initial and final configurations of the cubes in the box: the cubes that have changed their position are highlighted with orange.


Given the initial configuration of the toy cubes in the box, find the amounts of cubes in each of the n columns after the gravity switch!



Problem Constraints

1<=n<=100
1<=A[i]<=100


Input Format

First argument is array of integers of size n denoting the columns.


Output Format

Return the array of integers denoting the amount of cubes of the n columns after the gravity switch!


Example Input

INPUT-1
A=[3 2 1 2]
INPUT-2

A=[2 3 8 ]


Example Output

output-1
1 2 2 3
output-2
2 3 8


Example Explanation

Explanation-1 
The first example case is shown on the figure. The top cube of the first column falls to the top of the last column; the top cube of the second column falls to the top of the third column; the middle cube of the first column falls to the top of the second column.
Explanation-2
In the second example case the gravity switch does not change the heights of the columns.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        A.sort()
        
        return A

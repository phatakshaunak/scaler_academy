'''Q4. Gray Code
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

A gray code sequence must begin with 0.



Problem Constraints

1 <= A <= 16



Input Format

First argument is an integer A.



Output Format

Return an array of integers representing the gray code sequence.



Example Input

Input 1:

A = 2
Input 1:

A = 1


Example Output

output 1:

[0, 1, 3, 2]
output 2:

[0, 1]


Example Explanation

Explanation 1:

for A = 2 the gray code sequence is:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
So, return [0,1,3,2].
Explanation 1:

for A = 1 the gray code sequence is:
    00 - 0
    01 - 1
So, return [0, 1].'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):

        if A == 1:
            return [0, 1]
    
        ans, shift = [0, 1], 1
    
        return self.gcode(A-1, shift, ans)

        # Gray Code

    def gcode(self, A, shift, ans):
        
        if A == 0:
            return ans
        
        temp = []
        for i in range(len(ans)-1,-1,-1):
            temp.append(ans[i] + (1 << shift))
        
        for val in temp:
            ans.append(val)
        
        A -= 1
        shift += 1
        return self.gcode(A, shift, ans)


# def gray_code(N):
    
#     if N == 1:
#         return ['0','1']
    
#     ans = gray_code(N-1)
#     temp = []
    
#     for i in range(len(ans)):
#         temp.append('0' + ans[i])
    
#     for j in range(len(ans)-1,-1,-1):
#         temp.append('1' + ans[j])
    
#     return temp

# def gray_code(N):
    
#     if N == 1:
#         return [0,1]
    
#     if N == 0:
#         return
    
#     ans = gray_code(N-1)
#     temp = []
    
#     for i in range(len(ans)):
#         temp.append(ans[i])
    
#     for j in range(len(ans)-1,-1,-1):
#         temp.append((1<<(N-1)) + ans[j])
    
#     return temp
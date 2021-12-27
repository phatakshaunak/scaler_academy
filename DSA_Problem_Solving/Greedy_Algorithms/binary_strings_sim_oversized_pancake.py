'''Q1. Binary Strings
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given a string A consisting of 1's and 0's. Now the task is to make the string consisting of only 1's. But you are allowed to perform only the following operation:

Take exactly B consecutive elements of string and change 1 to 0 and 0 to 1.
Each operation takes 1 unit time so you have to determine the minimum time required to make the string of 1's only. If not possible return -1.



Problem Constraints

2 ≤ length of A ≤ 105
2 ≤ B ≤ (length of A)



Input Format

First argument is a string A consisting if 1's and 0's.
Second argument is an integer B which represents the number of consecutive elements which can be changed.



Output Format

Return an integer which is the minimum time to make the string of 1's only or -1 if not possible.



Example Input

Input 1:

 A = "00010110"
 B = 3
Input 2:

 A = "011"
 B = 3


Example Output

Output 1:

 3
Output 2:

 -1


Example Explanation

Explanation 1:

 You can get 1 by first changing the leftmost 3 elements, getting to 11110110, then the rightmost 3, getting to 11110001, 
 and finally the 3 left out 0's to 11111111; In 3 unit time.
Explanation 2:

It's not possible to convert the string into string of all 1's.'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        tmp = [0 for i in A]
        n = len(A)

        # for i in range(n):
        #     if A[i] == '1':
        #         tmp[i] = 1
        
        # ct = 0
        
        # for i in range(n):
            
        #     if tmp[i] == 0:
        #         if (i + B - 1) <= (n - 1):
        #             for j in range(i, i + B):
        #                 tmp[j] ^= 1
        #             ct += 1
        #         else:
        #             return -1
        
        # return ct

        # O(n*(n-b+1)) ~ O(n^2)

        flag = 0
        ct = 0
        for i in range(n - B + 1):
            # XOR flag with tmp element to decide if flipping needs to be stopped
            flag = flag ^ tmp[i]
            # Two conditions: if A[i] == 0 and flag == 0 or A[i] == 1 and flag == 1 (In both cases, bits are unset)
            if (A[i] == '0' and flag == 0) or (A[i] == '1' and flag == 1):
                # Flip flag
                flag ^= 1
                # Increment count
                ct += 1
                
                # Set tmp value to 1 to stop flips
                if (i + B) <= (n - 1):
                    tmp[i + B] = 1
        
        # Check same conditions for remaining elements. If a bit is unset, then it is not possible to flip, return -1
        i += 1
        # Check last elements
        while i < n:
            flag = flag ^ tmp[i]
            if (A[i] == '0' and flag == 0) or (A[i] == '1' and flag == 1):
                return -1
            i += 1

        return ct
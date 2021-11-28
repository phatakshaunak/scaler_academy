'''Q3. Rotate string
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A, rotate the string B times in clockwise direction and return the string.



Problem Constraints

1 <= |A| <= 105

1 <= B <= 109

String A consist only of lowercase characters.



Input Format

First and only argument is a string A.



Output Format

Return a string denoting the rotated string.



Example Input

Input 1:

 A = "scaler"
 B = 2
Input 2:

 A = "academy"
 B = 7


Example Output

Output 1:

 "erscal"
Output 2:

 "academy"


Example Explanation

Explanation 1:

 Rotate the given string twice so the string becomes "erscal".
'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        A = [i for i in A]
        
        # Accounting for when B > len(A)
        nrot = B % len(A)
        
        def rev(l,r,arr):
    
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                
                l += 1
                r -= 1
        
        rev(0, len(A)-1, A)
        
        rev(0, nrot-1, A)
        
        rev(nrot, len(A)-1, A)
        
        return ''.join(A)
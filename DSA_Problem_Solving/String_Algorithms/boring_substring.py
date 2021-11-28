'''Q3. Boring substring
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A of lowercase English alphabets. Rearrange the characters of the given string A such that there is no boring substring in A.

A boring substring has the following properties:

Its length is 2.
Both the characters are consecutive, for example - "ab", "cd", "dc", "zy" etc.(If the first character is C then the next character can be either (C+1) or (C-1)).
Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.



Problem Constraints

1 <= |A| <= 105



Input Format

The only argument given is string A.



Output Format

Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.



Example Input

Input 1:

 A ="abcd"
Input 2:

 A = "aab"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 String A can be rearranged into "cadb" or "bdac" 
Explanation 2:

 No arrangement of string A can make it free of boring substrings.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        '''
        Separate odd and even asci value characters into two arrays
        Sort both arrays
        Check if last of first and first of second are not consecutive for
        both concatenation arrangements, if yes return true.
        '''

        odd = [char for char in A if ord(char)&1]
        even = [char for char in A if not ord(char)&1]

        odd.sort()
        even.sort()

        if abs(ord(odd[-1]) - ord(even[0])) > 1 or abs(ord(even[-1]) - ord(odd[0])) > 1:
            return 1
        
        return 0
'''Q2. Closest Palindrome
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Groot has a profound love for palindrome which is why he keeps fooling around with strings.
A palindrome string is one that reads the same backward as well as forward.

Given a string A of size N consisting of lowercase alphabets, he wants to know if it is possible to make the given string a palindrome by changing exactly one of its character.



Problem Constraints

1 <= N <= 105



Input Format

First and only argument is a string A.



Output Format

Return the string YES if it is possible to make the given string a palindrome by changing exactly 1 character. Else, it should return the string NO.



Example Input

Input 1:

 A = "abbba"
Input 2:

 A = "adaddb"


Example Output

Output 1:

 "YES"
Output 2:

 "NO"


Example Explanation

Explanation 1:

 We can change the character at index 3(1-based) to any other character. The string will be palindromic.
Explanation 2:

 To make the string palindromic we need to change 2 characters.'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        count = 0
        N = len(A)

        i, j = 0, N - 1

        while i < j:

            if A[i] != A[j]:
                count += 1
            
            if count > 1:
                return 'NO'
            
            i += 1
            j -= 1
        
        if (count == 0 and N&1) or count == 1:
            return 'YES'
        
        return 'NO'
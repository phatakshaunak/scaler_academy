'''Q1. Amazing Subarrays
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
Constraints

1 <= length(S) <= 1e6
S can have special characters
Example

Input
    ABEC

Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        count = 0
        N = len(A)
        
        for i in range(N):
            
            if A[i] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                
                count += (N - i)
        
        return count % 10003
                

'''Q2. Count Occurrences
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Find number of occurrences of bob in the string A consisting of lowercase english alphabets.



Problem Constraints

1 <= |A| <= 1000


Input Format

The first and only argument contains the string A consisting of lowercase english alphabets.


Output Format

Return an integer containing the answer.


Example Input

Input 1:

  "abobc"
Input 2:

  "bobob"


Example Output

Output 1:

  1
Output 2:

  2


Example Explanation

Explanation 1:

  The only occurrence is at second position.
Explanation 2:

  Bob occures at first and third position.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        if len(A) < 3:
            return 0
        
        s = ''
        count = 0
        
        for i in range(3):
            s += A[i]
    
        if s == 'bob':
            count += 1
        
        for j in range(3,len(A)):
            
            s = s[1:] + A[j]
            
            if s == 'bob':
                count += 1
        
        return count

'''Q4. Closest Palindrome
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

'''Q6. String operations
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:

Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.

NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.



Problem Constraints

1<=N<=100000


Input Format

First argument is a string A of size N.



Output Format

Return the resultant string.



Example Input

A="AbcaZeoB"



Example Output

"bc###bc###"



Example Explanation

First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
Delete all the uppercase letters so string A becomes "bcaeobcaeo".
Now replace vowel with '#'.
A becomes "bc###bc###".'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        
        # A = A + A
        
        B = ''
        
        vow = {'a','e','i','o','u'}
        
        for i in range(len(A)):
            
            if A[i] in vow:
                
                B += '#'
                
            elif A[i] == A[i].upper():
                continue
            
            else:
                B += A[i]
        
        B = B + B  
        
        return B

'''
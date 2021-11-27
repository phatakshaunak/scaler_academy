'''Q2. Reverse the String
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.


Problem Constraints

1 <= N <= 3 * 105



Input Format

The only argument given is string A.



Output Format

Return the string A after reversing the string word by word.



Example Input

Input 1:
    A = "the sky is blue"
Input 2:
    A = "this is ib"  


Example Output

Output 1:
    "blue is sky the"
Output 2:
    "ib is this"    


Example Explanation

Explanation 1:
    We reverse the string word by word so the string becomes "the sky is blue".
Explanation 2:
    We reverse the string word by word so the string becomes "this is ib".'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        #Main idea is to accumulate a word and concatenate when a space is encountered. 
        M = len(A)
        ans = ''
        temp = ''
        # Reverse iterate and add word if encountered
        for i in range(M-1, -1, -1):

            if A[i] == ' ':
                if temp:
                    # Case for the first word (or last word of the original string)
                    if ans == '':
                        ans = ans + temp
                        temp = ''
                    else:
                        ans = ans + ' ' + temp
                        temp = ''

            else:
                # Keeping character order in word intact and avoiding separate reverse operation
                temp = A[i] + temp
        
        if temp:
            # Case for last word (or first of the original string)
            ans = ans + ' ' + temp
        
        return ans

        # M = len(A)
        # temp = ''
        # ans = ''
        # t_l = []
        # for i in range(len(A)):
        #     # Create a temp string accumulating words and appending to a temp list when a space is encountered

        #     if A[i] != ' ':
        #         temp = temp + A[i]
        #     else:
        #         if temp:
        #             t_l.append(temp)
        #             temp = ''
        
        # if temp:
        #     t_l.append(temp)
        
        # # Iterate from the right and append to a final string
        # l = len(t_l)
        # j = l - 1
        # while j >= 0:
        #     # Need to add a space for all words except the first word
        #     if j != 0:
        #         ans = ans + t_l[j] + ' '
        #     else:
        #         ans = ans + t_l[j]
        #     j -= 1
        
        # return ans

    #     # Track start and end indices skipping trailing/leading spaces
    #     N = len(A)
    #     s, e = 0, N - 1
    #     while s < N:
    #         if A[s] != ' ':
    #             break
    #         s += 1
    #     while e >= 0:
    #         if A[e] != ' ':
    #             break
    #         e -= 1
        
    #     # Iterate and remove extra spaces and add to a temp list
    #     temp = []
    #     ct = 0
    #     for i in range(s, e+1):

    #         if A[i] == ' ':
    #             ct += 1
    #         else:
    #             if ct > 0:
    #                 # Spaces before the character
    #                 temp.append(' ')
    #                 temp.append(A[i])
    #             else:
    #                 temp.append(A[i])

    #             ct = 0

    #     # Reverse all characters.
    #     M = len(temp)
    #     self.rev(temp, 0, M - 1)

    #     # Reverse all words
    #     s = 0
    #     for idx in range(M):
    #         if temp[idx] == ' ':
    #             # Reached a space, reverse between s and idx
    #             self.rev(temp, s, idx - 1)
    #             s = idx + 1
                
    #     self.rev(temp, s, M - 1)
        
    #     return ''.join(temp)

    # def rev(self, ls, i, j):

    #     while i < j:
    #         ls[i], ls[j] = ls[j], ls[i]
    #         i += 1
    #         j -= 1
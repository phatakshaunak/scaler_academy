'''Q5. Longest Common Prefix
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Problem Constraints

0 <= sum of length of all strings <= 1000000



Input Format

The only argument given is an array of strings A.



Output Format

Return the longest common prefix of all strings in A.



Example Input

Input 1:

A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:

A = ["abab", "ab", "abcd"];


Example Output

Output 1:

"a"
Output 2:

"ab"


Example Explanation

Explanation 1:

Longest common prefix of all the strings is "a".
Explanation 2:

Longest common prefix of all the strings is "ab".'''

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):

        # The idea is to traverse each character of a string with minimum length
        # Then iterate over all elements of the array and check if the characters match
        # If they match, append to ans, else return current ans
        # TC: O(l*N) where l is length of minimum string, SC: O(1)
        # This idea is similar to iterating over bits of a number ; here we iterate over characters
        # of the shortest string

        if not A:
            return ''
        elif len(A) == 1:
            return A[0]

        min_len = len(A[0])
        min_idx = 0
        N = len(A)
        
        for i in range(N):
            if len(A[i]) < min_len:
                min_len = len(A[i])
                min_idx = i
        
        ans = ''
        for j in range(min_len):

            for idx in range(N):
                if A[idx][j] != A[min_idx][j]:
                    return ans
            ans = ans + A[min_idx][j]
        
        return ans

        # if len(A) == 1:
        #     return A[0]
        # ans = ''

        # for idx in range(1,2):

        #     min_len = min(len(A[idx]), len(A[idx-1]))

        #     for j in range(min_len):

        #         if A[idx][j] == A[idx-1][j]:
        #             ans = ans + A[idx][j]
        #         else:
        #             break

        # for i in range(2, len(A)):
        #     curr = ''
        #     min_len = min(len(A[i]), len(A[i-1]))

        #     for j in range(min_len):
        #         if A[i][j] == A[i-1][j]:
        #             curr = curr + A[i][j]
        #         else:
        #             break
        #     if len(curr) < len(ans):
        #         ans = curr

        # return ans

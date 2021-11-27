'''Q2. Is Dictionary?
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographicaly in this alien language else return 0.



Problem Constraints

1 <= N, length of each word <= 105

Sum of length of all words <= 2 * 106



Input Format

First argument is a string array A of size N.

Second argument is a string B of size 26 denoting the order.



Output Format

Return 1 if and only if the given words are sorted lexicographicaly in this alien language else return 0.



Example Input

Input 1:

 A = ["hello", "scaler", "interviewbit"]
 B = "adhbcfegskjlponmirqtxwuvzy"
Input 2:

 A = ["fine", "none", "no"]
 B = "qwertyuiopasdfghjklzxcvbnm"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 The order shown in string B is: h < s < i for the given words. So return 1.
Explanation 2:

 "none" should be present after "no". Return 0.'''

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        
        #Map alphabet order to a hash map
        
        order = {}
        val = 1
        
        for i in B:
            order[i] = val
            val += 1
        
        '''
        Lexical order compares words character by character and ensures that the earliest character as possible is greater or equal to that of the previous word ; i.e. words are correctly sorted lexicographically.
        Some examples:
        Assume normal alphabet order abc....xyz
        1. Word lengths are the same ; dog > cat (As d > c)
        2. Word lengths are unequal ; apple > app(Even if characters a, p, p match, the first word has more characters putting it in a higher order)
        '''
        # Next compare each string's characters.
        
        for j in range(1, len(A)):
            
            # Loop over the smaller word's length. 
            len_check = min(len(A[j-1]), len(A[j]))
            
            for k in range(len_check):
                
                # No need to compare if jth words character is greater than the j-1th word
                
                if order[A[j][k]] > order[A[j-1][k]]:
                    break
                # As jth words character is less than j-1th word, this breaks lexicographical order
                
                elif order[A[j][k]] < order[A[j-1][k]]:
                    
                    # print(A[j][k], A[j-1][k])
                    return 0
            
            # Handle case when the jth word is smaller and matches all it's characters with partial string of j-1 ; eg. jth element is 'no' and j-1th element is 'none'   
            if len(A[j][k]) < len(A[j-1][k]):
                return 0
                    
        
        return 1
            
'''Q1. Sorted Permutation Rank with Repeats
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A, find the rank of the string amongst its permutations sorted lexicographically. Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations. Look at the example for more details.

NOTE:

The answer might not fit in an integer, so return your answer % 1000003 where 1000003 is a prime number.
String A can consist of both lowercase and uppercase letters. Characters with lesser ascii value are considered smaller i.e. 'a' > 'Z'.


Problem Constraints

1 <= len(A) <= 1000000



Input Format

First argument is a string A.



Output Format

Return an integer denoting the rank.



Example Input

Input 1:

 A = "aba"
Input 2:

 A = "bca"


Example Output

Output 1:

 2
Output 2:

 4


Example Explanation

Explanation 1:

 The order permutations with letters 'a', 'a', and 'b' :
    aab
    aba 
    baa
 So, the rank is 2.
Explanation 2:

 The order permutations with letters 'a', 'b', and 'c' :
    abc
    acb 
    bac
    bca
    cab
    cba
 So, the rank is 4.'''

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        mod = 1000003
        rank = 0
        hm = {}
        N = len(A)
        
        for idx in range(N):
            
            # Find frequencies of all elements to the right including ith character
            if A[idx] not in hm:
                hm[A[idx]] = 1
            else:
                hm[A[idx]] += 1
        # Loop through string
        for i in range(N):
            less = 0

            for j in range(i, N):
                
                # Count elements smaller than ith character
                if A[j] < A[i]:
                    less += 1
            
            temp = (less % mod * self.fact_mod((N - i - 1), mod)) % mod
            
            fact = 1
            # Get product of factorials
            for val in hm:
                if hm[val] > 1:
                    fact = (fact % mod * self.fact_mod(hm[val], mod)) % mod
                    # fact = (fact % mod * self.bin_exp(self.fact_mod(hm[val], mod), mod - 2, mod)) % mod
            
            # Get modulo inverse of fact
            fact = self.bin_exp(fact, mod - 2, mod)
            
            # Multiply temp and fact and add to ans
            
            add_ = (temp % mod * fact % mod) % mod
            
            rank = (rank % mod + add_ % mod) % mod
            # print(hm)
            hm[A[i]] -= 1
            # # Clear map for next iteration
            # hm.clear()
            # print(hm)
        
        return rank + 1

    def fact_mod(self, num, p):
        ans = 1
        while num > 1:
            ans = (ans % p * num % p) % p
            num = num - 1
        
        return ans
    
    def bin_exp(self, a, pw, p):

        ans = 1

        while pw:

            if pw&1:
                ans = (ans % p * a % p) % p
                a = (a % p * a % p) % p
            
            else:
                a = (a % p * a % p) % p
            
            pw = pw // 2
        
        return ans % p
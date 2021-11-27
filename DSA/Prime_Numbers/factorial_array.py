'''Q1. Factorial Array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Groot has an array A of size N. Boring right? Groot thought so too, so he decided to construct another array B of the same size and defined elements of B as:

B[i] = factorial of A[i] for every i such that 1<= i <= N.

factorial of a number X denotes (1 x 2 x 3 x 4……(X-1) x (X)).
Now Groot is interested in the total number of non-empty subsequences of array B such that every element in the subsequence has the same non empty set of prime factors.

Since the number can be very large, return it modulo 109 + 7.

NOTE: A set is a data structure having only distinct elements. Eg : the set of prime factors of Y=12 will be {2,3} and not {2,2,3}



Problem Constraints

1 <= N <= 105
1 <= A[i] <= 106
Your code will run against a maximum of 5 test cases.



Input Format

Only argument is an integer array A of size N.



Output Format

Return an integer deonting the total number of non-empty subsequences of array B such that every element in the subsequence has the same set of prime factors modulo 109+7.



Example Input

Input 1:

 A = [2, 3, 2, 3]
Input 2:

 A = [2, 3, 4]


Example Output

Output 1:

 6
Output 2:

 4


Example Explanation

Explanation 1:

 Array B will be : [2, 6, 2, 6]
 The total possible subsequences are 6 : [2], [2], [2, 2], [6], [6], [6, 6].
Input 2:

 Array B will be : [2, 6, 24]
 The total possible subsequences are 4 : [2], [6], [24], [6, 24].'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        '''
        Create a prime count array counting primes between 2 to max(A)
        Modify A with A[i]'s count value from the prime count array
        Store frequencies in a hash map.
        Use the formula 2^m - 1 for all the repeats to calculate total subsequences.
        Prime count array: O(max(A)) ; hashing and calculating overall takes O(len(A)) time.
        Time: O(max(A)loglogmax(A)) # for sieve + O(max(A)) #to iterate array + O(NlogN) #for exponentiation
        So overall O(NlogN) time
        Space: O(N) space for the map
        
        0 1 2 3 4 5 6 7 8 9 10 11.....
        0 0 1 2 2 3 3 4 4 4  4 5......
        
        [2 3 4] -->prime counts [1 2 2]-->hash{1:1, 2:2}-->2^1-1 + 2^2-1 = 4
        [2 3 2 3] -->prime counts [1 2 1 2]-->hash{1:2,2:2}-->2^2-1 + 2^2-1 = 6
        '''
        def bin_exp(a,b,p):
            ans = 1
            while b >= 1:
                if b&1:
                    ans = ((ans % p) * (a % p)) % p
                    a = ((a % p) * (a % p)) % p
                    b = b // 2
                else:
                    a = ((a % p) * (a % p)) % p
                    b = b // 2
            
            return ans
            
        mx = max(A)
        sieve = [1]*(mx+1)
        sieve[0] = 0
        sieve[1] = 0
        
        i = 2
        
        while i*i <= mx:
            for j in range(i*i,mx+1,i):
                sieve[j] = 0
            i += 1
        
        for k in range(1, len(sieve)):
            sieve[k] = sieve[k] + sieve[k-1]
            
        for x in range(len(A)):
            A[x] = sieve[A[x]]
            
        hm = {}
        for num in A:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        ans = 0
        m = int(1e9+7)
        
        for val in hm:
            if val != 0: #frequency of 0 primes should not be used in the calculation
                ans = (ans % m + bin_exp(2, hm[val], m) % m - 1) % m
        
        return ans
        
        '''[2 3 4 5 6]
        [1 2 2 3 3]
        {1:1, 2:2, 3:2}
        2^1-1 + 2^2-1 + 2^2 - 1 = 1 + 3 + 3 = 7
        1 2 3 4
        0 1 2 2
        {0:1,1:1,2:2}
        2^1-1 + 2^1-1 + 2^2-1 = 2-1+2-1+4-1 = 5 
        '''
'''Q3. ALL GCD PAIR
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A of size N containing GCD of every possible pair of elements of another array.

Find and return the original numbers which are used to calculate the GCD array in any order. For example, if original numbers are {2, 8, 10} then the given array will be {2, 2, 2, 2, 8, 2, 2, 2, 10}.



Problem Constraints

1 <= N <= 10000

1 <= A[i] <= 109



Input Format

The first and only argument given is the integer array A.



Output Format

Find and return the original numbers which are used to calculate the GCD array in any order.



Example Input

Input 1:

 A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
Input 2:

 A = [5, 5, 5, 15]


Example Output

Output 1:

 [2, 8, 10]
Output 2:

 [5, 15]


Example Explanation

Explanation 1:

 Initially, array A = [2, 2, 2, 2, 8, 2, 2, 2, 10].
 2 is the gcd between 2 and 8, 2 and 10.
 8 and 10 are the gcds pair with itself.
 Therefore, [2, 8, 10] is the original array.
Explanation 2:

 Initially, array A = [5, 5, 5, 15].
 5 is the gcd between 5 and 15.
 15 is the gcds pair with itself.
 Therefore, [5, 15] is the original array.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        hm = {}
        n = len(A)
        l = self.sq_root(n)
        A.sort(reverse = True)
        ans = []
        
        for num in A:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        
        for i in range(n):

            if hm[A[i]] > 0:

                for j in range(len(ans)):

                    temp = self.gcd(A[i], ans[j])

                    hm[temp] -= 2 # gcd(a,b) and gcd(b, a)
            
            if hm[A[i]] > 0:
                ans.append(A[i])
                hm[A[i]] -= 1 # gcd(a,a)

            if len(ans) == l:
                return ans

        return ans
    
    #TC O(N√N), SC O(1)
    
    def sq_root(self, num):

        s, e = 1, num // 2

        while s <= e:

            mid = s + (e - s) // 2

            if mid * mid == num:
                return mid
            
            elif mid * mid > num:
                e = mid - 1
            
            else:
                s = mid + 1
        
        return mid

    def gcd(self, a, b):

        while a:
            a, b = b % a, a
        
        return b

        # if a > b:
        #     a = a % b
        # else:
        #     b = b % b

        # if a:
        #     return a

        # return b
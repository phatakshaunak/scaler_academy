'''Q3. Number of Squareful Arrays
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Find and return the number of permutations of A that are squareful. Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].



Problem Constraints

1 <= length of the array <= 12

1 <= A[i] <= 109



Input Format

The only argument given is the integer array A.



Output Format

Return the number of permutations of A that are squareful.



Example Input

Input 1:

 A = [2, 2, 2]
Input 2:

 A = [1, 17, 8]


Example Output

Output 1:

 1
Output 2:

 2


Example Explanation

Explanation 1:

 Only permutation is [2, 2, 2], the sum of adjacent element is 4 and 4 and both are perfect square.
Explanation 2:

 Permutation are [1, 8, 17] and [17, 8, 1].'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        hm = {}

        for val in A:
            if val not in hm:
                hm[val] = 1
            else:
                hm[val] += 1
        ans = [0]
        self.perm(A, hm, [], ans)

        return ans[0]

    def perm(self, A, hm, curr, ans):
    
    
        if len(curr) > 1:
            if not self.is_sq(curr[-1] + curr[-2]):
                return
            
            if len(curr) == len(A) and self.is_sq(curr[-1] + curr[-2]):
                ans[0] += 1
                return
        
        for num in hm:
            if hm[num] > 0:
                hm[num] -= 1
                curr.append(num)
                self.perm(A, hm, curr, ans)
                hm[num] += 1
                curr.pop()

    def is_sq(self, num):
        
        s, e = 0, num
        
        while s <= e:
            
            mid = s + (e - s) // 2
            
            if mid * mid == num:
                return True
            
            elif mid * mid < num:
                s = mid + 1
            
            else:
                e = mid - 1
        
        return False
'''Q1. Ways to form Max Heap
Attempted
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes.

Find the number of distinct Max Heap can be made from A distinct integers.

In short, you have to ensure the following properties for the max heap :

Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.)
Every node is greater than all its children.
NOTE: If you want to know more about Heaps, please visit this link. Return your answer modulo 109 + 7.



Problem Constraints

1 <= A <= 100



Input Format

First and only argument is an inetegr A.



Output Format

Return an integer denoting the number of distinct Max Heap.



Example Input

Input 1:

 A = 4
Input 2:

 A = 10


Example Output

Output 1:

 3
Output 2:

 3360


Example Explanation

Explanation 1:

 Let us take 1, 2, 3, 4 as our 4 distinct integers
 Following are the 3 possible max heaps from these 4 numbers :
      4           4                     4
    /  \         / \                   / \ 
   3    2   ,   2   3      and        3   1
  /            /                     /    
 1            1                     2
Explanation 2:

 Number of distinct heaps possible with 10 distinct integers = 3360.'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        m = int(1e9 + 7)
        memo = {}
        return self.main_helper(A, memo, m) % (int(1e9 + 7))

    def main_helper(self, N, memo, m):

        # Base condition for nodes <= 2, only one possible configuration possible
        if N <= 2:
            if N not in memo:
                memo[N] = 1
            return 1
        
        # Check if already computed, return from map
        if N in memo:
            return memo[N]
        
        # Main logic

        # Get the height
        H = self.log_2(N)

        # Calculate intermediate variable
        X = self.bin_exp(2, H, m) - 1

        # Calculate leaves in the left subtree
        L = (X - 1) // 2 + min(((X + 1) // 2), (N - X))

        # Calculate leaves in the right subtree
        R = N - 1 - L

        # Store answer for redundant calls
        memo[N] = self.ncr(N - 1, L, m) * self.main_helper(L, memo, m) * self.main_helper(R, memo, m)

        return memo[N]

    def bin_exp(self, num, p, m):

            ans = 1

            while p:
                if p&1:
                    ans = (ans % m * num % m) % m
                
                num = (num % m * num % m) % m

                p = p // 2

            return ans % m

    def ncr(self, n, r, m):

        num, den = 1, 1

        for i in range(r, 0, -1):
            num = (num % m * n % m) % m
            n -= 1
            den = (den % m * i % m) % m

        return (num % m * self.bin_exp(den, m - 2, m)) % m
    
    def log_2(self, num):
        ans = 0
        while num:
            num //= 2
            if num:
                ans += 1
        
        return ans
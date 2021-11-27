'''Q3. Largest Coprime Divisor
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given two positive numbers A and B . You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1


Problem Constraints

1 <= A, B <= 109



Input Format

First argument is an integer A.
Second argument is an integer B.



Output Format

Return an integer maximum value of X as descibed above.



Example Input

Input 1:

 A = 30
 B = 12
Input 2:

 A = 5
 B = 10


Example Output

Output 1:

 5
Output 2:

 1


Example Explanation

Explanation 1:

 All divisors of A are (1, 2, 3, 5, 6, 10, 15, 30). 
 The maximum value is 5 such that A%5 == 0 and gcd(5,12) = 1
Explanation 2:

 1 is the only value such that A%5 == 0 and gcd(1,10) = 1'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def cpFact(self, A, B):
	   
	   def gcd(a,b):
	       
	       while b:
	           a = a % b
	           a, b = b, a
	       return a
	   
       # Optimized (Remove common factor of A and B from A until they are coprime. i.e. just keep dividing by their GCD until it becomes 1)
	   while gcd(A,B) > 1:
	       A = A // gcd(A,B)
	   
	   return A
	   # Naive (Run 1 to N and check each)
	   # for num in range(A,-1,-1):
	        
	   #     if A % num == 0:
	   #         if gcd(num,B) == 1:
	   #             return num
	   # Naive 2 (Find factors of N in N^0.5 and then check ; N^0.5log(max(N^0.5,B))
'''Q4. Smallest sequence with given Primes
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given three prime number(A, B, C) and an integer D. Find the first(smallest) D integers which have only A, B, C or a combination of them as their prime factors.



Problem Constraints

1 <= A, B, C <= 10000

1 <= D <= 100000



Input Format

First argument is an integer A.
Second argument is an integer B.
Third argument is an integer C.
Fourth argument is an integer D.



Output Format

Return an integer array of size D, denoting the first D integers described above.

NOTE: The sequence should be sorted in ascending order



Example Input

Input 1:

 A = 2
 B = 3
 C = 5
 D = 5
Input 2:

 A = 3
 B = 2
 C = 7
 D = 3


Example Output

Output 1:

 [2, 3, 4, 5, 6]
Output 2:

 [2, 3, 4]


Example Explanation

Explanation 1:

 4 = A * A ( 2 * 2 ), 6 = A * B ( 2 * 3 )
Explanation 2:

 2 has only prime factor 2. Similary 3 has only prime factor 3. 4 = A * A ( 2 * 2 )'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @return a list of integers
	def solve(self, A, B, C, D):
	    
	    i, j, k = 0, 0, 0
	    ans = [0] * (D+1)
	    ans[0] = 1
	    
	    for z in range(1,(D+1)):
	        
	        num1, num2, num3 = A*ans[i], B*ans[j], C*ans[k]
	        
	        min_num = min(num1,num2,num3)
	        
	        ans[z] += min_num
	        
#All if conditions are run through each iteration to increment the pointer if we have any duplicates in num1, num2 and num3. Then we can simply move forward on the other duplicate pointer as well as the number has been entered in the array
	        if min_num == num1:
	            i += 1
	        
	        if min_num == num2:
	            j += 1
	        
	        if min_num == num3:
	            k += 1
	    
	    return ans[1:]
	    
    	'''Important to note that we should use three separate if conditions instead of using elif. Using elif would not consider 
    	   duplicates in the three numbers and not increment the pointers.
    	   
    	   Multiple pointers can be incremented in an iteration as you need consider D elements in the array. Thus if one position is filled and equals to some or all of num1, num2 and num3, we need to increment some or all three pointers to the next position.
    	''' 
	   
	   # count = 1
	   # i, j, k = 0, 0, 0
	   # ans = [1]
	    
	   # while count <= D:
	        
	   #     num1, num2, num3 = A*ans[i], B*ans[j], C*ans[k]
	        
	   #     min_num = min(num1, num2, num3)
	        
	   #     if min_num == num1:
	   #         if ans[-1] == min_num:
	   #             i += 1
	   #             continue
	        
	   #     elif min_num == num2:
	   #         if ans[-1] == min_num:
	   #             j += 1
	   #             continue
	        
	   #     else:
	   #         if ans[-1] == min_num:
	   #             k += 1
	   #             continue
	        
	   #     ans.append(min_num)
	   #     count += 1
	    
	   # return ans[1:]

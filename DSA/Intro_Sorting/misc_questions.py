'''
Q1. Sort by Color
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.



Problem Constraints

1 <= N <= 1000000
0 <= A[i] <= 2


Input Format

First and only argument of input contains an integer array A.


Output Format

Return an integer array in asked order


Example Input

Input 1 :
    A = [0 1 2 0 1 2]
Input 2:

    A = [0]


Example Output

Output 1:
    [0 0 1 1 2 2]
Output 2:

    [0]


Example Explanation

Explanation 1:
    [0 0 1 1 2 2] is the required order.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        
        n0, n1, n2 = 0, 0, 0
        
        for i in A:
            
            if i == 0:
                n0 += 1
            
            elif i == 1:
                n1 += 1
            
            else:
                n2 += 1
        
        for i in range(len(A)):
            
            if n0 > 0:
                A[i] = 0
                n0 -= 1
            
            elif n1 > 0:
                A[i] = 1
                n1 -= 1
                
            else:
                A[i] = 2
                
        return A

'''Q2. Kth Smallest Element
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in <= B swaps.



Problem Constraints

1 <= |A| <= 100000

1 <= B <= min(|A|, 500)

1 <= A[i] <= 109



Input Format

First argument is vector A.

Second argument is integer B.



Output Format

Return the Bth smallest element in given array.



Example Input

Input 1:

A = [2, 1, 4, 3, 2]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output

Output 1:

 2
Output 2:

 2


Example Explanation

Explanation 1:

 3rd element after sorting is 2.
Explanation 2:

 2nd element after sorting is 2.'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
	    
	   # if len(A) == 1:
	   #     return A[0]
	    A = list(A)
	    
	    A.sort()
	    
	    return A[B-1]

'''Q3. Noble Integer
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.



Input Format

First and only argument is an integer array A.



Output Format

Return 1 if any such integer p is found else return -1.



Example Input

Input 1:

 A = [3, 2, 1, 3]
Input 2:

 A = [1, 1, 3, 3]


Example Output

Output 1:

 1
Output 2:

 -1


Example Explanation

Explanation 1:

 For integer 2, there are 2 greater elements in the array. So, return 1.
Explanation 2:

 There is no such integer exists.'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    
	   A.sort()
	   N = len(A)
	    # Iterate until second last element to avoid error on the duplicate check
	    
	   for i in range(N-1):
	        
	        #Skip duplicates
	        if A[i] == A[i+1]:
	            continue
	        
	        if A[i] == (N - 1 - i):
	            return 1
	   
	   # Check final element
	   if A[N-1] == (N - 1) - (N - 1):
	       return 1
	   
	   return -1
	   
	   # A : [-3 -2 -1 0 0 0]

'''Q4. Arithmetic Progression?
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N. Return 1 if the array can be rearranged to form an arithmetic progression, otherwise, return 0.

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.



Problem Constraints

2 <= N <= 105

-109 <= A[i] <= 109



Input Format

First and only argument is an integer array A of size N.



Output Format

Return 1 if the array can be rearranged to form an arithmetic progression, otherwise, return 0



Example Input

Input 1:

 A = [3, 5, 1]
Input 2:

 A = [2, 4, 1]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Explanation 2:

 There is no way to reorder the elements to obtain an arithmetic progression.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        '''
        Sort the array, store the difference between first two elements in a variable, continue iterating to check if that difference holds
        for all elements, return 1 if true, 0 if false
        '''
        
        A.sort()
        
        offset = A[1] - A[0]
        
        for i in range(2,len(A)-1):
            
            if (A[i] - A[i-1]) != offset:
                return 0
        
        return 1

'''Q5. Stepwise Selection Sort!
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N.

You need to sort the elements in increasing order using SelectionSort. Return a array containing the min value's index position before every iteration.

NOTE:

Consider 0 based indexing while looking for min value in each step of selection sort.
There will be total N - 1 iterations in selection sort so the output array will contain N - 1 integers.


Problem Constraints

2 <= N <= 104

1 <= A[i] <= 106

All elements are distinct in array A.



Input Format

First and only argument is an integer array A.



Output Format

Return an integer array containing N - 1 integers denoting min value's index position before every iteration.



Example Input

Input 1:

 A = [6, 4, 3, 7, 2, 8]


Example Output

Output 1:

 [4, 2, 2, 4, 4]


Example Explanation

Explanation 1:

 Explanation : 6 4 3 7 2 8 : Index of 1st min - 4
 After 1st Iteration : 2 4 3 7 6 8 : Index of 2nd min - 2
 After 2nd Iteration : 2 3 4 7 6 8 : Index of 3rd min - 2
 After 3rd Iteration : 2 3 4 7 6 8 : Index of 4th min - 4
 After 4th iteration : 2 3 4 6 7 8 : Index of 5th min - 4
 After 5th iteration. : 2 3 4 6 7 8.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        min_arr = []
        for i in range(len(A)):
            min_ind = i
            
            for j in range(i+1, len(A)):
                
                if A[j] < A[min_ind]:
                    min_ind = j
            
            min_arr.append(min_ind)
            A[i], A[min_ind] = A[min_ind], A[i]
        
        return min_arr[:len(A)-1]

# time O(n^2), space O(1) for insertion sort
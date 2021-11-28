'''Q3. Allocate Books
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A of size N and an integer B.

College library has N books,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.



NOTE: Return -1 if a valid assignment is not possible.



Problem Constraints

1 <= N <= 105
1 <= A[i], B <= 105



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return that minimum possible number



Example Input

A = [12, 34, 67, 90]
B = 2


Example Output

113


Example Explanation

There are 2 number of students. Books can be distributed in following fashion : 
        1) [12] and [34, 67, 90]
        Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
        2) [12, 34] and [67, 90]
        Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
        3) [12, 34, 67] and [90]
        Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
        Of the 3 cases, Option 3 has the minimum pages = 113.'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
	    
	    s, e = max(A), sum(A) # O(N)
	    '''Minimum possible value would be the maximum of array A when there are K students and K books, then minimum possible maximum allotment would be simply the maximum of the array. 
	       The maximum possible value would be when there is one student and K books. We can then assign sum of all the pages to that student.'''
	    ans = -1
	   # Edge case when more students than books in the array as each student needs at least 1 book
	    if B > len(A):
	        return ans
	        
	    while s <= e:
	        
	        mid = s + (e - s) // 2
	       # students = self.isvalid(A, B, mid)
	        
	        if self.isvalid(A, B, mid):
	            
	            '''The <= B condition in the isvalid function handles two possibilities ; In case we finish all books with <= mid pages between k students, then B-k would have zero pages. We can simply redistribute so that everyone has a book.
	               Both these cases are considered valid possibilities for our mid value to be an answer. mid can be considered as the at most minimum maximum value possible.
	               https://www.scaler.com/help_requests/46589/?source=auto_suggestions
	            '''
	            ans = mid   
	            e = mid - 1 # Move left to find a lower maximum
	        
	        else:
	            s = mid + 1 # Move right to find a higher value as all books may not have been alloted with the current mid
	   
	    return ans 
	
    def isvalid(self, A, B, m):
        
        curr, _sum = 0, 0
        
        for i in range(len(A)):
            
            _sum += A[i]
            if _sum > m:
                curr += 1
                _sum = A[i]
        
        return (curr + 1) <= B
        
    # TC O [len(A) * log(sum(A) - max(A))], SC O(1)

    

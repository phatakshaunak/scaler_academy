'''Find longest palindromic substrings for all prefixes in a string
https://stackoverflow.com/questions/63532882/finding-the-lengths-of-the-longest-palindromic-substrings-for-all-prefixes-of-a
Ex. Given 'ababa'
Output 1 1 3 3 5
'a' : 'a' (1)
'ab: 'a' or 'b' (1)
'aba': 'aba' (3)
'abab': 'aba' or 'bab' (3)
'ababa': 'ababa' (5)

Below solution runs O(N^3) time, O(N^2) space
Need to find a better approach potentially O(N^2) and reduced space
https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/?ref=rp 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        i, j = self.tabular(s)
        
        return s[i:j + 1] 
    
    def tabular(self, s):
        
        n = len(s)
        
        dp = [[0 for i in range(n)] for j in range(n)]
        
        ans1 = [float('-inf') for i in range(n)]
        
        ans = 1
        
        lft, rt = -1, -1
        
        for l in range(1, n + 1):
            
            for st in range(n - l + 1):
                
                e = l + st - 1
                
                if st == e:
                    dp[st][e] = 1
                
                elif e - st + 1 == 2:
                    
                    if s[st] == s[e]:
                        dp[st][e] = 1
                
                else:
                    
                    if s[st] == s[e] and dp[st + 1][e - 1]:
                        dp[st][e] = 1
                
                if dp[st][e] == 1:
                    
                    for r in range(n):
                        
                        if st >= 0 and e <= r:
                            
                            ans1[r] = max(ans1[r], e - st + 1)
                    
                    if l >= ans:
                        lft, rt = st, e
        
        print(ans1)
        return lft, rt
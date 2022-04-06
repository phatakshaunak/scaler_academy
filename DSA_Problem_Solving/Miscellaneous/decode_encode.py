def decode_string(st):
    
    st = list(st)
    
    curr = ''
    ans = ''
    for char in st:
        
        if curr == '' or curr[-1] == char:
            curr = curr + char
        
        else:
            freq = len(curr)
            offset = (ord(curr[-1]) - ord('A') + freq) % 26
            new_char = chr(ord('A') + offset)
            ans += new_char
            if freq > 1:
                ans += str(freq)
            
            curr = char
    
    if curr:
        freq = len(curr)
        offset = (ord(curr[-1]) - ord('A') + freq) % 26
        new_char = chr(ord('A') + offset)
        ans += new_char
        if freq > 1:
            ans += str(freq)
        
    return ans

'''
Count frequency of continuous characters and offset forward by their frequency. If count > 1, add the count to the 
final answer
'''

S = 'WIIINGGIFY'
decode_string(S)
'O/P: XL3OI2JGZ'
def insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        
        j = i - 1
        
        while j >= 0:
            
            if A[j + 1] < A[j]:
                A[j + 1], A[j] = A[j], A[j + 1]
        
            j -= 1
        
        print(arr)
        print()
        
def selection_sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        
        min_idx = i
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:

            arr[min_idx], arr[i] = arr[i], arr[min_idx]
            
def bubble_sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        
        for j in range(n - i - 1):
            
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
arr = [ 0, 1, 3 , 2 , 6 , 9 , 4]

def merge(arr , l , m , r):
    n1 = m + 1 - l
    n2 = r - m
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[l + i]
    
    for j in range(n2):
        R[j] = arr[m + j + 1]
    
    i , j , k = 0 , 0 , l
    
    while i <  n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j+=1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1 
        k += 1
   
  
def merge_sort(arr , l , r):
    if l < r :
        m = (l + (r-1)) // 2
        merge_sort(arr , l , m )
        merge_sort(arr , m + 1 , r)
        merge(arr , l , m , r)

merge_sort(arr , 0 , len(arr) - 1 )

print(arr)
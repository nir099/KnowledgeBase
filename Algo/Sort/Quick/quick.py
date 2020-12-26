arr = [ 0, 1, 3 , 2 , 6 , 9 , 4]

def part(arr , l , h):
    i = l - 1 
    pivot = arr[h]
    
    for j in range(l , h):
        if(arr[j] <=  pivot):
            i+=1
            arr[i] , arr[j] = arr[j] , arr[i]
    
    arr[i+1] , arr[h] = arr[h],arr[i+1]
    return (i+1)
   
   
def quick(arr , l , h):
    if len(arr) < 2:
        return
    if( l < h ):
        pi = part(arr , l , h)
        quick(arr , l , pi - 1)
        quick(arr , pi + 1 , h)
    return arr

print(quick(arr))

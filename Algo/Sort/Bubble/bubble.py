arr = [ 0, 1, 3 , 2 , 6 , 9 , 4]

def buble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(buble(arr))
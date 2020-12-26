arr = [ 0, 1, 3 , 2 , 6 , 9 , 4]

def selection(arr):
    for i in range(len(arr)):
        min_idx = arr[i]
        for j in range(i , len(arr)):
            if (arr[i] > arr[j]):
                min_idx = j
        arr[i], arr[min_idx-1] = arr[min_idx-1],arr[i]
    return arr

print(selection(arr))
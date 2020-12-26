def minMax(arr):
    min = arr[0]
    max = arr[0]
    for i in arr:
        if( i > max):
            max = i
        if( i < min):
            min = i
    return min, max

arr = [1 , 3 , 7 , 8 , 12 , 13 , 17 , 20 , 24]
print(minMax(arr))
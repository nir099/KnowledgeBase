def secondMax(arr):
    max1,max2 = 0 , 0
    if( arr[0] > arr[1]):
        max1 = arr[0]
        max2 = arr[1]
    else:
        max1 = arr[1]
        max2 = arr[0]
    for i in arr:
        if(i > max1):
            max2 =  max1
            max1 = i
        elif( i > max2 and max1 != i):
            max2 = i
    return max2  

arr = [ 1 , 3 ,5 , 2 , 10 , 9 , 22 , 15 , 8]

print(secondMax(arr))
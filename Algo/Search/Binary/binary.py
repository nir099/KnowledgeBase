def binary(arr , elem):
    m = len(arr) // 2
    if( len(arr) == 1 and arr[m] != elem):
        return False
    elif (arr[m] < elem):
        return binary(arr[m:] , elem)
    elif (arr[m] > elem):
        return binary(arr[:m] , elem)
    elif(arr[m] == elem):
        return True

arr = [ 1 , 3 , 7 , 8 , 12 , 13 , 17 , 20 , 24]

print(binary(arr, 5))
print(binary(arr, 8))
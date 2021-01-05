
arr = [1,4,6,8,4,3,2,9]

i = 0
j = len(arr) - 1

while(i < j):
    if(arr[i] % 2 == 1 and arr[j] % 2 == 1):
        arr[i] , arr[j] = arr[j] , arr[i]
        i += 1
        j -= 1
    elif(arr[i] % 2 == 0):
        i += 1
    elif(arr[j] % 2 == 0):
        j -= 1
    else:
        i += 1
        j -= 1

print(arr)
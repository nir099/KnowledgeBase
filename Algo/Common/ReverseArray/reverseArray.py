arr = [1,4,6,8,4,3,2,9]

# i and j are the pointers and i is pointing to the start of the array and j is pointing the end of the array
i = 0
j = len(arr) - 1

# in python you dont need temp variable to do the swap ( python is awsome ^.^)
while(i < j):
    arr[i] , arr[j] = arr[j] , arr[i]
    i += 1
    j -= 1

print(arr)
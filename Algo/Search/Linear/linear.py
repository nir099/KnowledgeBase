def search(arr , k ):
    for i in arr:
        if( i == k ):
            return True
    return False


arr = [ 1 , 3 , 7 , 8 , 12 , 13 , 17 , 20 , 24]

print(search(arr, 5))
print(search(arr, 8))
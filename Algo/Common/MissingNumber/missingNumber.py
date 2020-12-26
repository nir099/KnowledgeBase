def missingNumber(arr):
    n = len(arr) + 1
    sumOfarray = sum(arr)
    sumOf_N_numbers = (n * (n + 1))//2
    missingOne = sumOf_N_numbers - sumOfarray
    return missingOne

arr = [1,2,3,5,6]
print(missingNumber(arr))

arr = [1,1,2,3,4,5,6,7,8,8,9,10]
sum = 15

i = 0
j = len(arr) - 1
total = 0

while(i < j):
    total = arr[i] + arr[j]
    if(total == sum):
        print(arr[i],arr[j])
        i += 1
        j -+ 1
    elif(total < sum):
        i += 1
    else:
        j -= 1

import math
import os
import random
import re
import sys

class LinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = LinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_linked_list(node):
    while node:
        print(str(node.data), end = ' -> ')
        node = node.next


arr = [ 0, 1, 3 , 2 , 6 , 9 , 4]


#bubble
def buble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


#insertion 
def inser(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
      
  
#selection  
def select(arr):
    for i in range(len(arr)):
        min_idx = arr[i]
        for j in range(i , len(arr)):
            if (arr[i] > arr[j]):
                min_idx = j
        arr[i], arr[min_idx-1] = arr[min_idx-1],arr[i]
    return arr
   

# mereg / merge two arrays 
def merge(arr , l , m , r):
    n1 = m + 1 - l
    n2 = r - m
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[l + i]
    
    for j in range(n2):
        R[j] = arr[m + j + 1]
    
    i , j , k = 0 , 0 , l
    
    while i <  n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j+=1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1 
        k += 1
   
# merge     
def merge_sort(arr , l , r):
    if l < r :
        m = (l + (r-1)) // 2
        merge_sort(arr , l , m )
        merge_sort(arr , m + 1 , r)
        merge(arr , l , m , r)
#merge_sort(arr , 0 , len(arr) - 1 )


# quick sort partition
def part(arr , l , h):
    i = l - 1 
    pivot = arr[h]
    
    for j in range(l , h):
        if(arr[j] <=  pivot):
            i+=1
            arr[i] , arr[j] = arr[j] , arr[i]
    
    arr[i+1] , arr[h] = arr[h],arr[i+1]
    return (i+1)
   
   
# quick 
def quick(arr , l , h):
    if len(arr) < 2:
        return
    if( l < h ):
        pi = part(arr , l , h)
        quick(arr , l , pi - 1)
        quick(arr , pi + 1 , h)
    return arr


# linear search
def search(arr , k ):
    for i in arr:
        if( i == k ):
            return True
    return False


# binary search
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

#fibanochi
def fib(n):
    if ( n == 0):
        return 0
    elif( n == 1 or n == 2 ):
        return 1
    else:
        return fib(n-1) + fib(n-2)


#linked list reverse 
# 1 - 2 - 3 - 4 - 5 - None
# None - 5 - 4 - 3 - 2 - 1
# def reverse(head):
#     current = head
#     prev = None
#     while current is not None:
#         nextNode = current.next
#         current.next = prev
#         prev = current
#         current = nextNode
#     head = prev
#     return head
     
# linked list reverse with middle node
# 1 - 2 - 3 - 4 - 5 - None
# None - 5 - 4 - 3 - 2 - 1
def reverse(head):
    current = head
    Next = current.next
    prev = None
    while True: 
        current.next = prev
        if Next == None:
            break
        prev = current
        current = Next
        Next = Next.next
    head = current
    return head

llist = LinkedList()
arrLinkList = [1, 2, 3, 4, 5]
for i in arrLinkList:
    llist_item = i
    llist.insert_node(llist_item)

llist1 = reverse(llist.head)

print('before reverse the linked list : ', arrLinkList)
print('linked list reversed : ', end = ' ')
print_linked_list(llist1)
print()

# second max
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


#reverse string
def revStr(str):
    newStr = ''
    for i in range(len(str)):
        newStr += str[len(str) - 1 - i]
    return newStr


#palindrome
def palindrome(str):
    for i in range(len(str)//2):
        if not str[i] == str[len(str)-1 - i]:
            return False
    return True


# min max
def minMax(arr):
    min = arr[0]
    max = arr[0]
    for i in arr:
        if( i > max):
            max = i
        if( i < min):
            min = i
    return min, max


# missing no of a array
def missingNumber(arr):
    n = len(arr) + 1
    sumOfarray = sum(arr)
    sumOf_N_numbers = (n * (n + 1))//2
    missingOne = sumOf_N_numbers - sumOfarray
    return missingOne


print('unsorted array : ' , arr)
arr = quick(arr, 0 , len(arr) - 1)
print('quick sorted array : ', arr)
print('fibanocci : ', fib(9))
print('second max of an array : ', secondMax(arr))
print('binary serch check : ', binary(arr , 10))
print('palindrome check : ', palindrome('abcba'))
print('reverse a string : ', revStr('abcd efgh'))
print('min max of a array : ',minMax(arr))
print('serch missing no of a array : ', missingNumber([1,2,4,5,6]))
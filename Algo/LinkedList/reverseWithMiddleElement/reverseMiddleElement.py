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
        print(str(node.data))
        node = node.next

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
        

if __name__ == '__main__':

    llist = LinkedList()
    arr = [1, 2, 3, 4, 5]
    for i in arr:
        llist_item = i
        llist.insert_node(llist_item)

    llist1 = reverse(llist.head)

    print_linked_list(llist1)
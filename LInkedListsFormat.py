class LinkedList:
  def __init__(self):
    self.head = None

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
"""
list1 = LinkedList()
list1.head = Node('A')
list1.head.next = Node('B')
...
"""

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d


def ReverseLL(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  head = prev

ReverseLL(a)

def printLL(head):
  while head != None:
    print(head.data)
    head = head.next
printLL(d)

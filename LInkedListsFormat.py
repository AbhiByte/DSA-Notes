class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

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

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

def LLTraversal(head):
  current = head
  while current != None:
    print(current.data)
    current = current.next

def LLRecursiveTraversal(head):
  if head == None:
    return
  print(head.data)
  LLRecursiveTraversal(head.next)

LLTraversal(a)
print('')
LLRecursiveTraversal(a)

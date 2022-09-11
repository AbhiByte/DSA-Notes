#Lesson 1: Binary Search and Complexity

import math


"""Problem 1: Find a given number (card) by searching as few cards as possible.
We will use Binary Search"""

"""Binary Search Steps:
   1. Search middle for query
   2. If not found, divide list to left or right based on query and mid relationship
   3. Repeat until found/not found
   Remarks: Works for sorted lists only"""

#My solution
def find_cards(cards, query):
  #Indices, not values
  low = 0
  high = len(cards) - 1
  mid = int((low+high)/2)

  while True:
    if cards[mid] == query:
      return mid
    else:
      if cards[mid] < query:
        high = mid
        mid = int((low+high)/2)
      else:
        low = mid
        mid = int((low+high)/2)
    if low == high:
      return -1


#Course solution
def binary_search(lo, hi, condition):
    
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1




cards = [9, 7, 6, 4, 2, 1.1, 0.5]
query = 6
print(find_cards(cards, query))




             






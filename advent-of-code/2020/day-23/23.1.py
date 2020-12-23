class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

def play(current, largest, smallest):
  pickedUp = current.next
  pickedVals = [pickedUp.data, pickedUp.next.data, pickedUp.next.next.data]
  current.next = pickedUp.next.next.next
  destination = current.data - 1 if current.data > smallest else largest
  while destination in pickedVals:
      destination = destination - 1 if destination > smallest else largest

  node = current.next
  while node.data != destination:
    node = node.next
  pickedUp.next.next.next = node.next
  node.next = pickedUp

  return current.next

def print_cups(head):
  firstVal = head.data
  next = head.next
  vals = []
  while next.data != firstVal:
    vals.append(str(next.data))
    next = next.next
  print("".join(vals))

with open("input.txt", 'r') as f:
  input = [x.rstrip() for x in f.readlines()][0]
  cups = [int(c) for c in input]
  largest, smallest = max(cups), min(cups)
  
  current = None
  for i, cup in enumerate(reversed(cups)):      
    current = Node(cup, current)
    if i == 0:
      first = current
  first.next = current

  for i in range(100):
    current = play(current, largest, smallest)
  
  val = -1
  while val != 1:
    current = current.next
    val = current.data

  print_cups(current)
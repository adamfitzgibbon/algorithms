class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

def play(current, largest, smallest, map):
  pickedUp = current.next
  pickedVals = [pickedUp.data, pickedUp.next.data, pickedUp.next.next.data]
  current.next = pickedUp.next.next.next
  destination = current.data - 1 if current.data > smallest else largest
  while destination in pickedVals:
      destination = destination - 1 if destination > smallest else largest

  node = map[destination]
  pickedUp.next.next.next = node.next
  node.next = pickedUp

  return current.next

with open("input.txt", 'r') as f:
  input = [x.rstrip() for x in f.readlines()][0]
  cups = [int(c) for c in input]
  largest, smallest = max(cups), min(cups)
  cups += list(range(largest+1, 1000001))
  largest = 1000000
  map = {}
  current = None
  for i, cup in enumerate(reversed(cups)):      
    current = Node(cup, current)
    map[cup] = current
    if i == 0:
      first = current
  first.next = current

  for i in range(10000000):
    current = play(current, largest, smallest, map)
  
  oneNode = map[1]

  print(oneNode.next.data * oneNode.next.next.data)
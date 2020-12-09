import re 

class Bag():
  #bags = [] NANI
  def __init__(self, color):
    self.color = color
    self.bags = []

test = "light red bags contain 1 bright white bag, 2 muted yellow bags."

# print(re.findall("\S+ \S+ bags", test))

def find_bag(color, bag):
  if bag is None:
    return False
  if bag.color == color:
    return True
  for innerBag in bag.bags:
    if find_bag(color, innerBag):
      return True
  return False

def get_or_create_bag(bags, color):
  if color in bags:
    return bags[color]
  else:
    newBag = Bag(color)
    bags[color] = newBag
    return newBag

def assemble_bag(bags, color, innerColors):
  newBag = get_or_create_bag(bags, color)
  for innerColor in innerColors:
    newBag.bags.append(get_or_create_bag(bags, innerColor))

def print_bags(bags):
  for bag in bags.values():
    print(bag.color)
    for innerBags in bag.bags: 
      print(f"\t{innerBags.color}")

def count_bags(bags):
  counter = 0
  for bag in bags.values():
    if find_bag("shiny gold", bag):
      counter += 1

  print(counter-1)

with open("input.txt", 'r') as f:
  bags = {}
  for line in f:
    matches = re.findall("\S+ \S+ bag", line)
    matches = [x[:-4] for x in matches]
    newColor = matches[0]
    innerColors = matches[1:]
    assemble_bag(bags, newColor, innerColors)
  # print_bags(bags)
  
  count_bags(bags)
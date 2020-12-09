import re 

class Bag():
  #bags = [] NANI
  def __init__(self, color):
    self.color = color
    self.bags = []

test = "light red bags contain 1 bright white bag, 2 muted yellow bags."

# print(re.findall("\S+ \S+ bags", test))

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
    if str.isdigit(innerColor[0]):
      newBag.bags.append((int(innerColor[0]), get_or_create_bag(bags, innerColor[2:])))

def print_bags(bags):
  for bag in bags.values():
    print(bag.color)
    for innerBags in bag.bags: 
      print(f"\t{innerBags[1].color}: {innerBags[0]}")

def count_inner_bags(bag):
  if len(bag.bags) == 0:
    return 0
  sum = 0
  for innerBag in bag.bags:
    sum += innerBag[0]
    sum += innerBag[0] * count_inner_bags(innerBag[1])
  return sum

with open("input.txt", 'r') as f:
  bags = {}
  for line in f:
    matches = re.findall("[1-9]?[ ]?\S+ \S+ bag", line)
    matches = [x[:-4] for x in matches]
    newColor = matches[0]
    innerColors = matches[1:]
    assemble_bag(bags, newColor, innerColors)
  # print_bags(bags)
  
  print(count_inner_bags(bags["shiny gold"]))
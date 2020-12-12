class Direction():
  def __init__(self, name, left=None, right=None):
    self.name = name
    self.left = left
    self.right = right

north = Direction("N")
east = Direction("E", north)
south = Direction("S", east)
west = Direction("W", south)
north.left = west
north.right = east
east.right = south
south.right = west
west.right = north

directions = { 
  "N": north, 
  "E": east, 
  "S": south,
  "W": west
}

def rotate(currentDirection, turnTo, degrees):
  while degrees > 0:
    if turnTo == "L":
      currentDirection = currentDirection.left
    else:
      currentDirection = currentDirection.right
    degrees -= 90
  return currentDirection

def move(direction, magnitude, coords):
  if direction == "N":
    coords[1] += magnitude
  if direction == "S":
    coords[1] -= magnitude
  if direction == "E":
    coords[0] += magnitude
  if direction == "W":
    coords[0] -= magnitude

with open("input.txt", 'r') as f:
  coords = [0,0]
  currentDirection = east
  lines = [x.rstrip() for x in f.readlines()]
  for line in lines:
    action = line[0]
    val = int(line[1:])

    if action == "L" or action == "R":
      currentDirection = rotate(currentDirection, action, val)
    if action == "F":
      move(currentDirection.name, val, coords)
    else:
      move(action, val, coords)
    
  print(sum(map(lambda x: abs(x), coords)))
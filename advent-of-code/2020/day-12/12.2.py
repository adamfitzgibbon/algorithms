def rotate(coords, waypointCoords, turnTo, degrees):
  while degrees > 0:
    diff = [waypointCoords[0] - coords[0], waypointCoords[1] - coords[1]]
    if turnTo == "L":
      temp = [-diff[1], diff[0]]
      waypointCoords[0] = coords[0] + temp[0]
      waypointCoords[1] = coords[1] + temp[1]
    else:
      temp = [diff[1], -diff[0]]
      waypointCoords[0] = coords[0] + temp[0]
      waypointCoords[1] = coords[1] + temp[1]
    degrees -= 90

def move_waypoint(direction, magnitude, waypointCoords):
  if direction == "N":
    waypointCoords[1] += magnitude
  if direction == "S":
    waypointCoords[1] -= magnitude
  if direction == "E":
    waypointCoords[0] += magnitude
  if direction == "W":
    waypointCoords[0] -= magnitude

def move_to_waypoint(coords, waypointCoords, times):
  diff = [waypointCoords[0] - coords[0], waypointCoords[1] - coords[1]]
  coords[0] = coords[0] + diff[0] * times
  coords[1] = coords[1] + diff[1] * times
  waypointCoords[0] = coords[0] + diff[0]
  waypointCoords[1] = coords[1] + diff[1]

with open("input.txt", 'r') as f:
  coords = [0,0]
  waypointCoords = [10,1]
  lines = [x.rstrip() for x in f.readlines()]
  for line in lines:
    action = line[0]
    val = int(line[1:])

    if action == "L" or action == "R":
      rotate(coords, waypointCoords, action, val)
    elif action == "F":
      move_to_waypoint(coords, waypointCoords, val)
    else:
      move_waypoint(action, val, waypointCoords)
    
  print(sum(map(lambda x: abs(x), coords)))
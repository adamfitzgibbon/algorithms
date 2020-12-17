minRanges = 7
maxRanges = 15
cubes = {(x,y,z): False for x in range(-minRanges,maxRanges) for y in range(-minRanges, maxRanges) for z in range(-minRanges, maxRanges)}

def cycle():
  global cubes
  cubesToUpdate = {}
  for coords, val in cubes.items():
    x,y,z = coords
    activeNeighbors = 0
    for dx in range(-1,2):
      for dy in range(-1,2):
        for dz in range(-1,2):
          if dx == 0 and dy == 0 and dz == 0:
            continue
          if (x+dx, y+dy, z+dz) in cubes and cubes[x+dx, y+dy, z+dz]:
            activeNeighbors += 1
    cubesToUpdate[x,y,z] = (val and (activeNeighbors in (2,3))) or ((not val) and activeNeighbors == 3) 
  cubes = cubesToUpdate

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  for y, line in enumerate(lines):
    for x, val in enumerate(line):
      cubes[x,y,0] = val == "#"

  for i in range(6):
    cycle()
  
  activeCubes = 0
  for cube in cubes.values():
    if cube:
      activeCubes += 1
  
  print(activeCubes)
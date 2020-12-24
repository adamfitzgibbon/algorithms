"""in case anyone happens upon this and gets the wrong idea, the variable names in this problem are referring to black and white tiles"""

rangeVal = 200
tiles = {(x,y): False for x in range(-rangeVal,rangeVal) for y in range(-rangeVal,rangeVal)}

def flip():
  turnBlack = []
  turnWhite = []
  for coords, tile in tiles.items():
    blackNeighbors = 0
    x,y = coords
    neighbors = [(x-2,y), (x+2,y), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]
    for neighbor in neighbors:
      if not neighbor in tiles:
        continue
      if tiles[neighbor]:
        blackNeighbors += 1
    if tile and (blackNeighbors == 0 or blackNeighbors > 2):
      turnWhite.append(coords)
    if not tile and blackNeighbors == 2:
      turnBlack.append(coords)
  for coord in turnWhite:
    tiles[coord] = False
  for coord in turnBlack:
    tiles[coord] = True

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  commands = []
  for line in lines:
    command = []
    stash = None
    for c in line:
      if stash:
        command.append(stash + c)
        stash = None
      elif c not in ("n", "s"):
        command.append(c)
      else:
        stash = c
    commands.append(command)
  
  for command in commands:
    x,y = 0,0
    for c in command:
      if c == "e":
        x += 2
      if c == "se":
        x += 1
        y -= 1
      if c == "sw":
        x -= 1
        y -= 1
      if c == "w":
        x -= 2
      if c == "nw":
        x -= 1
        y += 1
      if c == "ne":
        x += 1
        y += 1
      
    if (x,y) in tiles:
      tiles[x,y] = not tiles[x,y]
    else:
      tiles[x,y] = True

  for i in range(100):
    flip()

  print(sum(tiles.values()))
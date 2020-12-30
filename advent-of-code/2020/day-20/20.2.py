tiles = {}
test = [[None for x in range(12)] for y in range(12)]
class Tile:
  def __init__(self, id, tile, removeBorders=True):
    self.id = id
    self.tile = [[c for i,c in enumerate(line) if i != 0 and i != len(line)-1] for j, line in enumerate(tile) if j!=0 and j!=len(tile)-1] \
      if removeBorders else tile
    self.left = None
    self.right = None
    self.top = None
    self.bottom = None
    self.border = { "L": [], "T": [], "R": [], "B": []}
    for j, row in enumerate(tile):
      for i, val in enumerate(row):
        if j == 0:
          self.border["T"].append(val)
        if j == len(tile) - 1:
          self.border["B"].append(val)
        if i == 0:
          self.border["L"].append(val)
        if i == len(tile[0]) - 1:
          self.border["R"].append(val)
  
  def __str__(self):
    return self.to_string(self.tile)
  
  def to_string(self, tile):
    s = f"Tile ID: {self.id}\n"
    return s + "\n".join(["".join(line) for line in tile]) + "\n"

  def check_border_by_label(self, label):
    if label == "L":
      return bool(self.left)
    elif label == "R":
      return bool(self.right)
    elif label == "T":
      return bool(self.top)
    elif label == "B":
      return bool(self.bottom)
    raise Exception("Unrecognized label!")

  def set_neighbor_by_label(self, label, otherId):
    if label == "L":
      self.left = otherId
    elif label == "R":
      self.right = otherId
    elif label == "T":
      self.top = otherId
    elif label == "B":
      self.bottom = otherId
    else:
      raise Exception("Unrecognized label!")
  
  def check_opposites(self, label1, otherTile):
    if label1 == "L":
      return otherTile.right == self.id
    elif label1 == "R":
      return otherTile.left == self.id
    elif label1 == "T":
      return otherTile.bottom == self.id
    elif label1 == "B":
      return otherTile.top == self.id
    else:
      raise Exception("Unrecognized label!")
  
  def get_opposite(self, label):
    if label == "L":
      return "R"
    elif label == "R":
      return "L"
    elif label == "T":
      return "B"
    elif label == "B":
      return "T"
    else:
      raise Exception("Unrecognized label!")

  def get_paired_sides(self):
    return sum([bool(self.left), bool(self.right), bool(self.top), bool(self.bottom)])

  def match_border(self, otherTile):
    for label, border in self.border.items():
      if self.check_border_by_label(label):
        continue
      for otherLabel, otherBorder in otherTile.border.items():
        if otherTile.check_border_by_label(otherLabel):
          continue
        if border == otherBorder or list(reversed(border)) == otherBorder:
          self.set_neighbor_by_label(label, otherTile.id)
          otherTile.set_neighbor_by_label(otherLabel, self.id)

  def arrange_other(self, otherTile, matchedSide):
    border = self.border[matchedSide]
    for otherBorder in otherTile.border.values():
      if border == otherBorder or list(reversed(border)) == otherBorder:
        self.rotate_other_until_mirrored(otherTile, matchedSide)
        otherLabel = self.get_opposite(matchedSide)
        if border != otherTile.border[otherLabel]:
          if otherLabel in ["R", "L"]: # flip based on side to reverse order
            otherTile.flip_vertical()
          else:
            otherTile.flip_horizontal()
        break

  def rotate_other_until_mirrored(self, otherTile, borderToMirror):
    while not self.check_opposites(borderToMirror, otherTile):
      otherTile.rotate()

  def rotate(self):
    tempL, tempR, tempT, tempB = self.left, self.right, self.top, self.bottom
    self.left, self.right, self.top, self.bottom = tempB, tempT, tempL, tempR
    tempL, tempR, tempT, tempB = self.border["L"], self.border["R"], self.border["T"], self.border["B"]
    self.border["L"], self.border["R"], self.border["T"], self.border["B"] = tempB, tempT, list(reversed(tempL)), list(reversed(tempR))

    # rotate clockwise by transposing and then flipping
    transposed = [[self.tile[x][y] for (x, val) in enumerate(line)] for (y, line) in enumerate(self.tile)]
    self.tile = [list(reversed(line)) for line in transposed]

  def flip_horizontal(self):
    tempL, tempR = self.left, self.right
    self.left, self.right = tempR, tempL
    tempL, tempR = self.border["L"], self.border["R"]
    self.border["L"], self.border["R"], self.border["T"], self.border["B"] = tempR, tempL, list(reversed(self.border["T"])), list(reversed(self.border["B"]))
    self.tile = [list(reversed(line)) for line in self.tile]
  
  def flip_vertical(self):
    tempT, tempB = self.top, self.bottom
    self.top, self.bottom = tempB, tempT
    tempT, tempB = self.border["T"], self.border["B"]
    self.border["T"], self.border["B"], self.border["L"], self.border["R"] = tempB, tempT, list(reversed(self.border["L"])), list(reversed(self.border["R"]))
    self.tile = [line for line in reversed(self.tile)]

def merge_tiles(megaTile, currentTile, x, y):
  scaledX, scaledY = x * len(currentTile.tile), y * len(currentTile.tile)
  test[y][x] = currentTile.id
  if megaTile[scaledY][scaledX]:
    return
  for j, row in enumerate(currentTile.tile):
    for i, val in enumerate(row):
      megaTile[scaledY + j][scaledX + i] = val
  
  if currentTile.right:
    merge_tiles(megaTile, tiles[currentTile.right], x + 1, y)
  if currentTile.bottom:
    merge_tiles(megaTile, tiles[currentTile.bottom], x, y + 1)

def arrange_tiles(currentTile):
  while currentTile:
    rightTile, bottomTile = tiles.get(currentTile.right), tiles.get(currentTile.bottom)
    if rightTile:
      currentTile.arrange_other(rightTile, "R")
    if bottomTile:
      currentTile.arrange_other(bottomTile, "B")
    while rightTile:
      nextRight = tiles.get(rightTile.right)
      if nextRight:
        rightTile.arrange_other(nextRight, "R")
      rightTile = nextRight
    currentTile = bottomTile

def is_monster(rawTile, j, i):
  if j < 1 or j > len(rawTile) - 2 or i > len(rawTile[0]) - 20:
    return False
  relativeCoords = [(1,1),(1,4),(0,5),(0,6),(1,7),(1,10),(0,11),(0,12),(1,13),(1,16),(0,17),(-1,18),(0,18),(0,19)]
  for dj, di in relativeCoords:
    if rawTile[j+dj][i+di] != "#":
      return False
  return True

def search_for_monsters(megaTile):
  monsters = 0
  for j, row in enumerate(megaTile.tile):
      for i, val in enumerate(row):
        if val == "#" and is_monster(megaTile.tile, j,i):
          monsters += 1
  return monsters

def count_terrain(megaTile):
  for _ in range(4):
    numMonsters = search_for_monsters(megaTile)
    if numMonsters > 0:
      return sum([x == "#" for line in megaTile.tile for x in line]) - 15 * numMonsters # 15 chars in a sea monster
    megaTile.rotate()

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  isTitle = True
  currentTitle = None
  currentTile = []
  for line in lines:
    if isTitle:
      isTitle = False
      currentTitle = line[-5:-1]
    elif not line:
      isTitle = True
      tiles[currentTitle] = Tile(currentTitle, currentTile)
      currentTile = []
    else:
      currentTile.append(list(line))
  tiles[currentTitle] = Tile(currentTitle, currentTile)
  currentTile = []
  
  # match tile borders  
  for tile in tiles.values():
    for otherTile in tiles.values():
      if tile.id == otherTile.id:
        continue
      tile.match_border(otherTile)
    
  # grab top left corner
  for tile in tiles.values():
    if tile.get_paired_sides() == 2:
      while not (tile.right and tile.bottom):
        tile.rotate()
      initial_corner = tile
      break

  # flip/rotate based on top left corner
  arrange_tiles(initial_corner)

  # allocate a list of lists to merge all the tiles into
  sideLength = int(len(tiles)**(1/2)*(len(initial_corner.tile)))
  megaTile = Tile("MEGA", [[None for x in range(sideLength)] for y in range(sideLength)], False)

  # recursively form the "mega tile"
  merge_tiles(megaTile.tile, initial_corner, 0, 0)

  for line in test:
    print(line)

  # search through all orientations until sea monsters are found
  if count := count_terrain(megaTile):
    print(count)
  else:
    megaTile.flip_vertical()
    if count := count_terrain(megaTile):
      print(count)
    else:
      print("Couldn't find any sea monsters!")